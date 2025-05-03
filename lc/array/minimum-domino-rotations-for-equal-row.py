class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # hashmap
        # time O(N), space O(1)
        N = len(tops)
        cnt_top = defaultdict(int)
        cnt_bot = defaultdict(int)
        cnt_eq = defaultdict(int)
        for i in range(N):
            cnt_top[tops[i]] += 1
            cnt_bot[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                cnt_eq[tops[i]] += 1

            if cnt_top[i] + cnt_bot[i] - cnt_eq[i] == N:
                res = min(res, cnt_top[i] - cnt_eq[i], cnt_bot[i] - cnt_eq[i])
        res = N
        for i in range(1, 7):
            if cnt_top[i] + cnt_bot[i] - cnt_eq[i] == N:
                res = min(res, cnt_top[i] - cnt_eq[i], cnt_bot[i] - cnt_eq[i])
        return res if res < N else -1
        
