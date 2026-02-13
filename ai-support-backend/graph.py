from typing import TypedDict
from langgraph.graph import StateGraph


# --------------------
# State Definition
# --------------------
class ChatState(TypedDict):
    question: str
    answer: str


# --------------------
# Router Node
# --------------------
def router_node(state: ChatState):
    return state


# --------------------
# Routing Decision
# --------------------
def route_decision(state: ChatState):
    question = state["question"].lower()

    unclear_tokens = ["this", "that", "it", "they", "something"]
    is_short = len(question.split()) < 4

    if is_short or any(t in question for t in unclear_tokens):
        return "clarify"

    if "document" in question or "pdf" in question:
        return "rag"

    return "llm"


# --------------------
# Clarification Node
# --------------------
def clarify_node(state: ChatState):
    return {
        "answer": "Could you please clarify your question or provide more details so I can help you better?"
    }


# --------------------
# RAG Node (USING rag.py)
# --------------------
def rag_node(state: ChatState):
    from rag import retrieve_context
    from llm import llm  # Ollama LLM

    context = retrieve_context(state["question"])

    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {state['question']}
    """

    response = llm.invoke(prompt)
    return {"answer": response}


# --------------------
# General LLM Node
# --------------------
def llm_node(state: ChatState):
    from llm import llm

    response = llm.invoke(state["question"])
    return {"answer": response}


# --------------------
# Build LangGraph
# --------------------
builder = StateGraph(ChatState)

builder.add_node("router", router_node)
builder.add_node("clarify", clarify_node)
builder.add_node("rag", rag_node)
builder.add_node("llm", llm_node)

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "clarify": "clarify",
        "rag": "rag",
        "llm": "llm",
    }
)

builder.set_finish_point("clarify")
builder.set_finish_point("rag")
builder.set_finish_point("llm")

graph = builder.compile()
