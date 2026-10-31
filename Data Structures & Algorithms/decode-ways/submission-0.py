class Solution:
    def numDecodings(self, s: str) -> int:
        #reccurance relation = #num ways to decode prev + num_ways to decode new one
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        if s[0] == "0":
            dp[1] = 0
        
        else:
            dp[1] = 1


        for i in range(2, len(s) + 1):

            char = s[i-1]

            if 0 < int(char) and int(char) <= 9:
                dp[i] += dp[i-1]
            
            two_digit = int(""+s[i-2] + s[i-1])

            if 10 <= two_digit and two_digit <= 26:
                dp[i] += dp[i-2]
        

        return dp[len(s)]
            

            

            
    
            

