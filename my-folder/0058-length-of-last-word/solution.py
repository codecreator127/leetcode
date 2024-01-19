class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        listOfWords = s.split(" ")

        return len(listOfWords[len(listOfWords) - 1])
