from pygame.locals import *
import time,math,random,pygame,sys
import menu

pygame.init()

global veggieTotal, playerScore

veggieTotal = 36
playerScore = 0

# main menu

# startButton = button(command = gameloop)
# highscoreButton = button(command = displayhighscore)
# quitButton = button(command = quit)

# this creates the image for the cursor as ascii art:

thickarrow_strings = (               #sized 24x24
"       XXXXXXXXXX       ",
"     XX..........XX     ",
"    X..XXXX..XXXX..X    ",
"   X.XX   X..X   XX.X   ",
"  X.X     X..X     X.X  ",
" X.X      X..X      X.X ",
" X.X      X..X      X.X ",
"X.X       X..X       X.X",
"X.X       X..X       X.X",
"X.X       X..X       X.X",
"X.XXXXXXXXX..XXXXXXXXX.X",
"X......................X",
"X......................X",
"X.XXXXXXXXX..XXXXXXXXX.X",
"X.X       X..X       X.X",
"X.X       X..X       X.X",
"X.X       X..X       X.X",
" X.X      X..X      X.X ",
" X.X      X..X      X.X ",
"  X.X     X..X     X.X  ",
"   X.XX   X..X   XX.X   ",
"    X..XXXX..XXXX..X    ",
"     XX..........XX     ",
"       XXXXXXXXXX       ")

# compiles the cursor from ascii art:

mousecursor = pygame.cursors.compile(thickarrow_strings, black='X', white='.', xor='o')

# defines cursor size:

cursorsize = [24,24]

# objects/classes:

# Object to create grid from:

class cell:
	def __init__(self,type,xCoord,yCoord):

# Load in the images:

		self.carrot = pygame.image.load('carrot_final.png')
		self.cabbage = pygame.image.load('cabbage_final.png')
		self.crater = pygame.image.load('crater_final.png')
		
		self.bomb = pygame.image.load('bombfusefull_final.png')
		self.bomb2 = pygame.image.load('bombfusehalf_final.png')
		self.bomb3 = pygame.image.load('bombfuseshort.png')
		
		self.mole = pygame.image.load('mole.png')
		self.booming = pygame.image.load('boom.png')

# pass in the arguments:

		self.kind = type
		
		self.x = xCoord
		self.y = yCoord
		
# set the bomb timer variable:
		
		self.bombTicker = 0
		
# set the image bases on self.kind:
		
		if self.kind == 1:
			self.image = self.carrot
		elif self.kind == 2:
			self.image = self.cabbage
		elif self.kind == 3:
			self.image = self.bomb
		elif self.kind == 4:
			self.image = self.crater
		
# Set up the display for self:
		
		self.disp = self.image.get_rect(center = (self.x,self.y))

# define the bomb placing method		

	def placeBomb(self,mouseX,mouseY):
# 		print 'Bomb placed!'
# 		if playerTurn = True:
# 		self.mouseLoc = pygame.mouse.get_pos()
# 		self.mouseX = self.mouseLoc[0]
# 		self.mouseY = self.mouseLoc[1]
		
		global veggieTotal
		
# Pass in the arguments:
		
		self.mouseX = mouseX
		self.mouseY = mouseY

# 		print self.mouseX, self.mouseY
		
		if abs(self.x - self.mouseX) <= 40 and abs(self.y - self.mouseY) <= 40:

# 			print 'placeBomb if sequence activated!'
# 			print self.mouseX, self.mouseY

# 			print 'Bomb placed!'
	
			self.bombTicker = 0
			
			if self.kind == 1 or self.kind == 2:
				veggieTotal -= 1
			self.kind = 3
			self.image = self.bomb
			
# 			print 'Veggies:', veggieTotal
	
	def boom(self,count):
		
		self.bombTicker = count
		
		if self.bombTicker == 1:
			self.image = self.bomb2
		
		elif self.bombTicker == 2:
			self.image = self.bomb3
		
		elif self.bombTicker == 3:
# 			self.image = self.booming
# 			time.sleep(2)
			self.kind = 4
			if self.kind == 4:
# 				time.sleep(2)
				self.image = self.crater
			
	def eaten(self,count):
		self.moleTicker = count
		if self.moleTicker == 2:
			self.image = self.mole
# 			print 'Veggie eaten!'
			
			global veggieTotal
			
			veggieTotal -= 1
			
# 			print 'Veggies:', veggieTotal
			
			self.kind = 4
			if self.kind == 4:
# 				time.sleep(2)
				self.image = self.crater


# Basic Game Logic:

# def gameloop:
# 
# # Enter Game Loop:
# 	
# 	Game build == 1;
# 	Set Score = 0;
# 
# 	if user hits mole:
# 		Add score
# 	elif: 
# 		Loop
# 		Add score
# 		elim clicked spaces
# 	if all cell.types == 4 remain:
# 		Level lost
# 		save score
# 
# Level Lost:
# 		Get user name
# 			Save user name
# 		Print score
# 
# 		Prompt user:
# 			play again?
# 			if answer == yes:
# 				Enter game loop
# 			elif:
# 				Return main menu.

# End game loop

class mole:
	def __init__(self):
		self.squareCenters = [(120,120),(201,120),(282,120),(363,120),(444,120),(525,120),(120,201),(201,201),(282,201),(363,201),(444,201),(525,201),(120,282),(201,282),(282,282),(363,282),(444,282),(525,282),(120,363),(201,363),(282,363),(363,363),(444,363),(525,363),(120,444),(201,444),(282,444),(363,444),(444,444),(525,444),(120,525),(201,525),(282,525),(363,525),(444,525),(525,525)]
		self.position = random.choice(self.squareCenters)
		
		self.locationIndex = self.squareCenters.index(self.position)
		
		game.clickCount = 2
		
		self.x = self.position[0]
		self.y = self.position[1]
		
		print self.x,self.y
		print ''
		print self.locationIndex
		print ''
		
	def move(self,inputList):
# 		self.moveChoices = self.squareCenters[self.moveChoicesIndex]
		
		self.moveChoices = []
		
		self.cells = inputList
		
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex+1)])
		except IndexError:
# 			print 'This is out of range, no biggie'
			pass
			
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex-1)])
		except IndexError:
# 			print 'This is out of range, no biggie'
			pass
			
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex+6)])
		except IndexError:
# 			print 'This is out of range, no biggie'
			pass
			
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex-6)])
		except IndexError:
# 			print 'This is out of range, no biggie'
			pass
		
		for i in self.moveChoices:
			self.iIndex = self.squareCenters.index(i)
			if abs(self.iIndex-self.locationIndex) == 1 and abs(i[0]-self.position[0]) > 82:
				self.moveChoices.remove(i)
			elif abs(self.iIndex-self.locationIndex) > 7:
				self.moveChoices.remove(i)
	
		self.priority1List = []
	
		for i in self.moveChoices:

			for j in self.cells:
			
				jCoordinates = (j.x,j.y)
			
# 				jIndex = self.squareCenters.index(jCoordinates)

				if jCoordinates == i and (j.kind == 1 or j.kind == 2):
					self.priority1List.append(i)
					break
	
		self.priority2List = []
	
		for i in self.moveChoices:

			for j in self.cells:
			
				jCoordinates = [j.x,j.y]
			
# 				jIndex = self.squareCenters.index(jCoordinates)

				if jCoordinates[0] == i[0] and (j.kind == 1 or j.kind == 2):
					self.priority2List.append(i)
					break
				elif jCoordinates[1] == i[1] and (j.kind == 1 or j.kind ==2):
					self.priority2List.append(i)
					break

		self.moveChoicesIndex = []
		
		for j in self.moveChoices:
			k = self.squareCenters.index(j)
			self.moveChoicesIndex.append(k)
			
# 		print 'C' self.moveChoices
# 		print ''
		print 'Choices:',self.moveChoicesIndex
		print ''

		self.priority1MoveChoicesIndex = []
		
		for j in self.priority1List:
			k = self.squareCenters.index(j)
			self.priority1MoveChoicesIndex.append(k)
		
		print 'Priority 1 Choices:',self.priority1MoveChoicesIndex
		print ''
		
		self.priority2MoveChoicesIndex = []
		
		for j in self.priority2List:
			k = self.squareCenters.index(j)
			self.priority2MoveChoicesIndex.append(k)
		
		print 'Priority 2 Choices:',self.priority2MoveChoicesIndex
		print ''

		try:
			self.position = random.choice(self.priority1List)
		
			self.x = self.position[0]
			self.y = self.position[1]
		
		except:
			try:
				self.position = random.choice(self.priority2List)
		
				self.x = self.position[0]
				self.y = self.position[1]
			
			except:
				self.position = random.choice(self.moveChoices)
		
				self.x = self.position[0]
				self.y = self.position[1]
		
		self.locationIndex = self.squareCenters.index(self.position)
		
		print 'New coordinates:',self.x,self.y
		print 'New index:',self.locationIndex
		
		self.locationIndex = self.squareCenters.index(self.position)
			
class game:
	def __init__(self):
	
		global veggieTotal, playerScore
	
		self.size = 1200, 650
		self.screen = pygame.display.set_mode(self.size)
		self.cells = [cell(random.randint(1,2),120,120),cell(random.randint(1,2),201,120),cell(random.randint(1,2),282,120),cell(random.randint(1,2),363,120),cell(random.randint(1,2),444,120),cell(random.randint(1,2),525,120),cell(random.randint(1,2),120,201),cell(random.randint(1,2),201,201),cell(random.randint(1,2),282,201),cell(random.randint(1,2),363,201),cell(random.randint(1,2),444,201),cell(random.randint(1,2),525,201),cell(random.randint(1,2),120,282),cell(random.randint(1,2),201,282),cell(random.randint(1,2),282,282),cell(random.randint(1,2),363,282),cell(random.randint(1,2),444,282),cell(random.randint(1,2),525,282),cell(random.randint(1,2),120,363),cell(random.randint(1,2),201,363),cell(random.randint(1,2),282,363),cell(random.randint(1,2),363,363),cell(random.randint(1,2),444,363),cell(random.randint(1,2),525,363),cell(random.randint(1,2),120,444),cell(random.randint(1,2),201,444),cell(random.randint(1,2),282,444),cell(random.randint(1,2),363,444),cell(random.randint(1,2),444,444),cell(random.randint(1,2),525,444),cell(random.randint(1,2),120,525),cell(random.randint(1,2),201,525),cell(random.randint(1,2),282,525),cell(random.randint(1,2),363,525),cell(random.randint(1,2),444,525),cell(random.randint(1,2),525,525)]
		
		self.garden = pygame.image.load('garden.png')
		
		self.gardenDisp = self.garden.get_rect(center = (323,323))
		
		self.mole = mole()
		
		while 1:
			pygame.mouse.set_cursor(cursorsize,(12,12),*mousecursor)
			
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:
# 					print 'Mouse clicked!'
					self.mouseLoc = pygame.mouse.get_pos()
# 					print self.mouseLoc
					self.mX = self.mouseLoc[0]
					self.mY = self.mouseLoc[1]
# 					print self.mX,self.mY

					if self.clickCount < 2:
						self.clickCount += 1
					else:
						self.clickCount = 0
					

					for i in self.cells:
# 						if i.bombTicker 
# 						self.ticker = i.bombTicker
# 						self.ticker += 1
						i.bombTicker += 1
						cell.placeBomb(i,self.mX,self.mY)
						if i.kind == 3:
							cell.boom(i,i.bombTicker)
					
					mole.move(self.mole,self.cells)
						
				if event.type == pygame.QUIT:
					print 'Game over'
					print 'Score:', playerScore
					pygame.quit()
					sys.exit()
				
			for i in self.cells:
				self.screen.blit(i.image,i.disp)
# 				pygame.display.flip()
				
				if self.mole.x == i.x and self.mole.y == i.y:
					self.moleSquare = i.kind
					if i.kind == 3:
						print 'Mole killed!'
						playerScore += 20+(veggieTotal*5)
						cell.boom(i,3)
						del self.mole
						self.mole = mole()
					if i.kind == 1 or i.kind == 2:
						cell.eaten(i,self.clickCount)

			self.moleCell = cell(self.moleSquare,880,120)
			
			self.screen.blit(self.moleCell.image,self.moleCell.disp)
			pygame.display.flip()
			self.screen.blit(self.garden,self.gardenDisp)
			
			if veggieTotal == 0:
				print 'Game over'
				print 'Score:', playerScore
# 				del self
				pygame.time.wait(500)
				break

if __name__ == "__main__" :
        play = game()
        play.run()

