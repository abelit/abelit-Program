def conflict(state,nextX):
	nextY=len(state)
	for i in range(nextY):
		if abs(state[i]-nextX) in (0,nextY-i):
			return True
	return False

#def queens(num,state):
#	if len(state)==num-1:
#		for pos in range(num):
#			if not conflict(state,pos):
#				yield pos

def queens(num=8,state=()):
	for pos in range(num):
		if not conflict(state,pos):
			if len(state)==num-1:
				yield(pos,)
			else:
				for result in queens(num,state+(pos,)):
					yield (pos,)+result

number=int(input("Please input the number of queens:"))
lst=list(queens(number))
total=len(lst)
print(lst)
print('There has %s methods to solve %s queens problem!' % (total,number))
