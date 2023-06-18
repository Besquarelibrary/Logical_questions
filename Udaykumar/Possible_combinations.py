# To find possible combinations for given number from selected list

# try to perform required logic operations
try:
    # maximum length of the input list
    max_len = int(input("Enter max length of list:"))
    # empty list to customize
    List = []
    # Loop to add elements into list
    for x in range(max_len):
        ele = int(input("enter ele to add in list:"))
        List += [ele]
    # Enter a number to find out combinations
    num = int(input("Enter a number:"))
    # Empty list to add combinations
    My_list = []
    # Iterating list to find possible combinations
    for i in List:
        # again iterating same list to compare elements with each other
        for j in List:
            # To find out possible combinations
            if i + j == num:
                # if statement to avoid duplicates
                if (i, j) not in My_list:
                    # adding possible combinations into list
                    My_list += [(i, j)]
            else:
                # extra loop to find next level combinations
                for k in List:
                    # if statement to avoid duplicates
                    if i + j + k == num:
                        # adding possible combinations into list
                        if (i, j, k) not in My_list:
                            My_list += [(i, j, k)]
    # To check if the list contain elements
    if any(My_list):
        print(My_list)
    else:
        print("No combinations found!")
# To avoid code crashing
except:
    print("Sorry..invalid input given...")

finally:
    pass
