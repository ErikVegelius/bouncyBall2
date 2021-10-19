print("hejHopp")
import sys,pygame

n=4
size= width, height = 320*n,240*n
speed =[1,1]
black = 0,0,0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("D:\projects\pyGame2\intro_ball.gif")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed [0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	screen.fill(black)
	screen.blit(ball,ballrect)
	pygame.display.flip()
