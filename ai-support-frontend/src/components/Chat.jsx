import { useState } from "react";
import axios from "axios";

export default function Chat() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!message) return;

    setMessages([...messages, { role: "user", text: message }]);

    const res = await axios.post("http://localhost:8000/chat", {
      message,
    });

    setMessages((prev) => [
      ...prev,
      { role: "bot", text: res.data.reply },
    ]);

    setMessage("");
  };

  return (
    <div>
      <div style={{ marginBottom: "10px" }}>
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}:</b> {m.text}
          </div>
        ))}
      </div>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask a support question..."
        style={{ width: "80%" }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
