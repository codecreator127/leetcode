class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #increasing order
        #find start and end
        #binary search

        left = 0
        right = len(nums) - 1

        
        output = [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]


        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                end = mid

                while start > 0 and nums[start - 1] == target:
                    start -= 1
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                
                return [start, end]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return output
            
            
            
        
