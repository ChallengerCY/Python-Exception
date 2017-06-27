#raise语句,可以显示异常
raise Exception
raise Exception('hyperdriver overload')

#自定义异常类
class SmoeCustomException(Exception):
    pass

#捕获异常
try:
    x=input()
    y=input()
    x1=int(x)
    y1=int(y)
    print(x1/y1)
except ZeroDivisionError:
    print("The second number can't be zero")

#设置一个异常开关
class MuffledCalculator:
    muffled=False
    def calc(self,expr):
        try:
            return eval(expr)
        except:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise

calculator=MuffledCalculator()
print(calculator.calc('10/5'))
print(calculator.calc('10/0'))
calculator.muffled=True
print(calculator.calc('10/0'))
