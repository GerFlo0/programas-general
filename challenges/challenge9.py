def dec_to_bin(dec_num = int):
    bin_num = []
    while dec_num>0:
        if dec_num%2 == 0: bin_num.append(0)
        else: bin_num.append(1)
        dec_num //= 2
    return bin_num[::-1]

dec_num = int(input("Ingrese el numero en decimal a convertir: "))
print(dec_to_bin(dec_num))