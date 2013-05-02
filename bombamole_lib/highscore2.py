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

		# split the high score storage into useable data
		firstText = str(intext).split(',')

# 		print text

		secondText = []
		
		for i in firstText:
			j = str(i).split('.')
			secondText.append(j)
		
		print secondText

		secondText = sorted(secondText, key = lambda i: int(i[1]), reverse = True)

		
                text1 = secondText[:10]
                
                for i in text1:
        # 		print i

                        iIndex = text1.index(i)
                        
                        j = str(i)
                
                        k = str(iIndex+1)+'. '+str(j[1:-1])
                
                        l = font.render(str(k), True, [255,255,255])
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
		

if __name__ == "__main__":
	begin = hs()
	begin.run()
