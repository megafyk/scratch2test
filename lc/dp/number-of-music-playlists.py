class Solution:

    def __init__(self):
        self.mod = 10**9 + 7
        self.memo = {}

    def dp(self, n, k, cur_goal, old_songs):
        if cur_goal == 0 and old_songs == n:
            return 1
        if cur_goal == 0 or old_songs > n:
            return 0
        if (cur_goal, old_songs) in self.memo:
            return self.memo[(cur_goal, old_songs)]
        # pick a new song
        res = (n - old_songs) * self.dp(n, k, cur_goal - 1, old_songs + 1) % self.mod

        # pick an old song
        # A song can only be played again only if k other songs have been played
        # gap between prev old song A and next old song A must be > k
        if old_songs > k:
            res += (old_songs - k) * self.dp(n, k, cur_goal - 1, old_songs) % self.mod
        self.memo[(cur_goal, old_songs)] = res
        return res % self.mod

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # complexity: time O(n * k * goal), mem O(n * goal)
        mod = 10**9 + 7
        return self.dp(n, k, goal, 0)
