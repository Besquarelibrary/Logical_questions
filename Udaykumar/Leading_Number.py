# To find leading numbers level by level.
def find_leader_numbers(x):
    while x:
        M = max(x)
        print(M)
        I = x.index(M)
        x = x[I + 1:]


x = [12, 3, 10, 5, 7]
find_leader_numbers(x)

