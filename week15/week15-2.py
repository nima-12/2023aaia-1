ans = 0
while True:
	a = int(input('Enter an integer ( 999 to end ): \n'))
	if a == 999:
		break
	ans += a
	
print('The total is:',ans,end='')


a = list(map(int,input().split()))

print(max(a) - min(a),end ='')