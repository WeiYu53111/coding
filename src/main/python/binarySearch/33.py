# coding=utf-8
# ----------------
# author: weiyu
# create_time : 12/8/2022
# description :


# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
# k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
# ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
#  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
#  你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
#  示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
#  示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5000
#  -10⁴ <= nums[i] <= 10⁴
#  nums 中的每个值都 独一无二
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转
#  -10⁴ <= target <= 10⁴
#
#
#  Related Topics 数组 二分查找 👍 2423 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 1 and nums[0] == target:
            return 0

        low = 0
        high = size - 1

        while low <= high:
            mid = int((high + low) / 2)
            if nums[mid] == target:
                return mid
            else:
                # 说明左半区没有包含旋转点
                if nums[low] <= nums[mid]:
                    # 判断target在左半区还是右半区
                    if nums[low] <= target < nums[mid]:
                        high = mid-1
                    else:
                        low = mid + 1
                else:  # 左半区包含旋转点,那么右半区必定是顺序递增
                    # 判断target是否在右半区,因为右半区容易判断,除此以外都是在左半区
                    if nums[mid] < target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
        return -1



if __name__ == '__main__':
    a = [5,1,2,3,4]
    obj = Solution()
    print(obj.search(a, 1))

# leetcode submit region end(Prohibit modification and deletion)
