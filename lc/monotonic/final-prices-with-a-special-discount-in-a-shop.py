class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # increasing monotonic stack
        # time O(n), space O(1)
        st = deque()
        for i in range(len(prices)):
            while st and st[-1][0] >= prices[i]:
                p,idx = st.pop()
                prices[idx] = p - prices[i]
            st.append((prices[i], i))

        return prices
