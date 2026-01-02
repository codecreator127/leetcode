class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # use sorting to find same words
        # one pass, use hashmap to find duplicate anagrams
        # bucket idea, create a new bucket if new anagram is found
        # O(n · k log k)

        sorted_words = {}
        output = []

        for i in range(len(strs)):
            sorted_word = "".join(sorted(list(strs[i])))

            if sorted_word not in sorted_words:
                sorted_words[sorted_word] = len(output)
                output.append([strs[i]])

            else:
                output[sorted_words[sorted_word]].append(strs[i])

        return output
