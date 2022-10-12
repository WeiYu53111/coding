# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/12/2022
# description :


"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。



示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]


提示：

1 <= n <= 9
"""


from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n<2:
            return [["Q"]]

        left = set()
        right = set()
        col = set()
        res = []

        self.dfs(n,0,left,right,col,[],res)

        return res

    def dfs(self,n,row,left,right,col,one,output):

        if row == n:
            tmp = self.formatStr(one,n)
            output.append(tmp)
            return

        for i in range(n):
            if i in col or i-row in left or i+row in right:
                continue

            col.add(i)
            left.add(i-row)
            right.add(i+row)

            one.append(i)
            self.dfs(n,row+1,left,right,col,one,output)
            one.pop()

            col.remove(i)
            left.remove(i-row)
            right.remove(i+row)

    def formatStr(self,data,n):
        format_one = []
        for i in data:
            tmp = ["." for i in range(n)]
            tmp[i]= "Q"
            format_one.append("".join(tmp))
        return format_one


if __name__ == '__main__':
    obj = Solution()
    print(obj.solveNQueens(4))