# mini_quiz.py

answers = {}

answers["q1"] = input("What is your favorite hobby? ")
answers["q2"] = input("Which city would you love to visit? ")
answers["q3"] = input("Do you prefer tea or coffee? ")

print("\nYour answers:")
for key, value in answers.items():
    print(f"{key}: {value}")
