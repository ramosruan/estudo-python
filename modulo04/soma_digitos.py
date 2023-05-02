soma = 0

x = int(input('Digite um número inteiro: '))

while x != 0:
    resto = x%10
    soma = soma + resto
    x = x // 10

print(soma)