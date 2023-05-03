def jumpingnumber(x):
    for i in range(x + 1):
        if (i < 10):
            print(i, end=" ")
            continue
        check = 1
        temp = i
        digit = temp % 10
        temp //= 10
        while (temp > 0):
            if (abs(digit - temp % 10) != 1):
                check = 0
                break
            digit = temp % 10
            temp //= 10
        if (check):
            print(i, end=" ")


x = 45
# y = max(jumpingnumber)
jumpingnumber(x)
