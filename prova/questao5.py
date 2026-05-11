
repeticoes = int(input('Digite a quantia de repetições: '))

numeros = []
soma = 0
for i in range(repeticoes):
    numero = int(input('Digite um valor: '))
    soma += numero # soma = soma + numero
    # -= *= '/='
    numeros.append(numero)

media = soma / repeticoes

print(f'soma total: {soma}', f'média: {media}', f'maior valor: {max(numeros)}', f'menor valor: {min(numeros)}', f'quantia de valores acima da media: {sum(1 for numero in numeros if numero > media)}', sep='\n')