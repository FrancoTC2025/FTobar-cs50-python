# pedir nombre al usuario, variable name, funciones :input guarda variable, quita espacios enblanco izq y der strip() y title () para colocar en mayus
name = input("What is your name?").strip().title()
# saludar usuario
print(f"hello, {name}")
