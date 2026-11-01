class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = len(nums) * [1] 

        if not nums:
            return 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(1 + dp[j], dp[i])

        return max(dp)







        