x = "The quick brown fox jump over the lazy dog"

Alpha = []

for i in range(65, 91):
    Alpha.append(chr(i))

# Method-1
print([ele if ele in x.upper() else "not there" for ele in Alpha])

# Method-2 
for ele in Alpha:
    if ele not in x.upper():
        print(ele, "Is not available...")

# Method-3
for ele in range(65, 91):
    if chr(ele) not in x.upper():
        print(chr(ele), "Not there")

# Method-4
print([chr(ele) if chr(ele) in x.upper() else "not there" for ele in range(65, 91)])
