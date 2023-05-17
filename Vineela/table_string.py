#Find the values in a given string by using index of given table.
	   
str = "Hi Team, this is Vineela"
#here we are taken 2 table
table = 2
#consider an empty string
str1 = ""
length = 0
#Itrating string by using for loop
for i in str:
    #checking the condition of askey values
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        #condition is true add values to str1 variable
        str1 += i
        #adding length count to length variable
        length += 1
print(str1)
print(length)
#Itrating string index by using loop
for i in range(1, length+1):
    #multiply 2*index
    result = table * i
    #check the length of result and length
    if result < length:
        #print in table formate
        print(f"{table} * {i} = {str1[result]}")
