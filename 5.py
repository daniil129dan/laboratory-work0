print("Введите коичество бутылок объемом 1 литром или меньше:")
a=input()
print("Введите коичество бутылок объемом больше литра:")
b=input()
print("Общая сумма выручки: $", "%.2f"%(float(a)*0.10+float(b)*0.25),sep="")