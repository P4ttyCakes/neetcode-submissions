class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = defaultdict(int)

        for task in tasks:
            freq[task]+=1

        
        maxHeap = []


        for val in freq.values():
            heapq.heappush(maxHeap, [-1 * val, 0])

        time = 0
        waitingList = []

        while maxHeap or waitingList:
            if maxHeap:
                val, _ = heapq.heappop(maxHeap)
                val+=1

                if val != 0:
                    waitingList.append([val, time + n])

            if len(waitingList) > 0:
                waitingItem = waitingList[0]
                waiting_val, wait_time = waitingItem

                if wait_time <= time:
                    waitingList.pop(0)
                    heapq.heappush(maxHeap, [waiting_val, waiting_val])
                
            time+=1
        
        return time

                









            






        
        