class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        
        count = 1
        for i in range(len(chars) - 1):
            current = chars[i]
            if chars[i + 1] != current:
                s += chars[i]
                if count != 1:
                    s += str(count)
                count = 1
            else:
                count += 1

        s += chars[-1]
        if count != 1:
            s += str(count)
        print(s)
        
        for i in range(len(chars)):
            if i < len(s):
                chars[i] = s[i]

        chars = chars[:len(s)]

        return len(chars)
            

