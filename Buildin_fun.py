x1 = abs(-7.25)
print(x1)
mylist = [True, False, True]
x2 = all(mylist)
print(x2)
x3 = any(mylist)
print(x3)
x4 = ascii("My name is Ståle")
print(x4)
x5 = bin(36)
print(x5)
x6 = bool(1)
print(x6)
def x7():
  a = 5
print(callable(x7))
x8 = chr(97)
print(x8)
x9 = compile('print(55)', 'test', 'eval')
exec(x9)
x10 = dict(name = "John", age = 36, country = "Norway")
print(x10)
mylist1 = ['apple', 'banana', 'cherry']
x11 = frozenset(mylist1)
print(x11)
print("Enter your name:")
x12 = input()
print("Hello, " + x12)
x13 = isinstance(5, int)
print(x13)
x14 = iter(["apple", "banana", "cherry"])
print(next(x14))
print(next(x14))
print(next(x14))
x15 = list(('apple', 'banana', 'cherry'))
print(x15)
x16 = max(5, 10)
print(x16)
def myfunc(a1):
  return len(a1)
x17 = map(myfunc, ('apple', 'banana', 'cherry'))
print(x17)
print(list(x17))
x18 = set(("apple", "banana", "cherry"))
print(x18)
a2 = ("b", "g", "a", "d", "f", "c", "h", "e")
x19 = sorted(a2)
print(x19)
x20 = tuple(("apple", "banana", "cherry"))
print(x20)
a3 = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33
print(type(a3))
print(type(b))
print(type(c))
a4 = (1, 2, 3, 4, 5)
x21 = sum(a4)
print(x21)
x22 = pow(4, 3)
print(x22)
x23 = range(6)
for n in x23:
  print(n)







