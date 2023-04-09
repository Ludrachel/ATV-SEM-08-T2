def peso_ideal(altura,sexo):
    if sexo == 1:
        return f'{((72.7 * altura)- 58):.2f}'
    if sexo == 2:
        return f'{((62.1 * altura)- 44.7):.2f}'
h = float(input('digite sua altura : '))
s = int(input('digite 1 se seu sexo for masculino ou 2 se for feminino : '))
print(peso_ideal(h,s))
