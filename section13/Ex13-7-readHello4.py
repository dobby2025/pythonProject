'''
Ex13-7-readHello4.py

readlines() - 줄단위 요소로 리스트 타압으로 반환
'''

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    for line in line_list:
        print(line, end='')
