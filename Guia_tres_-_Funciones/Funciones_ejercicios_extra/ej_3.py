# 3. Función que retorna una nueva función.

def ran():
    def ran_1():
        print("Ok")
    return ran_1()

ran()