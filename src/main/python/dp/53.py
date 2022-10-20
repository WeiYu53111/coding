# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/20/2022
# description :


# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  子数组 是数组中的一个连续部分。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
#  示例 2：
#
#
# 输入：nums = [1]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#
#
#
#
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#
#  Related Topics 数组 分治 动态规划 👍 5376 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # 重点是找出递推的关系
        # 递推往往是当前节点 的结果值 是由上一个节点 再结合当前节点 得到的
        # 递进的关系 可以 从后往前, 从前往后.
        # 题目是求最大的子串.   必须是连续的. 如果把当前节点当做子串最后的节点
        # 可能的情况就能固定下来.有两种可能, 一种是与上一个节点组合成最大子串, 自己就是最大子串
        # 就可以得到 dp[i] = max(dp[i-1] + i, i )
        # 遍历所有保留最大即可
        rs = nums[0]
        cur = nums[0]
        for i in range(1,len(nums)):
            cur = max(cur + nums[i],nums[i])
            rs = max(rs,cur)
        return rs


# leetcode submit region end(Prohibit modification and deletion)
