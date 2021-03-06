from pygame.locals import *
import time,math,random,pygame,sys,os
import menu
import pyganim,cPickle,datetime,hs,uinput

pygame.init()


global veggieTotal, playerScore, blitX, blitY, blitmX, blitmY, highscorefile, blitdX, blitdY

blitdX = 10
blitdY = 10
blitX = 10
blitY = 10
blitmX = 10
blitmY = 10

veggieTotal = 36
playerScore = 0

file = open("data/HighScore.txt", "a")

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

# setup a clock for the animations:
mainClock = pygame.time.Clock()

# define the frames and frame display time for the explosion animation:
boomAnim = pyganim.PygAnimation([('data/kaboom_frame2.png', 0.1),
                                ('data/kaboom_frame3.png', 0.1),
                                ('data/kaboom_frame4.png', 0.1),
                                ('data/kaboom_frame5.png', 0.1),
                                ('data/kaboom_frame6.png', 0.1),
                                ('data/kaboom_frame7.png', 0.1)], loop=False)

# define the frames and frame display time for the mole eating animation:
moleAnim = pyganim.PygAnimation([('data/mole_animation_1.gif', 0.1),
                                 ('data/mole_animation_2.gif', 0.1),
                                 ('data/mole_animation_3.gif', 0.1),
                                 ('data/mole_animation_4.gif', 0.1),
                                 ('data/mole_animation_5.gif', 0.1),
                                 ('data/mole_animation_6.gif', 0.1),
                                 ('data/mole_animation_7.gif', 0.1),
                                 ('data/mole_animation_8.gif', 0.1),
                                 ('data/mole_animation_9.gif', 0.1),
                                 ('data/mole_animation_10.gif', 0.1),
                                 ('data/mole_animation_11.gif', 0.1),
                                 ('data/mole_animation_12.gif', 0.1),
                                 ('data/mole_animation_13.gif', 0.1)],loop=False)

# define the frames and frame display time for the burned mole animation:
deadMole = pyganim.PygAnimation([('data/mole_crispy-animation_6.gif', 0.1),
                                 ('data/mole_crispy-animation_1.gif', 0.1),
                                 ('data/mole_crispy-animation_2.gif', 0.1),
                                 ('data/mole_crispy-animation_3.gif', 0.1),
                                 ('data/mole_crispy-animation_4.gif', 0.1),
                                 ('data/mole_crispy-animation_5.gif', 0.1),
                                 ('data/mole_crispy-animation_3.gif', 0.1),
                                 ('data/mole_crispy-animation_4.gif', 0.1),
                                 ('data/mole_crispy-animation_5.gif', 0.1),
                                 ('data/mole_crispy-animation_6.gif', 0.1),
                                 ('data/mole_crispy-animation_7.gif', 0.1)],loop=False)

# compiles the cursor from ascii art:
mousecursor = pygame.cursors.compile(thickarrow_strings, black='X', white='.', xor='o')

# defines cursor size:
cursorsize = [24,24]

# Class to create grid from:
class cell:
	def __init__(self,type,xCoord,yCoord):

# Load in the images and sounds:
		self.carrot = pygame.image.load('carrot_final.png')
		self.cabbage = pygame.image.load('cabbage_final.png')
		self.crater = pygame.image.load('crater_final.gif')
		
		self.bomb = pygame.image.load('bombfusefull_final.png')
		self.bomb2 = pygame.image.load('bombfusehalf_final.png')
		self.bomb3 = pygame.image.load('bombfuseshort.png')
		
		self.boomSound = pygame.mixer.Sound('data/Music/explosion.wav')
		self.munchSound = pygame.mixer.Sound('data/Music/Munching noise.wav')

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
		
		global veggieTotal
		
# Pass in the arguments:
		self.mouseX = mouseX
		self.mouseY = mouseY
		
# check to see if the user clicked inside the cell	
		if abs(self.x - self.mouseX) <= 40 and abs(self.y - self.mouseY) <= 40:
	
# set the cell's bomb ticker to 0
			self.bombTicker = 0
			
# change the cell to a bomb, both in type and display
# lower the vegetable count by one if the cell is a vegetable.
			if self.kind == 1 or self.kind == 2:
				veggieTotal -= 1
			self.kind = 3
			self.image = self.bomb
	
# define a method for the bomb exploding:
	def boom(self,count):
		
		global blitX,blitY,blitdX,blitdY
		
# pass in the bomb count
		self.bombTicker = count
		
# the image changes as the bomb counts down:
		if self.bombTicker == 1:
			self.image = self.bomb2
		
		elif self.bombTicker == 2:
			self.image = self.bomb3
		
# at 3, the bomb explodes
		elif self.bombTicker == 3:
			self.kind = 4
			if self.kind == 4:

				boomAnim.play()
				
# play the explosion sound:
				self.boomSound.play()
				
				blitX = self.x
				blitY = self.y

				self.image = self.crater
		elif self.bombTicker == 5:
                        deadMole.play()
                        blitdX = self.x
                        blitdY = self.y
                        self.image = self.crater
                        self.kind = 4
			
# Method for the vegetable being eaten:
# (I found it was easier to have the cell decide if it's been eaten, than have the mole decide)
			
	def eaten(self,count):
	
# the mole eats every other turn
		global blitmX,blitmY, veggieTotal
		
		self.moleTicker = count
		if self.moleTicker == 2:
			
# play the mol animation:
			moleAnim.play()
			blitmX = self.x
			blitmY = self.y
			
# lower the veggie count:			
			veggieTotal -= 1
			
			self.kind = 4
			if self.kind == 4:
				
				self.munchSound.play()
                                
				self.image = self.crater

# the mole class:
# (this class basically boils down to a tuple of two numbers, i.e. the mole's coordinates)

class mole:
	def __init__(self):
	
# 	create a list with the real coordinates of the centers of all the cells:
	
		self.squareCenters = [(120,120),(201,120),(282,120),(363,120),(444,120),(525,120),(120,201),(201,201),(282,201),(363,201),(444,201),(525,201),(120,282),(201,282),(282,282),(363,282),(444,282),(525,282),(120,363),(201,363),(282,363),(363,363),(444,363),(525,363),(120,444),(201,444),(282,444),(363,444),(444,444),(525,444),(120,525),(201,525),(282,525),(363,525),(444,525),(525,525)]
		
# 		the mole randomly chooses one of these pairs of coordinates
		
		self.position = random.choice(self.squareCenters)
		
# 		the mole's location can also be defined as an index inside the list of x,y pairs
		
		self.locationIndex = self.squareCenters.index(self.position)
		
# 		a silly hack to make the mole eat as soon as it's created:
		
		game.clickCount = 2
		
# 		pull x and y out of the location tuple:
		
		self.x = self.position[0]
		self.y = self.position[1]
		
# 		for debugging:
		
		print self.x,self.y
		print ''
		print self.locationIndex
		print ''
		
# 		the mole's move method:
# 		it takes a list as an argument, so that it is aware of the cell objects inside the main game class
		
	def move(self,inputList):
# 		self.moveChoices = self.squareCenters[self.moveChoicesIndex]
		
# 		empty list of choices for moving:
		
		self.moveChoices = []
		
# 		pass in the inputList argument:
		
		self.cells = inputList
		
# 		try to add the cell below, above, left, and right of the mole as move choices
# 		if they aren't found in the list (index out of range), pass
		
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
		
# 		this leads to allowing the mole to move across the screen (see the index mapping file for an illustration)
# 		so, we remove all choices who's x or y are across the screen:
		
		for i in self.moveChoices:
			self.iIndex = self.squareCenters.index(i)
			if abs(self.iIndex-self.locationIndex) == 1 and abs(i[0]-self.position[0]) > 82:
				self.moveChoices.remove(i)
			elif abs(self.iIndex-self.locationIndex) > 7:
				self.moveChoices.remove(i)
	
# 		create a priority 1 list from move choices
# 		this list consists of any squares neighboring the mole that contain vegetables
	
		self.priority1List = []
	
		for i in self.moveChoices:

			for j in self.cells:
			
				jCoordinates = (j.x,j.y)
			
# 				jIndex = self.squareCenters.index(jCoordinates)

				if jCoordinates == i and (j.kind == 1 or j.kind == 2):
					self.priority1List.append(i)
					break
	
# 		create a priority 2 list from move choices
# 		this list consists of any squares neighboring the mole who's row or column contain vegetables
	
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

# 		create lists of the indexes of our three move choice lists, and print them for debugging:

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

# 		first, try to pick a move from priority 1 list, if it is empty:
# 		second, try to pick a move from priority 2 list, if it is empty:
# 		third, pick a move from our initial move choice list

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
	
		global veggieTotal, playerScore, blitX, blitY, highscorefile
	
# 	set the screen size:
	
		self.size = 1200, 650
		game.screen = pygame.display.set_mode((self.size),0,32)
		
		playerScore = 0
		veggieTotal = 36
		
		self.owSound = pygame.mixer.Sound('data/Music/ow.wav')
		
# 		create the grid of cells:
		
		self.cells = [cell(random.randint(1,2),120,120),cell(random.randint(1,2),201,120),cell(random.randint(1,2),282,120),cell(random.randint(1,2),363,120),cell(random.randint(1,2),444,120),cell(random.randint(1,2),525,120),cell(random.randint(1,2),120,201),cell(random.randint(1,2),201,201),cell(random.randint(1,2),282,201),cell(random.randint(1,2),363,201),cell(random.randint(1,2),444,201),cell(random.randint(1,2),525,201),cell(random.randint(1,2),120,282),cell(random.randint(1,2),201,282),cell(random.randint(1,2),282,282),cell(random.randint(1,2),363,282),cell(random.randint(1,2),444,282),cell(random.randint(1,2),525,282),cell(random.randint(1,2),120,363),cell(random.randint(1,2),201,363),cell(random.randint(1,2),282,363),cell(random.randint(1,2),363,363),cell(random.randint(1,2),444,363),cell(random.randint(1,2),525,363),cell(random.randint(1,2),120,444),cell(random.randint(1,2),201,444),cell(random.randint(1,2),282,444),cell(random.randint(1,2),363,444),cell(random.randint(1,2),444,444),cell(random.randint(1,2),525,444),cell(random.randint(1,2),120,525),cell(random.randint(1,2),201,525),cell(random.randint(1,2),282,525),cell(random.randint(1,2),363,525),cell(random.randint(1,2),444,525),cell(random.randint(1,2),525,525)]
		
# 		load in the garden background image
		
		self.garden = pygame.image.load('garden.png')
		
		self.gardenDisp = self.garden.get_rect(center = (323,323))
		
		self.font = pygame.font.Font('data/FEASFBRG.ttf',30)
		
		self.moleLabel = self.font.render('Mole is hiding under:', True, [255,255,255])
		self.screen.blit(self.moleLabel, [760,60])
		
# 		self.scoreLabel = self.font.render('Score: '+str(playerScore), True, [255,255,255])
# 		self.screen.blit(self.scoreLabel, [760,360])
		
# 		initialize the mole object:
		
		self.mole = mole()
		
		self.cellXblit = 10
		self.cellYblit = 10		
		
# 		primary game loop:
		
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
# 							self.cellXblit = i.x
# 							self.cellYblit = i.y
# 						if i.kind == 4:
# 							boomAnim.play()
# 							boomAnim.blit(self.screen,(i.x,i.y))
							
					
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
						self.owSound.play()
						playerScore += 20+(veggieTotal*5)
						cell.boom(i,5)
						del self.mole
						self.mole = mole()
					if i.kind == 1 or i.kind == 2:
						cell.eaten(i,self.clickCount)
						#if i.kind == 4:
                                                #        moleAnim.play()
                                                #        moleAnim.blit(self.screen, (1045,300))

			self.moleCell = cell(self.moleSquare,880,160)
			
# blit the animations:
			self.animationBlit(blitX,blitY)
			self.animationBlitm(blitmX,blitmY)
			self.animationBlitd(blitdX,blitdY)
			
# set up a background for the score display:
			self.blackImage = pygame.image.load('data/black.png')
			
			self.blackBox = self.blackImage.get_rect(center = (780,360))
			self.screen.blit(self.blackImage, self.blackBox)
			
# set up the score display:
			self.scoreLabel = self.font.render('Score: '+str(playerScore), True, [255,255,255])
			self.screen.blit(self.scoreLabel, [760,360])
			
			self.screen.blit(self.moleCell.image,self.moleCell.disp)
			pygame.display.flip()
			self.screen.blit(self.garden,self.gardenDisp)
			
# game end logic:
			if veggieTotal == 0:
				print 'Game over'
				print 'Score:', playerScore
                                getinput = uinput.main()
                                getinput.run()
				game.textToWrite = raw_input('Please type a username to save your score: ')
				game.a = ','+self.textToWrite+'.'+str(playerScore)

				print self.a

				file.write(self.a)

				goBack = menu.run()
				goBack.runm()

# set up animation blit functions:
	def animationBlitm(self,x,y):
		self.blitmX = x-40
		self.blitmY = y-40
		moleAnim.blit(self.screen,(self.blitmX,self.blitmY))
		
	def animationBlitd(self,x,y):
		self.blitdX = x-40
		self.blitdY = y-40
		deadMole.blit(self.screen,(self.blitdX,self.blitdY))

	def animationBlit(self,x,y):
		self.blitX = x-80
		self.blitY = y-80
		boomAnim.blit(self.screen,(self.blitX,self.blitY))	

# return to the menu:
if __name__ == "__main__" :
        play = game()
        play.run()

