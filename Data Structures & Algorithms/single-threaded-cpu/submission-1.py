class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:


        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()

        j = 0
        time = 0
        minHeap = []
        res = []



        while minHeap or j < len(tasks) :


            #if idle skip to the next available

            if not minHeap:
                time = max(time, tasks[j][0])

            
            while j < len(tasks) and time >= tasks[j][0]:
                enqueueTime, processingTime, idx = tasks[j]
                heapq.heappush(minHeap, [processingTime,idx,enqueueTime])
                j+=1


            if minHeap:
                processingTime,idx,enqueueTime = heapq.heappop(minHeap)
                res.append(idx)
                time+=processingTime
        
        return res





                

            
        
            
            
    
            



            

            





        