class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # counting sort
        # n = len(asteroids), m = max(asteroids)
        # time O(n+m), space O(m)
        mx = max(asteroids)
        counter = [0] * (mx + 1)
        for a in asteroids:
            counter[a] += 1

        for x in range(1, len(counter)):
            if counter[x] > 0:
                if x > mass:
                    return False
                mass += x * counter[x]
        return True


class Solution1:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # sort
        # n = len(asteroids)
        # time O(nlogn), space O(n)
        asteroids.sort()
        for a in asteroids:
            if a > mass:
                return False
            mass += a
        return True
