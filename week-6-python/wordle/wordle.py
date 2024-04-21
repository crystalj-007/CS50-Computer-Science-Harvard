# Game where user must guess what the secret word is within six tries

import sys
import random

# each of our text files contains 1000 words
LISTSIZE = 1000

# Define constants for game states
EXACT = 2
CLOSE = 1
WRONG = 0

# Define color codes for output
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def main():
    
    # Ensure proper usage: user omits a command line argument entirely
    # TODO #1
    
    if len(sys.argv) !=2:
        print ("Usage: python3 wordle.py wordsize")
        sys.exit(1)
    
    # ensure argv[1] is either 5, 6, 7, or 8 and store that value in wordsize instead
    # TODO #2 
    
    wordsize = 0 #is this line necessary?
    if sys.argv[1] <'5' or sys.argv[1]>'8':
        print ("Error: wordsize must be either 5, 6, 7, or 8")
        sys.exit(1)
        
    else:
        wordsize = int(sys.argv[1]) 
        
        
    
        
    ########################################################################
    # open correct file, each file has exactly LISTSIZE words
    # Define the file path based on wordsize (base code)
    wl_filename = f"{wordsize}.txt"
    try:
        wordlist = open(wl_filename, "r")
    except FileNotFoundError:
        print(f"Error opening file {wl_filename}.")
        sys.exit(1) 
        
        
        
    ###################################################################3
    # Load the word file into a list
    options = []

    with open(wl_filename, "r") as wordlist:
        options = [line.strip() for line in wordlist]

    # Pseudorandomly select a word for the game
    random.seed()
    choice = random.choice(options)

    # Allow one more guess than the length of the word
    guesses = wordsize + 1
    won = False
    
    # Print greeting with color
    print(f"{GREEN}This is WORDLE{wordsize}{RESET}")
    print(f"You have {guesses} tries to guess the {wordsize}-letter word I'm thinking of")
    #########################################################################
    
    # main game loop, one iteration for each guess
    for i in range(guesses):
        # Obtain user's guess
        guess = get_guess(wordsize)

        # TODO #4
        #set all elements of status array initially to 0, aka WRONG
        # Create a list to hold guess status, initially set to 0
        status = [WRONG] * wordsize  # Initialize with WRONG (0)

        # Calculate score for the guess
        score = check_word(guess, wordsize, status, choice)

        print(f"Guess {i + 1}: ", end="")

        # Print the guess
        print_word(guess, wordsize, status)

        # If they guessed it exactly right, terminate the loop
        if score == EXACT * wordsize:
            won = True
            print("You won!")
            break
        
    if won !=True:
        print(f"Sorry, you lost. The word is {choice}")
        
    
    #return 0



def get_guess(wordsize):
    # TODO 3. Prompt user for input. Ensure users actually provide a guess that is the correct length
    
    while True:
        word = input(f"Input a {wordsize}-letter word: ")
        if len(word)==wordsize:
            break
            
    return word       


def check_word (guess,wordsize, status, choice):
    # compare guess to choice and score points as appropriate, storing points in status
    # TODO #5
    
    score =0
    for i in range(wordsize):
        if guess[i] == choice[i]:
            status[i] = EXACT
            score += EXACT
        elif guess[i] in choice:
            if guess[i] != choice[i]:
                status[i] = CLOSE
                
            
    return score
            
    
    # HINTS
    # iterate over each letter of the guess
        # iterate over each letter of the choice
            # compare the current guess letter to the current choice letter
                # if they're the same position in the word, score EXACT points (green) and break so you don't compare that letter further
                #/ if it's in the word, but not the right spot, score CLOSE point (yellow)
        # keep track of the total score by adding each individual letter's score from above

def print_word(guess,wordsize, status):

    # print word character-for-character with correct color coding, then reset terminal font to normal
    # TODO #6
    
    for i in range(wordsize):
        if status[i] == EXACT:
            print(f"{GREEN}{guess[i]}{RESET}", end=" ")
        elif status[i] == CLOSE:
            print(f"{YELLOW}{guess[i]}{RESET}", end=" ")
        else:
            print(f"{guess[i]}", end=" ")
    print()
           
           
           
#if __name__ == "__main__":
main()
    
    
    