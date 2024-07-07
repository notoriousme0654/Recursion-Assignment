class Solution(object):
    def isPowerOfTwo(self, n):
        if n >= 1 and (n & (n - 1)) == 0:
            return True
        return False
