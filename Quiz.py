questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. CSS"],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Boolean", "C. Integer", "D. List"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["A. input()", "B. print()", "C. output()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    }
]

score = 0

print("===== PYTHON QUIZ =====")

for number, question in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong ❌. Correct answer: {question['answer']}")

print("\n===== QUIZ COMPLETE =====")
print(f"Your score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent! 🏆")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")
