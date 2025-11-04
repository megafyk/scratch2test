class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)

        freq = defaultdict(int)
        res = []

        for i in range(n):
            freq[nums[i]] += 1
            if i+1-k >= 0:
                if i-k >= 0:
                    freq[nums[i-k]] -= 1

                pq = []
                for num,fre in freq.items():
                    if fre > 0:
                        heappush(pq, (-fre,-num))

                xsum = 0
                for _ in range(min(x, len(pq))):
                    t = heappop(pq)
                    fre,val = -t[0], -t[1]
                    xsum += fre * val
                res.append(xsum)
        return res
