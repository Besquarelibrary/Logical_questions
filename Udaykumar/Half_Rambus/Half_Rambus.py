rows = 7  # Number of rows in the pattern
columns = 4  # Number of columns in the pattern

def patterns():
    # Iterate over each row
    for row in range(1, rows + 1):
        
        # Print the asterisks for each column in increasing order
        for column in range(1, columns + 1):
            print(column * " *")  # Print asterisks based on the current column
        
        # Print the asterisks for each column in decreasing order
        for column in range(columns - 1, 0, -1):
            print(column * " *")  # Print asterisks based on the current column in reverse order
        
        break  # Exit the loop after the first iteration

patterns()  # Call the patterns function to execute the code

