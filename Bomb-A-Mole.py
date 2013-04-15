import sys
import pygame
from pygame.locals import *
import random
import time
import math

# main menu

# startButton = button(command = gameloop)
# highscoreButton = button(command = displayhighscore)
# quitButton = button(command = quit)


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
		
# 	def action:
# 		when mouse clicks:
# 			if mouseX is inside range (xMax-xMin) and mouseY is inside range (yMax-yMin):
# 				if playerTurn = True
# 					placeBomb
# 	def placeBomb:
# 		self.kind = 2
# 		Image = bomb

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
# 
# 	Has user clicked?
# 		Where?
# 			If on cell:
# 				type change
# 				image change
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
		pygame.init()
		self.size = width, height = 1200, 650
		self.screen = pygame.display.set_mode(self.size)
		
# 		self.cells = [cell(1,80,80),cell(1,161,80),cell(1,242,80),cell(1,323,80),cell(1,404,80),cell(1,485,80),cell(1,80,161),cell(1,161,161),cell(1,242,161),cell(1,323,161),cell(1,404,161),cell(1,485,161),cell(1,80,242),cell(1,161,242),cell(1,242,242),cell(1,323,242),cell(1,404,242),cell(1,485,242),cell(1,80,323),cell(1,161,323),cell(1,242,323),cell(1,323,323),cell(1,404,323),cell(1,485,323),cell(1,80,404),cell(1,161,404),cell(1,242,404),cell(1,323,404),cell(1,404,404),cell(1,485,404),cell(1,80,485),cell(1,161,485),cell(1,242,485),cell(1,323,485),cell(1,404,485),cell(1,485,485)]

		self.cells = [cell(1,120,120),cell(1,201,120),cell(1,282,120),cell(1,363,120),cell(1,444,120),cell(1,525,120),cell(1,120,201),cell(1,201,201),cell(1,282,201),cell(1,363,201),cell(1,444,201),cell(1,525,201),cell(1,120,282),cell(1,201,282),cell(1,282,282),cell(1,363,282),cell(1,444,282),cell(1,525,282),cell(1,120,363),cell(1,201,363),cell(1,282,363),cell(1,363,363),cell(1,444,363),cell(1,525,363),cell(1,120,444),cell(1,201,444),cell(1,282,444),cell(1,363,444),cell(1,444,444),cell(1,525,444),cell(1,120,525),cell(1,201,525),cell(1,282,525),cell(1,363,525),cell(1,444,525),cell(1,525,525)]
		
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			for i in self.cells:
				self.screen.blit(i.image,i.disp)
				pygame.display.flip()

game = game()

