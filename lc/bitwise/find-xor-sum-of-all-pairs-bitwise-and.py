from functools import reduce
from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        # complexity O(m*n)
        # res = arr1[0] & arr2[0]
        # for i in range(len(arr1)):
        #     for j in range(len(arr2)):
        #         if i == 0 and j == 0:
        #             continue
        #         res ^= arr1[i] & arr2[j]
        # return res

        # complexity O(m+n)
        xor1 = reduce(lambda x,y: x ^ y, arr1)
        xor2 = reduce(lambda x,y: x ^ y, arr2)
        return xor1 & xor2
