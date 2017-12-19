import explorerhat

#test code
	

	
for i in range(0,9999):
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.backwards()
print("done with forwards")
explorerhat.motor.stop()

