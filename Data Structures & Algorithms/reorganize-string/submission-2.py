class Solution:
    def reorganizeString(self, s: str) -> str:

        maxHeap = []
        max_num = 0
        res = ""

        freq = defaultdict(int)
        for char in s:
            freq[char]+=1
            max_num = max(max_num, freq[char])
        
        if max_num > ((len(s) + 1) // 2 ):
            return ""

        waiting_list = []

        for key, value in freq.items():
            heapq.heappush(maxHeap, [-1 * value, key])

        
        while maxHeap or waiting_list:

            if maxHeap:
                value, key = heapq.heappop(maxHeap)
                res+=key
                value+=1
            
            else:
                value = None
                key = None
            

            if waiting_list:
                heapq.heappush(maxHeap, waiting_list[0])
                waiting_list.pop()
            
            if key and value:
                waiting_list.append([value,key])

        return res

        




        


        

        

        






        