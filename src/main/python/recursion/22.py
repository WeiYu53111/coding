# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/10/2022
# description :

"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self._gen(n,0,0,"")
        return self.res


    def _gen(self,n,left,right,data):
        if left ==n and right == n:
            self.res.append(data)
            return
        if left < n:
            self._gen(n,left+1,right,data+"(")

        if right < left and right < n:
            self._gen(n,left,right+1,data+")")

if __name__ == '__main__':
    obj = Solution()
    res = obj.generateParenthesis(3)
    print(res)