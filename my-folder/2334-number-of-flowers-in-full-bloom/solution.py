class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """

        def binary_search_intervals(arr, query, condition):
            left, right = 0, len(arr) - 1
            intervals = []

            while left <= right:
                mid = (left + right) // 2  # Calculate the middle index

                if arr[mid][condition] < query and condition == 1:
                    left = mid + 1
                elif arr[mid][condition] <= query and condition == 0:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        #num of intervals and queries
        intervals = flowers

        #sort intervals based on start times
        start_sorted_intervals = sorted(intervals, key=lambda x: x[0])
        end_sorted_intervals = sorted(intervals, key=lambda x: x[1])

        print(start_sorted_intervals)
        print(end_sorted_intervals)

        queries = people

        query_dict = {}

        output = []

        for q in queries:

            num_start = binary_search_intervals(start_sorted_intervals, q, 0)
            num_end = binary_search_intervals(end_sorted_intervals, q, 1)

            output.append(num_start - num_end)

            print(num_start)
            print(num_end)
            # print(num_start - num_end)

        return output


        
