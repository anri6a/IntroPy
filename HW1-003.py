n = 456754
a = n//1000
b = n%1000
if ((a%10) + ((a//10)%10) + (a//100)) == ((b%10) + ((b//10)%10) + (b//100)): print('yes')
else: print('no')
