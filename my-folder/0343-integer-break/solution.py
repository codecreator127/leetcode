class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            total = 1
            while n > 4:
                total *= 3
                n -= 3
            
            total *= n
            return total
