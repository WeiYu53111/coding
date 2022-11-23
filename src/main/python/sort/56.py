# coding=utf-8
# ----------------
# author: weiyu
# create_time : 11/22/2022
# description :


# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
#  示例 1：
#
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
#  示例 2：
#
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
#  提示：
#
#
#  1 <= intervals.length <= 10⁴
#  intervals[i].length == 2
#  0 <= starti <= endi <= 10⁴
#
#
#  Related Topics 数组 排序 👍 1717 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged = []
        for part in intervals:
            if not merged or merged[-1][1] < part[0]:
                merged.append(part)
            else:
                merged[-1][1] = max(merged[-1][1], part[1])
        return merged

if __name__ == '__main__':
    intervals = [[9,12],[1,3],[2,4]]
    obj = Solution()
    print(obj.merge(intervals))
# leetcode submit region end(Prohibit modification and deletion)
