"""
This is a program for displaying the user's high scores.
"""
import sys, pygame
 
pygame.init() 

class hs(object):
	def __init__(self):
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
		firstText = str(intext).split(',')

# 		print text

		secondText = []
		
		for i in firstText:
			j = str(i).split('.')
			secondText.append(j)
		
		print secondText

		secondText = sorted(secondText, key = lambda i: int(i[1]))

		if len(secondText) > 12 and len(secondText) < 24:
			text1 = secondText[0:12]
			text2 = secondText[12:]
			
			for i in text1:
		# 		print i

				iIndex = text1.index(i)
			
				j = font.render(i, True, [255,255,255])
				screen.blit(j, [50, ((iIndex+1)*50)-10])
				
			for i in text2:
		# 		print i

				iIndex = text2.index(i)
			
				j = font.render(i, True, [255,255,255])
				screen.blit(j, [400, ((iIndex+1)*50)-10])
				
		elif len(secondText) > 24:
			text1 = secondText[0:12]
			text2 = secondText[12:24]
			text3 = secondText[24:]
			
			for i in text1:
		# 		print i

				iIndex = text1.index(i)
			
				j = font.render(str(i), True, [255,255,255])
				screen.blit(j, [50, ((iIndex+1)*50)-10])
				
			for i in text2:
		# 		print i

				iIndex = text2.index(i)
			
				j = font.render(str(i), True, [255,255,255])
				screen.blit(j, [400, ((iIndex+1)*50)-10])
				
			for i in text3:
		# 		print i

				iIndex = text3.index(i)
			
				j = font.render(str(i), True, [255,255,255])
				screen.blit(j, [800, ((iIndex+1)*50)-10])

		else:
		# For each item in the list of high scores, blit at a different y coordinate:
			for i in secondText:
		# 		print i

				iIndex = secondText.index(i)
			
				j = font.render(i, True, [255,255,255])
				screen.blit(j, [50, ((iIndex+1)*50)-10])

		# main loop:
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.flip()

if __name__ == "__main__":
	begin = hs()
	begin.run()
