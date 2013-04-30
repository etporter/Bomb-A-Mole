import sys, pygame
 
 
pygame.init()
  

pygame.display.set_caption('High Score')

dimensions=[1200,650]

font = pygame.font.Font(None, 48)

screen=pygame.display.set_mode(dimensions)

File_X = 1

File_Y = 2

File_Z = 3

File_T = 4

if File_X == 1:
        file1 = open("High Score.txt", "r") 
        # line = file1.readline()
        text = file1.read() 

        # print text

        # while line: 
        # 	print line 
        # 	line = file1.readline()

        text=font.render(text, True, [255,255,255])
        screen.blit(text, [490, 200])
        filex = 1

if File_Y == 2:
        file2 = open("High Score2.txt", "r") 
        # line = file2.readline()
        text = file2.read() 

        # print text

        # while line: 
        # 	print line 
        # 	line = file2.readline()

        text=font.render(text, True, [255,255,255])
        screen.blit(text, [490, 300])

if File_Z == 3:
        file3 = open("high score3.txt", "r") 
        # line = file3.readline()
        text = file3.read() 

        # print text

        # while line: 
        # 	print line 
        # 	line = file3.readline()

        text=font.render(text, True, [255,255,255])
        screen.blit(text, [490, 400])

if File_T == 4:
        file4 = open("High scores.txt", "r") 
        # line = file4.readline()
        text = file4.read() 

        # print text

        # while line: 
        # 	print line 
        # 	line = file4.readline()

        text=font.render(text, True, [255,255,255])
        screen.blit(text, [490, 50])

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()

Call2()
Call3()



