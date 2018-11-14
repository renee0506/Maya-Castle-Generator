import maya.cmds as cmds
from functools import partial
import random

class Cluster(object):

	def __init__(self, cluster = List()):
		self.cluster = cluster

	def __repr__(self):
		return "Cluster of Architecture: " + self.cluster

	def createCluster(self):
		
class Shape(object):

	def __init__(self, shape):
		self.shape = shape

	def __repr__(self):
		return self.shape

	def duplicate(self):
		duplicate = cmds.duplicate(self.shape)
		return Shape(duplicate)

	def randomize(self):
		rand1 = random.uniform(0.1, 5)
		rand2 = random.uniform(0.1, 5)
		cmds.move(rand1, 0, rand2, self, relative=True)

class Tower(Shape):

	def __init__(self, shape):
		super().__init__(shape)

	def __repr__(self):
		return "Tower:" + self.shape

	def duplicate(self):
		result = super().duplicate(self)
		return Tower(result)

	def randomize(self):
		rand1 = 
class Applicaton(object):

	def __init__(self, shape1 = None, shape2 = None, shape3 = None):
		self.shape1 = shape1
		self.shape2 = shape2
		self.shape3 = shape3
		self.win()

	def __repr__(self):
		return "Application: {shape1: %s, shape2: %s, shape3: %s}" %(self.shape1, self.shape2, self.shape3)

	def win(self):
	    myWinName = "winInstance"
	    
	    
	    if cmds.window(myWinName, exists = True):
	        cmds.deleteUI(myWinName)
	        
	    window = cmds.window(myWinName, title = "Castle Generation")
	    cmds.scrollLayout(horizontalScrollBarThickness = 16, verticalScrollBarThickness = 16)
	    cmds.text("Select Shape1:")
	    cmds.button(label = "Select", command = lambda x: self.SelectShape("shape1", cmds.ls(selection = True)))
	    cmds.text("Select Shape2:")
	    cmds.button(label = "Select", command = lambda x: self.SelectShape("shape2", cmds.ls(selection = True)))

	    cmds.text("Select Shape3:")
	    cmds.button(label = "Select", command = lambda x: self.SelectShape("shape3", cmds.ls(selection = True)))
	    
	    cmds.button(label = "Generate", command = self.Generate)
	    cmds.showWindow()

	def SelectShape(self, shape, objects):
		if len(objects) == 0:
			print "Select at least one valid object!"
		if shape == "shape1":
			self.shape1 = objects
		elif shape == "shape2":
			self.shape2 = objects
		elif shape == "shape3":
			self.shape3 = objects

	def Generate(self, *args):
		for i in range(0, 5):
			print(self.shape1)
			duplicate = cmds.duplicate(self.shape1)[0]
			rand1 = random.uniform(0.1, 5)
			rand2 = random.uniform(0.1, 5)
			cmds.move(rand1, 0, rand2, duplicate, relative=True)
		for i in range(0, 5):
			duplicate = cmds.duplicate(self.shape2)[0]
			rand1 = random.uniform(0.1, 5)
			rand2 = random.uniform(0.1, 5)
			cmds.move(rand1, 0, rand2, duplicate, relative=True)
		for i in range(0,5):
			print self.shape3
			duplicate = cmds.duplicate(self.shape3)[0]
			rand1 = random.uniform(0.1, 5)
			rand2 = random.uniform(0.1, 5)
			cmds.move(rand1, 0, rand2, duplicate, relative=True)

if __name__ == "__main__":
	app = Applicaton()




