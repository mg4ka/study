a = int(input())

print(('+' + ('-' * a)) * (a + 1) + '+')
print('|' + ' ' * a + '|', end='')
for z in range(1, a + 1):
    print(' ' * (a - 1) + str(z) + '|', end='')
print('\n' + ('+' + ('-' * a)) * (a + 1) + '+')
for i in range(1, a + 1):
    print('|' + str(i).rjust(a) + '|', end='')
    for z in range(1, a + 1):
        print(str(z * i).rjust(a) + '|', end='')
    print('\n' + ('+' + ('-' * a)) * (a + 1) + '+')