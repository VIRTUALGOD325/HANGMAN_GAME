

# 🧠 Hangman++: ML-Driven Puzzle Word Game

A unique take on Hangman that combines logic, cryptography, mazes, and ciphers—each puzzle reveals a letter of a hidden word. But beware: one mistake resets your progress. Powered by Machine Learning to dynamically adapt puzzle difficulty.

---

## 🎮 Game Concept

- Each round presents a **logic-based puzzle** (cipher, maze, symbol, etc.)
- Solving a puzzle correctly reveals **one letter** from a hidden word
- **You don't know the length of the word**
- You get **only ONE attempt per puzzle**
- Failing a puzzle resets your chance—**a new puzzle is generated**
- Once the word is fully revealed → you win 🎉

---

## 🧠 Intelligence Meets Gameplay

| Feature | Description |
|--------|-------------|
| 🎯 **Dynamic Difficulty** | ML/NLP models adjust puzzle difficulty based on player behavior |
| 🧩 **Puzzle Variety** | Puzzles range from logic grids to cryptograms, mazes, and more |
| 🧠 **Adaptive Puzzle Type** | The game selects puzzles that challenge your weaknesses |
| 🔒 **One-Life Mechanic** | One wrong answer resets your puzzle and hides any letter gain |
| 🧬 **No Letter Count Display** | The length of the hidden word is unknown until revealed |

---

## 🧪 Tech Stack

| Layer | Tech |
|------|------|
| 🔙 Backend | Flask (Python) |
| 🧠 AI/ML | scikit-learn, transformers, PyTorch (optional) |
| 🌐 Frontend | React.js (integrated at the final stage) |
| 📦 Dev Tools | PyCharm, VS Code |
| 🔗 API | REST (JSON-based) |

---

## 🏗️ Project Structure

```

hangman\_backend/
├── app.py                  # Main Flask entrypoint
├── config.py               # Config and environment variables
├── routes/                 # Flask Blueprints for game and puzzle APIs
│   ├── game\_routes.py
│   └── puzzle\_routes.py
├── engine/                 # Core game logic
│   ├── game\_engine.py
│   ├── puzzle\_manager.py
│   └── difficulty\_ml.py
├── puzzles/                # Logic for individual puzzle types
│   ├── cipher.py
│   ├── maze.py
│   └── symbol.py
├── utils/                  # Word selection, helpers
│   └── word\_selector.py
├── models/                 # ML/NLP models (to be integrated)
├── requirements.txt
└── README.md

````

---

## 🧭 Roadmap

### ✅ Phase 1: Backend Setup (Now)
- [x] Flask app boilerplate
- [x] Game state engine
- [ ] Word selector and session manager
- [ ] Puzzle controller with dynamic fetching
- [ ] ML stub for difficulty tuning

### 🔜 Phase 2: Puzzle Integration
- [ ] Implement puzzle types (cipher, maze, etc.)
- [ ] One-life mechanism
- [ ] Puzzle result → letter reveal logic

### 🔮 Phase 3: ML/NLP Models
- [ ] Player behavior tracking
- [ ] Adaptive puzzle difficulty model
- [ ] Optional clue engine

### 🎨 Phase 4: Frontend Integration
- [ ] React UI
- [ ] Visual maze/cipher renderers
- [ ] Progress tracking and animations

---

## 👨‍💻 Development Guide

### 1. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Flask app

```bash
python app.py
```

---

## 📌 Notes

* This project avoids traditional Hangman visuals.
* Word difficulty and puzzle logic will sync via an adaptive engine.
* Each puzzle is standalone with its own success/fail logic.

---

## ✨ Inspiration

Games like *Baba Is You*, *The Witness*, *Magnet Block*, and *Snakebird* shaped the direction of the puzzle design philosophy.

---

## 📫 Want to Contribute?

Clone, fork, suggest puzzle types, or propose AI models for adaptive gameplay. Creativity is welcome!

```

---

Would you like to start by:
- Coding the `app.py` and base routes, or
- Setting up the `game_engine.py` with word selection and session logic?

Let’s build it step by step.
```
