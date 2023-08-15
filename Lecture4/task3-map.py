# C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

data = '1 4 65 643 3'
print(data)
#data = data.split()
print(data)
data = list(map(int, data.split()))
print(data)