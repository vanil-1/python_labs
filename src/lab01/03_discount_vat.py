price, discount, vat = map(float, input().split())


def f(x):
    if str(x)[-2] == ".":
        return str(x) + "0"
    else:
        return round(x, 2)


base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(
    f"База после скидки: {f(base)} ₽\n\
НДС:{' ' * 15}{f(vat_amount)} ₽\nИтого к оплате:{' ' * 4}{f(total)} ₽"
)
