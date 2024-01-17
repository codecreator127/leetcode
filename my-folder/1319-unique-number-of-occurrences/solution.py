class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # sort list first
        arr.sort()

        print(arr)

        # iterate through array once, keeping a track of number
        occur_dict = {}
        
        occurences = 0
        current_num = arr[0]
        for i in range(len(arr)):
            if (arr[i] != current_num):
                current_num = arr[i]
                
                if occurences in occur_dict.keys():
                    return False
                else:
                    occur_dict[occurences] = 1

                occurences = 0
            occurences += 1

        if occurences in occur_dict.keys():
            return False
        else:
            occur_dict[occurences] = 1
        return True
