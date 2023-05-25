1. compare two strings whether anagrams or not?
a="beesquare"
b="squarebee"
d1={}
d2={}
for ele in a: 
#   checking element is present d1 or not using if condition.
    if ele in d1:
#       if ele is present increase value of element(key)
        d1[ele]+=1
    else:
#       if ele is not present then ele value is 1 stored in d1
        d1[ele]=1
for ele in b:
    if ele in d2:
        d2[ele]+=1
    else:
#       if ele is not present then ele value is 1 stored in d1
        d2[ele]=1
#     comparing two dict 
print(d1==d2)
output: True


#compare two strings whether anagrams or not?
a="goodboymahesh"
b="maheshgoodboy"
# c,d are sorted a,b it will display according to alphabetical order
c=sorted(a)
d=sorted(b)
if len(a)==len(b):
#     comparing c abd d
    if c==d:
        print("yes")
    else:
        print("no")
else:
    print("not an")
output: yes
-------------------- ---- ----------------------------------------------------------------------------------------------------------------

# compare two strings whether anagrams or not?
s="ghhheeks"
s2="skeeghhh"
for char in s:
#     comparing count of each character in string using count function
    if s2.count(char)!=s.count(char):
        print("no")
        break
else:
    print("yes")
output: yes

