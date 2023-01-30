from random import sample

start = int(input("What's the minimal number: "))
end = int(input("What's the maximum number: ")) + 1
numbers = range(start, end)

# + Plus (Addition)
# - Minus (Subtraction)
# ÷ Obelus (Division)
# x Times (Multiplication)
operators = ('+', '-', '÷', 'x')

for number in range(0, 5):
    choose = sample(numbers, 2)

    print(f'{choose[0]:>4}')
    print(f'{operators[0]:<1} {choose[1]:>2}')
    print('-' * 4)
