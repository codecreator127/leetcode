class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """

        count = 1
        letter = None

        for l in word:
            if l == letter:
                count += 1
            letter = l

        print(count)

        return count

