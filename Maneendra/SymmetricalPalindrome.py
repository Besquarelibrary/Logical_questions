class SymmetricalPalindrome:
    def symm_palin(string):
        # Calculate the index that divides the string into two halves
        half = len(string) // 2
        
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # If it is even, split the string into two halves
            first_half = string[half:]
            print(first_half)
            second_half = string[:half]
            print(second_half)
        else:
            # If it is odd, adjust the half index and split the string accordingly
            half = half + 1
            first_half = string[:half]
            second_half = string[half-1:]
        
        # Check if the two halves of the string are symmetrical
        if first_half == second_half:
            print('sym')
        else:
            print('not sym')
        
        # Check if the first half of the string is a palindrome
        if first_half == second_half[::-1]:
            print('palindrome')
        else:
            print('not palindrome')
            
            
def main():
    # Call the symm_palin method of the SymmetricalPalindrome class with the input string 'geeksoskeeg'
    sy_pa = SymmetricalPalindrome.symm_palin('geeksoskeeg')
    print(sy_pa)
    
    
if __name__ == '__main__':
    # Call the main function when the script is run directly
    main()
