from collections import deque 

class StockSpanner:

    def __init__(self):
        self.st = deque()
        # self.prices = []
        
    def next(self, price: int) -> int:
        # complexity: time O(n), mem O(n)
        ans = 1
        while self.st and self.st[-1][0] <= price:
            ans += self.st.pop()[1]
        self.st.append((price, ans))
        return ans


        # self.prices.append(price)
        # n = len(self.prices)
        # for i in range(n-1, -1, -1):
        #     if self.prices[i] > price:
        #         return n-i-1
        # return n

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)