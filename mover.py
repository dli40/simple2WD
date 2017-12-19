#property of Daniel Li: https://github.com/dli40
import explorerhat

#test code
	
explorerhat.motor.two.invert() #because this motor is backwards
	
for i in range(0,9999): #Will go forwards for 10,000 steps. It's about 5 seconds of motion. 
	explorerhat.motor.forwards()
print("done with forwards")
explorerhat.motor.stop()

for i in range(0,9999): #now go backwards
	explorerhat.motor.backwards()
		
explorerhat.motor.two.invert() #reset all changes before exiting	

