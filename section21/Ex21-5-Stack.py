'''
Ex21-5-Stack.py

스택(Stack)
    한 쪽 끝에서만 자료를 넣거나 빼낼 수 있는 자료구조.
    후입선출(LIFO - Last In First Out) 되어 있다.
'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        print(self.stack)

# 실행 코드
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print_stack()

while not stack.is_empty():
    print('stack pop: ', stack.pop())