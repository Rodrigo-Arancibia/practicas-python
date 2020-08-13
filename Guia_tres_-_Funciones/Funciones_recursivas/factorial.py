#  1 -> n == 1
# n * factorial(n-1)


def factorial(n):
    if n == 1:
        return 1
    else:
        fac = n * factorial(n-1)
        print( f"El factorial de {n} es: {n} * !{n-1}.  ", f"O sea: {fac}")

    return fac
    
factorial(10)