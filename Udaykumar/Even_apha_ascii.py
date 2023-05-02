# To print ascii value of char by adding +4, if count & ascii value of that char is even

My_str = "Besquare_Technologies"
My_Dict = {}

# Method-1
for ele in My_str:
    if (ord(ele)) % 2 == 0:
        if My_str.count(ele) > 1 and My_str.count(ele) % 2 == 0:
            My_Dict[ele] = My_str.count(ele)
print(My_Dict)

for key in My_Dict:
    if My_Dict[key] == max(My_Dict.values()):
        print(ord(key)+4)
    else:
        print(key, "Not allowed")


# Method-2
count = 0
for ele in My_str:
    if (ord(ele)) % 2 == 0:
        for j in My_str:
            if ele == j:
                count += 1
                if count > 1 and count % 2 == 0:
                    My_Dict[ele] = count
    count = 0
print(My_Dict)
for key in My_Dict:
    if My_Dict[key] == max(My_Dict.values()):
        print(ord(key)+4)
    else:
        print(key, "Not allowed")


