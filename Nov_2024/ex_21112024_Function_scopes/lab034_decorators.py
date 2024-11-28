def before_api_test(func):
    def wrapper():
        print("Check Env before test")
        print("Check is completed..")
        func()
        print("Testcase run completed successfully")
    return wrapper()

# def after_cloud_test(func):
#     def wrapper():
#         print("Check reports for cloud-test phase two")
#         print("Check is completed..")
#         func()
#         print("No Errors!")
#     return wrapper()

@before_api_test #decorator called here
def test_api():
    print("Actual API testcase runs here, we test the API")

@before_api_test
def test_cloud():
    print("Tests in cloud takes more time to complete..please wait")

