#Web Automation - Selenium
#Page - You're going to automate

# from dotenv import load_dotenv

class login_page():

    def __init__(self, email, passcode):
        print("PC")
        self.email = email
        self.passcode = passcode

    def login_confirm(self):
        if self.email == "abc@gmail.com" and self.passcode == "pass123":
            print("Login Successful")
        else:
            print("Login Failed")

email = input("Enter usernam : ")
passcode = input("Enter password :")

user_1 = login_page(email, passcode)
user_1.login_confirm()