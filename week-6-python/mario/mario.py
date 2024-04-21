# Objective: Create two half pyramids using # for steps

def main ():

    # 1. Establish variables for spaces and hashes (steps)
    space = " "
    step = "#"
    
    # 2. Use get height function to prompt user for input
    height = get_height()

    # 3. Create pyramid using for loop which loops from 1 to the height 
    for row in range(1, height+1):
        
        # Number of spaces corresponds the height minus the current row. This also ensures an extra space isnt printed on the last row
        print(space*(height-row), end="")
        
        # Number of steps is the same as the row
        print(step*row, end="")
        
        # Print 2 spaces
        print(space*2, end="")
        
        # Print steps for the other half of the pyramid
        print(step*row)

# Function prompts user to enter a valid height 
def get_height():
    
    # While loop ensures user will continue to be prompted for input until they enter valid input 
    while True:
        
        # Try-Except statement: allows program to take alternative actions in case error occurs
        # Try code: executed to prompt user for valid input (height = integer between 1 and 8) and height is returned if input is valid
        try:
            height=int(input("Enter the height: "))
            if height >=1 and height <=8:
                return height
        
        # Except code will execute if there is an error (user does not input an integer)
        except ValueError:
            print("Not an integer")

if __name__ == "__main__":
    main()