class Student:
    NUMBER_OF_TASKS = 37
    TEST_WEIGHT = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]
    NUMBER_OF_TESTS = len(TEST_WEIGHT)

    def __init__(self, name, age):
        print("Hello from Student!", id(self), self)
        self.name = name
        self.age = age
        self.phone = None
        self.birthday = None
        self.hw_task = [0] * Student.NUMBER_OF_TASKS
        self.tests = [0] * Student.NUMBER_OF_TESTS

    def print_info(self):
        print('----------------------------------------------------------------------')
        print("Name:          %s" % self.name)
        print("Age:           %s" % self.age)
        print("Phone:         %s" % self.phone)
        print("Birthday:      %s" % self.birthday)
        print("Rank:          %s" % sum(self.hw_task))

        print('----------------------------------------------------------------------')

    def accept_task(self, num_task):
        self.hw_task[num_task - 1] = 1

    def accept_test(self, num_test):
        self.tests[num_test - 1] = 1

def main():
    student1 = Student('Anty', 20)
    student1.accept_task(1)
    student1.accept_task(2)
    student1.accept_task(3)
    student2 = Student('Mary', 14)

    student1.age += 1
    student2.name = 'Alice'
    student1.print_info()
    student2.print_info()


if __name__ == '__main__':
    main()
