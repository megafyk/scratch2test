class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # string stack
        # time O(n), space O(n)
        n = len(s)
        
        lock_st = deque() # try to pop all lock "("
        unlock_st = deque()

        for i in range(n):
            if s[i] == "(" and locked[i] == "1":
                lock_st.append(i)
            elif s[i] == ")" and locked[i] == "1":
                if not lock_st and not unlock_st:
                    return False
                elif lock_st:
                    lock_st.pop()
                elif unlock_st:
                    unlock_st.pop()
            else:
                unlock_st.append(i)

        while lock_st:
            if not unlock_st:
                return False
            if lock_st[-1] > unlock_st[-1]:
                return False
            lock_st.pop()
            unlock_st.pop()

        return not lock_st and len(unlock_st) % 2 == 0
            