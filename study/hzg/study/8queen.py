# -*- coding: utf-8 -*-

"""八皇后问题"""

def is_safe(queens_added, x):
    y = len(queens_added)  # 每一行都有一个皇后，所以len(queens_added)获得的既是当前已经存在的皇后个数，也是下一个皇后所在的行数
    for i in xrange(y):
        if abs(queens_added[i] - x) in (0, y - i):  # 皇后所在的行数不可能相等，所以只要判断是否在同一列或在斜线上
            return False
    return True

def queens(num, queens_added=()):
    for x in xrange(num):
        if is_safe(queens_added, x):
            if len(queens_added) == num - 1:  # 如果已经放置了num-1个皇后，则返回最后一个皇后所在的列数
                yield (x,)
            else:
                for result in queens(num, queens_added + (x,)): # 递归调用
                    yield (x,) + result

queen_num = 8
for result in queens(queen_num):
    print result

