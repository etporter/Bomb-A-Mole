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

carrot = pygame.image.load('carrot.png')
cabbage = pygame.image.load('cabbage.png')
bomb = pygame.image.load('bomb.png')
crater = pygame.image.load('crater.png')


# objects/classes:

class cell:
	def __init__(self,type,left,top,width,height):
		self.kind = type
		
		self.left = left
		self.top = top
		self.width = width
		self.height = height
		
		self.disp = Rect(self.left,self.top,self.width,self.height)
		
		if self.kind == 1:
			self.image = carrot
		elif self.kind == 2:
			self.image = cabbage
		elif self.kind == 3:
			self.image = bomb
		elif self.kind == 4:
			self.image = crater
		
		self.image.get_rect()
		
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
# 		self.cells = [[cell(0,0,0),cell(0,1,0),cell(0,2,0),cell(0,3,0),cell(0,4,0),cell(0,5,0)],[cell(0,0,0),cell(0,1,1),cell(0,2,1),cell(0,3,1),cell(0,4,1),cell(0,5,1)],[cell(0,0,2),cell(0,1,2),cell(0,2,2),cell(0,3,2),cell(0,4,2),cell(0,5,2)],[cell(0,0,3),cell(0,1,3),cell(0,2,3),cell(0,3,3),cell(0,4,3),cell(0,5,3)],[cell(0,0,4),cell(0,1,4),cell(0,2,4),cell(0,3,4),cell(0,4,4),cell(0,5,4)],[cell(0,0,5),cell(0,1,5),cell(0,2,5),cell(0,3,5),cell(0,4,5),cell(0,5,5)]]
		self.cell = cell(1,5,5,80,80)
		self.screen.blit(self.cell.image,(self.cell.left,self.cell.top))
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

game = game()

