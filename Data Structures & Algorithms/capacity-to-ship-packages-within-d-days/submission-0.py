class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def can_load(capacity):
            days_taken = 1
            total = 0
            for weight in weights:

                if total + weight <= capacity:
                    total+= weight
                
                else:
                    days_taken+=1
                    total = weight
            
            if days_taken <= days:
                return True
            
            return False

        

        l = max(weights)
        r = sum(weights)


        while l < r:
            m = (r + l) // 2

            if can_load(m):
                r = m
            
            else:
                l = m +1
        
        return r



        