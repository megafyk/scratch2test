class Solution:
    def gain(self,p,t):
        return (p+1)/(t+1) - p/t

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # max heap
        # time O(nlogn), space O(n)
        pq = []
        for p,t in classes:
            heappush(pq, (-self.gain(p,t), p, t))

        while extraStudents > 0:
            _,p,t = heappop(pq)
            heappush(pq, (-self.gain(p+1,t+1), p+1, t+1))
            extraStudents -= 1

        a = 0
        for _,p,t in pq:
            a += p/t
        return a / len(classes)
