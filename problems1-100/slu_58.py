# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/8 23:15
@Author ： keatingnobug
@File ：slu_58.py
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord(s="luffy is still joyboy"))
