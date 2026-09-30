class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        cache = defaultdict(lambda: float("inf"))
        stops = k + 1

        best = float("inf")
        adj = defaultdict(list)

        for start, destination, price in flights:
            adj[start].append([destination, price])

        def dfs(airport, steps, current_cost):
            nonlocal best

            if steps == stops and airport != dst:
                return

            if airport == dst:
                best = min(best, current_cost)
                return

            if cache[(airport, steps)] <= current_cost:
                return

            if current_cost >= best:
                return

            cache[(airport, steps)] = current_cost

            for destination, price in adj[airport]:
                dfs(destination, steps + 1, current_cost + price)

        dfs(src, 0, 0)

        if best == float("inf"):
            return -1
        else:
            return best