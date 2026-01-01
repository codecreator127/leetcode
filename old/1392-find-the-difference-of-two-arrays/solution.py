class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        out1 = list(set(nums1) - set(nums2))
        out2 = list(set(nums2) - set(nums1))

        return [out1, out2]



        # # brute force

        # output = [[],[]]
        # for num in nums1:
        #     if num not in nums2 and num not in output[0]:
        #         output[0].append(num)

        # for num in nums2:
        #     if num not in nums1 and num not in output[1]:
        #         output[1].append(num)


        # return output
