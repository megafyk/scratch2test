class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # complexity: time O(nlogn), mem O(1)
        people = sorted(people)
        n = len(people)
        l,r = 0,n-1
        boat = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boat += 1
        return boat