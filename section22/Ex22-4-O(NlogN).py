'''
파일명: Ex22-4-O(NlogN).py

O(NlogN)
    선형 로그 시간 복잡도, 병합 정렬 등의 알고리즘

'''
'''
파일명: Ex21-4-O(nlogn).py

O(NlogN)
    선형 로그 시간 복잡도, 병합 정렬 등의 알고리즘
'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

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
sorted_arr = merge_sort(arr)
print(sorted_arr)

