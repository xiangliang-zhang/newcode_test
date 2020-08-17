#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/22 16:26
# @Author  : 一条很咸很咸的咸鱼

# 贿赂怪兽问题
# 绘制怪兽-金币数表格解法

def answer(x, arr1, arr2):
    if not x or (len(arr1) != len(arr2)) or (x != len(arr1)):
        return
    sum_agg = sum(arr2)
    dp = [[-1 for i in range(sum_agg + 1)] for i in range(x)]  # 初始化二维表格
    for j in range(sum_agg):
        if j == arr2[0]:
            dp[0][j] = arr1[0]
    for i in range(1, x):
        for j in range(1, sum_agg + 1):
            if j - arr2[i] >= 0:
                if dp[i - 1][j] >= arr1[i] or dp[i - 1][j - arr2[i]] != -1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr2[i]] + arr1[i])
                elif dp[i - 1][j] >= arr1[i]:
                    dp[i][j] = dp[i - 1][j]
            else:
                if dp[i - 1][j] >= arr1[i]:
                    dp[i][j] = dp[i - 1][j]

    for i in range(1, sum_agg + 1):
        if dp[x - 1][i] != -1:
            return i


print(answer(3, [7, 6, 13], [2, 1, 5]))
