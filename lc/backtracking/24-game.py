class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # backtrack
        # time O(4!*6^4), space O(4!)
        if len(cards) == 1: # collapse pairs [a,b,c] -> [(a,b), c] -> [d,c]
            return abs(24 - cards[0]) < 10**-6
        n = len(cards)
        res = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                nw_cards = [cards[k] for k in range(n) if k != i and k != j]
                a = cards[i]
                b = cards[j]

                cases = [a + b, a * b, a - b, b - a]
                if b != 0:
                    cases.append(a / b)
                if a != 0:
                    cases.append(b / a)
                for case in cases:
                    res |= self.judgePoint24(nw_cards + [case])
                    if res:
                        return True

        return res
