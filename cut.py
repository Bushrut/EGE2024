# Администрация одной из школ города N решила подготовить сюрприз для педагогов к празднованию Дня учителя и купить всем билеты на концерт. Приобретённые в августе билеты распределили между учителями школы. В начале нового учебного года в школу были приняты два молодых специалиста.
# Администрация столкнулась с проблемой: необходимо найти два соседних свободных места так, чтобы с двух сторон от них в том же ряду уже были распределённые места.
# Помогите администрации школы найти наибольший номер ряда, в котором есть такие места, и наименьший номер места из найденных в этом ряду подходящих пар.
#
# Входные данные представлены в файле Задание 10. content.docx
#
#     В первой строке находится количество (k) занятых мест;
#     В остальных строках находятся по два числа: номер-ряд и номер места купленного билета.
#
# Выходные данные: сумма наибольшего номера ряда и наименьшего номера места в этом ряду.
#
# Пример входного файла:
#
# 10
# 3 6
# 3 10
# 3 7
# 12 8
# 12 2
# 12 5
# 14 23
# 14 28
# 14 35
# 14 45
#
# В приведённом примере условию задачи удовлетворяют следующие места:
#
#     в 3 ряду места 8 и 9;
#     в 12 ряду места 3 и 4;
#     в 12 ряду места 6 и 7.
#
# Значит, наибольший номер ряда, удовлетворяющий требованию: 12. А наименьший номер свободного места в этом ряду: 3. В ответе нужно указать: 12 + 3 = 15.
#
# Ответ запишите числом — суммой найденных значений, без дополнительных пробелов и символов до и после (например: 181011).
n = int(input())
data = [input() for i in range(n)]
dt = []
for line in data:
    r, m = map(int, line.split())
    dt[r-1] = [m]
print(dt)