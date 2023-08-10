# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 0:56
@Author ： keatingnobug
@File ：slu_202.py
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        no_happy_list = []
        while True:
            if n == 1:
                return True
            else:
                n = sum(int(n) * int(n) for n in str(n))
                if n in no_happy_list:
                    return False
                else:
                    no_happy_list.append(n)


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(n=2))
