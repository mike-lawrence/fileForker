if __name__ == '__main__':
	import fileForker
	tempChild = fileForker.childClass(childFile='exampleChildFile')
	tempChild.initDict['a'] = 1
	tempChild.start()
	while tempChild.isAlive():
	  pass
