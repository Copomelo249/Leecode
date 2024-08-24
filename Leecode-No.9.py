x=12321

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return s==s[::-1]

result = Solution()
print(result.isPalindrome(x))