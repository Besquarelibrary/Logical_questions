from collections import Counter
s='geeksogeeks'
a=Counter(s)
c=0
for i in a.values():
    if i%2==1:
        c=c+1
if c<=1:
    print('anagram pallidrome')
else:
    print('not anagram pallindrome')
