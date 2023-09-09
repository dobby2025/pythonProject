'''
파일명: Ex12-4-module4.py

별명사용하기
    as(alias) 키워드 사용
'''

import converter as cvt

miles = cvt.kilometer_to_miles(150)
print(f'150km = {miles}miles')

pounds = cvt.gram_to_pounds(1000)
print(f'1000g = {pounds}pounds')
