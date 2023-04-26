import re

sentence='mahesh is very bad boy'
sentence='mahesh  $ is @ very bad @ boy'
words = re.findall('\w+', sentence)
print(words)
for i in words:
    print(i)

reverse_sentence = ' '.join(words[i] for i in range(len(words) - 1,-1,-1))


print(reverse_sentence)


