def area_of_rectangle(width, height):
    area = width*height
    return area
 
def perimeter_of_rectangle(width, height):
    perimeter = 2 * (width + height)
    return perimeter

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Nao e possivel dividir por 0"
    return a / b