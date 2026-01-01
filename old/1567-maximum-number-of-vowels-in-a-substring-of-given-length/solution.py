class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'

        vowel_num = 0
        output = 0
        left = 0
        curr_substring = ''

        for i in range(k):
            if s[i] in vowels:
                vowel_num += 1
                
        output = max(output, vowel_num)

        for i in range(k, len(s)):
            if s[left] in vowels:
                vowel_num -= 1

            if s[i] in vowels:
                vowel_num += 1

            left += 1
            output = max(output, vowel_num)
    

        return output
