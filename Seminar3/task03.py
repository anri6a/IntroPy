# Напишите программу для печати всех уникальных значений в словаре.                                          }

data = {'1': 'S001',
        '2': 'S002',
        '3': 'S001',
        '4': 'S005',
        '5': 'S005',
        '6': 'S009',
        '7': 'S007'}
#print(set(val for k, val in data.items()))
workDict = set(data.values())
print(workDict)
workDict = set(data.keys())
print(workDict)


