class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = float("inf")

        for i in range(len(strs)):
            s1 = strs[i]
            min_len = min(len(s1), min_len)
        



        common_prefix = ""
        for i in range(min_len):
            char = strs[0][i]
            for j in range(len(strs) - 1):
                string1 = strs[j]
                string2 = strs[j+1]

                if string1[i] != string2[i]:
                    return common_prefix
            
            common_prefix+=char
        
        return common_prefix


                





        