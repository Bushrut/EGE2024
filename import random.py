import random

answer_right = 0
answer_wrong = 0
for i in range(3):
    x = int(random.random() * 10)
    y = int(random.random() * 10)
    answer = input(f"What is {x} * {y}: ")
    if int(answer) == x * y:
        answer_right += 1
        print("Правильно")
    else:
        answer_wrong += 1
        print("Неправилльно!", "\nОтвет: x * y = ", x * y)
print(f'Правильных ответов: {answer_right}, ошибочных ответов: {answer_wrong}')