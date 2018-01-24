import random
playagain = True
while playagain == True:
    playagain = False
    playerstart1 = random.randint(1,13)
    playerstart2 = random.randint(1,13)
    playertotal = playerstart1 + playerstart2
    computerstart1 = random.randint(1,13)
    computerstart2 = random.randint(1,13)
    computertotal = computerstart1 + computerstart2
    restart = True
    check = 11
    while check <= 13:
        if playerstart1 == check and check == 11:
            playerstart1 = "Jack"
            playertotal == playerstart2 + 10
            check = check + 1
        elif playerstart1 == check and check == 12:
            playerstart1 = "Queen"
            playertotal == playerstart2 + 10
            check = check + 1
        elif playerstart1 == check and check == 13:
            playerstart1 = "King"
            playertotal == playerstart2 + 10
            check = check + 1
        else:
            check = check + 1
        if playerstart1 == 1:
            playerstart1 = "Ace"
            playertotal = 11
    check = 11
    while check <= 13:
        if playerstart2 == check and check == 11:
            playerstart2 = "Jack"
            playertotal = playertotal - 1
            check = check + 1
        elif playerstart2 == check and check == 12:
            playerstart2 = "Queen"
            playertotal = playertotal - 2
            check = check + 1
        elif playerstart2 == check and check == 13:
            playerstart2 = "King"
            playertotal = playertotal - 3
            check = check + 1
        else:
            check = check + 1
    if playerstart2 == 1:
            playerstart2 = "Ace"
            playertotal = playertotal + 11
    check = 11
    while check <= 13:
        if computerstart1 == check and check == 11:
            computerstart1 = "Jack"
            computertotal = 10
            check = check + 1
        elif computerstart1 == check and check == 12:
            computerstart1 = "Queen"
            computertotal = 10
            check = check + 1
        elif computerstart1 == check and check == 13:
            computerstart1 = "King"
            computertotal = 10
            check = check + 1
        else:
            check = check + 1
    if computerstart1 == 1:
        computerstart1 = "Ace"
        computertotal = 11
    check = 11
    while check <= 13:
        if computerstart2 == check and check == 11:
            computerstart2 = "Jack"
            computertotal = computertotal - 1
            check = check + 1
        elif computerstart2 == check and check == 12:
            computerstart2 = "Queen"
            computertotal = computertotal - 2
            check = check + 1
        elif playerstart2 == check and check == 13:
            computerstart2 = "King"
            computertotal = computertotal - 3
            check = check + 1
        else:
            check = check + 1
        if computerstart2 == 1:
            computerstart2 = "Ace"
            if computertotal + 11 < 22:
                computertotal = computertotal + 11
            else:
                computertotal = computertotal + 1
                check = 11
    if playerstart1 == "Ace" and playerstart2 != "Ace":
        print("you have an " + playerstart1 + ", and a " + str(playerstart2))
    elif playerstart1 != "Ace" and playerstart2 == "Ace":
        print("you have a " + str(playerstart1) + ", and an " + playerstart2)
    elif playerstart1 == "Ace" and playerstart2 == "Ace":
        print("you have two Aces")
    else:
        print("you have a " + str(playerstart1) + ", and a " + str(playerstart2))
    answer = input("Do you want to hit or stay?\n")
    if answer == "hit":
        stillgoing = True
    elif answer == "stay":
        stillgoing = False
    else:
        while answer != "hit" and answer != "stay":
            print("please type hit or stay")
            answer = input("Do you want to hit or stay?\n")
            if answer == "hit":
                stillgoing = True
            if answer == "stay":
                stillgoing = False
    while stillgoing == True:
        if answer == "hit":
            firsthit = random.randint(1, 13)
            check = 11
            while check <= 13:
                    if firsthit == check and check == 11:
                        print ("you got a Jack")
                        playertotal = playertotal + 10
                        print("Your total value is " + str(playertotal))
                        check = check + 1
                    elif firsthit == check and check == 12:
                        print ("you got a Queen")
                        playertotal = playertotal + 10
                        print("Your total value is " + str(playertotal))
                        check = check + 1
                    elif firsthit == check and check == 13:
                        print("you got a King")
                        playertotal = playertotal + 10
                        print("Your total value is " + str(playertotal))
                        check = check + 1
                    else:
                        check = check + 1
            if firsthit == 1:
                    print("you got an Ace")
                    if playertotal + 11 > 21:
                        playertotal = playertotal + 1
                        print("Your total value is " + str(playertotal))
                    else:
                        playertotal = playertotal + 11
                        print("Your total value is " + str(playertotal))
            else:
                if firsthit != 11 and firsthit != 12 and firsthit != 13:
                    print("you got a " + str(firsthit))
                    playertotal = int(playertotal) + int(firsthit)
                    print("Your total value is " + str(playertotal))
                if playertotal > 21:
                    print("You busted!")
                    playagain = input("Do you want to play again?\n")
                    if playagain == "yes":
                        playagain = True
                        break
                    elif playagain == "no":
                        quit()
                else:
                    answer = input("Do you want to hit or stay?\n")
                    if answer == "hit":
                        stillgoing = True
                    elif answer == "stay":
                        stillgoing = False
                    else:
                        while answer != "hit" and answer != "stay":
                            print("Pleaase type hit or stay")
                            answer = input("Do you want to hit or stay?\n")
    if playagain == True:
        continue
    printonce = True
    if computertotal > 15:
        print("I have a " + str(computerstart1) + " and a " + str(computerstart2) + " so my total is " + str(computertotal) + " so I will stay")
    while computertotal <= 15:
        if printonce == True: 
                print("I have a " + str(computerstart1) + " and a " + str(computerstart2) + " so my total is " + str(computertotal))
                printonce = False
        print("I'm going to hit")
        comphit = random.randint(1,13)
        if comphit > 1 and comphit < 11:
            computertotal = computertotal + comphit
            print("I got a " + str(comphit) + " and my total is now " + str(computertotal))
            while check <= 13:
                if comphit == check and check == 11:
                    comphit = 10
                    computertotal = computertotal + comphit
                    check = check + 1
                elif comphit == check and check == 12:
                    comphit = 10
                    computertotal = computertotal + comphit
                    check = check + 1
                elif comphit == check and check == 13:
                    comphit = 10
                    computertotal = computertotal + comphit
                    check = check + 1
                else:
                    check = check + 1
            if comphit == 1:
                print("I got an Ace")
                if computertotal + 11 > 21:
                    computertotal = computertotal + 1
                    print("My total value is " + str(computertotal))
                else:
                    computertotal = computertotal + 11
                    print("My total value is " + str(computertotal))
        if computertotal > 21:
            print("I busted")
            playagain = input("Do you want to play again?\n")
            if playagain == "yes":
                playagain = True
            elif playagain == "no":
                playagain = False
    if playertotal >= computertotal:
        print("My total was " + str(computertotal))
        print("You win!")
        playagain = input("Do you want to play again?\n")
        if playagain == "yes":
            playagain = True
        elif playagain == "no":
            quit()
        continue
    else:
        print("My total was " + str(computertotal))
        print("You lose")
    playagain = input("Do you want to play again?\n")
    if playagain == "yes":
        playagain = True
    elif playagain == "no":
        quit()
