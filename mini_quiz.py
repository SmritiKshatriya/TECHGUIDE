questions = ["q1", "q2", "q3"]
answers = ["", "", ""]

answers[0] = input("Which is your favourite programming language? ")
answers[1] = input("Do you prefer frontend or backend development? ")
answers[2] = input("What is your experience level with coding? ")

for key in range(len(answers)):
    print(f"{questions[key]}: {answers[key]}")