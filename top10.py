import random

TOP_OBSCURE_COUNTRIES = ["transnistria", "kiribati", "comoros", "nauru", "tuvalu", "timor-leste", "vanuatu", "palau", "djibouti", "micronesia"]
guesses = []
# ----- FUNCTIONS -----

# Welcomes the user to the quiz
def intro():
   name = input("What is thy name of the player currently playing the quiz named top10.py\n")

   # Greet user with their name
   print("Welcome Mr or Ms", name, "to the wonderful and marvelous quiz named top10.py")

# Gets the amount of tries the user wants at each question
def getLives():
   while True:
        lives = input("How many lives do you want yourself to be given in the wonderful and marvelous quiz named top10.py do you want\n")
        try:
            lives = int(lives)
            if lives > 0:
                return lives
            else:
                print("You are prohibited from entering a negative number of lives that you want yourself to be given in the wonderful and marvelous quiz named top10.py")
        except:
            print("You must input a number to be able to be given the lives you want yourself to be given in the wonderful and marvelous quiz named top10.py")
   

def inList(answer, list):
    if answer in list:
        return True
    else:
        return False 
    

# ----- MAIN CODE -----
intro()
lives = getLives()
score = 0
while lives > 0:
    answer = input("Would you kindly name one of the 10 most obscure countries on earth\n").lower()
    if inList(answer, TOP_OBSCURE_COUNTRIES):
        if inList(answer, guesses):
            print("You have already guessed that answer for the most obscure countries in this wonderful and marvelous quiz named top10.py")
        else:
            score =+ 10
            guesses.append(answer)
            print("that is one of the correct answers for the question about the most obscure countries within the wonderful and marvelous quiz named top10.py")       
    else:
        lives =- 1
        print("Oh great heavens you have inputted an incorrect answer for the question about the most obscure countries within the wonderful and marvelous quiz named top10.py")
print("You have ran out of the amount of lives you wanted yourself to be given in the wonderful and marvelous quiz named top10.py, your final score is {}".format(score))        

