import pygame

pygame.init()

win = pygame.display.set_mode((894,894))

pygame.display.set_caption("Star Wars: The Force of Jin")

walkRight=[pygame.image.load('jinR1.PNG'),pygame.image.load('jinR2.PNG')]
walkLeft=[pygame.image.load('jinL1.PNG'),pygame.image.load('jinL2.PNG')]
attackRight=[pygame.image.load('jinRA1.PNG'),pygame.image.load('jinRA2.PNG')]
attackLeft=[pygame.image.load('jinLA1.PNG'),pygame.image.load('jinLA2.PNG')]
stand=pygame.image.load('jinRS.PNG')
bg1=pygame.image.load('bg1.JPG')

x=70
y=100
pwidth=500
pheight=768
vel=5

isJumping=False
jumpCount=10

left=False
right=False
walkCount=0

def redrawGameWindow():
    global walkCount
    win.blit(bg1,(0,0))
    if (walkCount+1)>=6:
        walkCount=0

    if left:
        win.blit(walkLeft[walkCount//3],(x,y))
        walkCount+=1

    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount+=1

    else:
        win.blit(stand,(x,y))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(0)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
        x-=vel
        left=True
        right=False

    elif keys[pygame.K_RIGHT] and x<(894-pwidth):
        x+=vel
        right=True
        left=False

    else:
        right=False
        left=False
        walkCount=0

    if not isJumping:

        if keys[pygame.K_SPACE]:
            isJumping=True
            right=False
            left=False
            walkCount=0

    else:

        if jumpCount>=-10:
            neg=1
            if jumpCount<0:
                neg=-1

            y-=(jumpCount**2) * 0.5 * neg
            jumpCount-=1

        else:
            isJumping=False
            jumpCount=10


    redrawGameWindow()

pygame.quit()
