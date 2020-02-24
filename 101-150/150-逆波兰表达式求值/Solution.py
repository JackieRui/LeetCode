#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
根据逆波兰表示法，求表达式的值。
有效的运算符包括+,-,*,/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
输入: ["2", "1", "+", "3", "*"]  输出: 9
解释: ((2 + 1) * 3) = 9
输入: ["4", "13", "5", "/", "+"] 输出: 6
解释: (4 + (13 / 5)) = 6
输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]  输出: 22
解释:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution(object):

    def evalRPN(self, tokens: [str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        z = 0
        for token in tokens:
            if token in set(["+", "-", "*", "/"]):
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    z = int(x) + int(y)
                elif token == "-":
                    z = int(x) - int(y)
                elif token == "*":
                    z = int(x) * int(y)
                elif token == "/":
                    z = int(x) // int(y) if int(x)*int(y) > 0 else abs(int(x)) // abs(int(y)) * -1
                stack.append(z)
            else:
                stack.append(token)
        return z

def main():
    tokens = ["18"]
    solution = Solution()
    result = solution.evalRPN(tokens=tokens)
    print(result)

if __name__ == "__main__":
    main()
