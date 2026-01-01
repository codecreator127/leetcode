from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = []

        # def binary_search(num):
        #     left = 0
        #     right = len(potions) - 1

        #     mid = (left + right) // 2

        #     potions.sort()
        #     while left <= right:
        #         if potions[mid] >= num:
        #             right = mid - 1
        #         else:
        #             left = mid + 1

        #         mid = (left + right) // 2

        #     return (len(potions)) - (right + 1)

        potions.sort()
        for i in range(len(spells)):

            target = success / spells[i]

            output.append(len(potions) - bisect_left(potions, target))

        return output

