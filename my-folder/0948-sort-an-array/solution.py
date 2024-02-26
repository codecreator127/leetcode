import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # quick sort


        def quicksort(nums):

            if len(nums) <= 1:
                return nums

            pivot = random.choice(nums)

            lower, equal, higher = [], [], []

            for n in nums:
                if n > pivot:
                    higher.append(n)
                elif n < pivot:
                    lower.append(n)

                else:
                    equal.append(n)

            return quicksort(lower) + equal + quicksort(higher)

        return quicksort(nums)
