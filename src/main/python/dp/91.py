# coding=utf-8
# ----------------
# author: weiyu
# create_time : 10/31/2022
# description :

# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
#  要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
#
#
#  "AAJF" ，将消息分组为 (1 1 10 6)
#  "KJF" ，将消息分组为 (11 10 6)
#
#
#  注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
#
#  给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#
#  题目数据保证答案肯定是一个 32 位 的整数。
#
#
#
#  示例 1：
#
#
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#
#  示例 2：
#
#
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#
#  示例 3：
#
#
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 100
#  s 只包含数字，并且可能包含前导零。
#
#
#  Related Topics 字符串 动态规划 👍 1287 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:

    """
    这里有几个点

    1.与楼梯的题目相似, 存在递推关系  dp[i] = dp[i-1] + dp[i-2],因为每次是取一个字符解密还是取两个字符解密
    2.需要考虑两个组合 的时候需要满足  10 <= x <= 26
    3.从第二个字符开始就要考虑第二点的判断,因此初始化dp数组的时候，很麻烦，需要使用哨兵节点来
      统一处理
    4.dp数组初始化的时候，dp[0]的取值 要 =  1,而不是 0  理由是 当需要用到哨兵节点 dp[0]的时候，
      是取两个字符的情况 此时属于一种解法，因此  dp[0] = 1 ,dp[1] = 1
    5.因为使用了哨兵节点,  for 循环是根据 要遍历的字符串 来循环   下标的关系会变成  dp[i+1] 表示 s[i] 对应的状态
    """
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        size = len(s)
        dp = [0 for _ in range(size+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1,size):
            if s[i] == "0":
                if 1 <= int(s[i-1]) <=2:
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                dp[i+1] = dp[i] + (dp[i-1] if 10 <= int(s[i-1:i+1]) <=26 else 0)
        return dp[-1]


    def numDecodings_recursion(self, s: str) -> int:
        if s[0]=="0":
            return 0
        size = len(s)
        return self._recursion(s,size,0,1) + self._recursion(s,size,0,2)


    def _recursion(self,s,size,start,add):
        if start == size:
            return 1
        elif start < size < start + add:
            return 0

        end = start + add
        if s[start] != "0":
            if 10 <= int(s[start:end]) <=26 and add == 2:
                if end == size:
                    return 1
                else:
                    return self._recursion(s,size,end,1) + self._recursion(s,size,end,2)
            elif add == 1:
                if end == size:
                    return 1
                else:
                    return self._recursion(s,size,end,1) + self._recursion(s,size,end,2)
        return 0

if __name__ == '__main__':
    obj = Solution()
    input = "111111111111111111111111111111111111111111111"
    # print("递归:" + str(obj.numDecodings_recursion(input)))  # 1836311903
    print("dp:" + str(obj.numDecodings(input)))

# leetcode submit region end(Prohibit modification and deletion)
