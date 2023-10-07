'''
파일명: Ex22-7-O(n!).py

O(n!)
    팩토리얼 시간 복잡도, 순열을 구하는 알고리즘
'''

'''          
          0    1    2    3 
data  = ['a', 'b', 'c', 'd']
i = 0 
length = 4
'''
def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        '''
                  0    1    2    3 
        data  = ['a', 'b', 'c', 'd']
        i = 0 
        length = 4
        j : 0 
            data[0], data[0] = data[0], data[0]
            permute(data, 1, 4)
                i = 1 
                length = 4
                j : 1 
                    data[1], data[1] = data[1], data[1]
                    permute(data, 2, 4)
                        i = 2 
                        length = 4
                        j : 1 
                            data[1], data[1] = data[1], data[1]
                            permute(data, 2, 4)
                                i = 2 
                                length = 4
                        
        '''
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]

# 실행코드
data = list('abcd')
permute(data, 0, len(data))