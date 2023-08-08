# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/8 23:32
@Author ： keatingnobug
@File ：slu_67.py
"""
import itertools


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result_str, carry = "", 0
        for item_a, item_b in itertools.zip_longest(a[::-1], b[::-1], fillvalue=0):
            # if (sum := int(item_a) + int(item_b) + carry) >= 2:
            if (int(item_a) + int(item_b) + carry) >= 2:
                result_str += str((int(item_a) + int(item_b) + carry) % 2)
                carry = 1
            else:
                result_str += str(int(item_a) + int(item_b) + carry)
                carry = 0
        if carry != 0:
            result_str += str(carry)
        return result_str[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary(a="1010", b="111"))
