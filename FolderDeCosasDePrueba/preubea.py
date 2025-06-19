prueba = 'unknown'

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

