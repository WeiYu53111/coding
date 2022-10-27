# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/25/2022
# description :


# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
#
#  注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
#
#
#  示例 1：
#
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
#
#
#  示例 2：
#
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
#
#
#  示例 3：
#
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 300
#  1 <= wordDict.length <= 1000
#  1 <= wordDict[i].length <= 20
#  s 和 wordDict[i] 仅有小写英文字母组成
#  wordDict 中的所有字符串 互不相同
#
#
#  Related Topics 字典树 记忆化搜索 哈希表 字符串 动态规划 👍 1846 👎 0



"""
先思考递归是如何解决的，然后定义状态

推导出递推公式

递归：
每次从单词堆里面挑选一个单词，如果前面字符串都能对上，继续挑下一个单词直到长度 >= 结束
如果结束时字符串相同则表示可以拼出来，反之不行


"""

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [ False for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]




# leetcode submit region end(Prohibit modification and deletion)
