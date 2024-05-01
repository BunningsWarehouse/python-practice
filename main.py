# Create score variable
score = 0


# Ask user for name
name = input("What is thy name \n")


# Greet user and introduce quiz
print("Welcome to the magnifiscent quiz", name)
print("this quiz is about python")

# Ask user A question
answer = input("What is the function that outputs text in python? \n")


# Tell user the answer
print("you said", answer)
if answer == "print":
    print("you are correct")
    score += 10
elif answer == "":
    print("you said nothing so you automatically lose")
    print("the answer is print")
else:
    print("How did you get that wrong that's like the first thing you learn with python")
    print("the answer is print")
# Ask user A question
answer = input("What is the function that allows you to input text in python? \n")


# Tell user the answer
print("you said", answer)
if answer == "input":
    print("you are correct")
    score += 10
elif answer == "":
    print("you said nothing so you automatically lose")
    print("the answer is input")
else:
    print("It was literally in the question how did you not get this question")
    print("the answer is print")

# End the quiz
print("this is the end of the quiz you win i guess")
print("your score is", score)
if score < 10:
    print("dayum you suck")
elif score == 10:
    print("at least you got one question right")
else:
    print("congratulations you are good at python")