# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 23:56
@Author ： keatingnobug
@File ：slu_171.py
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res = res + (ord(columnTitle[-1 - i]) - ord('A') + 1) * 26 ** i
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber(columnTitle="ZZY"))
