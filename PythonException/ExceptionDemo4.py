#如果函数中发生异常并且没被处理，它会继续传播，一直到达主程序
def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print("Exception handle")

ignore_exception()