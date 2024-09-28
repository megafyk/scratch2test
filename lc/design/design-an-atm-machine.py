class ATM:

    def __init__(self):
        self.bank = [0] * 5
        self.value = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.bank[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        # complexity time O(n), mem O(1)
        res = [0] * 5
        for i in range(4, -1, -1):
            if amount < self.value[i]:
                continue
            
            if self.bank[i] > 0:
                wd = min(amount // self.value[i], self.bank[i])
                amount -= wd * self.value[i]
                res[i] += wd

        if amount != 0:
            return [-1]
        for i in range(5):
            self.bank[i] -= res[i]
        return res

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)