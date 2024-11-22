import datetime
import time
from turtledemo.penrose import start


def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time



def test_log(func):
    def wrapper():
        print("Test start time : ", show_time())
        func()
        print("Test end time :", show_time())
        print("Total time taken :")
    return wrapper()

@test_log
def test_case_1():
    print("Executing test-1....")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("....")
    time.sleep(5)
    print("Execution completed")
