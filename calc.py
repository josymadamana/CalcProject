def add(a,b):
	return a+b
def sub(a,b):
	return a-b
	#check 3
def mul(a,b):
	return a*b
def div(a,b):
	try:
		return a/b
	except:
		print "Exception Caught"
		#print("Added new- check")		
		#check 1
		raise
if __name__=="__main__":
	print(add(6,2))
	print(sub(6,2))
	print(mul(6,2))
	#check 2
	print(div(6,2))
	#print(div(6,1))
	#print("Done")		
	#print("Done")		
	#print("Done")		
	#print("Done")		
	#original	
	#print("Added new- check")		
