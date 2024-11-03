class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # unbounded knapsack
        # time O(target^2), space O(target)
        dic = {item : str(i+1) for i, item in enumerate(cost)}
        cost = sorted(dic.keys())

        @cache
        def dfs(t):
            if t == 0: return ''
            ans = "0"
            for c in cost:
                if t - c < 0: break
                res = dfs(t-c)
                if res != "0":
                    if len(res) + 1  > len(ans):
                        ans = res + dic[c]
                    elif len(res) + 1 == len(ans):
                        ans = max(ans, res + dic[c], key=int) # max size = target
            return ans
        return dfs(target)
