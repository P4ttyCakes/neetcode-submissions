class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0

        unvisited = set(range(n))
        best = [float("inf")] * n
        best[0] = 0
        total = 0

        while unvisited:
            # Pick the unvisited point with the cheapest connection.
            i = -1
            for j in unvisited:
                if i == -1 or best[j] < best[i]:
                    i = j

            unvisited.remove(i)
            total += best[i]

            # Check if connecting through i is cheaper for each remaining point.
            x1, y1 = points[i]
            for j in unvisited:
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                best[j] = min(best[j], distance)

        return total