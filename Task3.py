# Задача 3________________________________________________________

import random

def numbers_list(LEN_LIST):
    numbers = [random.randint(1,10) for _ in range(LEN_LIST)]
    return numbers

def unique_list(n):
    unique = n[0:0]
    for i in range(len(n)):
        if n[i] in unique: 
            continue
        unique.append(n[i])
    return unique

LEN_LIST = 6

print(numbers_list(LEN_LIST))
res =(LEN_LIST - len(set(unique_list(numbers_list(LEN_LIST)))))*2
print(f"{res} элемента/ов совпадают.\n"+
f"Список уникальных элементов: {unique_list(numbers_list(LEN_LIST))}")
