#THIS PYTHON FILE IS CREATED FOR THE SOLE PURPOSE OF PLAYING THE HANGMAN!

#this function is for the main menu
def Menu():
    print()
    print("Categories:")
    print("1. Animals")
    print("2. Countries")
    print("3. Red Velvet Songs")
    print()
    chosenCategory = int(input("Enter the number of your chosen category: "))
    if chosenCategory == 1:
        difficulty()
        choice = int(input("Enter the number of your chosen difficulty: "))
        if choice == 1:
            print("")
            print("Category: Animals")
            print("Difficulty: Easy")
            gameProcess(load(animalsEasy))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()
        elif choice == 2:
            print("")
            print("Category: Animals")
            print("Difficulty: Average")
            gameProcess(load(animalsAverage))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()   
        elif choice == 3:
            print("")
            print("Category: Animals")
            print("Difficulty: Average")
            gameProcess(load(animalsHard))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()   
        else:
            print("")
            print("Invalid number.")
            print("Try again.")
            Menu()            
    elif chosenCategory == 2:
        difficulty()
        choice = int(input("Enter the number of your chosen difficulty: "))
        if choice == 1:
            print("")
            print("Category: Countries")
            print("Difficulty: Easy")
            gameProcess(load(countriesEasy))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()                
        elif choice == 2:
            print("")
            print("Category: Countries")
            print("Difficulty: Average")
            gameProcess(load(countriesAverage))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()         
        elif choice == 3:
            print("")
            print("Category: Countries")
            print("Difficulty: Hard")
            gameProcess(load(countriesHard))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()    
        else:
            print("")
            print("Invalid number.")
            print("Try again.")
            Menu()   
    elif chosenCategory == 3:
        difficulty()
        choice = int(input("Enter the number of your chosen difficulty: "))
        if choice == 1:
            print("")
            print("Category: Red Velvet Songs")
            print("Difficulty: Easy")
            gameProcess(load(rvsongsEasy))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()    
        elif choice == 2:
            print("")
            print("Category: Red Velvet Songs")
            print("Difficulty: Average")
            gameProcess(load(rvsongsAverage))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores()    
        elif choice == 3:
            print("")
            print("Category: Red Velvet Songs")
            print("Difficulty: Average")
            gameProcess(load(rvsongsHard))
            score = (len(guessNo) * 50) - (len(missedLetters)*4)
            saveScore(score, playerName)
            sortedScores(arrangeHighScore())
            highscores() 
        else:
            print("")
            print("Invalid number.")
            print("Try again.")
            Menu()  
    else:
        print("")
        print("Invalid number.")
        print("Try again.")
        Menu()  

#function that contains the different difficulties available in this game!
def difficulty():
    print("")
    print("Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

#the file holders for the different categories and difficulties!
animalsEasy = "animalsEasy.txt"
animalsAverage = "animalsAverage.txt"
animalsHard = "animalsAverage.txt"

countriesEasy = "countriesEasy.txt"
countriesAverage = "countriesAverage.txt"
countriesHard = "countriesHard.txt"

rvsongsEasy =  "rvsongsEasy.txt"
rvsongsAverage = "rvsongsAverage.txt"
rvsongsHard = "rvsongsHard.txt"

#this function loads the content of the text files!
def load(file):
    wordList = []
    import random
    fileHandle = open(file, "r")
    for line in fileHandle:
        wordList.append(line[:-1])
    fileHandle.close
    word = random.choice(wordList)
    return word

guessNo = []
missedLetters = []
#this function is the overall process of the game!
def gameProcess(word):
    print()
    
    guessCorrect = False
    
    print(" _____")
    print(" |    |")
    print("      |")
    print("      |")
    print("      |")
    print("______|")
    print()
    
    while not guessCorrect:
        print("")
        print("Word:")
        for l in word:
            if l.upper() in guessNo:
                print(l, end=" ") 
            elif l == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print("")

        newWord = word.replace(" ", "")
        print("")
        guess = input("Enter the letter of your guess: ")
        guessNo.append(guess.upper())
        print("")
        print(f"Guess: {guess}")

        if guess.upper() not in newWord:
            missedLetters.append(guess)
            print(f"Missed Letters:{missedLetters}")    
            if len(missedLetters) == 1:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print("      |")
                print("      |")
                print("______|")
            elif len(missedLetters) == 2:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print(" |    |")
                print("      |")
                print("______|")
            elif len(missedLetters) == 3:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print(" |    |")
                print("      |")
                print("______|")
            elif len(missedLetters) == 4:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print("/|    |")
                print("      |")
                print("______|")
            elif len(missedLetters) == 5:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print("/|\   |")
                print("      |")
                print("______|")
            elif len(missedLetters) == 6:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print("/|\   |")
                print("/     |")
                print("______|")
            elif len(missedLetters) == 7:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print("/|\   |")
                print("/     |")
                print("______|")
                
            elif len(missedLetters) == 8:
                print(" _____")
                print(" |    |")
                print(" O    |")
                print("/|\   |")
                print("/ \   |")
                print("______|")
                break

        guessCorrect = True   
        for l in newWord:
            if l not in guessNo:
                guessCorrect = False
            
    if guessCorrect:
        print("")
        print("Congratulations!")
        print("Your guess is correct!")
        print(f"The word is {word}.")
    else:
        print("")
        print("Too bad.")
        print("You lost :<")
        print(f"The word is {word}.")

#this saves the user's score in the scores file
def saveScore(score, playerName):

    scorehandle = open("scores.txt", "a")
    scorehandle.write(f"{playerName}:{score}\n")
    scorehandle.close()

#this opens the scores text to be used for the highscores!
def arrangeHighScore():

    list = []
    dict={}
    dictValues = []
    sortDict = {}

    filehandle = open("scores.txt", "r")
    for line in filehandle:
        data = line[:-1].split(":")
        list.append(data)
    
        for i in list:
            dict[i[0]] = int(i[1])
    
    for v in dict.values():
        dictValues.append(v)
    
    dictValues.sort(reverse=True)
    
    for e in dictValues:
        for keys in dict.keys():
            if dict[keys] == e:
                sortDict[keys] = dict[keys]
    
    filehandle.close()   
    return sortDict

#this sorts the scores!
def sortedScores(scores):
    
    scoreHandle = open("scores.txt", "w")
    
    for items in scores.items():
            scoreHandle.write(f"{items[0]}:{items[1]}\n")
    scoreHandle.close()

#this aids in determining the top 5 scorers!
def highscores():
    list=[]
    filehandle = open("scores.txt", "r")
    
    for i in filehandle.readlines():
        list.append(i[:-1])
    filehandle.close()

    secondhandle = open("highestscorers.txt", "w")

    if len(list) < 5 and len(list) > 0:
        for e in list:
            secondhandle.write(e+"\n")
    elif len(list) == 5:
        for e in list:
            secondhandle.write(e+"\n")
    elif len(list) > 5:
        for e in list[0:5]:
            secondhandle.write(e+"\n") 
    secondhandle.close()   

print("")
print("H A N G M A N")
print("")
print("Instruction:")
print("Guess the word by supplementing the correct letters.")
print("Do it nice and accurately so the man will not die :<")
print("")
playerName = input("Enter your name: ")
Menu()

highscores = open("highestscorers.txt", "r")
i=1
print("")
print("Highscores:")
for line in highscores:
    print(f"{i}){line[:-1]}")
    i += 1
highscores.close()
print()










