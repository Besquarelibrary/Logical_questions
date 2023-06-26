# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter a number:"))

# Iterate over a range from 1 to num+1 (inclusive) to represent rows
for rows in range(1, num+1):
    # Iterate over a range from 1 to rows+1 (inclusive) to represent columns
    for columns in range(1, rows+1):
        # Print the current column number without a newline character
        print(columns, end='')

    # Print a newline character to move to the next line after printing the columns for the current row
    print()

