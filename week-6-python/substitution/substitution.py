import sys

def main():

    # 1. Ensure user provides single command-line argument (key)
    if len(sys.argv) !=2:
            print ("Usage: python substitution.py key")
            sys.exit(1)
                    
    # 2. Ensure key contains 26 characters       
    if len(sys.argv[1]) !=26:
        print("Key must contain 26 characters.")
        sys.exit(1)
        
    # 3. Ensure all characters are letters
    for i in range (len(sys.argv[1])):
        if str.isdigit(sys.argv[1][i]):
            print("All characters in key must be alphabetical")
            sys.exit(1)
         
    # 4. Ensure that there are no characters repeated
    # Convert all characters in key to lowercase
    sys.argv[1] = str.lower(sys.argv[1])    
    
    # Loop through key 
    for character in sys.argv[1]:
        # Count each character to check if they appear more than once
        if ((sys.argv[1]).count(character) > 1):
            print("No repeats")
            sys.exit(1)
                    
    # 5. Prompt user for input
    plaintext = input("Enter plaintext: ")
    
    # 6. Create empty string for ciphertext
    ciphertext=""
    
    # 7. Convert plaintext into ciphertext and append to ciphertext variable
    # For loop iterates length of plaintext number of times
    for i in range(len(plaintext)):
        
        # Execute this block if code if the character in the plaintext is an uppercase letter
        if str.isupper(plaintext[i]) and str.isalpha(plaintext[i]):
            # Variable postion stores real life position of character in the plaintext by minusing 65 from its ASCII value
            position = ord(plaintext[i])-65   
            
            # Add uppercase character from the key in the characters real life postion to string ciphertext
            ciphertext=  ciphertext+str.upper(sys.argv[1][position])
           
        # Execute this block if code if the character in the plaintext is a lowercase letter 
        elif str.islower(plaintext[i]) and str.isalpha(plaintext[i]):
            # Variable postion stores real life position of character in the plaintext by minusing 97 from its ASCII value
            position = ord(plaintext[i])-97  
            
            # Add lowercase character from the key in the characters real life postion to string ciphertext
            ciphertext=  ciphertext+str.lower(sys.argv[1][position])
        
        # For characters that are not letters
        else:
            ciphertext=ciphertext+plaintext[i]
    
    # 8. Print the ciphertext
    print(ciphertext)
       
if __name__ == "__main__":
    main()



