'''
파일명: Ex08-3-continue.py

continue
    whiele 문이나 for문과 같은 반복문을 강제로 건너뛰게 한다.
'''
total = 0
# range(1, 101) 1~100 까지 연속된수
for a in range(1, 101):
    if a % 3 == 0:  # 3의 배수
        continue
    total += a
    print(f'a: {a}, total {total}')

print(total)
