# Prompt user to type in some text, and then output the grade level for the text, according to the Coleman-Liau formula

def main():
    # 1. Prompt user for text
    text = input("Text: ")
    
    # 2. Establish variables which stores the number of letters, words and sentences, respectively
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # 3. Calculate index using Coleman-Liau formula
    L=((letters*1.0)/words)*100
    S=((sentences*1.0)/words)*100
    index = round(0.0588 * L - 0.296 * S - 15.8)
    
    # 4. Print grade level
    if index>1 and index<16:
        print("Grade", index)
        
    elif index<1:
        print("Before Grade 1")
        
    else:
        print("Grade 16+") 
        

# Function to count the number of  letters in text
def count_letters(text):
    letters=0
    
    # Determine which of the characters in the text are letters
    for i in range(len(text)):
        if str.isalpha(text[i]):
            letters+=1
            
    return letters


# Function to count the number of words in the text
def count_words(text):
    spaces=0
    
    # Determine how many spaces are in the text
    for i in range (len(text)):
        if str.isspace(text[i]):
            spaces+=1
            
    # Incremement by 1 because there is one less space than there are words       
    words = spaces+1
    
    return words


# Function to count the number of sentences in the text
def count_sentences(text):
    sentences=0
    
    # Determine how many fullstops, question marks or exclamation marks there are in the text
    for i in range(len(text)):
        if text[i]=="." or text[i]=="?" or text[i]=="!":
            sentences+=1
            
    return sentences

if __name__ == "__main__":
    main()  