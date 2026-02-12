from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import shutil

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

from rag import ingest_pdf, retrieve_context

load_dotenv()
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY")[:5])


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

llm = Ollama(
    model="mistral"
)

rag_prompt = ChatPromptTemplate.from_template(
    """
You are a customer support assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't have enough information."

Context:
{context}

Question:
{question}
"""
)

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_pdf(file_path)

    return {"status": "Document uploaded and processed"}

@app.post("/chat")
def chat(req: ChatRequest):
    context = retrieve_context(req.message)

    chain = rag_prompt | llm
    response = chain.invoke({
        "question": req.message,
        "context": context
    })

    return {"reply": response}
