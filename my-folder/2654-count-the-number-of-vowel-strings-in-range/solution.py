class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowelStrings = words[left:right + 1]



        vowels = ['a','e','i','o','u']

        count = 0

        for word in vowelStrings:
            if word[0] in vowels and word[len(word) - 1] in vowels:
                count += 1

        return count
