def fizzbuzz(max = int):
    for i in range(1,max+1):
        is_mult_3 = i%3 == 0
        is_mult_5 = i%5 == 0
        if(is_mult_3 and is_mult_5):
            print(f"fizzbuzz: {i}")
        elif(is_mult_3):
            print(f"fizz: {i}")
        elif(is_mult_5):
            print(f"buzz: {i}")
        else:
            print(i)

fizzbuzz(100)