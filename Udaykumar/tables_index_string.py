num = int(input("Enter a number for table:"))   # Number for table
My_str = "Hello This is Besquare"   # Input String

# With In-built methods

# Loop for table multiplications
for ele in range(1, len(My_str)+1):
    # Storing multiplication result into Var
    Result = num * ele
    # Comparing Result with Length of the string & Index of value of string
    if Result < len(My_str) and My_str[Result] != " ":
        print(num, "*", ele, "=", My_str[Result])
    elif Result < len(My_str) and My_str[Result] == " ":
        print(num, "*", ele, "=", My_str[Result + 1])
    # If the string index out of range else block will be excecuted
    else:
        print("Sorry!, String length range exceeded...")
        break

# Without In-Built Methods

Length = 0      # Var to store length of the string

# Loop to find length of the string
for ele in My_str:
    Length += 1

# Loop for table multiplications
for ele in range(1, Length+1):
    # Storing multiplication result into Var
    Result = num * ele
    # Comparing Result with Length of the string & Index of value of string
    if Result < Length and My_str[Result] != " ":
        print(num, "*", ele, "=", My_str[Result])
    elif Result < Length and My_str[Result] == " ":
        print(num, "*", ele, "=", My_str[Result + 1])
    # If the string index out of range else block will be excecuted
    else:
        print("Sorry!, String length range exceeded...")
        break

