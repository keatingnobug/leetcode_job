# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 23:05
@Author ： keatingnobug
@File ：slu_190.py
"""


class Solution:
    # 切换字符串反转
    # def reverseBits(self, n: int) -> int:
    #     bits = f"{str(bin(n))[2:]:0>32}"
    #     reversed_bits = bits[::-1]
    #     return int(reversed_bits, 2)
    # 移位操作
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)  # 取最后一位，新值左移作为第一位，依次遍历
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(n=43261596))
