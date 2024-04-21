import csv
import sys

# Databases.csv: STR counts for a list of individuals --> large.csv, small.csv
# Sequences.txt: contains DNA sequence to identify    --> 1.txt ... 20.txt

def main():

    # 1. Check for command-line usage. Ensure there are 3 command line arguements
    if len(sys.argv) !=3:
        print("Usage: python3 dna.py databases/csv_file.csv sequences/txt_file.txt")
        sys.exit(1)
    
    # 2. Open the CSV file and read its contents into memory (Read database file into a variable)
    # Create empty list to store rows of database file
    database_list = []
    
    # Open CSV file (sys.argv[1]), specify the file path and the mode (read). "with" ensures file automatically closes when done
    # 'database' is the file object that represents the opened CSV file in read mode
    # Create a CSV reader object 'database_reader' using csv.reader() which allows you to read the contents of the file
    # Append each row to database_list
    with open(sys.argv[1], "r") as database:     
         database_reader = csv.reader(database)   
         for row in database_reader:
             database_list.append(row)
             print(row)  
 
    # 3. Read DNA sequence file into a variable
    # sequence contains the contents of the DNA sequence from the file. 
    with open (sys.argv[2], "r") as file:
        sequence=file.read()  
        #print(sequence)
        
    # 4. Find longest match of each STR in DNA sequence
    # Create list of first row in csv file ['name', 'AGATC', 'AATG', 'TATC']
    STR_list = list(database_list[0]) 
    
    # Remove first element (name)  ['AGATC', 'AATG', 'TATC']
    STR_list.pop(0) 
    
    # 5. Convert database values to int
    # Start from the second row to skip the headerS
    for row in database_list[1:]:  
        
        # Start from the second element to skip the name
        for i in range(1, len(row)):  
            row[i] = int(row[i])
    
    # Create list of longest matches of each STR
    # Create empty list to store values of longest matches of each STR. 
    longest_matches_list=[]
    
    # Loop through STR_list and find longest match of each using longest match function
    for i in STR_list:
        longest_matches_list.append(longest_match(sequence, i))
    
    # 6. Check which person in the database has the same match count as in the longest_matches_list
    # Create empty list to store matches
    match = []

    # Loop iterates for the length of STR_list
    for i in range(len(STR_list)):
        
        # Loop for length of databsae_list i.e. 
        for j in range(1, len(database_list)):
            
            # List slice to skip header and name. If list slice in each element of database_list = longest_matches_list
            if database_list[j][1:] == longest_matches_list[i:]:
                
                # Append the name to the matches list
                match.append(database_list[j][0])

    # Check if matches were found
    # If there is a match, print the match
    if match:
        print(match[0])
    
    # Else print no match    
    else:
        print("No match")    
        
         
# Function finds the longest match of each STR in a sequence (given)
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
