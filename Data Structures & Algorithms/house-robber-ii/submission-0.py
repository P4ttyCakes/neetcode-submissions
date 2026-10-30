class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
                return nums[0]     

        def rob_help(nums: List[int]) -> int:
            if not nums:
                return 0

            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)


            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i-1])

            
            return dp[-1]




        no_first_house = rob_help(nums[1:])
        no_last_hosue = rob_help(nums[:-1])

        return max(no_first_house, no_last_hosue)



        