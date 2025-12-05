print("Space Invaders starting...")

import pygame, sys
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() #sets fps

#loads ma sprites
player_img = pygame.image.load("space_invaders/assets/player.png").convert_alpha()
enemy_img = pygame.image.load("space_invaders/assets/invader1.png")
#sizing up the sprites
player_img = pygame.transform.scale(player_img, (40, 40))
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()


#creating bullet
bullets = []                 
bullet_w, bullet_h = 4, 12
bullet_speed = -7        

#player vari
player_x = 370
player_y = 400
player_speed = 0

#draw player
def draw_player(x, y):
    screen.blit(player_img, (x, y))

#draw enemy
def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))


running = True



#main loop
while running == True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                booletX = player_x + 17  #center bullet on player (player w is 40 )
                booletY = player_y
                bullets.append(pygame.Rect(booletX, booletY, bullet_w, bullet_h))

    screen.fill((0,0,0))

    #player move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5


        # create a new list for bullets that are still on screen
    new_bullets = []

    for b in bullets:
        b.y += bullet_speed       
        if b.y > 0:               
            new_bullets.append(b)
        pygame.draw.rect(screen, (255, 255, 0), b)  #draw bullet

    #replace old list with only the bullets that are still on screen
    bullets = new_bullets
    

    #keep player on screen
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - 40:
     player_x = WIDTH - 40

    #draw player
    draw_player(player_x, player_y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
