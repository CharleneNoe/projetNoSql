import string

class AllDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self,database):
		self.db = database
		self.tree = database.tree
		self.water = database.water
		self.complaint = database.complaint
		self.collision = database.collision
		self.culture = database.culture
		self.park = database.park
		self.restaurant = database.restaurant

#This function will handle the insertion of names
	def insert(self,collection,data):
		if(collection=="tree"):
			self.tree.insert(data)
		if(collection=="water"):
			self.water.insert(data)
		if(collection=="complaint"):
			self.complaint.insert(data)
		if(collection=="culture"):
			self.culture.insert(data)
		if(collection=="collision"):
			self.collision.insert(data)
		if(collection=="park"):
			self.park.insert(data)
		if(collection=="restaurant"):
			self.restaurant.insert(data)
                
