def soma(n):
    if 0 <= n < 100000:
        soma = 0
        while n > 0:
            digito = n % 10
            soma += digito
            n //= 10
        return soma
    else:
        return "-1"
num = int(input('digite um número entre 0 e 100000 : '))
print(soma(num))
