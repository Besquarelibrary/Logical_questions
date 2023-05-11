L1 = [0, 3, 5, 6]
L2 = [2, 7, 1, 8, 4]

L = L1+L2
for i in range(len(L)):
    for j in range(len(L)):
        if L[i] <= L[j]:
            L[i], L[j] = L[j], L[i]

L1 = L[0:len(L1)]
L2 = L[len(L1):]

print(L1, L2)
