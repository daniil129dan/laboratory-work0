print("Введите сумму первоначального депозита: ")
a=int(input())
i=1
b=range(1, 5)
for i in b:
    a=a*0.4+a
    print("сумма вклада в",i ,"год: ",round(a,2))