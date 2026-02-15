import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [uploadStatus, setUploadStatus] = useState("");

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMsg = { role: "user", content: message };
    setMessages((prev) => [...prev, userMsg]);
    setMessage("");

    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: message }),
    });

    const data = await res.json();
    const botMsg = { role: "assistant", content: data.reply };

    setMessages((prev) => [...prev, botMsg]);
  };

  const uploadFile = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setUploadStatus("Uploading...");

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    if (res.ok) {
      setUploadStatus("Document uploaded successfully ✅");
    } else {
      setUploadStatus("Upload failed ❌");
    }
  };

  return (
    <div className="page">
      <div className="chat-container">
        <h1>AI Customer Support Assistant</h1>

        {/* Upload */}
        <div className="upload-row">
          <label className="upload-btn">
            Upload PDF
            <input type="file" accept=".pdf" hidden onChange={uploadFile} />
          </label>
          <span className="upload-status">{uploadStatus}</span>
        </div>

        {/* Messages */}
        <div className="chat-box">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`message ${msg.role === "user" ? "user" : "bot"}`}
            >
              {msg.content}
            </div>
          ))}
        </div>

        {/* Input */}
        <div className="input-row">
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask a support question..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
