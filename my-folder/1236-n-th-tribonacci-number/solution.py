class Solution:
    def tribonacci(self, n: int) -> int:
        
        sliding_window = [0, 1, 1]

        count = 2

        if n < 3:
            return sliding_window[n]

        else:
            while count < n:
                sliding_window.append(sliding_window[0] + sliding_window[1] + sliding_window[2])
                sliding_window.pop(0)
                count += 1

        
        return sliding_window[2]
