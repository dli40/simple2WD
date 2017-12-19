import explorerhat

#test code
	

	
for i in range(0,9999):
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.forwards()
print("done with forwards")
explorerhat.motor.stop()

