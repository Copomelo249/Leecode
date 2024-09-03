class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        F = [0] * (n + 1)
        # 设置初始值
        F[0] = 0
        F[1] = 1
        # 从 2 到 n 依次计算斐波那契数
        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2]
            # 返回第 n 个斐波那契数
        return F[n]
a=Solution()
print(a.fib(0))