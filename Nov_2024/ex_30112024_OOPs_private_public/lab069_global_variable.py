count = 0

def increment():
    global count #global keyword is used to access global variable inside function
    count = count + 1

increment()
increment()
increment()
increment()
print(count)