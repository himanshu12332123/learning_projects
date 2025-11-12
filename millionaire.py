questions = [[
    "What is the capital of France?",
    "A) Berlin",
    "B) Madrid",
    "C) Paris",
    "D) Rome",
    2,
],
[
    "What is 2 + 2?",
    "A) 3",
    "B) 4",
    "C) 5",
    "D) 22",
    1,
],
[
    "Which planet is known as the Red Planet?",
    "A) Earth",
    "B) Mars",
    "C) Jupiter",
    "D) Saturn",
    2,

],
]

prizes = [1000, 5000, 10000]

for question in questions:
    i = 0
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    a = int(input("enter your answer"))
    if(question[5] == a):
        print("correct answer")
        print(f"you won {prizes[i]}$")
        i += 1
    else:
        print(f"wrong answer. correct answer is option {question[5]}")
        

        break

