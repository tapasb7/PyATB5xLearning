# Create a Class Name API - RestfulBooker
# name, list_of_api , links {}
# print_apis, print_set()



class API():
    name = None
    api_list = ["API_1", "Google_API", "Cloud_API"]
    links = {"www.api.com", "www.google.com", "www.cloud.com"}

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

    def show_details(self):
        print(self.api_list)
        print(self.links)


RestfulBooker = API("Vida")
RestfulBooker.show_name()
RestfulBooker.show_details()
