# -*- coding:utf-8 -*-
from __future__ import print_function
import random
from time_wrapper import timing


@timing
def bubble_sort(l):
    """
    从第一个数字开始依次与后面一个数比较，如果比它大/小则交换两个数字
    保证最后一个数一定是列表中最大/小的数字
    :param l:
    :return:
    """
    tl = list(l)
    n = len(tl)
    k = n   # 用于记录最后交换的位置，说明后面的列表已经是有序的了
    cnt = 0
    for i in range(n):
        flag = True     # 用于标记本次是否有进行排序
        for j in range(1, k):   # j 永远记录大数的位置
            if tl[j - 1] > tl[j]:
                tl[j - 1], tl[j] = tl[j], tl[j - 1]
                k = j
                flag = False
                cnt += 1
        if flag:
            break

    print("[src]", l)
    print("[tar]", tl)
    return tl


@timing
def selection_sort(l):
    """
    记录最小的数字的下标
    先默认地一个最小，然后从后面找出最小和地一个做替换
    :param l:
    :return:
    """
    tl = list(l)
    n = len(tl)
    for i in range(0, n):
        i_min = i
        for j in range(i, n):
            if tl[i_min] > tl[j]:
                i_min = j
        tl[i_min], tl[i] = tl[i], tl[i_min]

    print("[src]", l)
    print("[tar]", tl)
    return tl


@timing
def insertion_sort(l):
    """
    找到第一个无序的索引，把它和前面的数依次对比，如果大则往后移动一位
    否则，说明找到了插入的位置，则将当前数字插入
    :param l:
    :return:
    """
    tl = list(l)
    n = len(tl)
    for i in range(1, n):
        if tl[i-1] > tl[i]:     # 找到无序的位置
            temp = tl[i]
            index = i       # 待插入的下标
            for j in range(i-1, -1, -1):    # 从i-1 循环到 0 (包括0)
                if tl[j] > temp:
                    tl[j+1] = tl[j]
                    index = j   # 记录待插入下标
                else:
                    break
            tl[index] = temp

    print("[src]", l)
    print("[tar]", tl)
    return tl


def test_main():
    test_list = [random.randint(0, 100) for _ in range(100)]
    # test_list = []

    l_sorted = bubble_sort(test_list)
    l_sorted = selection_sort(test_list)
    l_sorted = insertion_sort(test_list)


if __name__ == "__main__":
    test_main()
