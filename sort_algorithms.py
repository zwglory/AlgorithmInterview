# -*- coding:utf-8 -*-
from __future__ import print_function
import time
import random
from time_wrapper import timing


#####################################
@timing
def bubble_sort(l):
    """冒泡排序
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

    print("[src]", l[:100])
    print("[tar]", tl[:100])
    return tl


#####################################
@timing
def selection_sort(l):
    """选择排序
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

    print("[src]", l[:100])
    print("[tar]", tl[:100])
    return tl


#####################################
@timing
def insertion_sort(l):
    """插入排序
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

    print("[src]", l[:100])
    print("[tar]", tl[:100])
    return tl


#####################################
@timing
def shell_sort(l):
    """希尔排序
    就是把一个数组按照一定的步长分开，然后做插入排序
    有时候快的飞起
    :param l:
    :return:
    """
    tl = list(l)
    n = len(tl)
    gap = int(n/2.)
    while gap > 0:
        for i in range(gap, n):
            temp = tl[i]
            j = i
            while j >= gap and tl[j-gap] > temp:
                tl[j] = tl[j-gap]
                j = j - gap
            tl[j] = temp
        gap = int(gap/2.)

    print("[src]", l[:100])
    print("[tar]", tl[:100])
    return tl


#####################################
def merge(left, right):
    merged = []
    l_idx, r_idx = 0, 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            merged.append(left[l_idx])
            l_idx += 1
        else:
            merged.append(right[r_idx])
            r_idx += 1
    merged += left[l_idx:] + right[r_idx:]
    return merged


def merge_sort(l):
    """归并排序
    分治法思想
    将数列依次二分，左右分别排序，然后合并排序后的结果
    :param l:
    :return:
    """
    tl = list(l)
    if len(tl) <= 1:
        return tl
    n = len(tl)
    split_idx = int(n/2.)
    sorted_left  = merge_sort(l=tl[:split_idx])
    sorted_right = merge_sort(l=tl[split_idx:])
    return merge(left=sorted_left, right=sorted_right)


#####################################
def qsort_partition(l, left, right):
    """
    :param l:
    :param left: 左指针，左边界
    :param right: 右指针，右边界
    :return:
    """
    if left >= right:
        return l
    base = l[left]      # 基准数一直是 left
    lp = left
    rp = right
    while lp < rp:
        # 左右顺序不能改变
        while l[rp] >= base and lp < rp:
            rp -= 1
        while l[lp] <= base and lp < rp:
            lp += 1
        l[lp], l[rp] = l[rp], l[lp]

    l[left], l[lp] = l[lp], l[left]
    qsort_partition(l, left, lp-1)
    qsort_partition(l, rp+1, right)
    return l


def quick_sort(l):
    """快速排序
    快速排序通常明显比同为Ο(n log n)的其他算法更快，因此常被采用，
    而且快排采用了分治法的思想，所以在很多笔试面试中能经常看到快排的影子。

    分治法

    :param l:
    :return:
    """
    tl = list(l)
    return qsort_partition(tl, 0, len(tl)-1)


#####################################
def max_heapify(ary, start, end):
    """
    最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
    start 为当前需要调整最大堆的位置，end 为调整边界
    :param ary:
    :param start:
    :param end:
    :return:
    """
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end :
            break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break


@timing
def heap_sort(l):
    """堆排序
    堆排序在 top K 问题中使用比较频繁。
    堆排序是采用二叉堆的数据结构来实现的，
    虽然实质上还是一维数组。二叉堆是一个近似完全二叉树 。
    :param l:
    :return:
    """
    tl = list(l)
    n = len(tl)
    first = int(n / 2 - 1)  # 最后一个非叶子节点
    for start in range(first, -1, -1):  # 构造大根堆
        max_heapify(tl, start, n - 1)
    for end in range(n - 1, 0, -1):  # 堆排，将大根堆转换成有序数组
        tl[end], tl[0] = tl[0], tl[end]
        max_heapify(tl, 0, end - 1)

    print("[src]", l[:100])
    print("[tar]", tl[:100])
    return tl


#####################################
@timing
def build_in_sort(l):
    tl = sorted(l)
    print("[src]", l[:100])
    print("[tar]", tl[:100])
    return tl


#####################################
def test_main():
    test_list = [random.randint(0, 1000) for _ in range(1000)]

    l_sorted = bubble_sort(test_list)
    l_sorted = selection_sort(test_list)
    l_sorted = insertion_sort(test_list)
    l_sorted = shell_sort(test_list)

    tic = time.time()
    print("=" * 40)
    print("merge_sort")
    l_sorted = merge_sort(test_list)
    print("[src]", test_list[:100])
    print("[tar]", l_sorted[:100])
    print("Elapsing time: %0.5f s" % (time.time()-tic))

    tic = time.time()
    print("=" * 40)
    print("quick_sort")
    l_sorted = quick_sort(test_list)
    print("[src]", test_list[:100])
    print("[tar]", l_sorted[:100])
    print("Elapsing time: %0.5f s" % (time.time() - tic))

    l_sorted = heap_sort(test_list)

    l_sorted = build_in_sort(test_list)


if __name__ == "__main__":
    test_main()
