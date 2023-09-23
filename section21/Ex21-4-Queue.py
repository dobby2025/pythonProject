'''
Ex21-4-Queue.py

큐(Queue)
    기본적인 자료구조 한가지로, 먼저 넣은 데이터가 먼저 나오는
    FIFO(First In First Out) 형태의 자료구조
'''

def Queue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    while queue:
        print(f'Get Value: {queue.pop(0)}')

# 실행코드
Queue()