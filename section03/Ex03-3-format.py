'''
파일명: Ex03-3-format.py

format
    {} 를 활용하여 데이터 종류에 상관없이
    print문으로 표현이 가능.
'''
print('올해는 {}년 입니다.'.format(2023))
print('올해는 {}년, 내년은 {}년 입니다.'.format(2023, 2024))
print('나는 {}을 공부 합니다.'.format('Python'))
print('나는 {}과 {}를 탑니다.'.format('지하철', '버스'))

name = '홍길동'
age = 20
print('제 이름은 {} 입니다. \n나이는 {}입니다.'.format(name, age))

address = '''서울특별시 강남구
테헤란로 123
'''
print('주소: {addr}'.format(addr=address))

'''
f-string 포맷문자열
'''
name = 'Alice'
age = 30

print(f'My name is {name} and I am {age} years old.')

job = 'developer'
company = 'TechCo'

print(f'I work as a {job} at {company}.')

temperature = 25.7

print(f'The temperature today is {temperature:.2f} degrees Celsius.')
print('The temperature today is {:.2f} degrees Celsius.'.format(temperature))

