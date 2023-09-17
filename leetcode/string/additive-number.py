class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):

                x, y, z = num[:i], num[i:j], num[j:]
                if (x.startswith("0") and x != '0') or (y.startswith("0") and y != '0'):
                    continue

                while True:
                    if not z:
                        return True
                    temp = str(int(x) + int(y))
                    print(x, y, temp, z)
                    if z.startswith(temp):
                        x = y
                        y = temp
                        z = z[len(temp):]

                    else:
                        break
        return False


s = Solution()
print(s.isAdditiveNumber("1123358"))
print(s.isAdditiveNumber("101"))
print(s.isAdditiveNumber("0000"))
