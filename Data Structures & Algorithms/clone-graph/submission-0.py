"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #maybe have a hashmap of nodes? where each node should map to it's equivalent? 

        real_to_fake = {}

        if not node:
            return None

        def dfs(node):

            print("trying to process" , node.val)

            if node in real_to_fake:
                return real_to_fake[node]
                print('already in')

            
            fake = Node(node.val)
    
            real_to_fake[node] = fake

            for nei in node.neighbors:
                fake_connection = dfs(nei)
                real_to_fake[node].neighbors.append(fake_connection)
            

            print("Finished_processing" , node.val)
            return real_to_fake[node]

        return dfs(node)
            
            


        