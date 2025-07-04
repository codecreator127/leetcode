class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        # intuitive stupid way
        # use sb

        # s = 'a'
        # for o in operations:
        #     if o == 0:
        #         s += s
        #     elif o == 1:
        #         temp = s
        #         for letter in temp:
        #             s += chr(ord(letter) + 1)

        #             if (len(s) > k):
        #                 print(s)
        #                 return s[k - 1]
        
        #     if (len(s) >= k):
        #         return s[k - 1]

        # attempt 2, smarter way
        n, i = 1, 0

        while n < k:
            n *= 2
            i += 1
        d = 0

        while n > 1:
            if k > n // 2:
                k -= n // 2
                d += operations[i - 1]
            n //= 2
            i -= 1
        
        return chr(d % 26 + ord('a'))
