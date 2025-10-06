quiz = {}

quiz["1. Where is KBTCOE? "] =input("1. Where is KBTCOE? ")
quiz["2. What is 5 + 7? "] = input("2. What is 5 + 7? ")
quiz["3. Who is the Prime Minister of India? "] = input("3. Who is the Prime Minister of India? ")

print("----Answers----")
for question, answer in quiz.items():
    print(question, answer)
