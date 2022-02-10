# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.


class Solution:
    def rotatedDigits(self, n):
        invalid, diff = set(['3', '4', '7']), set(['2', '5', '6', '9'])
        result = 0

        for i in range(n + 1):
            lookup = set(list(str(i)))
            if invalid & lookup:
                continue
            if diff & lookup:
                result += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotatedDigits(10))
