# Determine the winner of a short scrabble-like game, where two players each enter their word, and the higher scoring player wins.

def compute_score(word):
    POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

    score = 0
    for i in range(len(word)):
        if str.islower(word[i]) and str.isalpha(word[i]):
            position=ord(word[i])-97
            score = score+POINTS[position]
        
        if str.isupper(word[i]) and str.isalpha(word[i]):
            position=ord(word[i])-65
            score = score+POINTS[position]
        
        else:   
            score=score+0
    
    return score

def main():

    word1 = input("Player 1: ")
    word2 = input("Player 2: ")
    
    score1=compute_score(word1)
    score2=compute_score(word2)
    
    print(f"Player 1 score: {score1}")
    print(f"Player 2 score: {score2}")
    
    if score1>score2:
        print("Player 1 wins")
        
    elif score2>score1:
        print("Player 2 wins")
    
    else:
        print("Tie")


if __name__ == "__main__":
    main()
    
    
