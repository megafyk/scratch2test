class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        

        def compare(str1, str2):
            int1 = int(str1)
            int2 = int(str2)
            if int1 == int2: return 0
            return 1 if int1 > int2 else -1
            
        i = j = 0
        while i < len(ver1) or j < len(ver2):
            t = 0
            if i == len(ver1) and j < len(ver2):
                t = compare("0", ver2[j])
                j += 1
            elif i < len(ver1) and j == len(ver2):
                t = compare(ver1[i], "0")
                i += 1
            else:
                t = compare(ver1[i], ver2[j])
                i += 1
                j += 1
            if t != 0: return t
        return 0