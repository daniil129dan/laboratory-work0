print("Введите сумму заказа:")
a=float(input())
n=a*0.6+a
print("Налог:", round(n,2))
c=a*1.8+a
print("Чаевые:",round(c,2))
print("Итог:",round(c+n,2))

