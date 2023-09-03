'''
파일명: Ex06-4-while4.py



'''
dan = 2
while dan <= 9:     # dan: 2 n:1-> 2x1=2 n:2 -> 2x2=4 ... 2x9=18
                    # dan: 3 n:1-> 3x1=3 n:2 -> 3x2=6 ... 3x9=27
                    # ...
                    # dan: 9 n:1-> 9x1=9 ... 9x9=81
                    # dan: 10일때 밖같쪽 while문 종료

    n = 1
    while n <= 9:
        print(f'{dan}X{n}={dan*n}', end=' ')
        n += 1
    dan += 1
    print()
