import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import primary,menu

file = open("data/HighScore.txt","a") #opens high score text file & equates it to var file
def get_key():            #reads the users keys as they type into the input box
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):     #initializes & displays the input box as a new screen in pygame
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):          #writes the text to the input box, prompting the user for input
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():             #initializes display, defines value for ask module, and writes to the high score file
  screen = pygame.display.set_mode((1200,650))
  main.scoring = ask(screen, "Enter Username")
  main.a = ','+main.scoring+'.'+str(primary.playerScore)
  file.write(main.a)
  menutime = menu.run()
  menutime.runm()
  

if __name__ == '__main__': main()
