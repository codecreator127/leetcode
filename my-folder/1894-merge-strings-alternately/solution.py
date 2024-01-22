class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(len(word1)):
            output += word1[i]
            if i < len(word2):
                output += word2[i]

        if len(word2) > len(word1):
            output += word2[len(word1):]

        return output
