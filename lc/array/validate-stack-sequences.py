class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # simulation
        # time O(n), space O(n)
        st = deque()
        i = 0
        
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[i]:
                st.pop()
                i += 1
        return not st
