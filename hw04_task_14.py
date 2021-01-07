'''Составить список чисел Фибоначчи содержащий 15
элементов.
(подсказка: числа Фибоначчи - последовательность, в
которой первые два числа равны либо 1 и 1, а каждое
последующее число равно сумме двух предыдущих
чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )'''

fib1 = 1
fib2 = 1

list_fib = [1, 1]

element = int(input("Номер элемента ряда Фибоначчи: "))

for n in range(element-2):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    list_fib.append(fib2)

print(list_fib)
