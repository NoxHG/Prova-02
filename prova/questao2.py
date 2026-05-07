import random
n = int(input('Digite uma quantia de números: '))

for i in range(1, n+1):
    numa = int(random.randint(1, 100))
    print(f'{i}º número alatório: {numa}')