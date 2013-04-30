import sys, pygame
 
 
pygame.init()
  

pygame.display.set_caption('High Score')

dimensions=[1200,650]

font = pygame.font.Font(None, 48)

screen=pygame.display.set_mode(dimensions)

file = open("High Score.txt", "r") 
# line = file.readline()
intext = file.read() 

# print text

# while line: 
# 	print line 
# 	line = file.readline()

text = str(intext).split('.')

print text

for i in text:
	print i

	iIndex = text.index(i)
	
	j = font.render(i, True, [255,255,255])
	screen.blit(j, [100, (iIndex+1)*50])

# text=font.render(text, True, [255,255,255])
# screen.blit(text, [100, 200]) 

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()



