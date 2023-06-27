"""
    Print the Half Rhombus Star Pattern
"""


# implemented the half_rhombus_pattern logic
def half_rhombus_pattern(size):
    for row in range(1, size+1):
        for col in range(1, row+1):
            print("* ", end='')
        print()
    for row in range(1, size):
        for col in range(size-row, 0, -1):
            print("* ", end="")
        print()


# calling the half_rhombus_pattern function        
def main():
    num = int(input("Enter the value: "))
    half_rhombus_pattern(num)


# call main function
if __name__ == "__main__":
    main()

