from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        output = []

        for i in range(len(s)):
            if s[i] != '*':
                output.append(s[i])
            else:
                output.pop()

        return "".join(output)
