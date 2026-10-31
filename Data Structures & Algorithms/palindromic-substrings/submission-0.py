class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0


        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) -1 , -1, -1):
            for j in range(i, len(s)):
                length = j - i + 1

                if length == 1:
                    dp[i][j] = True

                elif length == 2:
                    dp[i][j] = s[i] == s[j]
 
                else:
                     dp[i][j] = s[i] == s[j] and dp[i +1][j - 1]
                

                if dp[i][j]:
                    count+=1
        return count

                

        
        