class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")
        super().method()

class C(A):
    def method(self):
        print("C's method")
        super().method()

class D(B, C):
    def method(self):
        print("D's method")
        super().method()

# Usage
d = D()
d.method()
print(D.mro())  # Method Resolution Order
