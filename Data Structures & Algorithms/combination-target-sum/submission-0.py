class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(arr, curr, k):

            if curr == target:
                res.append(list(arr))
                return
            

            for i in range(k, len(nums)):
                if curr + nums[i] <= target:
                    arr.append(nums[i])

                    dfs(arr, curr + nums[i],  i)
                    arr.pop()
        
        dfs([],0, 0)
        return res


        