'''
3. Quiz Management System
Design a quiz application that stores multiple-choice questions.
The program should display questions one by one, accept user answers, 
calculate the score, and display the final result.
'''

print("---------------------------------------------------")
import random
print("Quiz Management System :- ")
print("There will be 10 random questions.")
print("The topic includes are Basics of Physics, Chemistry, Maths, Python and Board Games.")
print("Example :- \nQ1. What is 1+1 ? \nA.2\nB.3\nC.4\nD.5 \nAnswer : A")
print("---------------------------------------------------")

# ------------------------- QUESTIONS -------------------------
questions = [
    # Python (1–10)
    "What is the correct file extension for Python programs?",
    "Which keyword is used to define a function in Python?",
    "Which data type stores multiple values?",
    "What is the output of 2 + 3 * 4?",
    "Which symbol is used for comments in Python?",
    "Which function is used to take user input?",
    "What does len() function do?",
    "Which loop is used when iterations are known?",
    "Which operator checks equality?",
    "Which data type is immutable?",

    # Physics (11–20)
    "What is the SI unit of force?",
    "Which law states action and reaction?",
    "Speed is defined as?",
    "SI unit of electric current?",
    "Which quantity is a vector?",
    "Acceleration due to gravity on Earth?",
    "Device converting electrical to mechanical energy?",
    "Rear-view mirror type?",
    "Unit of power?",
    "Sound cannot travel through?",

    # Maths (21–30)
    "Approximate value of pi?",
    "Square root of 144?",
    "25 percent of 200?",
    "Value of 7 x 8?",
    "Which is a prime number?",
    "Perimeter of square with side 5?",
    "Next number: 2, 4, 6, 8, ?",
    "Area of rectangle (10 x 5)?",
    "Value of 2 cube?",
    "100 divided by 4?",

    # Chemistry (31–40)
    "Symbol of Hydrogen?",
    "Water is made of?",
    "pH value of pure water?",
    "Gas required for respiration?",
    "Formula of carbon dioxide?",
    "Liquid metal at room temperature?",
    "Rust is mainly?",
    "Acid present in lemon?",
    "Element with atomic number 1?",
    "Gas released in photosynthesis?",

    # Games (41–50)
    "Which is called Game of Kings?",
    "How many players play Chess?",
    "Game played with dice and tokens?",
    "Chess piece that moves all directions?",
    "Game that forms words?",
    "Tokens per player in Ludo?",
    "Game with snakes moving down?",
    "Main objective of Chess?",
    "Game played with striker and coins?",
    "Monopoly is about?"
]

# -------------------------- OPTIONS --------------------------
options = [
    ["A) .p", "B) .pt", "C) .py", "D) .python"],
    ["A) function", "B) def", "C) define", "D) fun"],
    ["A) int", "B) float", "C) list", "D) bool"],
    ["A) 20", "B) 14", "C) 24", "D) 10"],
    ["A) //", "B) /* */", "C) #", "D) --"],
    ["A) read()", "B) input()", "C) scan()", "D) get()"],
    ["A) Max", "B) Min", "C) Count", "D) Delete"],
    ["A) while", "B) do-while", "C) for", "D) repeat"],
    ["A) =", "B) ==", "C) !=", "D) <="],
    ["A) list", "B) set", "C) dict", "D) tuple"],

    ["A) Joule", "B) Newton", "C) Watt", "D) Pascal"],
    ["A) First", "B) Second", "C) Third", "D) Gravity"],
    ["A) DxT", "B) D/T", "C) T/D", "D) AxT"],
    ["A) Volt", "B) Ohm", "C) Ampere", "D) Coulomb"],
    ["A) Speed", "B) Distance", "C) Mass", "D) Velocity"],
    ["A) 8.9", "B) 9.8", "C) 10.8", "D) 9.0"],
    ["A) Generator", "B) Battery", "C) Motor", "D) Transformer"],
    ["A) Plane", "B) Concave", "C) Convex", "D) Cylindrical"],
    ["A) Joule", "B) Newton", "C) Watt", "D) Volt"],
    ["A) Solid", "B) Liquid", "C) Gas", "D) Vacuum"],

    ["A) 2.14", "B) 3.14", "C) 4.13", "D) 3.41"],
    ["A) 10", "B) 11", "C) 12", "D) 14"],
    ["A) 25", "B) 40", "C) 50", "D) 75"],
    ["A) 54", "B) 56", "C) 58", "D) 64"],
    ["A) 9", "B) 15", "C) 17", "D) 21"],
    ["A) 10", "B) 15", "C) 20", "D) 25"],
    ["A) 9", "B) 10", "C) 11", "D) 12"],
    ["A) 25", "B) 40", "C) 50", "D) 60"],
    ["A) 6", "B) 8", "C) 9", "D) 16"],
    ["A) 20", "B) 24", "C) 25", "D) 30"],

    ["A) H", "B) He", "C) O", "D) Hy"],
    ["A) H+N", "B) H+O", "C) O+C", "D) N+O"],
    ["A) 5", "B) 6", "C) 7", "D) 8"],
    ["A) Nitrogen", "B) CO2", "C) Oxygen", "D) Hydrogen"],
    ["A) CO", "B) CO2", "C) C2O", "D) O2C"],
    ["A) Iron", "B) Mercury", "C) Copper", "D) Aluminium"],
    ["A) Iron oxide", "B) Carbon", "C) CuSO4", "D) ZnO"],
    ["A) HCl", "B) Acetic", "C) Citric", "D) Sulphuric"],
    ["A) Oxygen", "B) Helium", "C) Hydrogen", "D) Carbon"],
    ["A) CO2", "B) Oxygen", "C) Nitrogen", "D) Hydrogen"],

    ["A) Chess", "B) Ludo", "C) Carrom", "D) Monopoly"],
    ["A) 1", "B) 2", "C) 3", "D) 4"],
    ["A) Chess", "B) Scrabble", "C) Ludo", "D) Snakes"],
    ["A) Rook", "B) Bishop", "C) Queen", "D) Knight"],
    ["A) Ludo", "B) Chess", "C) Scrabble", "D) Carrom"],
    ["A) 2", "B) 3", "C) 4", "D) 5"],
    ["A) Chess", "B) Monopoly", "C) Snakes & Ladders", "D) Carrom"],
    ["A) Capture all", "B) Check queen", "C) Checkmate king", "D) Reach end"],
    ["A) Chess", "B) Carrom", "C) Ludo", "D) Scrabble"],
    ["A) Speed", "B) Memory", "C) Property & money", "D) Letters"]
]

# -------------------------- ANSWERS --------------------------
answers = [
    "C","B","C","B","C","B","C","C","B","D",
    "B","C","B","C","D","B","C","C","C","D",
    "B","C","C","B","C","C","B","C","B","C",
    "A","B","C","C","B","B","A","C","C","B",
    "A","B","C","C","C","C","C","C","B","C"
]

score = 0
name = input("Enter your Name : ")
print(f"Hello! {name}, Let's Start the Quiz : ")

order = list(range(len(questions)))
random.shuffle(order)

for i in range(10):
    index = order[i]
    print(f"Q{i+1}.",questions[index])
    print(options[index][0])
    print(options[index][1])
    print(options[index][2])
    print(options[index][3])
    user = input("Answer : ").upper()
    if user == answers[index]:
        score = score + 1
    i = i + 1
    print()

print(f"{name}, your final score is : {score} out of 10")