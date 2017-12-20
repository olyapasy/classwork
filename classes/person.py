class Person:

    def __init__(self, name, age):
        self.name = name
        self.id = 0
        self.age = age
        self.birthday = None

    def print_info(self):
        print('----------------------------------------------------------------------')
        print("ID:            %s" % self.id)
        print("Name:          %s" % self.name)
        print("Age:           %s" % self.age)
        print("Birthday:      %s" % self.birthday)
