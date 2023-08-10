# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 0:05
@Author ： keatingnobug
@File ：slu_169.py
"""
from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_count = Counter(nums)
        for element in nums_count.keys():
            if nums_count[element] > len(nums) // 2:
                return element


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
