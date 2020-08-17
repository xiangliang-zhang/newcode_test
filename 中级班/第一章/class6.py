import numpy as np

str1 = 'aaadc'
str2 = 'aabc'
aim = 'aaaadabcc'


def create_table(str1, str2, aim):
    if (str1[0] != aim[0] and str2[0] != aim[0]) or (len(aim) != len(str1) + len(str2)):
        return
    list_TF = np.zeros((len(str1) + 1, len(str2) + 1))
    index1 = len(str1)
    index2 = len(str2)
    list_TF[0][0] = 1
    # 构建二维表的第一行
    for i in range(1, index1+1):
        if str1[i-1] != aim[i-1]:
            break
        list_TF[i][0] = 1
    # 构建二维表的第一列
    for j in range(1, index2+1):
        if str2[j-1] != aim[j-1]:
            break
        list_TF[0][j] = 1
    # 构建二维表的其余内容
    for i in range(1, index1+1):
        for j in range(1, index2+1):
            # 第一个字符串的第0个字符 = aim的第二个字符 并且 aim的第一个字符来自于第二个字符串 或者相反
            if (str1[i-1] == aim[i + j - 1] and list_TF[i - 1][j] == 1) or (str2[j-1] == aim[i+j-1] and list_TF[i][j-1] == 1):
                list_TF[i][j] = 1
    print(list_TF)
    if list_TF[len(str1)][len(str2)] == 1:
        return True
    else:
        return False

# def create_table2(str1, str2, aim):
#     if len(str1) + len(str2) != len(aim):
#         return False
#     if len(str1) >= len(str2):
#         max_str = str1
#         min_str = str2
#     else:
#         min_str = str1
#         max_str = str2
#     dp = np.zeros((len(min_str) + 1))
#     dp[0] = 1
#     for i in range(1, len(min_str)+1):
#         if min_str[i-1] != aim[i-1]:
#             break
#         dp[i] = 1
#     for i in range(1, len(max_str)+1):
#         for j in range(1, len(min_str)+1):
#             if (max_str[i-1] == aim[i+j-1] and dp[j] == 1) or (min_str[j-1] == aim[i + j -1] and dp[j-1] == 1):
#                 dp[j] = 1
#             else:
#                 dp[j] = 0
#     print(dp)
#     if dp[len(min_str)] == 1:
#         return True
#     else:
#         return False


print(create_table(str1, str2, aim))
# print(create_table2(str1, str2, aim))
