class Solution(object):
    # def minOperations(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
        
    #     #sorted set
        # unique_nums = sorted(set(nums))
        # n = len(nums)


        # i = 0
        # j = 0
        # min_ops = n
        # for i in range(len(unique_nums)):
        #     while j < len(unique_nums) and unique_nums[j] - unique_nums[i] <=len(nums) - 1:
        #         j+=1
        #         min_ops = min(min_ops , n -(j - i))
        # return min_ops

#   class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #find largest gap between adjacent nums
        n = len(nums)

        sorted_nums = sorted(set(nums))
        min_op = n

        j = 0

        for i in range(len(sorted_nums)):
            while j < len(sorted_nums) and sorted_nums[j] - sorted_nums[i] <= n - 1:
                j += 1
                min_op = min(min_op, n - (j - i))

        return min_op

