def media_final(n1,n2,n3,m):
    return (n1 + n2 * 2 + n3 * 3 + m)/ 7
def conceito(m):
    if m >= 9:
        return 'A\nAprovado'
    elif m >= 7.5 and m < 9:
        return 'B\nAprovado'
    elif m >= 6 and m < 7.5:
        return 'C\nAprovado'
    elif m >= 4 and m < 6:
        return 'D\nReprovado'
    elif m < 4:
        return 'E\nReprovado'
    
matricula = str(input('digite a sua matrícula : '))
nota1 = float(input('digite a primeira nota do aluno : '))
nota2 = float(input('digite a segunda nota do aluno : '))
nota3 = float(input('digite a terceira nota do aluno : '))
media = float(input('qual a media das notas ? : '))

mf = media_final(nota1,nota2,nota3,media)

print(matricula)
print(f'{mf:.2f}')
print(conceito(mf))
