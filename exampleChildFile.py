def exampleChildFunction(qTo,qFrom,a):
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
			print 'Message "'+message+'" received by child1'
			if message=='hi':
				qFrom.put('hello')
				import time
				time.sleep(5)
				done = True

exampleChildFunction(qTo,qFrom,**initDict)