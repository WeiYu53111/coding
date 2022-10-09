# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/9/2022
# description :


# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位
# 。
#
#  返回 滑动窗口中的最大值 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#  示例 2：
#
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#  1 <= k <= nums.length
#
#
#  Related Topics 队列 数组 滑动窗口 单调队列 堆（优先队列） 👍 1902 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        windows ,res = [],[]

        for i,x in enumerate(nums):
            if i >= k and windows[0] <= i-k:
                windows.pop(0)
            while windows and nums[windows[-1]] <= x:
                windows.pop()
            windows.append(i)
            if i >= k-1:
                res.append(nums[windows[0]])
        return res
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    obj = Solution()
    a = [1,3,-1,-3,5,3,6,7]
    res = obj.maxSlidingWindow(a,3)

    # 期望结果:[3,3,5,5,6,7]
    print(res)