class Stack:  # 栈数据结构与基本方法定义
    def __init__(self):
        self.list=[]

    def isEmpty(self):
        returnValue = True if len(self.list) == 0 else False
        return returnValue

    def length(self):
        return len(self.list)

    def push(self, x):
        self.list.append(x)

    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.list[-1]
        else:
            return None

    def printStack(self):
        print("Top ->:")
        for i in range(len(self.list) - 1, -1, -1):
            print(self.list[i])


def bottom(s, x):  # 将元素x压入栈底
    a = s.pop()
    if s.isEmpty():
        s.push(x)
        s.push(a)
        return
    bottom(s, x)
    s.push(a)
    return


def stackreverse(s):  # 不使用额外数据结构将栈逆序
    t = s.pop()
    if s.isEmpty():
        s.push(t)
        return
    stackreverse(s)
    bottom(s, t)
    return


s = Stack()
A = [1, 2, 3, 4, 5, 6, 7]
for num in A:
    s.push(num)
print("原栈")
s.printStack()
stackreverse(s)
print("逆序后")
s.printStack()