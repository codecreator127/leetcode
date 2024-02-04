class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #sliding window

        p1 = 0
        count = 0
        lives = k
        max_ones = 0

        p2 = 0
        while lives > 0 and p2 < len(nums):
            if nums[p2] == 1:
                count += 1
            if nums[p2] == 0:
                count += 1
                lives -= 1
            p2 += 1
        
        max_ones = count

        if p2 >= len(nums):
            return len(nums)

        while p2 < len(nums):
            print(count)
            if nums[p2] == 1:
                count += 1

            elif nums[p2] == 0:
                lives -= 1
                count += 1
                
                while lives < 0:
                    if nums[p1] == 0:
                        p1 += 1

                        lives += 1
                        count -= 1

                    elif nums[p1] == 1:
                        p1 += 1
                        count -= 1
        
            p2 += 1
            max_ones = max(max_ones, count)


        return max_ones
