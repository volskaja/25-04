import pygame,sys

pygame.init()
#värvid
kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("slon.png")
posX=X-mesilane.get_rect().width
posY=Y-mesilane.get_rect().height
#posX=0
#posY=0
lõpp=False
sammX=0
sammY=0
while not lõpp:
	kell.tick(250)
	events=pygame.event.get()
	for i in pygame.event.get():
		if i.type==pygame.QUIT():
			sys.exit()
	if posX==0 and posY==0:
		sammX=1
		sammY=0		
	if posX==X-mesilane.get_rect().width and posY<=Y-mesilane.get_rect().height:	
		sammX=0
		sammY=1
	if posX<=X-mesilane.get_rect().width and posY==Y-mesilane.get_rect().height:	
		sammX=1
		sammY=0
		sammX=-sammX
	if posX==0 and posY>=Y-mesilane.get_rect().height:					
		sammX=0
		sammY=1
		sammY=-sammY
	posX+=sammX
	posY+=sammY
	ekraan.blit(mesilane,(posX,posY))	
	pygame.display.flip()
	ekraan.fill(roheline)
	
pygame.quit()
