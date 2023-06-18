sentence = "Hello world, how are you?"
words = []
current_word = ''
for char in sentence:
    if char == ' ':
        # words.append(current_word)
        words=words+[current_word]
        current_word = ''
    # else:
    current_word += char

if current_word:
    words.append(current_word)

print(words)