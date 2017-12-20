class A:
    def __init__(self):
        self.attr = 'attrA'

    def foo(self):
        print("Foo")


class A1(A):
    def __init__(self):
        super().__init__()


class B(A1):
    def __init__(self):
        super().__init__()
        self.attr2 = "attrB"


b = B()
b.foo()
print(b.attr)
print(b.attr2)
