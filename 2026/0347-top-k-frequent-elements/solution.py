class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate through, use dict to store seen nums and frequency
        # get sorted list from dict, and return the first k nums

        # seen = {}

        # for num in nums:
        #     if num not in seen:
        #         seen[num] = 1
        #     else:
        #         seen[num] += 1

        # output = []

        # sorted_list = [k for k, _ in sorted(seen.items(), key=lambda item: item[1], reverse=True)]

        # return sorted_list[0:k]

        ## bucket sort

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        output = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)

                if (len(output) == k):
                    return output
