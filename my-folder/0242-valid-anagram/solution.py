class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # naive method is to use set, but repeated chars?

        # if set(s) == set(t) and len(s) == len(t):
        #     return True
        # return False

        # O(n^2)

        # if (len(s) != len(t)):
        #     return False

        # # O(n)
        # list1 = list(t)

        # print(list1)

        # # O(n)
        # for letter in s:
        #     if letter not in list1:
        #         return False
            
        #     list1.remove(letter)

        # return True


        # better, use multiple for loops so O(n)

        if (len(s) != len(t)):
            return False

        dict1 = {}
        dict2 = {}

        for letter in s:
            if letter not in dict1:
                dict1[letter] = 1
            dict1[letter] += 1

        for letter in t:
            if letter not in dict2:
                dict2[letter] = 1
            dict2[letter] += 1

        
        for key in dict1.keys():
            if key not in dict2:
                return False
            if dict1[key] != dict2[key]:
                return False

        return True
