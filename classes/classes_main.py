from student import Student
from professor import Professor
from pprint import pprint
def main():

    student1 = Student('Anty', 20)
    student1.accept_task(1)
    student1.accept_task(2)
    student1.accept_task(3)
    student2 = Student('Mary', 14)

    student1.age += 1
    student2.name = 'Alice'
    student2.accept_test(12)
    student1.accept_test(7)
    student1.print_info()
    student2.print_info()


    pprint(student1.__dict__)


    professor1 = Professor('Dr.Who',30)
    professor1.print_info()

if __name__ == '__main__':
    main()