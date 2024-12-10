class Solution:
    def valid(self, s, l):
        i,j = 0,0
        cnt = defaultdict(int)
        while j < len(s):
            if s[i] != s[j]:
                i = j
            else:
                if j - i < l - 1:
                    j += 1
                else:
                    cnt[s[i:j+1]] += 1
                    if cnt[s[i:j+1]] == 3:
                        return True
                    i += 1
                    j += 1
        return False

    def maximumLength(self, s: str) -> int:
        # binary search + sliding window + counting
        # time O(nlogn), space O(n)
        l,r = 1, len(s)
        res = -1
        while l <= r:
            mid = l + (r-l) // 2
            if self.valid(s, mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res

    # def maximumLength(self, s: str) -> int:
    #     n = len(s)
    #     arr = [(s[0], 1)]
    #     for i in range(1, n):
    #         if s[i] == s[i-1]:
    #             arr.append((s[i], arr[i-1][1] + 1))
    #         else:
    #             arr.append((s[i], 1))
    #     mx = -1
    #     for l in range(1, n):
    #         cnt = {}
    #         for ch,freq in arr:
    #             if ch not in cnt:
    #                 cnt[ch] = 0

    #             if freq >= l:
    #                 cnt[ch] += 1
    #                 if cnt[ch] == 3:
    #                     mx = l
    #                     break
    #     return mx
