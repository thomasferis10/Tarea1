
def suma(a,b):
    real = a[0] + b[0]
    imaginario = a[1] + b[1]
    return (real, imaginario)



def resta(c,d):
    real = c[0] - d[0]
    imaginario = c[1] - d[1]
    return (real, imaginario)



def multiplicacion(a,b):
    real = (a[0] * b[0])-(a[1] * b[1])
    imaginario = (a[1] * b[0])+(a[0] * b[1])
    return (real, imaginario)



def division(a,b):
    real = ((a[0] * b[0]) + (a[1] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    imaginario = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    return (real, imaginario)


def modulo(a,b):
    real = (a * a + b * b)**0.5
    return (real)


def conjugado(a,b):
    real = a
    imaginario = -b
    return (real, imaginario)


print("Bienvenido a su libreria de computación cuántica")
print("Realizado por Thomas Feris Riaño")
