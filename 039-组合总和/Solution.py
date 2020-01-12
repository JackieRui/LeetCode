#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution(object):

    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        results = []
        answer = []
        self.DFS(candidates, target, 0, answer, results)
        return results

    def DFS(self, candidates, target, start, answer, results):
        for i in range(start, len(candidates)):
            if target > 0:
                answer.append(candidates[i])
                self.DFS(candidates, target-candidates[i], i, answer, results)
                answer.pop()
            elif target < 0:
                return
            else:
                result = answer[:]
                results.append(result)
                return



def main():
    candidates = [2, 3, 5]
    target = 8
    solution = Solution()
    result = solution.combinationSum(candidates=candidates, target=target)
    print(result)

if __name__ == "__main__":
    main()

"""
"""
