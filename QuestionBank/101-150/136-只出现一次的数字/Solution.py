#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
输入: [2,2,1] 输出: 1
输入: [4,1,2,1,2] 输出: 4
"""

class Solution(object):

    def singleNumber(self, nums: [int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[i]

def main():
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    result = solution.singleNumber(nums=nums)
    print(result)

if __name__ == "__main__":
    main()

