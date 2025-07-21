class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        output = ''
        count = 0
        curr = None

        for l in s:
            if l != curr:
                curr = l
                count = 1
            elif l == curr:
                count += 1
            if count < 3:
                output += l
            elif count >= 3:
                continue
        return output
