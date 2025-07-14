class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # sorting + 2 pointers
        # time O(nlogn + mlogm), space O(1)
        players.sort()
        trainers.sort()
        i,j = 0,0
        pairs = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                pairs += 1
                i += 1
                j += 1
            else:
                j += 1
        return pairs