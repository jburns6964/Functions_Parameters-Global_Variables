##dice roll program
#generates a random number and displays it as a dice. can be used for games 

#IMPORTS#
import random
import time

#GRAFICS#
s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

#FUNCTIONS#
def roll():
    print("rolling.....")
    roll = random.randint(1,6)
    return roll
    

def show_dice(roll):
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)
    elif roll == 0:
        pass

    ##MAIN BIT##
end = "false"
    #ASKING STUFF#
Q = input("would you like me to roll the dice?(yes or no) ")
    #YES TO ASKING BIT#
if Q == "yes":
    #ASKING 'BOUT ROLLING TILL A SIX IS ROLLED#
        M = input("would you like me to roll intill I roll a 6?(yes or no) ")
    #YES TO ASKING 'BOUT ROLLING TILL A SIX IS ROLLED#
        if M == "yes":
            while end == "false":
                Roll = roll()
                show_dice(Roll)
                if Roll == 6:
                    end = "true"
                else:
                    pass
    #NO TO ASKING 'BOUT ROLLING TILL A SIX IS ROLLED AND INSTEAD ASKING 'BOUT ROLLING TILL THE SAME TWO NUMBERS ARE ROLLED#
        elif M == "no":
            N = input("would you like me to roll intill I roll two numbers that are the same in a row?(yes or no) ")
            ends = "no"
    #YES TO ROLLING TILL SAME TWO NUMBERS ROLLED AFTER EACH OTHER#
            if N == "yes":
                while ends == "no":               
                    Roll = roll()
                    show_dice(Roll)
                    rall = Roll
                    Roll = roll()
                    show_dice(Roll)
                    if rall == Roll:
                        ends = "yes"
    #SAYING NO TO THE ROLLING TILL SAME TWO NUMBERS ROLLED AFTER EACH OTHER BIT# 
            elif N == "no":
                pass
    
    #BIT 'BOUT SAYING NO TO EVERYTHING#
elif Q == "no":
    pass
    

#ERRORS: missing brackets, misspelled words, no return in function, etc.
