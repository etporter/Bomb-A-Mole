import pygame
from pygame.locals import *
import sys, os
if sys.platform == 'win32' or sys.platform == 'win64':
	os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

Screen = max(pygame.display.list_modes())
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("[Program] - [Author] - [Version] - [Date]")
Surface = pygame.display.set_mode(Screen,FULLSCREEN)

Click = pygame.mixer.Sound("snd.ogg")

Explosion = pygame.image.load("expl.png").convert_alpha()
Explosions = []
for y in xrange(1):
	for x in xrange(7):
		rect = (x*Explosion.get_width()/7,y*Explosion.get_height(),Explosion.get_width()/7,Explosion.get_height())
		Explosions.append(Explosion.subsurface(rect))
ExplosionFrame = -10

Font = pygame.font.Font("font.ttf",40)

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

Time = [0,3,00]
OriginalTime = list(Time)

test = Font.render("0",True,(255,0,0))
width = test.get_width()
height = test.get_height()
totalwidth = 12 * width

def quit():
	pygame.mouse.set_visible(True)
	pygame.event.set_grab(False)
	pygame.quit(); sys.exit()
def GetInput():
	global usrcode
	key = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE: quit()
			usrcode += str(event.unicode).lower()
			if password in usrcode: quit()
			if len(usrcode) > len(password):
				usrcode = usrcode[1:]
mode = "counting"
def Update():
	global mode,Time,ExplosionFrame
	if mode == "counting":
		Time[2] -= 1
		if Time[2] == 15: Click.play()
		if Time[2] < 0:
			Time[2] = 99
			Time[1] -= 1
			if Time[1] < 0:
				Time[1] = 59
				Time[0] -= 1
				if Time[0] < 0:
					Time = [0,0,0]
					mode = "exploding"
					Click.play(40)
	else:
		ExplosionFrame += 0.1
		if int(ExplosionFrame) == 21:
			ExplosionFrame = -10
			Time = list(OriginalTime)
			mode = "counting"
def Draw():
	Surface.fill((0,0,0))
	t1 = str(Time[0])
	if len(t1) == 1: t1 = "0"+t1
	t2 = str(Time[1])
	if len(t2) == 1: t2 = "0"+t2
	t3 = str(Time[2])
	if len(t3) == 1: t3 = "0"+t3
	string = t1+" : "+t2+" : "+t3
	start_pos = (Screen[0]/2)-(totalwidth/2)
	for character in string:
		if character != "1":
			pos = [start_pos,(Screen[1]/2)-(height/2)]
		else:
			pos = [start_pos+int(round((51.0/99.0)*width)),(Screen[1]/2)-(height/2)]
		Surface.blit(Font.render(character,True,(255,0,0)),pos)
		start_pos += width
	if mode == "exploding":
		if ExplosionFrame >= 0:
			surf = Explosions[int(ExplosionFrame)]
			surf = pygame.transform.smoothscale(surf,map(lambda x:x*4,surf.get_size()))
			Surface.blit(surf,((Screen[0]/2)-(surf.get_width()/2),(Screen[1]/2)-(surf.get_height()/2)))
	pygame.display.flip()
def main():
	Clock = pygame.time.Clock()
	while True:
		GetInput()
		Update()
		Draw()
		Clock.tick(100)
if __name__ == '__main__': main()
