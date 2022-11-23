# coding=utf-8
# ----------------
# author: weiyu
# create_time : 11/17/2022
# description :

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #self.bubbleSort(nums)
        self.mergeSort(nums)
        return nums[-k]

    def bubbleSort(self,nums:List[int]):
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp

    def mergeSort(self,nums:List[int]):
        self._mergeSort_between(nums,0,len(nums)-1)

    def _mergeSort_between(self,nums:List[int],start,end):
        if start >= end:
            return

        mid = int((start + end)/2)
        self._mergeSort_between(nums,start,mid)
        self._mergeSort_between(nums,mid+1,end)
        self._merge(nums,start,mid,end)


    def _merge(self,nums:List[int],low,mid,high):
        tmp = []
        i,j = low,mid+1
        while i<= mid and j <= high:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1

        start = i if i <= mid else j
        end = mid if i <= mid else high

        tmp.extend(nums[start:end+1])
        nums[low:high+1] = tmp














if __name__ == '__main__':
    a = [3,8,7,5,10,2]
    obj = Solution()
    print(obj.findKthLargest(a,2))
    print(a)