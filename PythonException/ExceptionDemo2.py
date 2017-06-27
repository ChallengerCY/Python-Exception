#捕获多个异常
try:
    x=input()
    y=input()
    print(x/y)
except ZeroDivisionError:
    print("The Second number cant't be zero")
except TypeError:
    print("That's wasn't a number,was it?")

#用一个块捕获多个异常
try:
    x=input()
    y=input()
    print(x/y)
except(ZeroDivisionError,TypeError,NameError):
    print('You numbers were bogus...')

#显示的捕获异常
try:
    x=input()
    y=input()
    print(x/y)
except(ZeroDivisionError,TypeError,NameError) as e:
    print(e)

#全部捉
try:
    x=input()
    y=input()
    print(x/y)
except Exception as e:
    print(e)
