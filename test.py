class Entry:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def hello(self):
        print("Hello", self.name, self.surname)

entry = Entry("Onur", "Sen")
entry.hello()