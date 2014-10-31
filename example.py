if __name__ == '__main__':
	import fileForker
	tempChild = fileForker.childClass(childFile='exampleChildFile.py')
	tempChild.initDict['a'] = 1
	tempChild.start()
	tempChild.qTo.put('hi')
	tempChild2 = fileForker.childClass(childFile='exampleChildFile2.py')
	tempChild2.initDict['qFromOther'] = tempChild.qFrom
	tempChild2.start()
	tempChild.qTo.put('hi')
	done = False
	while not done:
		if not tempChild2.qFrom.empty():
			message = tempChild2.qFrom.get()
			print 'Message "'+message+'" received by parent'
			if message=='goodbye':
				done = True
	while tempChild2.isAlive():
	  pass
