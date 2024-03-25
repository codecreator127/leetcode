class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #brute force

        duplicates = {}

        output = []
        for num in nums:
            if num not in duplicates:
                duplicates[num] = 1
            else:
                output.append(num)


        return output
