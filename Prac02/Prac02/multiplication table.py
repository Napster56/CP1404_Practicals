def table(a):
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            print(str(i * j), end='\t')
        if i * j % a == 0 and i * j != a * a:
            print('\n')


a = int(input("Enter a number 0-15: "))
if a >= 0 and a <= 15:
    table(a)
else:
    pass