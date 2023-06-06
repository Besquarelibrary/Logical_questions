# Importing Data from Data module
from Data import Data

# Input String from user
My_str = input("Enter a string, which contain Uppercase letters:")

# try block to perform given logic
try:
    # Iterating the characters from given string
    for ele in My_str:
        # Fetching the value of the char using dict
        print(Data[ele], end="")
# To avoid code crashing
except:
    print("Invalid input given")

finally:
    pass
