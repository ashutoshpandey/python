__author__ = 'Ashutosh'

x = 0
while (x<=10):
    print('Square of ' + str(x) + ' is ' + str(x*x))
    x = x+1

print('**********************')

for i in range(1,10):
    print(i, ' ', end='')

print('**********************')

#upper part
max = 10
for i in range(1,max):          # 1 to 9

    for j in range(1,10 + max-i):
        print(' ', end='')

    for k in range(1,i+1):
        print(k, '', end='')

    print('')

#lower part
for i in range(1,max):

    for j in range(1,10 + i+1):
        print(' ', end='')

    for k in range(1,max-i):
        print(k, '', end='')

    print('')
