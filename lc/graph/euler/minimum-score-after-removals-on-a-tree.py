class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # graph euler path on tree
        # time O(n^2), space O(n)
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        n = len(nums)
        xor = [num for num in nums]
        st = [0] * n # st[u] => first time see u
        en = [0] * n # en[u] => last time see u
        time = 0
        def dfs(u, par):
            nonlocal time
            st[u] = time
            time +=1
            xor_u = nums[u]
            for v in adj[u]:
                if v != par:
                    xor_u ^= dfs(v, u)
            en[u] = time
            time += 1
            xor[u] = xor_u
            return xor_u

        dfs(0, -1)
        res = sys.maxsize
        for i in range(1, n): # i is end node of cut edge 1
            for j in range(i+1, n): # j is end node of cut edge 2
                if st[i] <= st[j] <= en[i]: # j inside subtree i
                    a = xor[j]
                    b = xor[i] ^ xor[j]
                elif st[j] <= st[i] <= en[j]:
                    a = xor[i]
                    b = xor[j] ^ xor[i]
                else:
                    a,b = xor[i],xor[j]

                c = xor[0] ^ a ^ b
                diff = max(a,b,c) - min(a,b,c)
                res = min(res, diff)
        return res
