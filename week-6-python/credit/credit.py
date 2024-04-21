# Objective: Validate credit card numbers using the Luhn Algorithm, and return whether a valid card number is Mastercard, Visa or Amex.

import math 

def main():
    
    # 1. Prompt user for valid input using get_number function
    number = get_number()

    # 2. Calculate the check sum: 
    # Multiply every other digit by 2 from second to last digit and add product's digits together
    # Add sum to sum of digits that werent multiplied by 2
    # Valid if total is a round number
    
    # Establish variable sum and set to 0
    sum=0
    for i in range(1, 10):
        
        # Access individual digits by dividing number by mod 10 to a power
        # Then divide by 10 to a power. Use floor division // to drop decimal
        digit =  (number % math.pow(10, i*2))//math.pow(10, i*2-1)
        
        # Multiply digit by 2
        digit=digit*2
        
        # Add digits of that product to sum
        # Access individual digits by divding by %10 to get remainder and floor divsion by 10 (drops decimal)
        sum=sum +(digit % 10) + (digit // 10)
        
    # Establish variable sum2 to store sum of digits that weren't multiplied by 2
    sum2=0
    for i in range(1,10):
        
        # Same logic as before
        digit2 = (number % math.pow(10, i*2-1))//math.pow(10, i*2-2)
        sum2=sum2+digit2

    # Add sum totals. Total should be round number
    total = sum+sum2
    
    # 3. Check card for length and starting digits
    # Establish variable for length of card number
    length = len(str(number))

    # Execute code if the total is a round number (no remainder when mod by 10)
    if total%10==0:
        
        # VISA starts with 4 and has 13 or 16 digits
        if (length== 13 or length== 16) and str(number)[0]=='4':
            print("VISA")
            
        # MASTERCARD starts with 51, 52, 53, 54 or 55 and has 16 digits
        elif length== 16 and str(number)[0]=='5' and (str(number)[1]=='1' or str(number)[1]=='2' or str(number)[1]=='3' or str(number)[1]=='4' or str(number)[1]=='5'):
            print("MASTERCARD")
         
        # AMEX starts with 34 or 37 and has 15 digits   
        elif length== 15 and str(number)[0]=='3'and (str(number)[1]=='4' or str(number)[1]=='7'):
            print("AMEX")
    
    # Print invalid if card number doesnt meet any of the conditions      
    else:
        print ("INVALID")
        

# Function prompts user to enter a valid card number 
def get_number():
    
    # While loop ensures user will continue to be prompted for input until they enter valid input 
    while True:
        
        # Try-Except statement: allows program to take alternative actions in case error occurs
        # Try code: executed to prompt user for valid input (positive integer) and number is returned if input is valid
        try:
            number=int(input("Enter a card number: "))
            if number >=0:
                return number
        
        # Except code will execute if there is an error (user does not input an integer)
        except ValueError:
            print("Not a valid card number ")
            
if __name__ == "__main__":
    main()  