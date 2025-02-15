class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.cur = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.cur *= num
            self.products.append(self.cur)
        else:
            self.products = []
            self.cur = 1
        

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        elif len(self.products) == k:
            return self.cur
        else:
            return self.products[-1] // self.products[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)