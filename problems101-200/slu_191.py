# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 23:44
@Author ： keatingnobug
@File ：slu_191.py
"""


class Solution:
    # 转字符串统计
    def hammingWeight(self, n: int) -> int:
        return str(bin(n))[2:].count('1')

    # 移位统计
    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     for i in range(32):
    #         if n & 1 == 1:
    #             count += 1
    #         n >>= 1
    #     return count


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(n=7))
