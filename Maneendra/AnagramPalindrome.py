class AnagramPalindrome:
    def ana_palindrome(word):
        # Create an empty dictionary to store character frequencies
        dict_word = {}
        
        # Iterate over each character in the word (word)
        for i in word:
            # Check if the character (i) is already present in dict_word
            if i in dict_word:
                # If it is, increment its frequency by 1
                dict_word[i] += 1
            else:
                # If it is not, initialize its frequency to 1
                dict_word[i] = 1
        
        # Print the character frequencies for debugging purposes
        print(dict_word)
        
        # Count the number of characters with odd frequencies
        odd = 0
        for j in dict_word.values():
            if j % 2 == 1:
                odd += 1
        
        # Check if there are more than 1 characters with odd frequencies
        if odd > 1:
            return 'False'
        else:
            return 'True'
            
            
def main():
    # Call the ana_palindrome method of the AnagramPalindrome class with the word 'geeksogeeks'
    ana = AnagramPalindrome.ana_palindrome('geeksogeeks')
    print(ana)
    

if __name__ == '__main__':
    # Call the main function when the script is run directly
    main()
