def fibonacci():
    fibo = [0,1]
    for i in range(1,51):
        fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])
    return fibo

print(fibonacci())