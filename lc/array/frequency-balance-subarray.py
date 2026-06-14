class Solution:
    def getLength(self, nums: List[int]) -> int:
        # 2 hashmap
        # time O(n^2), space O(n)
        n = len(nums)
        res = 0
        freq = defaultdict(int)
        res = 0

        def exists_f(freq_f):
            if len(freq_f) == 2:
                arr = [k for k in freq_f.keys()]
                return 2 * arr[0] == arr[1] or arr[0] == 2 * arr[1]
            return False

        for i in range(n):
            freq[nums[i]] += 1

            freq_f = defaultdict(int)
            for k, v in freq.items():
                freq_f[v] += 1

            if len(freq) == 1 or exists_f(freq_f):
                res = max(res, i + 1)
            else:
                tmp_freq = dict(freq)
                for j in range(i + 1):
                    t = tmp_freq[nums[j]]
                    tmp_freq[nums[j]] -= 1

                    if tmp_freq[nums[j]] > 0:
                        freq_f[tmp_freq[nums[j]]] += 1

                    freq_f[t] -= 1
                    if freq_f[t] == 0:
                        del freq_f[t]

                    if exists_f(freq_f):
                        res = max(res, i - j)
        return res
