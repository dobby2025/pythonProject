'''
파일명: Ex21-0-recursive.py

재귀함수(Revcursive function)
    함수 내부에서 자기 자신을 호출하는 함수를 말한다.
'''

def count_number(n):
    while n > 0:
        print(n)
        n -= 1



'''
recursive_count_number(5) => print(5)
     recursive_count_number(4) => print(4)
        recursive_count_number(3) => print(3)
             recursive_count_number(2) => print(2)
                 recursive_count_number(1) => print(1)
                    recursive_count_number(0) => return (종료)
'''
def recursive_count_number(n):
    if(n <= 0):
        return
    print(n)
    recursive_count_number(n - 1)

# 실행코드
# count_number(5)
recursive_count_number(5)
