'''
파일명: Ex05-1-if.py

조건문 
    특정 조건을 만족하는지 여부에 따라
    실행하는 코드가 달라야 할 때 사용하는 명령어
    들여쓰기를 사용하여 코드의 범위 정의.
    
1. 방법
    if 조건식:
        조건식이 참일경우 실행할 코드 영역

2.
    if 조건식:
        조건식이 참일경우 실행할 코드 영역
    else:
        조건식이 거짓일경우 실행할 코드 영역


3.
    if 조건식1:
        조건식1 참일경우 실행할 코드영역
    elif 조건식2:
        조건식2 참일경우 실행할 코드영역
    elif 조건식3:
        조건식3 참일경우 실행할 코드영역
    else:
        모든 조건식이 거짓일경우 실행할 코드영역
'''
# if
a = 100
b = 200
if b > a:
    print('b는 a보다 크다.')
    
    
    print('if문 코드영역')

# if ~ else
a = 7
b = 4
if b >= a:
    print('b는 a보다 크거나 같다.')
else:
    print('b는 a보다 작다.')

# if ~ elif ~ else
c = 3
if c == 1:
    print('c는 1이다.')
elif c == 2:
    print('c는 2이다.')
elif c == 3:
    print('c는 3이다.')
else:
    print('1,2,3 모두 아니다.')

