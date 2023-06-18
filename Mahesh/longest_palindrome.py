# check whether given array of items palindrome or not and grater digit palindrome in list?
l=[11,121,2551552,3234,13,234334]
c=[]
for i in l:
#     converting int into string and reversing int and check two strings equal or not
    if str(i)==str(i)[::-1]:
#         appending in c variable
        c.append(i)
print(c)
# comparing large palindrome in list
c=max(c)
c

output: [12, 121, 2551552]
	2551552
