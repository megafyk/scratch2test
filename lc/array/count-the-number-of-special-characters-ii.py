class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # array
        # time O(n), space O(1)
        lower_last = [-1] * 26
        upper_first = [-1] * 26
        od_a, od_z, od_A, od_Z = ord("a"), ord("z"), ord("A"), ord("Z")
        for i, c in enumerate(word):
            od = ord(c)
            if od_a <= od <= od_z:
                lower_last[od - od_a] = i
            elif od_A <= od <= od_Z:
                if upper_first[od - od_A] == -1:
                    upper_first[od - od_A] = i
        cnt = 0
        for i in range(26):
            if (
                lower_last[i] != -1
                and upper_first[i] != -1
                and lower_last[i] <= upper_first[i]
            ):
                cnt += 1
        return cnt
