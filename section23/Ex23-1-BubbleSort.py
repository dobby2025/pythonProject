'''
파일명: Ex23-1-BubbleSort.py

1. 버블 정렬(Bubble Sort)
    인접한 두 원소를 비교하여 정렬하는 알고리즘 중 하나로,
    가장 간단한 정렬 알고리즘 중 하나이다.

    시간복잡도 : O(N^2)
'''

def bubble_sort(arr):
    n = len(arr)

    '''
           0  1  2  3  4
    arr = [3, 1, 5, 6, 8]
    n = 5
    i = 0 : 
        for 문 조건 : range(n - i - 1) => range(4)
        j = 0 : arr[0] > arr[1] : true    
        j = 1 : arr[1] > arr[2] : true
        j = 2 : arr[2] > arr[3] : true
        j = 3 : arr[3] > arr[4] : false
    i = 1 : 
        for 문 조건 : range(5 - 1 - 1) => range(3)
         j = 0 : arr[0] > arr[1] : true
         j = 1 : arr[1] > arr[2] : true
         j = 2 : arr[2] > arr[3] : false
         
       0  1  2  3  4
arr = [1, 3, 5, 6, 8]         
    i = 2 : 
        for 문 조건 : range(5 - 2 - 1) => range(2)
        j = 0 : arr[0] > arr[1] : true
        j = 1 : arr[1] > arr[2] : false
        
    i = 3 : 
        for 문 조건 : range(5 - 3 - 1) => range(1)
        j = 0 : arr[0] > arr[1] : false

       0  1  2  3  4
arr = [1, 3, 5, 6, 8]       
    i = 4 : 
        for 문 조건 : range(5 - 4 - 1) => range(0)
        
    '''

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 실행코드
arr = [6, 5, 3, 1, 8]
print(bubble_sort(arr)) # [1, 3, 5, 6, 8]