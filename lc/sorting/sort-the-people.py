class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # complexity: time O(nlogn), mem O(n)
        h_with_idx = [(val, idx) for idx, val in enumerate(heights)]
        h_with_idx = sorted(h_with_idx, reverse=True)
        return [names[idx] for val, idx in h_with_idx]
