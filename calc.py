def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	try:
		return a/b
	except:
		print "Exception Caught"
		raise
if __name__=="__main__":
	print(add(6,2))
	print(sub(6,2))
	print(mul(6,2))
	print(div(6,0))
	#print("Done")		
	
