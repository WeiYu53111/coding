# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/26/2022
# description :

"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。

示例 1：

输入：x = 121
输出：true


输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。



进阶：你能不将整数转为字符串来解决这个问题吗？

数字倒序

 cur = 0
 cur * 10  + (x % 10)
 (x % 10) 求余得到最低位
 cur * 10 表示上次最低位的 放到第一位


"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        cur = 0
        num = x
        while num != 0:
            cur = cur * 10 + num % 10
            num = int(num/10)
        return cur == x


if __name__ == '__main__':
    obj = Solution()
    print(obj.isPalindrome(121))