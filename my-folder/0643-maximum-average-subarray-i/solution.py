class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = curr = 0

        for i in range(k):
            curr += nums[i]

        biggest = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[left]

            biggest = max(biggest, curr)
            left += 1

        return biggest / k

