# 🎯 Quiz Management System

A lightweight and interactive **Python CLI Quiz Application** designed to test your knowledge across multiple subjects, including **Python Programming, Physics, Mathematics, Chemistry, and Board Games & Trivia**.

The application contains a pool of **50 questions** and randomly selects **10 unique questions** for every session, ensuring a fresh quiz experience each time you play.

---

## ✨ Features

* 🎲 **Dynamic Question Selection**
  Randomly selects **10 distinct questions from a 50-question pool** using Python's `random.shuffle()`.

* 📚 **Multi-Subject Question Pool**
  Covers five different categories:

  * 🐍 Python Basics
  * ⚛️ Fundamental Physics
  * 📐 High-School Mathematics
  * 🧪 Basic Chemistry
  * 🎲 Classic Board Games & Trivia

* 👤 **Personalized Experience**
  Asks for the player's name and provides a personalized score summary at the end of the quiz.

* 🔤 **Flexible Input Handling**
  Accepts both uppercase and lowercase answers, such as `A` and `a`.

* 📊 **Instant Score Calculation**
  Calculates and displays the final score after all 10 questions have been answered.

* 🔄 **Fresh Quiz Every Run**
  Because the questions are randomized, each session can provide a different combination of questions.

---

## 🚀 How It Works

```text
            Start Quiz
                │
                ▼
        Enter Player Name
                │
                ▼
       Load 50 Questions
                │
                ▼
        Shuffle Question Pool
                │
                ▼
       Select 10 Questions
                │
                ▼
     ┌──────────────────────┐
     │   Question 1 → 10    │
     │   A / B / C / D      │
     └──────────┬───────────┘
                │
                ▼
       Check Each Answer
                │
                ▼
        Calculate Score
                │
                ▼
       Display Final Result
```

### Step-by-Step

1. The program initializes a question bank containing **50 multiple-choice questions**.
2. The player is prompted to enter their name.
3. The question pool is randomized using Python's `random.shuffle()`.
4. The program selects **10 questions** from the shuffled pool.
5. Each question is displayed with four options: **A, B, C, and D**.
6. The player's answer is checked against the correct answer.
7. After all 10 questions, the program calculates the final score.
8. The personalized result is displayed at the end.

---

## 🧠 Question Categories

| Category                | Focus                               |
| ----------------------- | ----------------------------------- |
| 🐍 Python               | Programming fundamentals            |
| ⚛️ Physics              | Basic physics concepts              |
| 📐 Mathematics          | High-school mathematics             |
| 🧪 Chemistry            | Fundamental chemistry               |
| 🎲 Board Games & Trivia | General knowledge and classic games |

---

## 🛠️ Tech Stack

| Technology              | Usage                       |
| ----------------------- | --------------------------- |
| 🐍 Python               | Core programming language   |
| 🎲 `random`             | Question randomization      |
| ⌨️ CLI                  | User interaction            |
| 🧠 Conditional Logic    | Answer validation & scoring |
| 📦 Lists / Dictionaries | Question bank management    |

---

## ▶️ Running the Quiz

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/quiz-management-system.git
```

### 2. Navigate to the project

```bash
cd quiz-management-system
```

### 3. Run the program

```bash
python quiz.py
```

> Make sure Python 3.x is installed on your system.

---

## 📊 Scoring

The quiz contains **10 questions per session**.

| Score | Result             |
| ----: | ------------------ |
|  9–10 | 🏆 Excellent       |
|   7–8 | 🌟 Great Job       |
|   5–6 | 👍 Good Attempt    |
|   0–4 | 📚 Keep Practicing |

---

## 🎯 Project Objective

This project was created to practice fundamental Python programming concepts while building a small but complete interactive application.

### Concepts Practiced

* Variables and data types
* Lists and dictionaries
* Functions
* Loops
* Conditional statements
* User input
* String manipulation
* Randomization
* Basic program flow
* Score calculation

---

<div align="center">

### 🐍 Built with Python

**Learn. Play. Improve. Repeat.**

⭐ If you enjoyed the project, consider giving the repository a star!

</div>
