import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        output = math.log(n, 4)

        if output % 1 == 0:
            return True
        
        return False
        
