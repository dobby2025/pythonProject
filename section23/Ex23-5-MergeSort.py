'''
파일명: Ex23-5-MergeSort.py

병합정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각을 재귀적으로 합병 정렬하고, 다시 합치면서
    정렬하는 알고리즘

'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    '''
    [5, 2, 8, 6, 1, 9, 3, 7]
    mid = 4
    1.
    merge_sort([5, 2, 8, 6])
        mid = 2
        1-1 <- left = [2, 5]
        merge_sort([5, 2])
            mid = 1
            1-1-1
            merge_sort([5]) -> [5]
            1-1-2
            merge_sort([2]) -> [2]
            1-1-3
            merge([5], [2]) -> [2, 5]
        1-2 <- right = [6, 8]
            merge_sort([8, 6])
            mid = 1
            1-2-1
            merge_sort([8]) -> [8]
            1-2-2
            merge_sort([6]) -> [6]
            1-2-3
            merge([8], [6]) -> [6, 8]

        1-3
         merge([2, 5], [6, 8])  

    '''

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    '''
    merge([5], [2])

    result = [2, 5]
    i = 0
    j = 1
    '''

    i = j = 0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

arr = [5, 2, 8, 6, 1, 9, 3, 7]
print(arr[:4])
sorted_arr = merge_sort(arr)
print(sorted_arr)
