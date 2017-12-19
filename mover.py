import explorerhat

#test code
	
explorerhat.motor.two.invert() #because this motor is backwards
	
for i in range(0,9999):
	explorerhat.motor.forwards()
print("done with forwards")
explorerhat.motor.stop()

for i in range(0,9999):
	explorerhat.motor.backwards()

