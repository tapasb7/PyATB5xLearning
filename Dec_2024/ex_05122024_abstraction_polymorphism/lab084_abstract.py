from abc import ABC, abstractmethod

class Excel_reader(ABC):
    @abstractmethod
    def read_from_excel(self):
        pass

class Browser(Excel_reader):
    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def close_browser(self):
        pass

class TestCase():

    def prepare_testbed(self):
        print("prepare testbed")

    def start_browser(self):
        print("Browser starting")

    def read_from_excel(self):
        print("Reading test data from Excel")

    def close_browser(self):
        print("Closing Browser")


    def run_test(self):
        self.prepare_testbed()
        self.start_browser()
        self.read_from_excel()
        self.close_browser()

    @staticmethod
    def log_result():  # static methods can be called using classname.methodname
        print("-----------------------")
        print("results logged")

obj_1 = TestCase()
obj_1.run_test()
TestCase.log_result() #static method called using class-name only. object not required



