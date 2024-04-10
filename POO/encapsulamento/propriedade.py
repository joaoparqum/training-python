class Foo:

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, valor):
        self._x += valor

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)