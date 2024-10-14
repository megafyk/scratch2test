class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        
        times = [(arrival, leaving, target) for target, (arrival, leaving) in enumerate(times)]
        times = sorted(times)
        
        next_chair = 0
        chairs = []
        leaving_q = []
        for time in times:
            arrival, leaving, target = time
            while leaving_q and leaving_q[0][0] <= arrival:
                _, chair = heappop(leaving_q)
                heappush(chairs, chair)
            
            if chairs:
                cur_chair = heappop(chairs)
            else:
                cur_chair = next_chair
                next_chair += 1
            
            heappush(leaving_q, (leaving, cur_chair))
            if target == targetFriend:
                return cur_chair
        return 0