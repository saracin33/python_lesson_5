
i = 2
j = 0
for n in range(1,1001):
    while (n>=i*i) and (j!=1):
        if n%i == 0:
            j = 1
            i += 1
        else: i += 1
    else:
        if j == 1:
            print(n, 'Составное число')
        else:
            print(n, 'Простое число')





