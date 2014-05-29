class User(object):
	def __init__(self, name):
		self.name = name
	def greet(self):
		print "my name is %s!" % self.name

class SuperUser(User):
	def shout(self):
		print "%s is SUPER!!" % self.name

bob = User("Bob")
tom = SuperUser("Tom")
print bob.name
bob.greet()
tom.greet()
tom.shout()
