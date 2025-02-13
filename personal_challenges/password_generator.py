#input
#1. length of password
#2. include uppercase
#3. include special characters
#4. include numbers

#output
#1. password

import random
import string

def password_generator(length, include_uppercase, include_special_characters, include_numbers):
    password = ''
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_special_characters:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input('Enter the length of the password: '))
include_uppercase = input('Include uppercase? (y/n): ') == 'y'
include_special_characters = input('Include special characters? (y/n): ') == 'y'
include_numbers = input('Include numbers? (y/n): ') == 'y'

print(password_generator(length, include_uppercase, include_special_characters, include_numbers))
