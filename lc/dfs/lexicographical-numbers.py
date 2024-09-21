class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # dfs trie
        # complexity: time O(n), space O(n)
        arr = []
        st = deque([i for i in range(9, 0, -1)])

        while st:
            node = st.pop()
            if node > n:
                continue
            arr.append(node)
            for i in range(9, -1, -1):
                tmp = node * 10 + i
                if tmp <= n:
                    st.append(tmp)
        return arr

    # def dfs(self, val, res, n):
    #     if val > n:
    #         return
    #     res.append(val)
    #     for i in range(10):
    #         if val * 10 + i > n:
    #             break
    #         self.dfs(val * 10 + i, res, n)

    # def lexicalOrder(self, n: int) -> List[int]:
    #     res = []
    #     for i in range(1, 10):
    #         self.dfs(i, res, n)
    #     return res
