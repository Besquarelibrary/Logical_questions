class Solution:
    def jumpingNums(self, number):
        # decrementing the loop
        for next in range(number, 0, -1):
            # taking 'Non_Jump' to counting the Non Jumping nums
            Non_Jump = 0
            # converting the given integer number to a string
            string = str(next)
            # taking 'length' to counting the length of the string
            length = 0
            for count in string:
                length += 1
            for each in range(length - 1):
                # comparing each numbers difference equal to '1'
                if (int(string[each]) - int(string[each+1])) ** 2 != 1:
                    Non_Jump = 1
            # compare Non_Jump count is == 0
            if Non_Jump == 0:
                return next


def main():
    solution = Solution()
    result = solution.jumpingNums(8769)
    print(result)
    

if __name__ == '__main__':
    main()
