from random import sample
from generate import create_a4_paper

start = int(input("What's the minimal number: "))
end = int(input("What's the maximum number: ")) + 1
numbers = range(start, end)

# + Plus (Addition)
# - Minus (Subtraction)
# ÷ Obelus (Division)
# x Times (Multiplication)
operators = ('+', '-', '÷', 'x')
operations = []

for number in range(0, 16):
    choose = sample(numbers, 2)
    operation = []

    operation.append(f'{choose[0]:>4}')
    operation.append(f'{operators[0]:<1} {choose[1]:>2}')
    operation.append('-' * 6)

    operations.append(operation)

    # print(f'{choose[0]:>4}')
    # print(f'{operators[0]:<1} {choose[1]:>2}')
    # print('-' * 4)

create_a4_paper('operations.pdf', operations)
# create_a4_paper2('operations.pdf')
