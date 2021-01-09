a = [1, 2, 3, 4, 5]

for e in a:
    print(e)

it = iter(a)
while True:
    try:
        val = next(it)
    except StopIteration:
        break
    print(f'val = {val}')


class MyList:
    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        pass

from collections import deque
stack = deque()
stack.append(3)
stack.pop()

len(stack) == 0
stack 
