name = input("What’s your favorite programming language? ")
mail = input("Do you prefer frontend or backend? ")
contact = input("Do you like working with data? ")


ans = {}
ans[1] = name
ans[2] = mail
ans[3] = contact

for key,value in ans.items():
    print(key, ":", value)