# -*- coding:utf-8 -*-
import random
from time_wrapper import timing


@timing
def bubble_sort(l):
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
    tl = list(l)
    i_min = 1
    last_min = 0
    flag = False
    n = len(tl)
    while flag:
        for i in range(last_min, n-1):
            if tl[i] < tl[last_min]:
                pass

    print("[src]", l)
    print("[tar]", tl)
    return tl


def test_main():
    test_list = [random.randint(0, 100) for _ in range(100)]
    l_sorted = bubble_sort(l=test_list)
    l_sorted = selection_sort(l=test_list)


if __name__ == "__main__":
    test_main()
