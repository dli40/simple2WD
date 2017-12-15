import explorerhat

def left():
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.forwards()
	
def right():
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.backwards()
	
def test_reset():
	explorerhat.forward()
	explorerhat.left()
	explorerhat.right()
	explorerhat.backward()
	
		
def end():
	explorerhat.motor.stop()
	
#test code
	
explorerhat.test_reset()
explorerhat.end()
	
