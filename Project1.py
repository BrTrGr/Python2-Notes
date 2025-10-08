score = 0
answers_correct = (score,"|5")


print("What is 10 - 3?")
answer1 = input()
if answer1 == "7":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


print("Who is the current president of Spain")
print("""a. Donald Trump
         b. Mariano Rajoy
         c. Mario Sanchez
         d. Pedro Sanchez""")
answer2 = input()
if answer2 == "d" or "D":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    


print("What is the square root of 361?")
answer3 = input()
if answer3 == "19":
    print("Correct!")
    score += 1
else:   
    print("Incorrect")
    

print("Wich of  these animals is a mammal?")
print(("""a. Dolphin
          b. Crocodrile
          c. Penguin
          d. Shark"""))
answer4 = input()
if answer4 == "a" or "A" or "dolphin" or "Dolphin":
    print("Correct!")
    score += 1
else:
    print("Are you ok?")


print("What is the capital of Nauru?")
answer5 = input()
if answer5 == "Yaren":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


print(score * 20)
print(answers_correct)