class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        highest = 0

        for i in range(len(gain)):
            curr += gain[i]
            highest = max(highest, curr)

        return highest
