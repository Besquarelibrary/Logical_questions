# to find the given string is a anagram or not
num1=input("enter a string1:")
num2=input("enter a string2:")
# comparing  both the strings
if len(num1)==len(num2):
    count=0
# in i it will store the num1 characters
    for i in num1:
# if the characters of i in num2
        if i in num2:
# then increment the count 
            count+=1
# incremented values will stored in count
    print("anagram")
# if the given condition is not true
else:
    print("not a anagram")

