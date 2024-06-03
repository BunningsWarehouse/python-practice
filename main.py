# Imports random
import random
# set 
QUESTION_FORMAT = "{}\n A. {} \n B. {} \n C. {} \n D. {} \n"
GOOD_COMMENTS = ["Congratulations, you are doing well", "You are very smart!!1!!!!!11!!!", "You know python fairly well"]
BAD_COMMENTS = ["Please quit your coding career oml you are so bad", "you always fail to make me proud", "python is such an easy coding language how are you this bad"]
QUESTIONS = ["What year was python made? \n", 
             "Who was the Creator of Python?"]
OPTIONS = [["1991", "1992", "1993", "2035"], ["Kendrick Lamar", "Bjarne Stroustrup", "Guido van Rossum", "James Gosling"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [0,2]
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
    # Create score variable
    for i in range(len(QUESTIONS)):
            score = 0
            question_tries = tries
            while question_tries > 0:
                # Ask user A question
                answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                              OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
                if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                    print("you said", answer)
                    print("you are correct")
                    print(random.choice(GOOD_COMMENTS))
                    score += 10
                    break
                elif answer == "":
                    print("you said nothing so you automatically lose")
                elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                    print("you said", answer)
                    print("you are incorrect")
                    print(random.choice(BAD_COMMENTS))
                    question_tries -=1
                else:
                    print("that wasn't an option so you automatically lose")
            print("the answer is", OPTIONS[i][ANSWERS[i]])
# End the quiz
    print("this is the end of the quiz you win i guess")
    print("{}, your score is {}".format(name, score))
    if score < 10:
        print("dayum you suck")
    elif score == 10:
        print("at least you got one question right")
    elif score == 20:
        print("you are good at python")
    play = input("Do you want to try again? \n").lower()