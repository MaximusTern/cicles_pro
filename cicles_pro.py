#pro6
number = 254314
n = 0
while (number > 0):
    a = number % 10
    n = n + a
    number = number // 10
print(n)

#pro7
number = 254314
n = 1
while (number > 0):
    a = number % 10
    n = n * a
    number = number // 10
print(n)

#pro8

numb = input("введи число: ")
for char in numb:
    if char == '5':
        print('Цифра 5 есть в числе')
        break
    else:
        print('Цифры 5 нет в числе')

#pro9
num = 1238
m = 0
for i in str(num):
    if int(i) > m:
        m = int(i)
print(m)

#pro10
num = 546546
num = str(num)
k = 0
for i in num:
    if i == '5':
        k += 1
print(k)