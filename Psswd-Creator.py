import random
import string

print (""" 
                           _                       _             
 _ __  ___ _____      ____| |   ___ _ __ ___  __ _| |_ ___  _ __ 
| '_ \/ __/ __\ \ /\ / / _` |  / __| '__/ _ \/ _` | __/ _ \| '__|
| |_) \__ \__ \\ V  V / (_| | | (__| | |  __/ (_| | || (_) | |   
| .__/|___/___/ \_/\_/ \__,_|  \___|_|  \___|\__,_|\__\___/|_|   
|_|                                                              
        [*] BY          Black Wolf
        [*] ORG         ELITE 6-27
        [*] GITHUB      github.com/JMR3Y
        [*] VERSION     V.1.0
""")
characters = string.ascii_letters + string.punctuation  + string.digits
number = input('>>>[+]Numero de contraseñas que quieres crear: ')
number = int(number)
length = input('>>>[+]Longitud de la contraseña 8/24: ')
length = int(length)

if length <7 or length >25:
    print("La longitud debe estar entre 8 y 24!")
else:
    for password in range(number):
        pw = ''
        for char in range(length):
            pw += random.choice(characters)
        print ("[*]Password: ")
