#https://docs.python.org/3/tutorial/modules.html
print('#' * 50)
print('6. Modules')

import fibo
fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)

print('assign it to a local name')
fi = fibo.fib
fi(500)




print('#' * 50)
print('6.1. More on Modules')

print('imports names from a module')
from fibo import fib, fib2
fib(500)

print('imports  used when utilising')
from fibo import fib as fibonacci
fibonacci(500)




print('#' * 50)
print('6.1.1. Executing modules as scripts')

