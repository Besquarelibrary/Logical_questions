class ReverseString:
    def rev_str(string):
        # Create an empty list to store individual words
        words = []
        
        # Create an empty string to store the current word being formed
        current_word = ""
        
        # Iterate over each character in the input string
        for each in string:
            # Check if the character is equal to a space
            if each == " ":
                # If it is a space, add the current_word to the list of words
                words.append(current_word)
                
                # Reset the current_word to an empty string
                current_word = ""
            else:
                # If it is not a space, concatenate the character to the current_word
                current_word += each
        
        # Add the last word (after the last space) to the list of words
        words.append(current_word)
        print('words:', words)
        
        # Reverse the order of the words and store them in rev_word
        rev_word = words[::-1]
        print('rev_word:', rev_word)
        
        # Join the words in rev_word with spaces in between and assign it to the variable result
        result = " ".join(rev_word)
        
        # Return the final reversed string
        return result
        
        
def main():
    # Call the rev_str method of the ReverseString class with the input string 'Besquare Technology pvt ltd'
    final_result = ReverseString.rev_str('Besquare Technology pvt ltd')
    print(final_result)
    
    
if __name__ == '__main__':
    # Call the main function when the script is run directly
    main()
