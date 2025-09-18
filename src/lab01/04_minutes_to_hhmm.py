m = int(input('Минуты: '))
def f(x):
    if x // 10 == 0: return f'0{x}'
    else: return x
print(f'{f(m // 60)}:{f(m % 60)}')