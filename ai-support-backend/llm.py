from langchain_community.llms import Ollama

# Single shared LLM instance
llm = Ollama(
    model="mistral"   # or mistral, llama2, etc.
)
