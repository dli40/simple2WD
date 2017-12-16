import explorerhat

#test code
	
explorerhat.motor.one.forwards()
explorerhat.motor.two.forwards()
print("finished going forwards")
#reverse
explorerhat.motor.one.backwards()
explorerhat.motor.two.backwards()
print("finished going backwards")	
#right
explorerhat.motor.one.forwards()
explorerhat.motor.two.backwards()
print("finished going left")	
#left
explorerhat.motor.one.backwards()
explorerhat.motor.two.forwards()
print("finished going right")	
	
