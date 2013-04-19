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

thickarrow_strings = (               #sized 24x24
"        X.X.X.X.        ",
"     X.X.X.X.X.X.X.     ",
"    X.X    .X    .X.    ",
"   .X      X.      .X   ",
"  X.       .X       X.  ",
" .X        X.        .X ",
" X.        .X        X. ",
" X         X.         X ",
"X.         .X         X.",
".X         X.         .X",
"X.         .X         X.",
".X.X.X.X.X.X.X.X.X.X.X.X",
"X.X.X.X.X.X.X.X.X.X.X.X.",
".X         X.         .X",
"X.         .X         X.",
".X         X.         .X",
" X         .X         X ",
" X.        X.        .X ",
" .X        .X        X. ",
"  X.       X.       .X  ",
"   .X      .X      XX   ",
"    X.X    X.    X.X    ",
"     X.X.XX.X.X.X.X     ",
"        X.XX.XXX        ")

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
		
# 		self.disp = Rect(self.left,self.top,self.width,self.height)

		self.kind = random.randint(1,2)
		
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
			self.kind = 3
			self.image = self.bomb
	
# 	def clickOn(self):
# 		for event in pygame.event.get():
# 			if event.type == MOUSEBUTTONDOWN:
# 				print 'Mouse clicked!'

# class mole:
# 	def __init__(self,Xcoord,YCoord):
# 	
# 	def bombed:
# 		squeal
# 		die


# Basic Game Logic:

# def gameloop:
# 
# # Enter Game Loop:
# 	
# 	Game build == 1;
# 	Set level = 1;
# 	Set Score = 0;
# 
# 	If user has clicked the maximum number of boxes:
# 		Generate animation, or image change
# 
# 	if user hits mole:
# 		Level win
# 		Add score
# 		Add level
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


class game:
	def __init__(self):
		self.size = width, height = 1200, 650
		self.screen = pygame.display.set_mode(self.size)

		self.cells = [cell(1,120,120),cell(1,201,120),cell(1,282,120),cell(1,363,120),cell(1,444,120),cell(1,525,120),cell(1,120,201),cell(1,201,201),cell(1,282,201),cell(1,363,201),cell(1,444,201),cell(1,525,201),cell(1,120,282),cell(1,201,282),cell(1,282,282),cell(1,363,282),cell(1,444,282),cell(1,525,282),cell(1,120,363),cell(1,201,363),cell(1,282,363),cell(1,363,363),cell(1,444,363),cell(1,525,363),cell(1,120,444),cell(1,201,444),cell(1,282,444),cell(1,363,444),cell(1,444,444),cell(1,525,444),cell(1,120,525),cell(1,201,525),cell(1,282,525),cell(1,363,525),cell(1,444,525),cell(1,525,525)]
		
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
					for i in self.cells:
						cell.placeBomb(i,self.mX,self.mY)
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			for i in self.cells:
				self.screen.blit(i.image,i.disp)
				pygame.display.flip()

game = game()

