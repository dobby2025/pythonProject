'''
파일명: Ex13-8-readHello5.py

readlines() - 줄단위 요소로 리스트 타압으로 반환
'''

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    for no, line in enumerate(line_list):
        print(f'{no+1} {line}', end='')
