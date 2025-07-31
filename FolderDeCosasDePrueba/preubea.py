'''prueba = 'unknown'

def func():
    global prueba 
    print(prueba)
    if prueba == 'unknown':
        prueba = 'known'
    return prueba

def func2():
    return prueba

func()
print(func2())
print(prueba)
'''
'''
# This is a decorator
def measure_time(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - t0:.5f} seconds")
        return res
    return wrapper

@measure_time
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print(is_prime(99999999999973))


'''
'''
def greet(f):
    def decorator():
        print("Hi form decorator")
        f()
        print("Bye from decorator")
    return decorator

@greet
def demo():
    print("Hi from demo")

#demo = greet(demo)

demo()
'''
'''
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You added sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You've added fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream")

get_ice_cream("chocolate")
'''

import datetime
def log(func):
    def wrapper(*args, **kwargs):
        with open(r"e:\nkh31\Documents\IntegradoraAldo10.0\IntegradoraAldoATMP9.0\FolderDeCosasDePrueba\logs.txt", "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val
        
    return wrapper
    
@log    
def run(a, b, c=3):
    print(a + b + c)

run(5, 10, c=3)
