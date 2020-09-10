#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。
例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:
输入: 1
输出: "A"
示例 2:
输入: 28
输出: "AB"
示例 3:
输入: 701
输出: "ZY"
"""


class Solution(object):
    
    def convertToTitle(self, n: int) -> str:
        titles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result = ''
        while n > 26:
            # 取整
            if n % 26 == 0:
                i = n // 26 - 1
                result += titles[i-1]
                n -= i * 26
            else:
                i = n // 26
                result += titles[i-1]
                n = n % 26
        result += titles[n-1]
        return result


def main():
    n = 703
    solution = Solution()
    result = solution.convertToTitle(n=n)
    print(result)


if __name__ == '__main__':
    main()







