# 归并排序--> 分治算法


def sort(left, right):
    re = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            re.append(left[i])
            i += 1
        else:
            re.append(right[j])
            j +=1
    re += left[i:]
    re += right[j:]
    return re

#  先分
def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = mergesort(a[:mid])
    right = mergesort((a[mid:]))
    return sort(left, right)


arr = [2, 3, 4, -9, -3, 10]
print(mergesort(arr))


# 堆排序
# 堆排序
# n 就是树的节点个数，i 就是对哪个节点进行heapify


def heapify(tree, n, i):
    if i > n:
        return
    left = 2*i + 1
    right = 2*i + 2
    max_value = i
    if left <= n and tree[left] > tree[max_value]:
        max_value = left
    if right <= n and tree[right] > tree[max_value]:
        max_value = right
    if max_value != i:
        tree[i], tree[max_value] = tree[max_value], tree[i]
        heapify(tree, n, max_value)


def build_heap(tree, n):
    root = (n-1)//2
    for i in range(root, -1, -1):
        heapify(tree, n, i)
    root = (n - 1)// 2

# 插入一个元素
def insert(arr,i):
    arr.append(i)
    build_heap(arr, len(arr)-1)
    print(arr)

# 删除
def heap_sort(tree, index_length):
    build_heap(tree, index_length)
    print(tree)
    # 把第一个节点和最后一个节点进行交换
    for i in range(index_length, 0, -1):
        tree[0], tree[i] = tree[i], tree[0]
        # 然后进行heapify
        heapify(tree, i-1, 0)


arr = [2, 5, 3, 1, 10, 4]
heap_sort(arr, len(arr)-1)
print(arr)


# bubble sort
# 相邻的两个数做比较然后交换位置
def bubble(arr, n):
    for i in range(n):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]


def bubble_loop(arr, n):
    for i in range(n, 0, -1):
        bubble(arr, i)


arr = [2, 3, 1, -9, -3, 10]
bubble_loop(arr, len(arr)-1)
print(arr)


# 选择排序
# 记录最大的那个数的索引，然后将最大那个数的索引和最后一个数进行交换


def choose(arr, n):
    max_index = 0
    for i in range(n+1):
        if arr[max_index] < arr[i]:
            max_index = i
    return max_index


def choose_sort(arr, n):
    for i in range(n, 0, -1):
        index = fast(arr, i)
        arr[index], arr[i] = arr[i], arr[index]


arr = [2, 3, 1, -9, -3, 10]
choose_sort(arr, len(arr)-1)
print(arr)

# 插入排序
def insert(arr, n):
    key = arr[n]
    i = n
    while i > 0 and arr[i - 1] > key:
        arr[i] = arr[i - 1]
        i -= 1
    arr[i] = key


def insert_loop(arr, n):
    for i in range(1, n + 1):
        insert(arr, i)


arr = [2, 3, 1, -9, -3, 10]
insert_loop(arr, len(arr) - 1)
print(arr)


# 快速排序
# 找到一个基准，将大于基准的放在基准的后面。将小于基准的放在基准的前面


def partition(arr, left, right):
    base = arr[left]
    i = left + 1
    j = right
    while (True):
        # 左指针向左进行扫描 当遇见比base 大的数的时候停下
        while i <= j and arr[i] <= base:
            i += 1
        # 右指针向右扫描  当遇见比base 小的数的时候停下
        while j >= i and arr[j] >= base:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


def loop(arr, left, right):
    if left >= right:
        return
    center = partition(arr, left, right)
    loop(arr, left, center - 1)
    loop(arr, center + 1, right)


arr = [2, 5, 3, 1, 10, 4]
loop(arr, 0, len(arr) - 1)
print(arr)

# 统计排序 用于最大值和最小值差距较小的区间 用于arr当中有很多重复的数字的时候
# 根据每个数出现的次数 进行输出

def count_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    # 构建一个长度为max_num - min_num 的数组
    result = [0 for i in range(max_num - min_num+1)]
    # 开始统计arr 中重复数字的个数
    for i in arr:
        result[i] += 1
    re = []
    for i in range(len(result)):
        for j in range(result[i]):
            re.append(i)
    return re
arr=[0,1,9,9,3,0,4,2,8,4,6]
print(count_sort(arr))
