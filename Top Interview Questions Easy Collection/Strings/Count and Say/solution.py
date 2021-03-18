from typing import Dict, List

'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    - countAndSay(1) = "1"
    - countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into 
        a different digit string.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''

cache: Dict[int, str] = {
    1: '1'
}


def say(n: int):
    if n in cache:
        return cache[n]

    prepare_to_say = say(n - 1)

    current_char, times = prepare_to_say[0], 0
    say_sequence = []

    for c in prepare_to_say:
        if current_char != c:
            say_sequence += [str(times), current_char]
            current_char, times = c, 0
        times += 1

    say_sequence += [str(times), current_char]
    say_sequence = ''.join(say_sequence)
    cache[n] = say_sequence

    return say_sequence


def countAndSay(n: int) -> str:
    if n < 1:
        n = 1
    if n > 30:
        n = 30

    return say(n)


if __name__ == '__main__':
    import time
    for n in range(1, 31, 1):
        start_time = time.time()
        count_and_say = countAndSay(n)
        end_time = time.time()
        print(f'seq {n}\tcost time: {end_time-start_time}sec\tanswer {count_and_say}')
