def sum(a,b):
    answer = a+b
    return answer

def subtract(a,b):
    answer = a-b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def divide(a,b):
    answer = a/b
    return answer

def exponent(a,b):
    answer = a**b
    return answer

operations = {"+": sum, 
              "-": subtract,
              "*": multiply,
              "/": divide,
              "^": exponent
              }