class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.strip().split()

        print(strings)

        print(strings.reverse())

        return " ".join(strings)


