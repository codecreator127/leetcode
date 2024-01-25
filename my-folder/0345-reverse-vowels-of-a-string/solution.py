class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = "aeiou"
        s = list(s)
        print(s)

        wordvowels = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                wordvowels.append(s[i])
                s[i] = "_"

        wordvowels.reverse()

        print(wordvowels)

        count = 0
        for i in range(len(s)):
            if s[i] == "_":
                s[i] = wordvowels[count]
                count += 1
        return ''.join(s)
        


        
