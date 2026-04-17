import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    const response = await fetch("https://book-ai-project-final.onrender.com//ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();
    setAnswer(data.answer);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>📚 Book AI Project</h1>

      <input
        type="text"
        placeholder="Ask about a book..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{ padding: "10px", width: "300px" }}
      />

      <br /><br />

      <button onClick={askQuestion}>Ask</button>

      <p>{answer}</p>
    </div>
  );
}

export default App;