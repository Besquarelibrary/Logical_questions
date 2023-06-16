# Function to implement combinations logic
def combinations(my_list):
    # New empty list to store resultant combinations
    result = []
    # Loops to generate elements for combinations by iterating given list
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            for k in range(j+1, len(my_list)):
                # Condition to eliminate duplicate combinations
                if my_list[i] != my_list[j] and my_list[i] != my_list[k] and my_list[j] != my_list[k]:
                    # Adding resultant elements into new list
                    result.append((my_list[i], my_list[j], my_list[k]))
    # storing new resultant list into function
    return result

# Input list
my_list = [2, 3, 4, 5]
# printing output using function calling
print(combinations(my_list))
