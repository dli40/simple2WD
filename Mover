import explorerhat

def forward(self):
	self.motor.forwards()
	
def backward(self):
	self.motor.backwards()
	
def left(self):
	self.motor.one.backwards()
	self.motor.two.forwards()
	
def right(self):
	self.motor.one.forwards()
	self.motor.two.backwards()
	
def test_reset(self):
	self.forward()
	self.left()
	self.right()
	self.backward()
	
		
def end(self):
	self.motor.stop()
	
#test code
	
explorerhat.test_reset()
explorerhat.end()
	
