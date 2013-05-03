"""
This is a program for displaying the user's high scores.
"""
import menu
import sys, pygame
 
pygame.init() 

class hs(object):
	def __init__(self):
		pygame.display.set_caption('High Score')

		# set the window size:
		dimensions=[1200,650]

		font = pygame.font.Font('data/FEASFBRG.ttf', 30)

		screen=pygame.display.set_mode(dimensions)

# load the high score storage file:
		file = open("data/HighScore.txt", "r") 

# read the file:
		intext = file.read()

# split the high score storage into a list of name.score items
		firstText = str(intext).split(',')
		
# create a new list
		secondText = []
		
# Split the strings of name.score into tuples of (name,score) and add those tuples to the new list
		for i in firstText:
			j = str(i).split('.')
			secondText.append(j)

# sort our new list by highest score first
		secondText = sorted(secondText, key = lambda i: int(i[1]), reverse = True)

# take only the top ten scores:
                text1 = secondText[:10]
                
# display those scores on screen:
# (since pygame doesn't support multi-line strings, I had to blit each item at the same x, but a different y
                for i in text1:

                        iIndex = text1.index(i)
                        
                        j = str(i)
                
                        k = str(iIndex+1)+'. '+str(j[1:-1])
                
                        l = font.render(str(k), True, [255,255,255])

# this makes them "stack" on the screen as if they were a multi-line string
                        screen.blit(l, [50, ((iIndex+1)*50)-10])


# main loop:
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        mymenu = menu.run()
                                        mymenu.runm()

			pygame.display.flip()
			
			file.close()
		
# return to the menu:
if __name__ == "__main__":
	begin = hs()
	begin.run()
