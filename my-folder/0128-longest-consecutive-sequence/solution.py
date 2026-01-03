class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # intuition, one pass for O(n), use set to get unique, and just do while loop to check if max
        # only check if it is start of sequence, i.e. num -1 don't exist

        numSet = set(nums)

        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
