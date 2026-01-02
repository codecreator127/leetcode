class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # intuition method
        # use a dictionary to store checked nums
        # worst case: O(n)
        # best case: O(2)

        duplicates = {}    
        for num in nums:
            if num not in duplicates:
                duplicates[num] = 1
            else:
                return True

        return False


        # attempt 2: try use set + length
        # O(n)
        # if (len(set(nums)) < len(nums)):
        #     return True
        # return False

