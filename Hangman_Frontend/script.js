let sessionId = "";
let currentPuzzleType = "";


async function startSession() {
  const age = document.getElementById("age").value;
  const res = await fetch("http://127.0.0.1:5000/start", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ age: parseInt(age) })
  });

  const data = await res.json();
  sessionId = data.session_id;
  loadPuzzle();
}

async function loadPuzzle() {
  const res = await fetch(`http://127.0.0.1:5000/next?session_id=${sessionId}`);
  const data = await res.json();

  currentPuzzleType = data.type;
  document.getElementById("puzzleQuestion").innerText = data.question;
  document.getElementById("puzzleArea").style.display = "block";
}

async function submitAnswer() {
  const answer = document.getElementById("answerInput").value;

  const res = await fetch("http://127.0.0.1:5000/solve", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      session_id: sessionId,
      puzzle_type: currentPuzzleType,
      answer: answer
    })
  });

  const data = await res.json();
  document.getElementById("resultText").innerText = data.correct
    ? "✅ Correct!"
    : "❌ Wrong!";
}
