class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            euclid = point[0]**2 + point[1]**2
            minHeap.append((euclid, point[0], point[1]))
        
        heapq.heapify(minHeap)
        res = []

        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        
        return res
