from collections import Counter
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        res = 0

        cntRow = Counter(map(tuple, board))
        cntCol = Counter(zip(*board))

        for cnt in (cntRow, cntCol):
            # need 2 distinct types of row/col
            if len(cnt) != 2:
                return -1

            # nums of each type must be ~ n // 2
            if sorted(cnt.values()) != [n//2, (n+1)//2]:
                return -1

            # nums of 0s vs 1s must be equal (n even), or diff by 1 (n is odd)
            for line in cnt:
                tmpcnt = Counter(line)
                if sorted(tmpcnt.values()) != [n//2, (n+1)//2]:
                    return -1
            
            # 2 distinct line must be compliment (XOR)
            line1, line2 = cnt
            if not all(x^y for x,y in zip(line1,line2)):
                return -1
            
            if n & 1:
                moves = 0
                # most significant bit
                msb = 1 if line1.count(1) > line1.count(0) else 0
                for i in line1:
                    moves += i ^ msb
                    msb ^= 1
                res += moves // 2
            else:
                # get min between msb = 1 vs msb = 0
                min_moves = n
                for msb in (0,1):
                    moves = 0
                    for i in line1:
                        moves += i ^ msb
                        msb ^= 1
                    min_moves = min(min_moves, moves)  
                
                res += min_moves // 2
                
        return res