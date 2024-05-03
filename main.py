# Create score variable
score = 0


# Ask user for name
name = input("What is thy name \n")


# Greet user and introduce quiz
print("Welcome to the magnifiscent quiz", name)
print("this quiz is about python")

# Ask user A question
answer = input("What is the function that outputs text in python? \n").lower()


# Tell user the answer
if answer == "print".lower():
    print("you said", answer)
    print("you are correct")
    score += 10
elif answer == "":
    print("you said nothing so you automatically lose")
    print("the answer is print")
else:
    print("you said", answer)
    print("How did you get that wrong that's like the first thing you learn with python")
    print("the answer is print")

# Ask user A question
answer = input("What is the function that allows you to input text in python? \n").lower()


# Tell user the answer

if answer == "input".lower():
    print("you said", answer)
    print("you are correct")
    score += 10
elif answer == "":
    print("you said nothing so you automatically lose")
    print("the answer is input")
else:
    print("you said", answer)
    print("It was literally in the question how did you not get this question")
    print("the answer is print")

# Ask user A question
question =  "What year was python made?"
a = "1991"
b = "1992"
c = "1993"
d = "2035"
answer = input("{}\n A. {} \n B. {} \n C. {} \n D. {} \n".format(question, a, b, c, d)).lower()


# Tell user the answer

if answer == a or answer == "A".lower():
    print("you said", answer)
    print("you are correct")
    score += 10
elif answer == "":
    print("you said nothing so you automatically lose")
    print("the answer is 1991")
elif answer == d or answer == "D".lower():
    print("you said", answer)
    print("according to you python was made 12 years into the future from now")
    print("the answer is 1991")
elif answer == c or answer == "C".lower() or answer == b or answer == "B".lower():
    print("you said", answer)
    print("you are incorrect")
    print("the answer is 1991")
else:
    print("that wasn't an option so you automatically lose")

# End the quiz
print("this is the end of the quiz you win i guess")
print("{}, your score is {}".format(name, score))
if score < 10:
    print("dayum you suck")
elif score == 10:
    print("at least you got one question right")
elif score == 20:
    print("eh you're alright at python")
else:
    print("you are good at python")