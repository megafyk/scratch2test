class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # string with hashtable
        # time O(n+m), space O(1)
        wcount = defaultdict(int)
        for w2 in words2:
            cnt = Counter(w2)
            for k,v in cnt.items():
                if v > wcount[k]:
                    wcount[k] = v
        res = []

        for w1 in words1:
            cnt = Counter(w1)
            check = True
            for k,v in wcount.items():
                if k not in cnt or cnt[k] < v:
                    check = False
                    break
            if check:
                res.append(w1)
        return res
            
    # def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    #     # brute force
    #     # time O(n*m*l1*l2), space O(1)
    #     def subset(w1, w2):
    #         j = 0
    #         if len(w1) < len(w2): return False
    #         for i in range(len(w1)):
    #             if w1[i] == w2[j]:
    #                 j+=1
    #             if j == len(w2):
    #                 return True
    #         return False
            
    #     res = []
    #     for w1 in words1:
    #         check = True
    #         for w2 in words2:
    #             if not subset(w1, w2):
    #                 check = False
    #                 break
    #         if check:
    #             res.append(w1)
    #     return res