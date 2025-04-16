import numpy as np

# 定义一个变量类
class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    # 设置这个变量是由哪个函数创建的(output)
    def set_creator(self, func):
        self.creator = func

    def backward(self):
        # 保存当前的创造函数
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            # 得到保存在fun(creator)中的输入和输出
            x, y = f.input, f.output
            # 设置输入(input-x.grad)的梯度为输出(output-y.grad)的梯度乘以函数的导数
            x.grad = f.backward(y.grad)

            if x.creator is not None:
                funcs.append(x.creator)

class Function:
    def __call__(self, input):
        x = input.data
        # 执行不同function具体的计算过程
        y = self.forward(x)
        # 封装成Variable变量
        output = Variable(y)
        output.set_creator(self)
        self.input = input
        self.output = output
        return output

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()


class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y

    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx


class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y

    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx


A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

print(y.data)

# backward
y.grad = np.array(1.0)
y.backward()
print(x.grad)















