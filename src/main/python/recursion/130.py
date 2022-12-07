# coding=utf-8
# ----------------
# author: weiyu
# create_time : 12/7/2022
# description :


# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
# "X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#
#  示例 2：
#
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n == board[i].length
#  1 <= m, n <= 200
#  board[i][j] 为 'X' 或 'O'
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 896 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[ 0 for _ in range(cols)] for _ in range(rows)]
        # 横
        for i in range(cols):
            if board[0][i] == "O":
                self.search(board,visited,0,i,rows,cols)

            if board[rows-1][i] == "O":
                self.search(board,visited,rows-1,i,rows,cols)

        # 竖
        for i in range(rows):
            if board[i][0] == "O":
                self.search(board,visited,i,0,rows,cols)

            if board[i][cols-1] == "O":
                self.search(board,visited,i,cols-1,rows,cols)

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] != 1:
                    board[i][j] = "X"


    def search(self,board,visited,x,y,rows,cols):
        if visited[x][y] == 1 or board[x][y] == "X":
            return
        visited[x][y] = 1
        directs = [(-1,0),(1,0),(0,-1),(0,1)]
        for xadd,yadd in directs:
            if  0 < x+xadd < rows and  0 < y+yadd < cols:
                self.search(board,visited,x+xadd,y+yadd,rows,cols)

if __name__ == '__main__':
    data = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    obj = Solution()
    obj.solve(data)
    print(data)

    # 	期望结果:[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]




# leetcode submit region end(Prohibit modification and deletion)
