def exampleChild2Function(qTo,qFrom,qFromOther):
	done = False
	while not done:
		if not qFromOther.empty():
			message = qFromOther.get()
			print 'Message "'+message+'" received by child2'
			if message=='hello':
				qFrom.put('goodbye')
				import time
				time.sleep(5)
				done = True

exampleChild2Function(qTo,qFrom,**initDict)