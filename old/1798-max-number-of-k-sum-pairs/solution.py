class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        p1 = 0
        p2 = len(nums) - 1


        count = 0
        nums.sort()

        while p1 < p2:
            if nums[p1] + nums[p2] == k:
                count += 1
                p1 += 1
                p2 -= 1
            elif nums[p1] + nums[p2] < k:
                p1 += 1
            elif nums[p1] + nums[p2] > k:
                p2 -= 1

        return count
            
