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


def stacksort(s):  # 不使用额外数据结构进行栈排序
    t1 = s.pop()  # 取出栈顶元素
    if s.isEmpty():  # 递归结束条件
        s.push(t1)
        return
    stacksort(s)  # 使用递归方法对取出后的栈进行排序
    t2 = s.pop()  # 比较交换栈顶元素
    if t1 > t2:
        t1, t2 = t2, t1
    s.push(t2)
    stacksort(s)  # 再次进行排序
    s.push(t1)
    return


s = Stack()
A = [1, 5, 2, 3, 5, 6, 7, 8, 2, 3, 10, 4]
for num in A:
    s.push(num)
print("原栈")
s.printStack()
stacksort(s)
print("排序后")
s.printStack()
