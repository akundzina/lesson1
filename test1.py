#metaclasses
'''class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if 'baz' not in body:
            raise TypeError()
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def bar(self):
        return self.baz()
'''
#decorators

'''def log(f):
    def logged(x,y):
        rv = f(x, y)
        print(f.__name__, x, y, '->', rv)
        return rv
    return logged
@log
def add(x,y=3):
    return x + y

add(4,6)'''
#print(add.__defaults__)
#print(add.__code__)
#generators
'''def gen():
    i=0
    while True:
        i += 1
        yield i'''
#context managers

#generator test - get primes till max value
import time
start = time. time()

from dis import dis
def f(x, y):
    return x + y
dis(f)

def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

'''def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number

primes = Primes(10000)

print(primes)

for x in primes:
    print(x)'''

primes = (i for i in range(2, 100) if check_prime(i))

print(primes)

for x in primes:
    print(x)

end = time. time()
print(end - start)

#test error handling with input
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
         raise ValueError("That is not a positive number!")
except ValueError as ve:
     print(ve)
finally:
    print(a)

