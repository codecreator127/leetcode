class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        rolling_sum = 0
        for i in range(len(nums)):

            print(rolling_sum)
            print(total - rolling_sum)

            if rolling_sum == (total - nums[i] - rolling_sum):
                return i

            rolling_sum += nums[i]

        return -1
