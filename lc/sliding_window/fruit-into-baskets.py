class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        # time O(n), space O(1)
        cnt = defaultdict(int)
        res = 0
        n = len(fruits)
        i = 0
        for j in range(n):
            if fruits[j] not in cnt:
                while len(cnt) == 2:
                    cnt[fruits[i]] -= 1
                    if cnt[fruits[i]] == 0:
                        del cnt[fruits[i]]
                    i+=1
                cnt[fruits[j]] = 1
            else:
                cnt[fruits[j]] += 1
            res = max(res, sum(cnt.values()))
        return res