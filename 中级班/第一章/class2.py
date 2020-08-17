import pandas as pd
import numpy as np

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cal(a, b):
    fenzi = a.y - b.y
    if fenzi == 0:
        return str(0)
    fenmu = a.x - b.x
    if fenmu == 0:
        return '无穷大'
    i = min(fenzi, fenmu)
    if i > 0:
        while i >= 2:
            if fenzi % i == 0 and fenmu % i == 0:
                fenzi = fenzi / i
                fenmu = fenmu / i
            i -= 1
        return str(int(fenzi)) + "/" + str(int(fenmu))
    elif i < 0 and (fenzi < 0 and fenmu > 0 or fenzi > 0 and fenmu < 0):
        i = min(abs(fenzi), abs(fenmu))
        while i >= 2:
            if fenzi % i == 0 and fenmu % i == 0:
                fenzi = fenzi / i
                fenmu = fenmu / i
            i -= 1
        return '-' + str(int(abs(fenzi))) + "/" + str(int(abs(fenmu)))
    else:
        i = min(abs(fenzi), abs(fenmu))
        while i >= 2:
            if fenzi % i == 0 and fenmu % i == 0:
                fenzi = fenzi / i
                fenmu = fenmu / i
            i -= 1
        return str(int(abs(fenzi))) + "/" + str(int(abs(fenmu)))


def tabel(length, arrx, arry):
    tabel_test = pd.DataFrame(index=range(1, length + 1), columns=range(1, length + 1), data=np.nan)
    for index1 in range(len(arrx)):
        for index2 in range(len(arry)):
            tabel_test.iloc[index1, index2] = cal(point(arrx[index1], arry[index1]), point(arrx[index2], arry[index2]))
    for item in range(length):
        tabel_test.iloc[item, item] = '基准'
    result = []
    for item in range(length):
        data = tabel_test.iloc[:, item].value_counts()
        result.append((data.index[0], data[0]))
    x = sorted(result, key=lambda x: x[1], reverse=True)[0][1]
    return x + 1


# print(tabel(5, arrx=[1, 2, 3, 4, 5], arry=[1, 1, 1, 1, 1]))
# print(tabel(5, arrx=[1, 1, 1, 1, 1], arry=[1, 2, 3, 4, 5]))
# print(tabel(5, arrx=[1, 2, 3, 4, 5], arry=[1, 2, 3, 4, 5]))
# print(tabel(5, arrx=[1, 2, 3, 4, 5], arry=[1, 2, 3, 4, 5]))
