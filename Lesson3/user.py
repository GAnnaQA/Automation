class User:
    first_name = "No name"
    last_name = "No surname"
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def getFirstName(self):
        print("Ваше имя", self.first_name)
    def getLastName(self):
        print("Ваша фамилия", self.last_name)
    def getFullName(self):
        print("Вас зовут", self.first_name, self.last_name)