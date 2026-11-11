class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #since A starts at 1 then a we need to have our original number and subtract one


        res = []

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            digit = chr(offset + ord('A'))
            res.append(digit)
            columnNumber = (columnNumber - 1) // 26
        
        res = "".join(res)
        return res[::-1]










        