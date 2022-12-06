# coding=utf-8
# ----------------
# author: weiyu
# create_time : 12/6/2022
# description :




# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 2000] 内
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 广度优先搜索 二叉树 👍 717 👎 0

from typing import Optional,List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = []
        rs = []
        q.append(root)
        order = True
        while q:
            tmp = []
            size = len(q)
            for i in range(size):
                node = q[i]
                if order:
                    tmp.append(node.val)
                else:
                    tmp.insert(0,node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            q = q[size-1:]
            order = not order
            rs.append(tmp)
        return rs




# leetcode submit region end(Prohibit modification and deletion)
