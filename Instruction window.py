import pygame
 
 
pygame.init()
  

pygame.display.set_caption('Instructions')
 
display_instructions = True

clock=pygame.time.Clock()

dimensions=[1200,650]

done=False

font = pygame.font.Font(None, 48)

screen=pygame.display.set_mode(dimensions)

display_instructions = True
instruction_page = 1

black	= (   0,   0,   0)
white	= ( 255, 255, 255)

carrotpic = pygame.image.load ('carrot_final.png')
cabbagepic = pygame.image.load ('cabbage_final.png')
molepic = pygame.image.load ('mole_final.png')
bombpic = pygame.image.load ('bombfusefull_final.png')
clockpic = pygame.image.load('clock_final.png')
threepic = pygame.image.load('three_final.png')
craterpic = pygame.image.load('crater_final.png')


while done==False and display_instructions:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True #
		if event.type == pygame.MOUSEBUTTONDOWN:
			instruction_page += 1
			if instruction_page == 9:
				display_instructions = False
				
	
	screen.fill(white)
 
	if instruction_page == 1:
		text=font.render("How to Play Bomb-A-Mole", True, black)
		screen.blit(text, [500, 200])

	if instruction_page == 2:
		text=font.render("You are a farmer and moles are trying to take your carrots and cabbage", True, black)
		screen.blit(text, [150, 200])
		screen.blit(carrotpic,(550, 500))
		screen.blit(cabbagepic,(700,500))
		
	if instruction_page == 3:
		text=font.render("So you need to destroy them", True, black)
		screen.blit(text, [480, 200])
		screen.blit(molepic,(640,500))

	if instruction_page == 4:
		text=font.render("With Bombs!", True, black)
		screen.blit(text, [575,200])
		screen.blit(bombpic,(640,500))

	if instruction_page == 5:
		text=font.render("You have 60 seconds to destroy as many moles as you can", True, black)
		screen.blit(text, [235, 200])
		screen.blit(clockpic,(640,500))

	if instruction_page == 6:
		text=font.render("After every vegetable the mole takes he moves 3 spaces", True, black)
		screen.blit(text, [260, 200])
		screen.blit(threepic,(640,500))

	if instruction_page == 7:
		text=font.render("Watch out because bombs also create craters which nothing can grow in", True, black)
		screen.blit(text, [140, 200])
		screen.blit(craterpic,(640,500))

	if instruction_page == 8:
		text=font.render("Your score is based on how many moles you bomb in 60 seconds", True, black)
		screen.blit(text, [190,200])

		text=font.render("After 60 seconds your score is recorded", True, black)
		screen.blit(text, [400,400])

		text=font.render("So Bomb-A-Mole and save your garden!", True, black)
		screen.blit(text, [400,600])


	clock.tick(5)
	
	pygame.display.flip()

pygame.quit ()
