# coding=utf-8
# ----------------
# author: weiyu
# create_time : 12/1/2022
# description :


# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
#  示例 3：
#
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 6
#  -10 <= nums[i] <= 10
#  nums 中的所有整数 互不相同
#
#
#  Related Topics 数组 回溯 👍 2321 👎 0
from typing import List
from typing import Set

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = []
        used = []

        for i in range(size):
            self.bfs(nums,i,used,result,size)


        return result


    def bfs(self,nums: List[int],index:int,used :List[int],result:List[int],size):
        if index in used:
            return

        used.append(index)
        if size == len(used):
            one = [nums[i] for i in used]
            result.append(one)
        else:
            for i in range(size):
                if i not in used:
                    self.bfs(nums,i,used,result,size)
        used.remove(index)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    obj = Solution()
    rs = obj.permute([1,2,3])
    print(rs)