import math

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = [1]

        for i in range(1, rowIndex + 1):
            output.append(output[-1] * (rowIndex - i + 1) // i)
    	
        return output

