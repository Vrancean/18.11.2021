a=str(input('dati numele:'))
if ord(a[0]) in range(65,91):
    for i in a[1:]:
        if ord(i)>96 and ord(i)<123:
            n=True
        else:
            n=False
else:
    n=False
if n==True:
    print('corect')
else:
    print('incorect')