'''
파일명: Ex02-9-mutable-immutable.py

mutable - 메모리 값을 변경 가능 객체
    리스트(list), 세트(set), 딕셔너리(dict) .. 등
'''
me = [1, 2, 3]
print(me)
print(id(me))

me.append(4)
print(me)
print(id(me))

'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
imme = 10
print(imme)
print(id(imme))

imme += 1 # imme = imme + 1
print(imme)
print(id(imme))

imme2 = 10
print(imme2)
print(id(imme2))

print('================================')

# 튜플 id값 확인하기
thistuple = ('피카츄', '라이츄', '파이리')
print(thistuple)
print(id(tuple))
# casting(형변환) ['피카츄', '라이츄', '파이리']
thiscast = list(thistuple)
thiscast[1] = '잠만보'
thistuple = tuple(thiscast) # ('피카츄', '잠만보', '파이리')
print(thistuple)
print(id(thistuple))