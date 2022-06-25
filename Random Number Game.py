import random         # Import RNG

lowDigit = 1          # Bottom line for random number
highDigit = 100       # Top line for random number
digit = 0             # Computer chosen random number
countInput = 0        # Amount of guesses
win = False           # Guessed the number?
playGame = True       # Does game continue?
x = 0                 # User typed number
startScore = 100      # Starting score number
score = 0             # Current score number
maxScore = 0          # Maximum score per current session
# =========================================================

# -------------- MainLoop
while (playGame):
    digit = random.randint(lowDigit, highDigit)                      # Guessing number
    # print(f"Chosen number is:  {digit}")                           # ---- Это чит код
    print("^" * 50)                                                  # Formating
    countInput = 0                                                   # Number of tries to guess
    score = startScore                                               # Default score
    print("The computer guessed the number, try to guess it!")
    
    # ---------- InnerLoop
    while (not win and score > 0):                                   # Loop responsible for 1 round
        print("~" * 50)                                              # Formating                            
        print("If you want to leave current round press 0")          # and 
        print(f"Current score: {score}")                             # text
        print(f"Your RECORD: {maxScore}")                            # output
        
        x = ""                                                       # Resetting X for while loop conditions 
        while (not x.isdigit()):                                     # Controling input of INTEGER
            x = input(f"Input number from {lowDigit} till {highDigit}: ")
            if (not x.isdigit()):
                print("."*30 + "Input INTEGER please!")

        x = int(x)                                                   # Converting STR input to INT data type
        
        if (x == digit):                                             # If user guessed the number
            win = True                                               # Than victory
        elif (x == 0):                                               # Manual end of round with 0
            win = True
        else:                                                        # If user didn't guess, showing tips
            length = abs(x - digit)
            
            if (length < 3):
                print("\nBurning!")
            elif (length < 5):
                print("\nHot!")
            elif (length < 10):
                print("\nWarm")
            elif (length < 15):
                print("\nChill")
            elif (length < 20):
                print("\nCold!")
            else:
                print("\nDead Freezing")
                
            if (countInput == 7):
                score -= 10                                           # Decreasing score for TIP
                if(digit % 2 == 0):
                    print("Number is even")
                else:
                    print("Number is odd")
            elif (countInput == 6):
                score -= 8
                if (digit % 3 == 0):
                    print("Number splits by 3")
                else:
                    print("Number doesn't split by 3")
            elif (countInput == 5):
                score -= 4
                if (digit % 4 == 0):
                    print("Number splits by 4")
                else:
                    print("Number doesn't split by 4")
            elif (countInput > 2 and countInput < 5):
                score -= 2
                if (x > digit):
                    print("Computer number is SMALLER than yours")
                else:
                    print("Computer number is BIGGER than yours")
            elif (score < 15 and score > 4):                          # Random instance, number changes to range from 1 to 5
                if (random.randint(0, 100) < 30):
                    print("You are boring, I guessed another number! (Pssss... From 1 to 5")
                    digit = random.randint(1,5)
                    
            score -= 5                                                # Score decrease each guess
        countInput += 1                                               # Number of guesses made increase
    
    if(x == digit):                                                   # Eiher victory or lose anouncement
        print("$" * 50)
        print(f"CONGRATULATIONS! You are victorious! Right number is: {digit}")
    else:
        print(f"Sorry! You are out of score! \nRight number is: {digit}")

    if (input("Enter - Play again. 0 - Exit the game ") == "0"):      # Allows user to play again or exit
        playGame = False
    else:
        win = False
        
    if (score > maxScore):                                            # Writing down records
        maxScore = score
        
print("|" * 50)                                                       # Empty input(), to show farewell sign
input("""Thank you for your time!                                             
Comeback again, next game will be even better!
Good luck!
P.S Press Enter once again, to close""")
quit()