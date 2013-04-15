import sys
import pygame
from pygame.locals import *
import random
import time
import math

# main menu

startButton = button(command = gameloop)
highscoreButton = button(command = displayhighscore)
quitButton = button(command = quit)

carrot = pygame.image.load('carrot.png')
cabbage = pygame.image.load('cabbage.png')
bomb = pygame.image.load('bomb.png')
crater = pygame.image.load('crater.png')


# objects/classes:

class cell:
	def __init__(self,type,Xcoord,Ycoord):
		self.kind = type
		
		if self.kind == 1
			Image = carrot
		elif self.kind == 2
			Image = cabbage
		elif self.kind == 3
			Image = bomb
		elif self.kind == 4
			Image = crater
		
	def action:
		when mouse clicks:
			if mouseX is inside range (xMax-xMin) and mouseY is inside range (yMax-yMin):
				if playerTurn = True
					placeBomb
	def placeBomb:
		self.kind = 2
		Image = bomb

class mole:
	def __init__(self,Xcoord,YCoord):
	
	def bombed:
		squeal
		die


# Basic Game Logic:

def gameloop:

# Enter Game Loop:
	
	Game build == 1;
	Set level = 1;
	Set Score = 0;


	Has user clicked?
		Where?
			If on cell:
				type change
				image change

	If user has clicked the maximum number of boxes:
		Generate animation, or image change

	if user hits mole:
		Level win
		Add score
		Add level
	elif: 
		Loop
		Add score
		elim clicked spaces
	if all cell.types == 4 remain:
		Level lost
		save score
		save lvl

Level Lost:
		Get user name
			Save user name
		Print score

		Prompt user:
			play again?
			if answer == yes:
				Enter game loop
			elif:
				Return main menu.

# End game loop




