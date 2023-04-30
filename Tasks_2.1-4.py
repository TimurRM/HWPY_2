# Задача 1. Напишите программу, которая принимает на вход число N и 
# выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    result = []
    fact = 1
    for i in range(1, n+1):
        fact *= i
        result.append(fact)
    return result

n = int(input("Введите число N: "))
print(factorial(n))


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.


print("X\tY\tZ\t¬(X ∧ Y)\t(¬(X ∧ Y)) ∨ Z")


for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            result = not(x and y) or z
            print(f"{x}\t{y}\t{z}\t{not(x and y)}\t\t{result}")



# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой 
# строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def chars_calc(s1, s2):

    counts = {}
    for i in s1:
        count = 0
        for j in s2:
            if i == j:
                count += 1
        counts[i] = count

    return counts


s1 = "one"
s2 = "onetwonine"
counts = chars_calc(s1, s2)
for char, count in counts.items():
    print(f"{char} - {count}")

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

# 1
def shift_list(N, k):
    lst = list(range(-N, N+1))
    new_lst = lst[-k:] + lst[:-k]
    return new_lst

print(shift_list(7, 2)) 

# 2
import random

N = 7
lst = [random.randint(-N, N) for i in range(N)]
new_lst = lst[-2:] + lst[:-2]

print(lst)
print(new_lst)

