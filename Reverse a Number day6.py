"""Problem statement
You are given a number 'n'.
Return an integer that is the reverse of ‘n’.
Note:
Reverse of ‘n’ means an integer where, the most significant digit of ‘n’ is the least significant digit of the number, the second most significant digit of ‘n’ is the second least significant digit of the number and so on. """
from typing import List

def reverseNumber(n: int) -> int:
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num
