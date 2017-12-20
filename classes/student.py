from person import Person

class Student(Person):
    NUMBER_OF_TASKS = 37
    TEST_WEIGHT = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]
    NUMBER_OF_TESTS = len(TEST_WEIGHT)

    def __init__(self, name, age):
        print("Hello from Student!", id(self), self)
        super().__init__(name,age)
        self.phone = None
        self.group = "AI-15-X"
        self.hw_task = [0] * Student.NUMBER_OF_TASKS
        self.tests = [0] * Student.NUMBER_OF_TESTS

    def print_info(self):
        super().print_info()
        print("Phone:         %s" % self.phone)
        print("Rank:          %s" % self.total_rank())
        print("Group:         %s" % self.group)
        print('----------------------------------------------------------------------')

    def accept_task(self, num_task):
        self.hw_task[num_task - 1] = 1

    def accept_test(self, num_test):
        self.tests[num_test - 1] = 1



    def total_rank(self):
        result = sum(self.hw_task)
        for i in range(self.NUMBER_OF_TESTS):
            result += (self.tests[i] * self.TEST_WEIGHT[i])
        return result
