# To short a list without using inbuilt methods
x = [9, 3, 5, 2, 67, 8]


def sorting(x):
    for i in range(len(x) - 1):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


print(sorting(x))
