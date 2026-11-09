
def func():
    global count
    if count == 4:
        return 
    count+=1
    print(count)
    func()


count = 0

func()