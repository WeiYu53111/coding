# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/11/2022
# description :


# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
#
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。
#
#
#
#  示例 1：
#
#
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f",
# "l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
#  示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n == board[i].length
#  1 <= m, n <= 12
#  board[i][j] 是一个小写英文字母
#  1 <= words.length <= 3 * 10⁴
#  1 <= words[i].length <= 10
#  words[i] 由小写英文字母组成
#  words 中的所有字符串互不相同
#
#
#  Related Topics 字典树 数组 字符串 回溯 矩阵 👍 714 👎 0
from typing import List


class Node:
    def __init__(self, c):
        self.c = c
        self.flag = False
        self.next = {}


class DictTree:

    def __init__(self):
        self.data = {}

    def insert(self, word):
        tmp = self.data
        for i in word:
            a = tmp.get(i, None)
            if a is None:
                a = Node(i)
                tmp[i] = a
            tmp = a.next
        a.flag = True


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if board is None or words is None:
            return []

        if len(board) == 0 or len(words) == 0 or len(board[0]) == 0:
            return []

        # 构建字典树减少递归
        tree = DictTree()
        for word in words:
            tree.insert(word)

        # 存放结果
        res = set()

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                # visited用于标识那个字符已经被访问过了
                visited = [[0 for i in range(cols)] for i in range(rows)]
                self._search(i, j, rows, cols, tree.data, res, board, "", visited)
        return [i for i in res]

    def _search(self, x, y, max_row, max_col, map, res, board, word, visited):
        c = board[x][y]
        node = map.get(c, None)
        if node is None:
            return

        if node.flag:
            res.add(word + c)

        visited[x][y] = 1

        if max_row > x + 1 >= 0 and max_col > y >= 0 and visited[x + 1][y] == 0:
            self._search(x + 1, y, max_row, max_col, node.next, res, board, word + c, visited)

        if max_row > x - 1 >= 0 and max_col > y >= 0 and visited[x - 1][y] == 0:
            self._search(x - 1, y, max_row, max_col, node.next, res, board, word + c, visited)

        if max_row > x >= 0 and max_col > y + 1 >= 0 and visited[x][y + 1] == 0:
            self._search(x, y + 1, max_row, max_col, node.next, res, board, word + c, visited)

        if max_row > x >= 0 and max_col > y - 1 >= 0 and visited[x][y - 1] == 0:
            self._search(x, y - 1, max_row, max_col, node.next, res, board, word + c, visited)

        visited[x][y] = 0


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # test1
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    # test2
    """
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain", "hklf", "hf"]
    """
    obj = Solution()
    print(obj.findWords(board, words))
