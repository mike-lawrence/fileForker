# Useful to have the following at the top of all your child files in case you want to uncomment and run directly
'''
class dummyQTo:
	def empty(self):
		return True

class dummyQFrom:
	def put(self,message):
		print message

qTo = dummyQTo()
qFrom = dummyQFrom()
'''

#Also useful to put any variables expected to be supplied to initDict here, again in case you want to uncomment and run directly, but also to help you remember what the script is expecting
'''
a = 1
'''
def exampleChildFunction(qTo,qFrom):
	print qTo #make sure 'qTo' is visible
	print a #make sure 'a' is visible 
	import math
	def g():
		print qTo #make sure 'qTo' is visible inside a function
		print a #make sure 'a' is visible inside a function
		print math.sqrt(4) #make sure 'math' is visible inside a function
	g()

	done = False
	while not done:
		if not qTo.empty():
			message = qTo.get()
			print message
			if message=='hi':
				qFrom.put('hello')
				import time
				time.sleep(5)
				done = True

exampleChildFunction(qTo,qFrom)