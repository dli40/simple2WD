import explorerhat

#test code
	
for i in range(0,5): #forward
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.forwards()
print("finished going forwards")
for i in range(0,5): #reverse
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.backwards()
print("finished going backwards")	
for i in range(0,5): #right
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.backwards()
print("finished going left")	
for i in range(0,5): #left
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.forwards()
print("finished going right")	
	
