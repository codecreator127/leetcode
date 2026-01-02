class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # intuition is double for loop, O(n^2)
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        # faster method
        # use hashmap, store seen nums in hashmap and then check if target - current = smt in seen

        seen = {}

        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [seen[target - nums[i]], i]
  
            if nums[i] not in seen:
                seen[nums[i]] = i
            
