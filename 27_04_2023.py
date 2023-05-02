# To findout if number is armstrong & prime from the given list like L = [1, 10, 30] that will be 1, 110, 11030...

My_List = [1, 21, 53, 7, 9]
completed_interations_count = 0
armstrong_number = 0
flag = False

for ele in My_List:
    while completed_interations_count == 0:
        for s in str(ele):
            armstrong_number += int(s) ** len(str(ele))
    
        if armstrong_number == ele:
            flag = True
        else:
            flag = False
            
        if flag:
            print(ele, "is an Armstrong number")
        else:
            print(ele, "is not an Armstrong number")

        if ele > 1 and all(ele % i != 0 for i in range(2, ele)):
            print(ele, "is a prime number")
        else:
            print(ele, "is not a prime number")

        completed_interations_count += 1

    while completed_interations_count < len(My_List)-1:
        for e in range(1, len(My_List)):
            ele = int(str(My_List[0]) + str(My_List[e]))
            armstrong_number = 0
            
            for s in str(ele):
                armstrong_number += int(s) ** len(str(ele))
                
            if armstrong_number == ele:
                flag = True
            else:
                flag = False
                
            if flag:
                print(ele, "is an Armstrong number")
            else:
                print(ele, "is not an Armstrong number")

            if ele > 1 and all(ele % i != 0 for i in range(2, ele)):
                print(ele, "is a prime number")
            else:
                print(ele, "is not a prime number")

            completed_interations_count += 1

