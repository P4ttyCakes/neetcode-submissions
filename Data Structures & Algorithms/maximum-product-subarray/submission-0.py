class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        if len(nums) > 0:
            dp[0] = nums[0]
            curr_min = dp[0]

        else:
            return 0

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] * nums[i], curr_min * nums[i])

            curr_min =  min(nums[i], dp[i-1] * nums[i], curr_min * nums[i])



        return max(dp)


        


        