import explorerhat

#test code
	
for i in range(0,5): #forward
	explorerhat.motor.one.forwards()
	print("motor one going forwards")
	explorerhat.motor.two.forwards()
	print("motor two going forwards")    
print("finished going forwards")
for i in range(0,5): #reverse
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.backwards()
for i in range(0,5): #right
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.backwards()
for i in range(0,5): #left
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.forwards()	
	
