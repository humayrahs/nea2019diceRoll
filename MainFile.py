#NEA 2019- Dice game
import random
import time

def open_file(filename, state):
    return open(filename + ".txt", state)

#Odd Or Even Checker
def is_odd(number):
    if int(number) % 2 == 0:
        odd = False                 #Simple function that sees if, when divided 
    else:                           #in 2, the given number has a remainder
        odd = True
                            
    return odd

def sort(numbers):
    while True:
        hasSorted = False
        selectedIndex = 0
        for i in range(1, len(numbers)):
            if numbers[selectedIndex][0] < numbers[i][0]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
                hasSorted = True
            selectedIndex = i
        if not hasSorted:
            return numbers

def login_program():
    #Number of Players
    num_players = 0

    while num_players == 0:
        num_players = int(input("How many people are playing? "))
    
    players = []

    print("\n\nOk, " + str(num_players) + " are playing. We now need each of you to log in.\n")

    #Assigning Players To Users
    while len(players) < num_players:       #Just making sure every user gets a name

        #Login System

        print("[User " + str(len(players) + 1) + "]")
        
        new_user = input("\nAre you a new User? Y or N: ").capitalize()

        #Make A User
        
        if new_user == "Y":
            username = input("Username: ")
            name = input("Name: ")          
            password = input("Password: ")

            while name.isalpha() != True:
                name = input("\nName must be letters only. Re-type name: ")

            with open(username + ".txt", "w") as file:
                file.write(name + "\n" + password)

            print("\nNow Log In: \n")

        #Log In
            
        username = input("Username: ")
        password = input("Password: ")

        login = False

        try:
            file = open_file(username, "r")
        except FileNotFoundError:
            print("File doesn't exist. Restarting...")
            time.sleep(0.5)
            login_program()

        file = open_file(username, "r")
 
        for line in file:
            #print(line.strip("\n"))
            if password == line:
                login = True

        file = open_file(username, "r")
        if login == True:
            print("Welcome " + file.readline())
            players.append(username) #next iteration, also refer to each user as players[x]
        elif login == False:
            print("Login failed. Restarting...")   
            time.sleep(0.5)
            login_program()

        file.close()
        #username = input("Userame of player " + str(len(players) + 1) + ": ")

    print("\n")
    print(players)
    return players

def whole_program():

    players = login_program()

    #Game
    score = [0]*len(players)
    turns = 0

    while turns < 5:
        for i in range(len(players)):       #Players[i] refers to the current player

            
            dice_1 = random.randint(1,6)    #The (1,6) represents the 6 sides of the dice
            dice_2 = random.randint(1,6)
            roll = dice_1 + dice_2          #While the user won't see this value,
                                            #it makes coding easier

            '''
            dice_1 = 4
            dice_2 = 2
            roll = dice_1 + dice_2 #testing purposes only!!
            '''
            
            print("Round " + str(turns+1))
            print("It's " + str(players[i]) + "'s turn. Press Enter to Roll.")
            input()                         #Input creates the illusion they're rolling the dice
            print(players[i] + " rolled a " + str(dice_1) + " and a " + str(dice_2) + ".")
            print("Roll Total = " + str(roll))

            if dice_1 == dice_2:            
                print("You a rolled a double, press Enter to roll again.")
                input()
                dice_3 = random.randint(1,6)
                print(players[i] + " rolled a " + str(dice_3))
                score[i] += dice_3
                
            if is_odd(roll) == False:
                score[i] += 10
            elif is_odd(roll) == True:
                if score[i] - 5 >= 0:
                    score[i] -= 5
                else:
                    score[i] = 0

            print(players[i] + "'s score: " + str(score[i]) + ".")
            input()
        turns += 1

    #if both players have the same score at the end of the game:
    while score[0] == score[1]:
        print("\nThe final scores seem to be a tie.")
        for i in range(len(players)):
            
            tie_dice = random.randint(1,6)
            score[i] += tie_dice
            
            print(players[i] + "'s turn. Press Enter to roll: ")
            input()
            print(players[i] + " has rolled a " + str(tie_dice) + ".")
            print("\n" + players[i] + "'s total: " + str(score[i]) + ".")

        #Checking to see who has the bigger score after the tie 
            if players[i] == 0:                 #Checking whose turn it is
                if score[i] > score[i+1]:
                    print(players[i] + " is in the lead with " + str(score[i]) + "points.")
                    
                elif score[i] < score[i+1]:
                    print(players[i+1] + " is in the lead with " + str(score[i+1]) + "points.")
                    
                elif score[i] == score[i+1]:
                    print("Still a tie.")
                    
            elif players[i] == 1:
                if score[i] > score[i-1]:
                    print(players[i] + " is in the lead with " + str(score[i]) + "points.")
                    
                elif score[i] < score[i-1]:
                    print(players[i-1] + " is in the lead with " + str(score[i-1]) + "points.")
                    
                elif score[i] == score[i-1]:
                    print("Still a tie.")
    
    #Highscore
    max_score = 0
    for a in range(len(players)):
        if score[a] > max_score:    #player 1, then player 2, etc...
            max_score = score[a]
            max_score_name = players[a]

    print("The winner is " + max_score_name + " with " + str(max_score) + " points.")

    with open("leaderboard.txt", "a") as file:
        file.write(str(max_score) + ", " + max_score_name + "\n")

    with open("leaderboard.txt", "r") as file:
        data = file.readlines()

    sort(data)
    
    print("Top 5 scores:")
    for i in range(5):
        print(data[i])

whole_program()
