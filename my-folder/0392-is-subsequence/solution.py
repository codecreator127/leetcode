class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if len(s) == 0:
            return False
        if len(s) > len(t):
            return False
        subsequence = 0
        for i in range(len(t)):
            if subsequence < len(s) and t[i] == s[subsequence]:
                subsequence += 1
        
        return subsequence == len(s)
