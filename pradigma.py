def detectar_SQL_inyection(texto): 
    patrones_peligrosos=["'", "--", ";", "/*", "*/", "OR", "AND", "DROP", "SELECT", "UNION"]

    texto_mayus = texto.upper()

    for patron in patrones_peligrosos:
        if patron in texto_mayus:
            return True 

    return False

entrada= input("Ingrese el usuario: ")

if detectar_SQL_inyection(entrada):
        print("Posible intento de SQL Inyection detectado")

else:
        print("Usuario validado correctamemte :) ")


# def saludo():
    
# print("Hola mundo")



# print("Hola")