# coding=utf-8
# ----------------
# author: weiyu
# create_time : 12/2/2022
# description :
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        high = len(matrix)
        wigth = len(matrix[0])

        result = []
        status = [[0 for _ in range(wigth)] for _ in range(high)]
        pos_x = 0
        pos_y = 0
        # 1表示向右,2表示向下,3表示向左,4表示向上
        direct = {
            1:2,
            2:3,
            3:4,
            4:1
        }
        cur = 1
        while True:
            # 判断是否已经访问过
            if status[pos_y][pos_x] !=0 or pos_x == -1:
                return result
            # 记录访问过的状态
            status[pos_y][pos_x] = 1
            result.append(matrix[pos_y][pos_x])

            # 调整下标,如果超界了则调整方向以及下标
            pos_x,pos_y,cur = self.getNextPos(direct,cur,pos_x,pos_y,wigth,high,status)

    def getNextPos(self,directs,cur,pos_x,pos_y,max_x,max_y,status):
        new_cur = cur
        for _ in range(2):
            new_pos_x = pos_x
            new_pos_y = pos_y
            # 根据当前方向前进
            if new_cur == 1:
                new_pos_x = pos_x + 1
            elif new_cur == 2:
                new_pos_y = pos_y + 1
            elif new_cur == 3:
                new_pos_x = pos_x - 1
            else:
                new_pos_y = pos_y - 1

            # 判断前进的方向是否有问题
            if 0 <= new_pos_y < max_y and 0 <= new_pos_x < max_x  and status[new_pos_y][new_pos_x] == 0:
                return new_pos_x, new_pos_y, new_cur
            else:

                new_cur = directs[new_cur]
        return -1,-1,-1

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    obj = Solution()
    rs = obj.spiralOrder(matrix)
    print(rs)



