"""
Print the star_pattern
"""


def right_angle(num):
    for value in range(0, num):
        space = '  ' * value
        star = '* ' * (num - value)
        print(space + star)


# calling the star_pattern function
right_angle(10)
