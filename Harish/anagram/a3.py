from collections import Counter
s='geeksogeeks'
s1='skeegeeksgo'
if Counter(s)==Counter(s1):
    print('Anagram')
else:
    print('Not Anagram')
