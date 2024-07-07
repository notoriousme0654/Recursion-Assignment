class Recursion:
    def pow(n):
        if n == 1:
            return True
        elif n % 3 == 0 and n != 0:
            n = n // 3
            return Recursion.pow(n)
        return False

class Solution:
    def isPowerOfThree(self, n):
        a = Recursion()
        return a.pow(n)
