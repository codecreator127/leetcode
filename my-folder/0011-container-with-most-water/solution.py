class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        p1 = 0
        p2 = len(height) - 1
        maxh = max(height)

        while p1 < len(height) and p2 > 0 and p1 < p2:
            area = max((min(height[p1], height[p2]) * (p2 - p1)), area)

            if area >= (maxh * (p2 - p1)):
                break

            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1

        return area

