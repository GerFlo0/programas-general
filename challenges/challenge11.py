#functions
def is_balanced(ecuation = str, dir = dict):
    ecuation = [dir.get(char) for char in ecuation if char in dir.keys()]
    for val in list(dir.values())[:3]:
        index_list = [i for i in range(len(ecuation)) if ecuation[i] == val][::-1]
        for i in index_list:
            try:
                if ecuation[i+1] == -val: ecuation = ecuation[:i]+ecuation[i+2:]
                else: return False
            except: return False
    return True

#variables
dir = {"(":1,"[":2,"{":3,")":-1,"]":-2,"}":-3}
ecuation = str

#main code
ecuation = input("Ingrese la ecuacion a evaluar: ")
print(is_balanced(ecuation,dir))