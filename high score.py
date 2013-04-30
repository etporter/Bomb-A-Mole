"""
This is a program for displaying the user's high scores.
"""
import sys, pygame
 
pygame.init() 

pygame.display.set_caption('High Score')

# set the window size:
dimensions=[1200,650]

font = pygame.font.Font(None, 48)

screen=pygame.display.set_mode(dimensions)

# load the high score storage file:
file = open("High Score.txt", "r") 

# read the file:
intext = file.read()

# split the high score storage into useable data
text = str(intext).split('.')

print text

# For each item in the list of high scores, blit at a different y coordinate:
for i in text:
	print i

	iIndex = text.index(i)
	
	j = font.render(i, True, [255,255,255])
	screen.blit(j, [50, ((iIndex+1)*50)-10])

# main loop:
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()



