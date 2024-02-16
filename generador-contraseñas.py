import string
import random

#establecemos longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))

#genera los caracteres para usar en la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation  

#genera aleatoriamente la contraseña con la longitud determinada
contraseña = "".join(random.choice(caracteres) for i in range(longitud))

#imprime la contraseña generada
print("La contraseña generada es: " + contraseña)