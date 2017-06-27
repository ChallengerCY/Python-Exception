#可以在try/except后面加入else
try:
    print(1)
except:
    print(2)
else:
    print(3)

#简单的例子
while True:
    try:
        x=input()
        y=input()
        value=x/y
        print("x/y is",value)
    except Exception as e:
        print("error is ",e)
        print("again")
    else:
        break

#finally
#finally用来在可能的异常后进行清理，finally里面的语句可定会被执行
#可以组合使用try except else finally
x=None
try:
    x=1/0
except Exception as e:
    print(e)
else:
    print(x)
finally:
    del x