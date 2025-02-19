import os, random, string

os.system('cls')

def generate_random_text(length = int):
    def mix_string(string):
        lista = list(string)
        random.shuffle(lista)
        return ''.join(lista)
    
    text = ''
    characters = string.ascii_lowercase
    characters += string.ascii_uppercase
    characters += string.punctuation
    characters += string.digits
    
    for i in range(length):
        text += random.choice(characters)
    
    return text

print(f"\n{generate_random_text(int(input('Ingrese la longitud del texto: ')))}")