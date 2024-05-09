QUESTION_FORMAT = "{}\n A. {} \n B. {} \n C. {} \n D. {} \n"
# Create score variable
score = 0
# Create play variable
play = "yes"
# Ask user for name
name = input("What is thy name \n")


# Greet user and introduce quiz
print("Welcome to the magnifiscent quiz", name)
print("this quiz is about python")

# ask user how many attempts at the questions they want
while True:
    try:
        tries = input("How many tries do you want at each question? 1-4 \n")
        tries = int(tries)
        break
    except:
        print("that ain't a number")


# start game loop
while play == "yes":
    question_tries = tries
    while question_tries > 0:
        # Ask user A question
        answer = input("What is the function that outputs text in python? \n").lower()


        # Tell user the answer
        if answer == "print".lower():
            print("you said", answer)
            print("you are correct")
            score += 10
            break
        elif answer == "":
            print("you said nothing so you automatically lose")
        else:
            print("you said", answer)
            print("How did you get that wrong that's like the first thing you learn with python")
            question_tries -= 1
    print("the answer is print")    
    # Ask user A question
    question_tries = tries
    while question_tries > 0:
        answer = input("What is the function that allows you to input text in python? \n").lower()


        # Tell user the answer

        if answer == "input".lower():
            print("you said", answer)
            print("you are correct")
            break
            score += 10
        elif answer == "":
            print("you said nothing so you automatically lose")
        else:
            print("you said", answer)
            print("It was literally in the question how did you not get this question")
            question_tries -= 1
    print("the answer is print")    

    question_tries = tries
    while question_tries > 0:
        # Ask user A question
        question =  "What year was python made?"
        a = "1991"
        b = "1992"
        c = "1993"
        d = "2035"
        answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()


        # Tell user the answer

        if answer == a or answer == "A".lower():
            print("you said", answer)
            print("you are correct")
            score += 10
            break
        elif answer == "":
            print("you said nothing so you automatically lose")
            
        elif answer == d or answer == "D".lower():
            print("you said", answer)
            print("according to you python was made 12 years into the future from now")
            question_tries -= 1
        elif answer == c or answer == "C".lower() or answer == b or answer == "B".lower():
            print("you said", answer)
            print("you are incorrect")
            question_tries -=1
        else:
            print("that wasn't an option so you automatically lose")
    print("the answer is 1991")
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
    play = input("Do you want to try again? \n").lower()