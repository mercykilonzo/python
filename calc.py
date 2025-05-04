def add (a,b):
    answer = a+b
    return answer

def subtract (a,b):
    answer = a -b
    return answer

def mutiply(a,b):
    answer = a*b
    return answer

def divide(a,b):
    answer = a/b
    return answer


def modulus(a,b):
    answer = a%b
    return answer

def exponent(a,b):
    answer= a**b
    return answer


def square(a):
    answer= a*a
    return answer

def cube(a):
    answer = a*a*a
    return


def sum(* numbers):
    total = 0
    for number in numbers:
        total+=number
    return total