n = int(input("введите трехзначное число\n"))
res = (n%10) + ((n//10)%10) + (n//100) 
print(res)