# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/19/2022
# description :
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
#
#  斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
#
#
#  示例 1：
#
#
# 输入：n = 2
# 输出：1
#
#
#  示例 2：
#
#
# 输入：n = 5
# 输出：5
#
#
#
#
#  提示：
#
#
#  0 <= n <= 100
#
#
#  Related Topics 记忆化搜索 数学 动态规划 👍 417 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n==0:
            return 0
        else:
            return self.fib(n-1) + self.fib(n-2)

    def fib2(self, n:int ) -> int:
        dp = [ 0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+ dp[i-2]

        return dp[n]

if __name__ == '__main__':
    obj = Solution()
    print(obj.fib(6))
    print(obj.fib2(6))
