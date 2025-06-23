class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) == len(sentence2): return sentence1 == sentence2
        
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) > len(s2): s1, s2 = s2, s1

        start, end1, end2 = 0, len(s1)-1, len(s2)-1
        
        while start < len(s1) and s1[start] == s2[start]:
            start += 1

        while end2 >= 0 and s1[end1] == s2[end2]:
            end1 -= 1
            end2 -= 1
        
        return end1 < start # cover all s1