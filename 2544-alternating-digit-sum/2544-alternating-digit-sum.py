class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x = str(n)
        total = 0
        for i in range(len(x)):
            if i % 2 == 0:
                total = total + int(x[i])
            else:
                total = total - int(x[i])
        return total