a = input('Введите 6-значный номер билета: ')
if len(a) != 6:
    print('Вы ввели не 6-ти значный номер билета')
else:
    b1 = 0
    b2 = 0
    for i in range(len(a)//2):
        b1 += int(a[i])
        b2 += int(a[len(a)//2 + i])
    if b1 == b2:
        print('Ваш билетик счастливый!')
    else:
        print('Повезет в следующий раз!')