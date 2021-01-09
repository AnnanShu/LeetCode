list1 = [1,2,3,4]
list1.insert(-1, 6)
list1

list1.pop(-2)
list1

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_level = 0
        self.length = 0
        self.stack = []


    def push(self, x: int) -> None:
        if self.length == 0:
            self.length += 1
            self.stack.append(x)
        elif x < self.stack[-1]:
            self.length += 1
            self.stack.append(x)
        else:
            self.length += 1
            self.min_level += 1
            self.stack.insert(-1, x)

    def pop(self) -> None:
        if self.min_level == 0:
            self.length -= 1
            self.stack.pop()
        else:
            self.length -= 1
            self.min_level -= 1
            self.stack.pop(-2)


    def top(self) -> int:
        return self.stack[-2]


    def getMin(self) -> int:
        return self.stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()