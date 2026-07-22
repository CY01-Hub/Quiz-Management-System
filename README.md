# 🎯 Quiz Management System
A lightweight, interactive Python CLI application that tests users on trivia across Physics, Chemistry, Mathematics, Python Programming, and Board Games.
The program randomly selects 10 questions from a 50-question pool each run, providing a fresh challenge every time you play!

## ✨ Features :-
- Dynamic Question Selection: Randomly picks 10 distinct questions out of 50 each session using Python's random.shuffle.
- 📚 Multi-Subject Pool: Covers five general topics:
Python Basics, Fundamental Physics, High-School Mathematics, Basic Chemistry, Classic Board Games & Trivia.
- Personalized Experience: Greets players by name and delivers a customized score summary at the end.
- Input Handling: Accepts both lowercase and uppercase inputs (e.g., a or A) seamlessly.

## 🚀 How It Works :-
1. The script initializes a database of 50 questions, options, and corresponding correct answers.
2. It prompts you to enter your name.
3. The system shuffles the question bank indices randomly.
4. It presents 10 sequential multiple-choice questions (A, B, C, D).
5. After all questions are answered, your final score is calculated out of 10 and displayed.
