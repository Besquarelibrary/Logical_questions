class DutchColor:
    def dutch(elements):
        # Initialize three pointers: low, mid, and high
        low, mid, high = 0, 0, len(elements)-1
        
        # Partition the array into three regions: 0s, 1s, and 2s
        while(mid <= high):
            if elements[mid] == 0:
                # If the current element is 0, swap it with the element at the low index
                elements[mid], elements[low] = elements[low], elements[mid]
                low += 1
                mid += 1
            elif elements[mid] == 1:
                # If the current element is 1, move the mid pointer forward
                mid += 1
            else:
                # If the current element is 2, swap it with the element at the high index
                elements[mid], elements[high] = elements[high], elements[mid]
                high -= 1
        
        # Return the sorted array
        return elements
    

def main():
    # Call the dutch method of the DutchColor class with the input list [0, 1, 0, 2, 1, 0, 2, 0, 1, 2, 0]
    result = DutchColor.dutch([0, 1, 0, 2, 1, 0, 2, 0, 1, 2, 0])
    print('output:', result)
    
if __name__ == '__main__':
    # Call the main function when the script is run directly
    main()
