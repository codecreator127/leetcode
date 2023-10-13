class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        #choose path 1 or path 2

        path1 = cost[0]
        path2 = cost[1]

        for i in range(2, len(cost)):
            chosen_path = cost[i] + min(path1, path2)

            path1 = path2
            path2 = chosen_path

        return min(path1, path2)

