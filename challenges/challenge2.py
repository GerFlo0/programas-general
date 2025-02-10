def is_anagram(str1 = str, str2 = str):
    if(str1 == str2): return False
    return sorted(str1) == sorted(str2)

str1 = input("Ingrese la primer cadena de texto: ").lower()
str2 = input("Ingrese la segunda cadena de texto: ").lower()
print(is_anagram(str1,str2))