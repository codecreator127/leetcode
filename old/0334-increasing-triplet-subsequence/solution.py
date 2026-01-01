import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        max1 = float('inf')
        max2 = float('inf')

        for i in range(len(nums)):
            if nums[i] <= max1:
                max1 = nums[i]
            elif nums[i] <= max2:
                max2 = nums[i]
            else:
                return True

        return False

