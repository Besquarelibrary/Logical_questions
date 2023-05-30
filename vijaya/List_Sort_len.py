# The given 2 lists should be combined sorted and the output of the list should be in a sort way with the length 
L1 = [0, 3, 5, 6]
L2 = [2, 7, 1, 8, 4]
# Adding the two lsits.
L = L1+L2
#taken 2 loops 
for i in range(len(L)):
    for j in range(len(L)):
        #the value in l[i] should be less than l[j]
        if L[i] <= L[j]:
            #then swap the l[i] and l[j]
            L[i], L[j] = L[j], L[i]
#slice the elements in L which are before the length of l1
L1 = L[0:len(L1)]
#slice the elements in L which are after the length of L1
L2 = L[len(L1):]
print(L1, L2)
