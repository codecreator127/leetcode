class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sorted_by_length = sorted(strs, key=len)

        prefix = sorted_by_length[0]

    	for i in range(1, len(sorted_by_length)):
            while prefix != sorted_by_length[i][0:len(prefix)]:
                prefix = prefix[0:len(prefix) - 1]

        return prefix
        
