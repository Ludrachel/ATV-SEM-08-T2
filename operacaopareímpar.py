def valor(x):
    if x % 2 == 0:
        return x + 5
    else:
        return x + 8
num = int(input('digite qualquer número : '))
print(valor(num))
