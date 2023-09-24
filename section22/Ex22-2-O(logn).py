'''
파일명: Ex22-2-O(logn).py

O(logN)
    로그 시간 복잡도, 이진 탐색처럼 문제를 절반으로 나누어 해결하는 알고리즘
'''


def binary_search(arr, x):

    # 검색 범위 시작점 설정
    low = 0
    # 검색 범위 끝점 설정
    high = len(arr) - 1

    '''
    arr = [1, 3, 5, 7, 8, 9, 10, 11, 21]
    
    low = 8
    high = 8
    mid = 8
    arr[mid] = 21
    x = 21
    '''
    num = 0
    while low <= high:
        num += 1
        print(num)
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

# 실행코드
arr = [1, 10, 5, 7, 8, 9, 3, 11, 21]
arr = sorted(arr)

print(arr)
print(binary_search(arr, 21))
