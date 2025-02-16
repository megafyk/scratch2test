class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # backtrack
        # time O(n!), space O(n)
        used = [False] * (n+1)

        res = [-1 for i in range(2*(n-1) + 1)]

        def backtrack(idx):
            if idx == len(res):
                return True

            if res[idx] != -1:
                return backtrack(idx+1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                used[num] = True
                if num == 1:
                    res[idx] = 1
                    if backtrack(idx+1):
                        return True
                    res[idx] = -1
                else:
                    if idx + num < len(res) and res[idx+num] == -1:
                        res[idx] = num
                        res[idx+num] = num

                        if backtrack(idx+1):
                            return True

                        res[idx] = -1
                        res[idx+num] = -1
                used[num] = False

            return False

        backtrack(0)
        return res
