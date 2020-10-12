import random
import math
import sys

# Fill array manually
def FillManually(arrayToFill):
    OutputArray(arrayToFill)

    for i in range(4):
        boatSize = 4-i
        for j in range(i+1):
                if(boatSize > 1):
                    print(u"\u001b[44m\nVvedite koordinati nachala i konca korablya s razmerom " + str(boatSize) + u" :\u001b[0m\n")
                    boatStartX = int(input(u"\u001b[44mNachalo X:\u001b[0m "))
                    boatStartY = int(input(u"\u001b[44mNachalo Y:\u001b[0m "))
                    boatEndX = int(input(u"\u001b[44mKonec X:\u001b[0m "))
                    boatEndY = int(input(u"\u001b[44mKonec Y:\u001b[0m "))
                    print("\n")

                    for k in range(boatSize):
                        stepY = int(k * abs(boatEndX - boatStartX) / (boatSize - 1))
                        stepX = int(k * abs(boatEndY - boatStartY) / (boatSize - 1))
                        arrayToFill[boatStartY + stepX][boatStartX + stepY] = 1

                    for k in range(boatSize):
                        stepY = int(k * abs(boatEndX - boatStartX) / (boatSize - 1))
                        stepX = int(k * abs(boatEndY - boatStartY) / (boatSize - 1))

                        for m in range(3):
                                for n in range(3):
                                    if (boatStartY + stepX + (m-1) >= 0 and boatStartX + stepY + (n-1) >= 0 and boatStartY + stepX + (m-1) <= 9 and boatStartX + stepY + (n-1) <= 9):
                                        if (arrayToFill[boatStartY + stepX + (m-1)][boatStartX + stepY + (n-1)] != 1):
                                            arrayToFill[boatStartY + stepX + (m-1)][boatStartX + stepY + (n-1)] = 3


                    OutputArray(arrayToFill)
                else:
                    print("\nVvedite koordinati nachala i konca korablya s razmerom " + str(boatSize) + " :")
                    boatPosX = int(input("Position X: "))
                    boatPosY = int(input("Position Y: "))
                    print("\n")
                    
                    arrayToFill[boatPosY][boatPosX] = 1

                    for m in range(3):
                                for n in range(3):
                                    if (boatPosY + (m-1) >= 0 and boatPosX + (n-1) >= 0 and boatPosY + (m-1) <= 9 and boatPosX + (n-1) <= 9):
                                        if (arrayToFill[boatPosY + (m-1)][boatPosX + (n-1)] != 1):
                                            arrayToFill[boatPosY + (m-1)][boatPosX + (n-1)] = 3

                    OutputArray(arrayToFill)

    print(u"\u001b[41m\nPole zapolnino!\u001b[0m\n\n")

# Fill array auto
def FillAuto(arrayToFill):
    for i in range(4):
        boatSize = 4-i
        for j in range(i+1):
                if(boatSize > 1):
                    p = False

                    while(p == False):
                        f = False

                        boatStartX = int(math.floor(random.random() * 9.99999))
                        boatStartY = int(math.floor(random.random() * 9.99999))
                        direction = int(math.floor(random.random() * 3.99999))

                        if (direction < 2):
                            directionToGo = -1
                        else:
                            directionToGo = 1
                        

                        if (direction == 0):
                            if (boatStartX - (boatSize - 1) < 0):
                                continue
                            else:
                                boatEndX = boatStartX - (boatSize - 1)
                                boatEndY = boatStartY
                        if (direction == 1):
                            if (boatStartY - (boatSize - 1) < 0):
                                continue
                            else:
                                boatEndX = boatStartX
                                boatEndY = boatStartY - (boatSize - 1)
                        if (direction == 2):
                            if (boatStartX + (boatSize - 1) > 9):
                                continue
                            else:
                                boatEndX = boatStartX + (boatSize - 1)
                                boatEndY = boatStartY
                        if (direction == 3):
                            if (boatStartY + (boatSize - 1) > 9):
                                continue
                            else:
                                boatEndX = boatStartX
                                boatEndY = boatStartY + (boatSize - 1)

                        # Putting boat
                        for k in range(boatSize):
                            stepY = int(k * abs(boatEndX - boatStartX) / (boatSize - 1))
                            stepX = int(k * abs(boatEndY - boatStartY) / (boatSize - 1))

                            if (arrayToFill[boatStartY + stepX*directionToGo][boatStartX + stepY*directionToGo] == 1 or arrayToFill[boatStartY + stepX*directionToGo][boatStartX + stepY*directionToGo] == 3):
                                f = True
                                break

                            arrayToFill[boatStartY + stepX*directionToGo][boatStartX + stepY*directionToGo] = 1
                            
                        if (f == True):
                            continue

                        # Putting 3 around boat
                        for k in range(boatSize):
                            stepY = int(k * abs(boatEndX - boatStartX) / (boatSize - 1))
                            stepX = int(k * abs(boatEndY - boatStartY) / (boatSize - 1))

                            #print (stepX)
                            #print (stepY)

                            for m in range(3):
                                for n in range(3):
                                    if (boatStartY + stepX*directionToGo + (m-1) >= 0 and boatStartX + stepY*directionToGo + (n-1) >= 0 and boatStartY + stepX*directionToGo + (m-1) <= 9 and boatStartX + stepY*directionToGo + (n-1) <= 9):
                                        if (arrayToFill[boatStartY + stepX*directionToGo + (m-1)][boatStartX + stepY*directionToGo + (n-1)] != 1):
                                            arrayToFill[boatStartY + stepX*directionToGo + (m-1)][boatStartX + stepY*directionToGo + (n-1)] = 3



                        # OutputArray(arrayToFill)

                        p = True


                if(boatSize == 1):
                    g = False

                    while(g == False):

                        boatPosX = int(math.floor(random.random() * 9.99999))
                        boatPosY = int(math.floor(random.random() * 9.99999))

                        # print (str(boatPosX) + " " + str(boatPosY))

                        if (arrayToFill[boatPosY][boatPosX] == 0):
                            arrayToFill[boatPosY][boatPosX] = 1
                            
                            for m in range(3):
                                for n in range(3):
                                    if (boatPosY + (m-1) >= 0 and boatPosX + (n-1) >= 0 and boatPosY + (m-1) <= 9 and boatPosX + (n-1) <= 9):
                                        if (arrayToFill[boatPosY + (m-1)][boatPosX + (n-1)] != 1):
                                            arrayToFill[boatPosY + (m-1)][boatPosX + (n-1)] = 3

                            # OutputArray(arrayToFill)
                            g = True                  


                #OutputArray(arrayToFill)

    print(u"\n\u001b[44mPole zapolnino!\u001b[0m")

# Creating array
def CreateArray():
    array = [0] * 10
    for i in range(10):
        array[i] = [0] * 10
    return array

# Output array
def OutputArray(arrayOut):
 
    # print(u"\u001b[2J");

    print(u"\u001b[34m    0 1 2 3 4 5 6 7 8 9")
    print("    |||||||||||||||||||\u001b[0m")
    i = 0
    for row in arrayOut:
        print(u"\u001b[34m"+str(i) + "---\u001b[0m" + ' '.join([str(elem) for elem in row]))
        i+=1

# Game
def Play (CArray, PArray):
    displayComputerArray = CreateArray()
    displayPlayerArray = CreateArray()
    shotsComputerArray = CreateArray()
    shotsPlayerArray = CreateArray()

    a = 3
    while(True):

        computerCountX = 0
        playerCountX = 0
        
        for i in range(len(CArray)): 
            for j in range(len(CArray[0])): 
              if (CArray[i][j] == 1 and shotsComputerArray[i][j] == 1):
                    displayComputerArray[i][j] = "X"
                    computerCountX += 1
              if (CArray[i][j] == 0 and shotsComputerArray[i][j] == 1):
                    displayComputerArray[i][j] = "0"
              if (CArray[i][j] == 0 and shotsComputerArray[i][j] == 0):
                    displayComputerArray[i][j] = "_"
              if (CArray[i][j] == 1 and shotsComputerArray[i][j] == 0):
                    displayComputerArray[i][j] = "_"
              if (CArray[i][j] == 3 and shotsComputerArray[i][j] == 0):
                        displayComputerArray[i][j] = "_"
              if (CArray[i][j] == 3 and shotsComputerArray[i][j] == 1):
                    displayComputerArray[i][j] = "0"

        for i in range(len(PArray)): 
            for j in range(len(PArray[0])): 
              if (PArray[i][j] == 1 and shotsPlayerArray[i][j] == 1):
                    displayPlayerArray[i][j] = "X"
                    playerCountX += 1
              if (PArray[i][j] == 0 and shotsPlayerArray[i][j] == 1):
                    displayPlayerArray[i][j] = "0"
              if (PArray[i][j] == 0 and shotsPlayerArray[i][j] == 0):
                    displayPlayerArray[i][j] = "_"
              if (PArray[i][j] == 1 and shotsPlayerArray[i][j] == 0):
                    displayPlayerArray[i][j] = "_"
              if (PArray[i][j] == 3 and shotsPlayerArray[i][j] == 0):
                        displayPlayerArray[i][j] = "_"
              if (PArray[i][j] == 3 and shotsPlayerArray[i][j] == 1):
                    displayPlayerArray[i][j] = "0"
        
        if (playerCountX == 20):
            print("YOU LOSE :(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(:(")
            break
        if (computerCountX == 20):
            print("YOU WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break

        print("Computer")
        OutputArray(displayComputerArray)
        print("\n")
        print("Player")
        OutputArray(displayPlayerArray)

        if(a%2 != 0):
            print("\n\n STRELIAY!")
            shotX = int(input("X: "))
            shotY = int(input("Y: "))
            print("\n\n")

            shotsComputerArray[shotY][shotX] = 1

            if (CArray[shotY][shotX] == 1):
                print("POPAL!!!!\n\n")
                continue
        else:
            print("\n\nSTRELIAYET COMPUTER!\n\n")
            shotX = int(math.floor(random.random() * 9.99999))
            shotY = int(math.floor(random.random() * 9.99999))

            if (PArray[shotY][shotX] == 1):
                continue

            shotsPlayerArray[shotY][shotX] = 1

            if (PArray[shotY][shotX] == 1):
                print("COMPUTER POPAL!!!!\n\n")
                continue
        a+=1



computerArray = CreateArray()
FillAuto(computerArray)

playerArray = CreateArray()
FillManually(playerArray)

print ("\n")

Play(computerArray,playerArray)