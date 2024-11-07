import time

#Welcome user to the game
print()
print ("* * * Hello! Welcome to Adventure on the Chattooga Trail * * *")
print()
#add slight delay for gameplay flow
time.sleep(1)
print ("You will be going on a hike in the woods and have some challenges to overcome!")
print()
#add slight delay for gameplay flow
time.sleep(1)
print ("Have fun!")
print ()
print("*****************************************************************")
print()
#add slight delay for gameplay flow
time.sleep(2)


#Declare and initialize yo across-game variables
mainGameInput = '' # controls overall game while loop
userSkillPoint = 0 # the number of skill points the user has at the start of the game


#Begin start of main game while loop
while mainGameInput != 'no':

    #Declare and initialize yo in-game variables
    userDecision1 = '' # controls the user's first decision to look or go
    userPathLook = ''   # controls which of three paths the user looks down
    userTreeDecision = '' # controls choice in the tree puzzle
    userStreamDecision = '' # controls choice in the stream puzzle
    userSnakeDecision = '' # controls choice in the snake puzzle

    #Describe setting in woods
    print()
    print ("It is a beautiful day, and you have decided to go for a hike in the woods.")
    print()
    #add slight delay for gameplay flow
    time.sleep(1)
    print ("The birds are singing, the sun is shining, and you are having a wonderful time!")
    print()
    #add slight delay for gameplay flow
    time.sleep(1)
    print ("Suddenly the path in front of you splits three different ways! You have to decide which way to go next.")
    print ()
    #add slight delay for gameplay flow
    time.sleep(2)

    #First user decision tree: look down path or go down path
    #User is at start of game or user decides to look down a path
    while userDecision1 == '' or userDecision1 == 'look':
        print()
        print ("Which path would you like to look down?")
        print()
        #User decides which path to look down
        userPathLook = input("Please type 1, 2, or 3:  ")
        #User looks down first path
        if userPathLook == "1":
            print()
            print ("You look down path number 1 to your left. A large tree has fallen across it!")
            print()
            #add slight delay for gameplay flow
            time.sleep(1)
            print ("Would you like to go down this path or look at another?")
            print()
            userDecision1 = input("Your choices are: look, go: ")
        #User looks down second path
        elif userPathLook == "2":
            print()
            print ("You look down path number 2 straight ahead. There is a deep stream running across it.")
            print()
            #add slight delay for gameplay flow
            time.sleep(1)
            print ("Would you like to go down this path or look at another?")
            print()
            #add slight delay for gameplay flow
            time.sleep(1)
            userDecision1 = input("Your choices are: look, go: ")
        #User looks down third path
        elif userPathLook == "3":
            print()
            print ("You look down path number 3 to your right. There is a snake lying in the middle of it, basking in the sunlight.")
            print()
            #add slight delay for gameplay flow
            time.sleep(1)
            print ("Would you like to go down this path or look at another?")
            print()
            #add slight delay for gameplay flow
            time.sleep(1)
            userDecision1 = input("Your choices are: look, go:  ")
    #User decides to go down a specific path
    while userDecision1 == 'go':
        #User chose Path 1
        if userPathLook == "1":
            #Start Path 1, tree puzzle
            #Tree puzzle setup
            if userTreeDecision == '':
                print()
                print ("You decide to go down the left path.")
                print()
                print ("You walk up to the tree across the path. The large old sycamore looks like it fell down recently. It had to have been at least 200 years old.") 
                print ("The trunk is smooth and at least 3 feet across. You see what might be a very faint path to the left that leads away from the main trail further into the dark woods.")
                print()
                #add slight delay for gameplay flow
                time.sleep(1)
                print ("What would you like to do?")
                #Get user's tree puzzle decision
                print()
                userTreeDecision = input ("Your choices are: take new path, climb, go under:  ")
            #User decides to climb over tree, incorrect solution
            elif userTreeDecision == "climb":
                print()
                print ("You try to climb over the fallen tree, but the trunk is too big and too smooth! You slide back down to the ground.")
                #add slight delay for gameplay flow
                time.sleep(1)
                print()
                print ("What would you like to do?")
                print()
                #Get User's next tree puzzle decision
                userTreeDecision = input ("Your choices are: take new path, climb, go under:  ")
            #User decides to go under tree, incorrect solution
            elif userTreeDecision == "go under":
                print()
                print ("You try to go underneath the trunk of the tree, but it is too close to the ground. You almost get stuck!")
                #add slight delay for gameplay flow
                time.sleep(1)
                print()
                print ("What would you like to do?")
                print()
                #Get User's next tree puzzle decision
                userTreeDecision = input ("Your choices are: take new path, climb, go under:  ")
            #User decides to take new path, correct solution
            elif userTreeDecision == "take new path":
                print()
                print ("You follow the faint trail into the dark woods around the top of the fallen tree to the main path on the other side.")
                print()
                userDecision1 = 'correct'
                #Go to Game Over block below
        elif userPathLook == "2":
            #Start Path 2, stream puzzle
            #Stream puzzle setup
            if userStreamDecision == '':
                print()
                print ("You decide to keep going straight ahead.")
                print()
                print ("The stream is clear and sparkles in the sunlight. The sound of rushing water fills your ears. It looks more than a couple of feet deep. It is about 10 feet wide, ")
                print ("and very cold when you stick your hand in the water. You can see the main trail continue on the far side of the stream. A tree branch hangs low over the water.")
                print()
                #add slight delay for gameplay flow
                time.sleep(1)
                print ("What would you like to do?")
                #Get user's stream puzzle decision
                print()
                userStreamDecision = input ("Your choices are: jump, wade, use branch:  ")
            #User decides to jump over stream, incorrect solution
            elif userStreamDecision == "jump":
                print()
                print ("You take a few steps back to give yourself a running start, jump as far as you can...and land in the cold water.") 
                print ("You climb back out of the stream on the side you started on.")
                #add slight delay for gameplay flow
                time.sleep(1)
                print()
                print ("What would you like to do?")
                #Get user's stream puzzle decision
                print()
                userStreamDecision = input ("Your choices are: jump, wade, use branch:  ")
            #User decides to wade across stream, incorrect solution
            elif userStreamDecision == "wade":
                print()
                print ("You decide to try and wade across the stream. The water is deep and fast and the rocks are slippery. ")
                print ("You lose your footing, fall in, and climb back out of the stream on the side you started on.")
                #add slight delay for gameplay flow
                time.sleep(1)
                print()
                print ("What would you like to do?")
                #Get user's stream puzzle decision
                print()
                userStreamDecision = input ("Your choices are: jump, wade, use branch:  ")
            #User decides to use the branch, correct solution
            elif userStreamDecision == "use branch":
                print()
                print ("You grab the low hanging branch and use it to pull yourself across the stream. Your feet slip a few times, but ")
                print ("the branch keeps you from being swept away. You climb out of the stream on the far side.")
                print()
                userDecision1 = 'correct'
                #Go to Game Over block below
        elif userPathLook == "3":
            #Start Path 3, snake puzzle
            #Snake puzzle setup
            if userSnakeDecision == '':
                print()
                print ("You decide to go down the right path.")
                print()
                print ("The snake is in the middle of the path about 10 feet away from you. You try to take a closer look at the snake. You are not sure what kind of snake it is. ")
                print ("It is red, brown, and grey and looks about 4 feet long. There is a stick by the side of the path, as well as some rocks. The area around the snake is leafy and flat.")
                print()
                #add slight delay for gameplay flow
                time.sleep(1)
                print ("What would you like to do?")
                #Get user's snake puzzle decision
                print()
                userSnakeDecision = input ("Your choices are: poke snake, go around, throw rocks:  ")
            #User decides to poke the snake, incorrect solution
            elif userSnakeDecision == "poke snake":
                print()
                print ("You pick up the stick, creep closer to the snake, and poke it with the stick to try and make it move. ")
                print ("It coils aggressively and tries to bite you! (Don't poke snakes with sticks!)")
                #add slight delay for gameplay flow
                time.sleep(1)
                print()
                print ("What would you like to do?")
                print()
                #Get User's next snake puzzle decision
                userSnakeDecision = input ("Your choices are: poke snake, go around, throw rocks:  ")
            #User decides to throw rocks at snake, incorrect solution
            elif userSnakeDecision == "throw rocks":
                print()
                print ("You pick up a few rocks and throw them at the snake, trying to scare it away. You miss, thank goodness, ")
                print ("because you would have hurt the poor snake if you had hit it. (Not nice to throw rocks at snakes!)")
                #add slight delay for gameplay flow
                time.sleep(1)
                print()
                print ("What would you like to do?")
                print()
                #Get User's next snake puzzle decision
                userSnakeDecision = input ("Your choices are: poke snake, go around, throw rocks:  ")
            #User decides to go around the snake, correct solution
            elif userSnakeDecision == "go around":
                print()
                print ("You decide to leave the snake alone and go around it. You leave the path and slowly walk around the snake giving it lots of space. ")
                print ("The snake ignores you and continues to sleep in the sun. You meet back up with the main path on the far side of the snake.")
                print()
                userDecision1 = 'correct'
                #Go to Game Over block below

    #User has chosen correct solution for their puzzle, GAME OVER
    if userDecision1 == 'correct':
        #add slight delay for gameplay flow
        time.sleep(2)
        print()
        print ("Congratulations! You have successfully overcome the obstacle in your path!") 
        print()
        #add slight delay for gameplay flow
        time.sleep(1)
        print ("You feel awesome and continue your hike, seeing lots of birds and trees and animals on your adventure.")
        print()
        #add slight delay for gameplay flow
        time.sleep(1)
        #increment skill point counter
        userSkillPoint = userSkillPoint + 1
        print ("You just earned 1 hiking skill point!")
        print ("You have a total of " + str(userSkillPoint) + " so far! Good job!")
        print()
        print("*****************************************************************")
        print()
        print("GAME OVER")
        print()
        #add slight delay for gameplay flow
        time.sleep(1)
        #Ask user if they would like to restart the game
        print ("Would you like to play again?")
        print()
        mainGameInput = input("Type yes or no: ")

#End of main game code

#If user is done and breaks main while loop...
#User goodbye
print()
print("*****************************************************************")
print()
print ("Thank you for playing today!")
print ()
print ("You earned " + str(userSkillPoint) + " hiking skill points.")
print()
print ("Goodbye!")
time.sleep(3)