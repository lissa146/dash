import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("base dash clone")
clock = pygame.time.Clock()



WHITE = (255, 255, 255)
BLUE = (0,0, 255)

pw, ph = 10, 20
px, py = 50, 50
vx, vy = 5,0
g = 0.5
jmp = -10
double_jmp = -15
jumping = False
double_jump = False
jump_pressed = False

while True:
    clock.tick(60)
    
    #event stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    #phyiscs sec
    
    #player movement
    if keys[pygame.K_LEFT]:
        px -= vx
    if keys[pygame.K_RIGHT]:
        px += vx
    if keys[pygame.K_UP]:
        if not jumping:
            vy = jmp
            jumping = True
        elif not double_jump:
            vy = double_jmp
            #dou
    
    vy += g
    py += vy
    
    
    if py >= 600 - ph:
        py = 600 - ph
        jumping = False
        vy = 0
    
    #render sec
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLUE, (px , py, pw, ph))
    
    pygame.display.flip()
    
    
    
