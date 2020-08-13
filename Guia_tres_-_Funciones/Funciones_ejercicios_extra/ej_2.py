# 2. Función que pueda ser llamada de todas estas formas:
# f(), f(1), f(x=1), f(y=1), f(x=1, y=1), f(y=1, x=1).

def ran(x=0, y=0):
    print("x=", x, "y=", y)

ran()
ran(1)
ran(x=1)
ran(y=1)
ran(x=1, y=1)
ran(y=1, x=1)