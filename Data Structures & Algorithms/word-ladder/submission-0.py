class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                prefix = word[:i] + "*" + word[i + 1:]
                adj[prefix].append(word)

        print(adj)


        queue = deque([])
        queue.append([beginWord, 1])

        visited = set()
        while queue:

            word, length = queue.popleft()

            if word in visited:
                continue
            
            visited.add(word)

            

            if word == endWord:
                return length

            
            for i in range(len(word)):

                prefix = word[:i] + "*" + word[i + 1:]

                for nei in adj[prefix]:
                    if nei not in visited and nei != word:
                        visited.add(word)
                        queue.append([nei, length + 1])
            
        return 0
                    





