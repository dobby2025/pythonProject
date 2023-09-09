'''
Ex13-6-readHello3.py

readline() 함수
    파일에서 1줄을 읽고 그 결과를 반환 한다.
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    while True:
        str = file.readline()
        if not str:     # 읽을 값이 없으면 True가 된다.
            break
        print(str, end='')
