# Задача 1________________________________________________________
import random

numbers = [random.randint(1,10) for _ in range(6)]
print(numbers)
result = list(filter(lambda element: element>5,numbers))
print(result)
