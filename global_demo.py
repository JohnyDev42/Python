x = 10

def modify():
	global x
	x = x+1
	print "Inside function:", x

modify()
print "outside function:", x
print "hello"
print "from server"
