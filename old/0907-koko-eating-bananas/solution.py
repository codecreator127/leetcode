class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1

        right = max(piles)

        
        speed = right
        while left <= right:
            mid = (left + right) // 2

            time = 0
            # calculate total time to eat at this speed
            for bananas in piles:
                time += math.ceil(bananas / mid)

            if time <= h:
                speed = min(speed, mid)
                right = mid - 1

            else:
                left = mid + 1

        return speed

