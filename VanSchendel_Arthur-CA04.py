#VanSchendel_Arthur-CA04
#11/2017
#This program is a 4 dices game, when you play it tells you what do you get (pair, two pairs, run of three, run of three with pair etc...)

def Main_menu():                 
    print("Main Menu")
    print("A. Numbers")
    print("B. Strings")
    print("C. Games")
    print("X. Exit")
    print("")
    option = input("Enter an option(A, B, C or X):")
    option = option.upper()          #user can put capital letter or not, it will work (for a,b,c or x of course)
    option_Game = False
    while option_Game == False:
        if option == "A" or option == "B" or option == "C" or option == "X":
            if option == "A":
                print("Option A is under programming")
            elif option == "B":
                print("Option B is under programming")
            elif option == "C":
                Game()
            elif option == "X":
                print("You exit the program")
            option_Game = True
        else:
            print("Please enter a correct option")
            print()
            print("Main Menu")
            print("A. Numbers")
            print("B. Strings")
            print("C. Games")
            print("X. Exit")
            print("")
            option = input("Enter an option(A, B, C or X):")
            option = option.upper()
    return option;

import random
import sys


def search_same(text, nb):
    count = counter.count(nb)  #count variable is to count the number of times a number comes out on the dice (ex: counts how many 2 you got)
    if count > 0:
        print(str(count)+' '+text)
        return True
    else:                #boolean value that way I can use it in the if statements to pass conditions
        return False

def search_run_from(start, length):         #search run from start position
    for i in range(length):
        if counter[start+i] == 0:
            return False
    return True

def search_run_counter(length):                 #search run from all valid start positions
    nb_run = 0
    for i in range(1, 6-length+2):             #first item of list useless, i stop at 6-length+2 because a run can start maximum at 4 : 4 - 5 - 6
        if search_run_from(i, length):
            nb_run += 1
    return nb_run

counter = [0]*7                      #counter : counts the number of times each number has been picked
def Game(): 
    for i in range(7):
        counter[i] = 0

    dices = []
    nb_dices = 4
    if len(sys.argv) > 1:        
        nb = int(sys.argv[1])

    for i in range(nb_dices):
        dices.append(random.randint(1,6))     #fill the list dices with the random numbers

    print("The score of the first dice is:",dices[0])
    print("The score of the second dice is:",dices[1])
    print("The score of the third dice is:",dices[2])
    print("The score of the fourth dice is:",dices[3])
    print()

    print(dices)
    print()
    sortdices = sorted(dices)
    print("In the right order:")
    print()
    print(sortdices)                     #list dices with the numbers in ascending order
    print()
                                    
    for dice in dices:
        counter[dice] += 1             

    print("You have got:")
    print()
    nb_run4 = search_run_counter(4)
    nb_run3 = search_run_counter(3)
    if (nb_run4 > 0):
        print(str(nb_run4)+ " Run of four")
    elif counter.count(2) > 0 and search_run_counter(3) > 0:
        print("Run of three with a pair")
    elif (nb_run3 >0):
        print(str(nb_run3)+" Run of three")
    elif search_same("Four the same", 4):
        print("")
    elif search_same("Three the same", 3):
        print("")
    elif search_same("Pair", 2):
        print("")
    else:
        print("All different")
    print("You are now returning to the main menu")
    print()


while Main_menu() != "X":
    print("")



    



