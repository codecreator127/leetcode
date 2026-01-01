class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        offset = 0
        longest_length = 0
        current_window = []
        for i in range(len(nums)):
            if nums[i] == 1:
                current_window.append(nums[i])
            else:
                if 0 not in current_window:
                    offset = 1
                    current_window.append(nums[i])
                else:
                    current_window = current_window[current_window.index(0) + 1:]
                    current_window.append(nums[i])

            longest_length = max(longest_length, len(current_window) - offset)
            

        return min(longest_length, len(nums) - 1)
