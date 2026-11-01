class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
        if total_sum  % 2 == 1:
            return False

        target = total_sum / 2

        dp = set()


        for num in nums:
            additional = []

            for number in dp:
                additional.append(number + num)
            
            for i in range(len(additional)):
                dp.add(additional[i])
            
            dp.add(num)
        
        if target in dp:
            return True
        
        return False



 

        