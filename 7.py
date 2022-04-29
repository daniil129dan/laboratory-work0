print("Введите число: ")
n=int(input())#Ввод числа 
sum=0
for i in range(n): #цикл for
    sum=(n*(n+1)/2)#подсчет суммы
print(round(sum))