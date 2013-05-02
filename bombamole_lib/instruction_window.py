import pygame
import menu
 
 
pygame.init()
  

class instr(object):
        def __init__(self):
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
                craterpic = pygame.image.load('data/mole_animation_1.gif')


                while done==False and display_instructions:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        done=True #
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        instruction_page += 1
                                        if instruction_page == 9:
                                                display_instructions = False
                                                
                        
                        screen.fill(black)
                 
                        if instruction_page == 1:
                                text=font.render("How to Play Bomb-A-Mole", True, white)
                                screen.blit(text, [380, 200])

                        if instruction_page == 2:
                                text=font.render("You are a farmer and moles are trying to take your carrots and cabbage", True, white)
                                screen.blit(text, [20, 200])
                                screen.blit(carrotpic,(460, 500))
                                screen.blit(cabbagepic,(610,500))
                                
                        if instruction_page == 3:
                                text=font.render("So you need to destroy them", True, white)
                                screen.blit(text, [355, 200])
                                screen.blit(molepic,(520,500))

                        if instruction_page == 4:
                                text=font.render("With Bombs!", True, white)
                                screen.blit(text, [455,200])
                                screen.blit(bombpic,(520,500))

                        if instruction_page == 5:
                                text=font.render("You have to destroy as many moles as you can", True, white)
                                screen.blit(text, [235, 200])
                                screen.blit(clockpic,(520,500))

                        if instruction_page == 6:
                                text=font.render("After every vegetable the mole moves 3 spaces", True, white)
                                screen.blit(text, [220, 200])
                                screen.blit(threepic,(520,500))

                        if instruction_page == 7:
                                text=font.render("Watch out because bombs also create craters which nothing can grow in", True, white)
                                screen.blit(text, [8, 200])
                                screen.blit(craterpic,(520,500))

                        if instruction_page == 8:
                                text=font.render("Your score is based on how many moles you bomb", True, white)
                                screen.blit(text, [220,100])

                                text=font.render("The round is done when there is no more vegetables", True, white)
                                screen.blit(text, [203,300])

                                text=font.render("So Bomb-A-Mole and save your garden!", True, white)
                                screen.blit(text, [288,500])


                        clock.tick(5)
                        
                        pygame.display.flip()

                mymenu = menu.run()
                mymenu.runm()

if __name__ == "__main__":
        start = instr()
        start.run()
