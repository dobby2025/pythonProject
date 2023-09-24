'''
파일명: Ex22-3-O(N).py

O(N)
    선형 시간 복잡도, 입력 크기에 비례하여
    시간이 걸리는 알고리즘
'''

def linear_search(arr, x):
    size = len(arr)
    for i in range(size):
        if arr[i] == x:
            return i

    return -1

# 실행코드
arr = [1, 3, 5, 7, 9]
print(linear_search(arr, 9))


