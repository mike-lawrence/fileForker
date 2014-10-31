if __name__ == '__main__':
	import fileForker
	tempChild = fileForker.childClass(childFile='exampleChildFile.py')
	tempChild.initDict['a'] = 1
	tempChild.start()
	tempChild.qTo.put('hi')
	done = False
	while not done:
		if not tempChild.qFrom.empty():
			message = tempChild.qFrom.get()
			print message
			if message=='hello':
				done = True
	while tempChild.isAlive():
	  pass
