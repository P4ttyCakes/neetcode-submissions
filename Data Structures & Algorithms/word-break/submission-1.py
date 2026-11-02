class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) -1, -1, -1):


            for word in wordDict:
                print(word, i)
                if i + len(word) > len(s):
                    continue

                if word == s[i: i + len(word)]:
                    
                    print("found_match", s[i: i + len(word)])
                    dp[i] = dp[i + len(word)]

                
                if dp[i] == True:
                    break
        
        return dp[0]




            



        