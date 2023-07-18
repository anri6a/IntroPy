from random import randint

N = int(input("Введите количество арбузов: "))
w = []

for i in range(N):
    weigth = randint(1000, 3000)
    w.append(weigth)

print(f"Веса всех арбузов - {w}")
print(f"Самый легкий арбуз весит {min(w)}")
print(f"Самый тяжелый арбуз весит {max(w)}")