print('Enter name : ')
name = input()
print('Hello ' + name)

print('Enter number : ')
x = int(input())


if x>=5 and x<10:
    print(x*x)
elif x>=10:
    print(x*10)             # all statements that starts with 'tab' will be considered as part of elif
    print('hello')
print('ok')                 # since this statement don't use tab character, it means it is not part of 'elif'



i=1
sum = 0
while i<=x:
    sum = sum + i
    i=i+1

    if i>5:
        break

print('The sum = ' + str(sum));


sum = 0
for i in range(1,11):       #  for(i=1;i<=10;i++)    or   for(i=1;i<11;i++)
    sum = sum + i

print('The sum = ' + str(sum))


sum = 0
for i in [1,2,3,4,5]:
    sum = sum + i

print('The sum = ' + str(sum))


for letter in name:         # automatically reads character by character
    print(letter)


numbers = [10,11,12,13,14]

for i in range(0,len(numbers)):             # 0 to n-1
    if numbers[i]%2==0:
        print(numbers[i])

