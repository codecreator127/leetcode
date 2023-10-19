class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        output_s = ' ' * len(s)
        for i in range(len(s)):
            if s[i] != '#':
                output_s += s[i]
            else:
                output_s = output_s[:-1]

        output_t = ' ' * len(t)
        for i in range(len(t)):
            if t[i] != '#':
                output_t += t[i]
            else:
                output_t = output_t[:-1]
        
        if output_t.strip() == output_s.strip():
            return True
        return False

