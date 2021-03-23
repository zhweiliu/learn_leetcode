from typing import List

'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. \
For numbers which are multiples of both three and five output “FizzBuzz”.
    
Example 1:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        ret: List[str] = []
        for i in range(n):
            num = i + 1

            s = ''

            if num%3 == 0:
                s = 'Fizz'

            if num%5 == 0:
                s += 'Buzz'

            if len(s) == 0:
                s = str(num)

            ret.append(s)

        return ret


if __name__ == '__main__':
    n = 15

    sol = Solution()
    print(sol.fizzBuzz(n))

