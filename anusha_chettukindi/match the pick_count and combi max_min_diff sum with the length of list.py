PROGRAM TO PRINT THE COMBINATIONS WHEN THE COMBINATION MIN MAX MAX DIFFERENCE AND PICK COUNT SUM MATCHED WITH THE LENGTH OF THE LIST

CODE IN PYTHON:
________________________
#initialize the list
l=[4,3,2,1,6,2]
#to store the combinations
l1=[]
#to store the combinations in a list without duplicate combinations
l2=[]
#when there is no combinations exist in the list
flag=0
#pick count to piuck the elements from the existed list and store it in the new list l1
pick_count=3
#loop through the list every element exist in each combinations
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            #storing the values in the list
            l1.append(l[i])
            l1.append(l[j])
            l1.append(l[k])
            #to sort elements in ascending order
            l1.sort()
            #for checking is there any combination exist like l1
            if l1 not in l2:
                #to add the new combination to the l2
                l2.append(l1)
                #to store the difference of maximum and minimum value in the list
                max=l1[2]
                min=l1[0]
                max_min_diff=max-min
                sum=pick_count+max_min_diff
                #to compare the sum with length of list
                if(sum==len(l)):
                    flag=1
                    #to print the matched combinations list
                    print("pick_count matched length combinations are:",l1)
                    #to store new combination 
                    l1=[]
                #when that combination not matched with the length
                else:
                    l1=[]
#for indicating no combinations in the list
if(flag==0):
    print("No combinations exist in this list which match witch the pickcount diff sum")

OUTPUT:
pick_count matched length combinations are: [1, 3, 4]
pick_count matched length combinations are: [3, 4, 6]
pick_count matched length combinations are: [1, 2, 4]
pick_count matched length combinations are: [1, 2, 4]
