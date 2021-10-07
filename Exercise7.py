from random import randint

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end = ", " )
print()

print('Enter the temperature in C you would like to convert to F')
temp = int(input())
print(temp * (9/5) + 32)

rand = randint(1, 9)
guess = -1
while guess != rand:
    print('Enter a guess from 1 to 9')
    guess = int(input())
    if guess == rand:
        print('Well guessed!')

rep = 1
for i in range(10):
    for j in range(abs(abs(i -5) -5)):
        print('*', end='')
    print()

print('give a word to be reversed')
word = input()
for c in range(len(word)):
    print(word[len(word) - (c+1)], end='')
print()

print('enter a comma separated series of numbers')
ls = input()
ls = ls.split(',')
even = 0
odd = 0
for n in ls:
    n = int(n.strip())
    if n % 2 == 0:
        even += 1
    else:
        odd+= 1
print('number of even numbers: ' + str(even))
print('number of odd numbers: ' + str(odd))

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
print('types from sample list')
for item in datalist:
    print(type(item))

for n in range(7):
    if n % 3 == 0:
        continue
    print(n)
