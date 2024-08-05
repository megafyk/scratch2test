from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
    # def kthDistinct(self, arr: List[str], k: int) -> str:
    #     # brute force
    #     # complexity: time O(n), mem O(n)
    #     cnt = Counter(arr)
    #     for w,c in cnt.items():
    #         if c == 1:
    #             if k == 1:
    #                 return w
    #             k-=1
    #     return ""    
