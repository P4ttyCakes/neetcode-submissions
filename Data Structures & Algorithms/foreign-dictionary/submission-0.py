class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {char: [] for word in words for char in word}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i+1]


            if len(first) > len(second) and first[:len(second)] == second[:len(second)]:
                return ""

            
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    adj[second[j]].append(first[j])
                    break
        

        
        visited = set()
        completed = set()
        order = []
        def dfs(char):

            if char in completed:
                return True
            
            if char in visited:
                return False
            
            visited.add(char)

            for pre in adj[char]:

                if dfs(pre) == False:
                    return False
            

            order.append(char)
            completed.add(char)
            visited.remove(char)

            return True
        
        for char in adj:
            if dfs(char) == False:
                return ""

        return "".join(order)                

            



        
        