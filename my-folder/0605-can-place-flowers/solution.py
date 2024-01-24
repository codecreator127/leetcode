class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) < 2 and flowerbed[0] == 1:
            return False
        if n > len(flowerbed):
            return False
        if len(flowerbed) < 2 and flowerbed[0] == 0 and n == 1:
            return True

        emptySpaces = 0

        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i + 1] == 0 and flowerbed[i] != 1:
                flowerbed[i] = 1
                emptySpaces += 1
            elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i] != 1:
                emptySpaces += 1
            elif 0 < i < len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    emptySpaces += 1

        return emptySpaces >= n


