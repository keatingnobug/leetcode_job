# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/8 23:23
@Author ： keatingnobug
@File ：slu_66.py
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int("".join(str(digit) for digit in digits)) + 1
        return list(int(digit) for digit in str(number))


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne(digits=[9, 9, 9]))  # 999存在数组越界的场景
