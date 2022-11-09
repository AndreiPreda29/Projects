print("Welcome to my  quiz game!")

playing = input("Do you want to try it? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play !")
score = 0

answer = input("What does HMS? ")
if answer.lower() == "Her Majesty's":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does USSR stand for? ")
if answer.lower() == "union of soviet socialist republics":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does EU stand for? ")
if answer.lower() == "european union":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does EEA stand for? ")
if answer.lower() == "european economic area":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")