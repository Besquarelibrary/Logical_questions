#Find the values in a given string by using index of given table.

str = "This is mahesh from besquare"
#here we are taken table using user input
n = (int(input("enter a number)))
#consider an empty string
s = ""
c = 0
#Itrating string by using for loop
for i in str:
    #checking the condition of askey values if it is not in range of askey value ignore it
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        #condition is true add values to s variable
        s += i
        #adding length count to c variable
        c += 1
print(s)
print(c)
#Itrating string index by using loop from start index 1 to len(c)
for i in range(1, c+1):
    #multiply n*index
    result = n * i
    #check the length of result is graterthan c
    if result < c:
        #print in table formate using print function
        print(f"{n} * {i} = {s[c]}")
output: enter a number 5
               5*1=i
               5*2=e
               .
               .
               .
               .
               etc...
