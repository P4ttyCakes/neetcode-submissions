class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #we need to find the divisor that can make uo both strings


        def isDivisor(i):
            if len(str1) % i != 0 or len(str2) % i != 0:
                return False
            
            f1 = len(str1) // i
            f2 = len(str2) // i

            if str1[:i] * f1 == str1 and str1[:i] * f2 == str2:
                return True
            
            return False
    

        for i in range(min(len(str1),  len(str2)) , 0, -1):
            if isDivisor(i):
                return str1[:i]
        
        return ""




        