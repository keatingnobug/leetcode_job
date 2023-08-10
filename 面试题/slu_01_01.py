# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/11 1:15
@Author ： keatingnobug
@File ：slu_01_01.py
"""
class Solution:
    def isUnique(self, astr: str) -> bool:
        astr_list=[]
        for element in astr:
            if element in astr_list:
                return False
            else:
                astr_list.append(element)
        return True