##################################1
from string import punctuation
from string import octdigits
import re
a = input("Введите предложение чтобы определить  сколько раз цифры встречаются в тексте;"
          "\nзнаки препинания и  восклицательных знаков в тексте: ")

print("Каждое предложение заглавными буквами:")
print(''.join(map(str.capitalize, re.split(r'([.!?]\s+)', (a)))))

print("Количество восклицательных знаков:")
print(a.count("!"))

print("Общее количество восклицательных знаков и знаков препинания:")
print(sum(b in punctuation for b in a))

print("Количество цифр:")
print(sum(c in octdigits for c in a))


####################################2

# b = int(input('введите одно число: '))
# num = input("Введите несколько цифр через пробел: ")
# print(num)
# nums = list(num.split())
# print(nums)
# a = []
# for i in nums:
#     a.append(int(i))
# print(a)
# print(a.count(b))
################################3
# b = 0
# a = input("Введите несколько цифр чтобы узнать сумму и среднее арифметическое")
#
# for i in a:
#     b += int(i)
# print(f"Сумма:{b}")
# print(f"Среднее арифметическое от: {b / len(a)}")

