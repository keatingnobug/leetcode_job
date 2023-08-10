# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 0:16
@Author ： keatingnobug
@File ：slu_168.py
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            if columnNumber % 26 == 0:
                res = chr(26 + ord('A') - 1) + res
                columnNumber = (columnNumber - 26) // 26
            else:
                res = chr(columnNumber % 26 + ord('A') - 1) + res
                columnNumber = columnNumber // 26
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(columnNumber=2147483647))
