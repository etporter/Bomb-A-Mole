import sys
import pygame
from pygame.locals import *
import random
import time
import math

pygame.init()

# main menu

# startButton = button(command = gameloop)
# highscoreButton = button(command = displayhighscore)
# quitButton = button(command = quit)

# thickarrow_strings = (               #sized 24x24
# "XXXXXXXXXXXXXXXX        ",
# "X........XXXX           ",
# "X.....XXXX              ",
# "X...XXX                 ",
# "X..XXX                  ",
# "X..XXX                  ",
# "X.XX  X                 ",
# "X.X    XX               ",
# "X.X    XXX              ",
# "XXX     X.X             ",
# "XX       X.X            ",
# "XX        X.XX          ",
# "XX        XX.XX         ",
# "X          XX.XXX       ",
# "X           XX.XXX      ",
# "X            XX..XXX    ",
# "             XX....XXX  ",
# "              XX.....XX ",
# "               X......XX",
# "               XX......X",
# "                X......X",
# "                XX.....X",
# "                 XX...XX",
# "                  XXXXX ")

# thickarrow_strings = (               #sized 24x24
# "        X.X.X.X.        ",
# "     X.X.X.X.X.X.X.     ",
# "    X.X    .X    .X.    ",
# "   .X      X.      .X   ",
# "  X.       .X       X.  ",
# " .X        X.        .X ",
# " X.        .X        X. ",
# " X         X.         X ",
# "X.         .X         X.",
# ".X         X.         .X",
# "X.         .X         X.",
# ".X.X.X.X.X.X.X.X.X.X.X.X",
# "X.X.X.X.X.X.X.X.X.X.X.X.",
# ".X         X.         .X",
# "X.         .X         X.",
# ".X         X.         .X",
# " X         .X         X ",
# " X.        X.        .X ",
# " .X        .X        X. ",
# "  X.       X.       .X  ",
# "   .X      .X      XX   ",
# "    X.X    X.    X.X    ",
# "     X.X.XX.X.X.X.X     ",
# "        X.XX.XXX        ")

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

mousecursor = pygame.cursors.compile(thickarrow_strings, black='X', white='.', xor='o')

cursorsize = [24,24]

# objects/classes:

class cell:
	def __init__(self,type,xCoord,yCoord):
		
		self.carrot = pygame.image.load('carrot.png')
		self.cabbage = pygame.image.load('cabbage.png')
		self.bomb = pygame.image.load('bomb.png')
		self.crater = pygame.image.load('crater.png')
	
		self.kind = type
		
		self.x = xCoord
		self.y = yCoord
		
		self.bombTicker = 0
		
		if self.kind == 1:
			self.image = self.carrot
		elif self.kind == 2:
			self.image = self.cabbage
		elif self.kind == 3:
			self.image = self.bomb
		elif self.kind == 4:
			self.image = self.crater
		
		self.disp = self.image.get_rect(center = (self.x,self.y))
		
	def placeBomb(self,mouseX,mouseY):
# 		print 'placeBomb activated!'
# 		if playerTurn = True:
# 		self.mouseLoc = pygame.mouse.get_pos()
# 		self.mouseX = self.mouseLoc[0]
# 		self.mouseY = self.mouseLoc[1]
		
		self.mouseX = mouseX
		self.mouseY = mouseY

# 		print self.mouseX, self.mouseY
		
		if abs(self.x - self.mouseX) <= 40 and abs(self.y - self.mouseY) <= 40:

# 			print 'placeBomb if sequence activated!'
# 			print self.mouseX, self.mouseY
	
			self.bombTicker = 0
			self.kind = 3
			self.image = self.bomb
	
	def boom(self,count):
		self.bombTicker = count
		if self.bombTicker == 3:
			self.kind = 4
			self.image = self.crater
			
	def eaten(self,count):
		self.moleTicker = count
		if self.moleTicker == 3:
			print 'Veggie eaten!'
			self.kind = 4
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
# 		Kill Mole
# 		Add score
# 		New Mole
# 	elif: 
# 		Loop
# 		Add score
# 		elim clicked spaces
# 	if all cell.types == 4 remain:
# 		Level lost
# 		save score
# 		save lvl
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
		
		game.clickCount = 3
		
		self.x = self.position[0]
		self.y = self.position[1]
		
		print self.x,self.y
		print ''
		print self.locationIndex
		print ''
		
	def move(self):
# 		self.moveChoices = self.squareCenters[self.moveChoicesIndex]
		
		self.moveChoices = []
		
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex+1)])
		except IndexError:
			print 'This is out of range, no biggie'
			
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex-1)])
		except IndexError:
			print 'This is out of range, no biggie'
			
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex+6)])
		except IndexError:
			print 'This is out of range, no biggie'
			
		try:
			self.moveChoices.append(self.squareCenters[int(self.locationIndex-6)])
		except IndexError:
			print 'This is out of range, no biggie'
		
		for i in self.moveChoices:
			self.iIndex = self.squareCenters.index(i)
			if abs(self.iIndex-self.locationIndex) == 1 and abs(i[0]-self.position[0]) > 82:
				self.moveChoices.remove(i)
			elif abs(self.iIndex-self.locationIndex) > 7:
				self.moveChoices.remove(i)
		
		self.moveChoicesIndex = []
		
		for j in self.moveChoices:
			k = self.squareCenters.index(j)
			self.moveChoicesIndex.append(k)
			
		print self.moveChoices
		print ''
		print self.moveChoicesIndex
		print ''
	
		self.position = random.choice(self.moveChoices)
		
		self.x = self.position[0]
		self.y = self.position[1]
		
		self.locationIndex = self.squareCenters.index(self.position)
		
		print 'New coordinates:',self.x,self.y
		print 'New index:',self.locationIndex
		
		self.locationIndex = self.squareCenters.index(self.position)
			
class game:
	def __init__(self):
		self.size = 1200, 650
		self.screen = pygame.display.set_mode(self.size)
		self.cells = [cell(random.randint(1,2),120,120),cell(random.randint(1,2),201,120),cell(random.randint(1,2),282,120),cell(random.randint(1,2),363,120),cell(random.randint(1,2),444,120),cell(random.randint(1,2),525,120),cell(random.randint(1,2),120,201),cell(random.randint(1,2),201,201),cell(random.randint(1,2),282,201),cell(random.randint(1,2),363,201),cell(random.randint(1,2),444,201),cell(random.randint(1,2),525,201),cell(random.randint(1,2),120,282),cell(random.randint(1,2),201,282),cell(random.randint(1,2),282,282),cell(random.randint(1,2),363,282),cell(random.randint(1,2),444,282),cell(random.randint(1,2),525,282),cell(random.randint(1,2),120,363),cell(random.randint(1,2),201,363),cell(random.randint(1,2),282,363),cell(random.randint(1,2),363,363),cell(random.randint(1,2),444,363),cell(random.randint(1,2),525,363),cell(random.randint(1,2),120,444),cell(random.randint(1,2),201,444),cell(random.randint(1,2),282,444),cell(random.randint(1,2),363,444),cell(random.randint(1,2),444,444),cell(random.randint(1,2),525,444),cell(random.randint(1,2),120,525),cell(random.randint(1,2),201,525),cell(random.randint(1,2),282,525),cell(random.randint(1,2),363,525),cell(random.randint(1,2),444,525),cell(random.randint(1,2),525,525)]
		
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

					if self.clickCount < 3:
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
					
					mole.move(self.mole)
						
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			for i in self.cells:
				self.screen.blit(i.image,i.disp)
				pygame.display.flip()
				
				if self.mole.x == i.x and self.mole.y == i.y:
					self.moleSquare = i.kind
					if i.kind == 3:
						print 'Mole killed!'
						cell.boom(i,3)
						del self.mole
						self.mole = mole()
					if i.kind == 1 or i.kind == 2:
						cell.eaten(i,self.clickCount)

			self.moleCell = cell(self.moleSquare,880,120)
			
			self.screen.blit(self.moleCell.image,self.moleCell.disp)
			pygame.display.flip()

game = game()

