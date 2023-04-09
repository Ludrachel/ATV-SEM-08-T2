def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    if n % 3 == 0:
        return "FIZZ"
    if n % 5 == 0:
        return "BUZZ"
    return n
num = int(input('digite qualquer número : '))
print(fizzbuzz(num))
