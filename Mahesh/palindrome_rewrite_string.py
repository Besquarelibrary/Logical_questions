2. check whether given string is palindrome or not? Rewrite the string if you want?
a="geeksgeeks"
# converting string into list
a=list(a)
d1={}
for ele in a:
#     checking element is present d1 or not using if condition.
    if ele in d1:
#         if ele is present increase value of element(key)
        d1[ele]=d1[ele]+1
    else:
#         if ele is not present then ele value is 1 stored in d1
        d1[ele]=1
c=0
# checking values in d1 not keys
for value in d1.values():
#     modules of 2 by value if it equal to 1
    if value%2==1:
        c+=1
        
if c<=1:
    print("yes")
else:
    print("no")
output: yes

