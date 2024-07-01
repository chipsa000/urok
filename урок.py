import random

number = random.randint(1, 50)
attempts = 0

print('Угадайте число от 1 до 50. У вас 5 попыток!')

while attempts < 100:
    guess = int(input('Введите число: '))
    if guess < number:
        print('Загаданное число больше!')
    elif guess > number:
        print('Загаданное число меньше!')
    else:
        print('Поздравляю! Вы угадали число', number, 'за', attempts, 'попыток!')
    attempts += 1 

print('Вы исчерпали все попытки!')