
# 1. horse weight is 100 and half horse

depth=55
i=0

def losh(ves):
	global depth,i
	i+=1

	if i<depth:
		res = ves+losh(ves)/2.0
	else:
		res = 0
	

	
	
	return res
	

res = losh(100)
print(res)
