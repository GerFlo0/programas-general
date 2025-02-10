def inver_str(in_str = str):
    out_str = ""
    for i in range(len(in_str)-1,-1,-1):
        out_str += in_str[i]
    return out_str

txt = "hola caracola"
print(txt)
print(inver_str(txt))

print(input("ingrese el texto a invertir: ")[::-1])