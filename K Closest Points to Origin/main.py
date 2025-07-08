class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            # Create a list of tuples: (distance, point)
            heap = [(math.sqrt(x[0]**2 + x[1]**2), x) for x in points]
            heapq.heapify(heap)  # Min-heap based on distance

            res = []
            for _ in range(k):
                dist, point = heapq.heappop(heap)
                res.append(point)

            return res
