#input
#1. length of password
#2. include uppercase
#3. include special characters
#4. include numbers

#output
#1. password

import os
import random
import string

os.system('cls')

def password_generator(length, include_uppercase, include_special_characters, include_numbers):
    def mezclar_cadena(cadena):
        lista = list(cadena)
        random.shuffle(lista)
        return ''.join(lista)
    
    password = ''
    characters = mezclar_cadena(string.ascii_lowercase)
    if include_uppercase:
        characters += string.ascii_uppercase
        characters = mezclar_cadena(characters)
    if include_special_characters:
        characters += string.punctuation
        characters = mezclar_cadena(characters)
    if include_numbers:
        characters += string.digits
        characters = mezclar_cadena(characters)
    for i in range(length):
        password += random.choice(characters)
    print(characters)
    return password

length = int(input('Enter the length of the password: '))
include_uppercase = input('Include uppercase? (y/n): ') == 'y'
include_special_characters = input('Include special characters? (y/n): ') == 'y'
include_numbers = input('Include numbers? (y/n): ') == 'y'

print("\nYour new password is:")
print(password_generator(length, include_uppercase, include_special_characters, include_numbers)+'\n')
