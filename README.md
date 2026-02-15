# 🧠 AI Customer Support Assistant (RAG + LangGraph)

An end-to-end AI-powered customer support assistant built using **React**, **FastAPI**, **LangChain**, **LangGraph**, and **local LLMs (Ollama)**.

The system supports **document upload**, **retrieval-augmented generation (RAG)**, **clarification-aware reasoning**, and **multi-document querying**.

---

## ✨ Features

- 📄 **PDF Upload from UI** (Knowledge Ingestion)
- 🔍 **Retrieval-Augmented Generation (RAG)** using Chroma DB
- 🧠 **LangGraph-based control flow**
- ❓ Clarifies ambiguous user queries
- 🚫 Prevents hallucinations
- 🤖 Local LLM support via **Ollama (Mistral)**
- 💬 ChatGPT-style React UI
- 📚 Multi-document support
- ⚡ FastAPI backend with OpenAPI docs

---

## 🏗️ Architecture Overview

### 🔷 High-Level Flow

User (React UI)
   |
   | 1. Upload PDF / Ask Question
   v
FastAPI Backend
   |
   |-- /upload → PDF ingestion
   |-- /chat   → LangGraph execution
   v
LangGraph Orchestration
   |
   |-- Intent / Clarity Check
   |-- Clarifying Question (if needed)
   |-- RAG Node (Vector Retrieval)
   |-- LLM Reasoning
   v
Response returned to UI


---

### 🔷 LangGraph Control Flow

User Question
   ↓
Router Node (Is question clear?)
   ├── No → Ask Clarifying Question
   └── Yes
        ↓
Retrieve Relevant Documents (Chroma)
        ↓
LLM Reasoning (Mistral via Ollama)
        ↓
Final Answer


---

### ✅ This Ensures

- Ambiguous questions don’t trigger hallucinations
- Answers are grounded in uploaded documents
- Multi-document contexts are handled correctly

---

## 🧠 Retrieval-Augmented Generation (RAG)

- PDFs are split into chunks
- Chunks are embedded using sentence-transformers
- Stored in **Chroma Vector DB**
- Relevant chunks retrieved per query
- LLM answers only using retrieved context

If relevant information is missing, the assistant responds with:

> “I don’t have enough information to answer that.”

---

## 🖥️ Tech Stack

### Frontend

- React (Vite)
- Fetch API
- Chat-style UI (Flexbox)

### Backend

- FastAPI
- LangChain
- LangGraph
- ChromaDB
- Ollama (Mistral LLM)
- HuggingFace Embeddings

---

## 📸 Screenshots

![Chat UI](screenshots/chat-ui.png)
![PDF Upload](screenshots/upload.png)
![Clarification](screenshots/clarification.png)


<img width="1040" height="888" alt="image" src="https://github.com/user-attachments/assets/af2f85c2-721e-4dfa-9b47-ceb5b5155c16" />
