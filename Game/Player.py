print('Imported Player')
import os
from Game.Pokemon import New_Pokemon

class Player(object):
	def __init__(self, ID, force=False):
		self._Player_Pokemon = open('Owned_Pokemon_txt', 'w+')
		self._id = str(ID)
		self._position = (0, 0)
		self.maxHealth = 100
		self.health = self.maxHealth
		self.level = 0
		self.experience = 0
		self.pokemon = []
		self.userfile = 'UserData/' + self._id + '.user'
		if os.path.isfile(self.userfile) and force == False:
			self.loadData (self.userfile)
		else:
			newPlayer = open(self.userfile, 'w')
			newPlayer.write("[" + self._id + "]\npos=0,0\nhealth=100\nmaxHealth=100\nlevel=0\nexperience=0\npokemon=0")
	def loadData (self, file):
		with open(file, 'r') as f:
			for line in f:
				if line[0] == '[':
					self._id = line[1:len(line)-2]
					continue

				editLine = line.split('=')
				if editLine[0] == "pos":
					temp = editLine[1].split(',')
					self._position = (int(temp[0]), int(temp[1]))
				elif editLine[0] == "health":
					self.health = int(editLine[1])
				elif editLine[0] == "maxHealth":
					self.maxHealth = int(editLine[1]) 
				elif editLine[0] == "level":
					self.level = int(editLine[1])
				elif editLine[0] == "experience":
					self.experience = int(editLine[1]) 
				elif editLine[0] == "pokemon":
					self.pokemon = [] # Set this as a index
	def get_health(self):
		return self.health
	def get_hurt(self):
		self.health = self.health - 5
	def MoveLeft (self):
		self._position = (self._position[0] - 1, self._position[1])
	def MoveRight (self):
		self._position = (self._position[0] + 1, self._position[1])
	def MoveUp (self):
		self._position = (self._position[0], self._position[1] + 1)
	def MoveDown (self):
		self._position = (self._position[0], self._position[1] - 1)
	def GetPosition (self):
		return self._position
	def get_pokemon(self):
		current_pokemon = []
		for pokemon in self.pokemon:
    			current_pokemon.append(pokemon.get_name())
		return current_pokemon
	def add_pokemon(self, name, pokefile):
		complete = False
		for line in pokefile:
			line = line.strip().split(',')
			if(line[0] == ''):
				pass
			elif(line[0] == name):
				self.pokemon.append(New_Pokemon(name))
				complete = True
		return complete