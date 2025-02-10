def is_cousin(in_num = int):
    cousins = [2]
    for num in range(cousins[-1]+1,in_num+1):
        for cou in cousins:
            if num%cou == 0: break
            if cou == cousins[-1]: cousins.append(num) 
    #print (cousins)
    return in_num in cousins

print(is_cousin(1000))