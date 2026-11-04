class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        #so this looks to be tree question, or a graph question, where we want to find the minimum distance to a lock combination
        #use bfs, each lock has 8 paths to the next, that's a graph, we don't want to revisit nodes, taht's a wsate
        #use a queue and slowly traverse out from each combination, until we reach the node, once we do that's the minum turns


        #i need to be doing the adding once a combination or node is being appended, so it is not appended onto the heap more than once
        #or if it is appended more than once, I need to make sure it is beign passed when it already has or else it will cause a cycle.
        def child(lock):    
            children = []

            for i in range(len(lock)):
                char = lock[i]

                add_one = str((int(char) + 1) % 10)
                minus_one = str(((int(char) -1) + 10) % 10)

                children.append(lock[:i] + add_one + lock[i + 1:])
                children.append(lock[:i] + minus_one + lock[i + 1:])
            
            return children


        if '0000' in deadends:
            return -1
        
        visited = set(deadends)

        queue = deque([])
        queue.append(['0000', 0]) #start and distance


        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            



            for children in child(lock):
                if children not in visited:

                    queue.append([children, turns + 1])
                    visited.add(children)

        return -1





        
        

        