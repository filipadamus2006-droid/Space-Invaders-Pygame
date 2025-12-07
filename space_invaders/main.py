print("Space Invaders starting...")
import random
import pygame, sys
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#setting game state
game_over = False

#loads ma sprites
player_img = pygame.image.load("space_invaders/assets/player.png").convert_alpha()
enemy_img = pygame.image.load("space_invaders/assets/invader1.png")
#sizing up the sprites
player_img = pygame.transform.scale(player_img, (40, 40))
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()

player_shoot_cooldown = 30   #time between shots
player_shoot_timer = 0       #cd timer
 


#enemy class
class enemy:

    def __init__(self, x, y, image):
        self.x = x
        self.shoot_cooldown = random.randint(60, 120)  # 1–2 seconds approx
        self.shoot_timer = 0
        self.y = y
        self.start_y = y
        self.image = image
        self.speed = 2  #how fast the enemy moves to da side
        self.direction = 1  #1 = moving right, -1 = moving left
        self.image = pygame.transform.scale(image, (40, 40))  
        self.bullets = []  #list to store bullets fired by the enemy, need 4 collision
        self.bullet_w = 4         
        self.bullet_h = 12         
        self.bullet_speed = 2      
        self.shoot_cooldown = 90   #frames 2 wait between shots
        self.shoot_timer = 0       # counts frames till next shot


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen_width):
        global game_over
        self.x += self.speed * self.direction
        if self.x <= 0 or self.x + self.image.get_width() >= screen_width:
            self.direction *= -1 
            self.y += 50 
        if self.y + self.image.get_height() >= player_y - 10:  # enemy near player bottom
            game_over = True

    def shoot(self):
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_cooldown:
            bullet_x = self.x + self.image.get_width() // 2
            bullet_y = self.y + self.image.get_height()
            self.bullets.append(pygame.Rect(bullet_x, bullet_y, self.bullet_w, self.bullet_h))
            self.shoot_timer = 0
            # Pick a new random cooldown for the next shot
            self.shoot_cooldown = random.randint(60, 120)

    def update_bullets(self, screen):
        new_bullets = []
        for b in self.bullets:
            b.y += self.bullet_speed  # move bullet down
            if b.y <= HEIGHT:          # only keep bullets that are on screen
                new_bullets.append(b)
                pygame.draw.rect(screen, (255, 0, 0), b) 
        self.bullets = new_bullets
enemyclass = enemy

#enemy respawn
enemy_r_delay = 60   #frames til respawn
respawn_timer = 0


start_y = 50

ENEMY_COUNT = 3
enemies = []
#enemy spawn
ENEMY_COLS = 5
ENEMY_ROWS = 2
x_gap = (WIDTH - ENEMY_COLS * 40) // (ENEMY_COLS + 1)
row_gap = 90  # big gap

enemies.clear()
for row in range(ENEMY_ROWS):
    for col in range(ENEMY_COLS):
        x = x_gap + col * (40 + x_gap)
        y = start_y + row * row_gap
        enemies.append(enemyclass(x, y, enemy_img))



#creating bullet
bullets = []                 
bullet_w, bullet_h = 4, 12
bullet_speed = -5  


#player vari
player_x = 370
player_y = 400
player_speed = 0
player_lives = 3
player_invulnerable = False          
player_invulnerable_timer = 0        
player_flash_timer = 0               
player_visible = True  
high_score = 0
score = 0

def draw_player(x, y):
    if player_visible:
        screen.blit(player_img, (x, y))

running = True

font = pygame.font.Font(None, 32)   #for score

#main loop
while running == True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    #player shooting
    if keys[pygame.K_SPACE] and player_shoot_timer <= 0:
        bullet_x = player_x + (player_img.get_width() - bullet_w) // 2
        bullet_y = player_y
        bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_w, bullet_h))
        player_shoot_timer = player_shoot_cooldown

    # decrement cooldown timer once per frame
    if player_shoot_timer > 0:
        player_shoot_timer -= 1

    #player hitbox            
    playerHitbox = pygame.Rect(player_x, player_y, 40, 40)

 
    screen.fill((0,0,0))
    
    for e in enemies:
        e.draw(screen)
        e.update(WIDTH)
        e.shoot()
        e.update_bullets(screen)


    #check if bullets hit player
    for e in enemies:
        for b in e.bullets[:]:
            if playerHitbox.colliderect(b):
                e.bullets.remove(b)
                if not player_invulnerable:
                    player_lives -= 1
                    print("Player hit! Lives left:", player_lives)
                    player_invulnerable = True
                    player_invulnerable_timer = 120
                    player_flash_timer = 0
                    player_visible = True  #become visible



    
    # handle hit and respawn enemy
    for e in enemies:
        enemyhitbox = pygame.Rect(e.x, e.y, e.image.get_width(), e.image.get_height())
        for b in bullets[:]:
            if enemyhitbox.colliderect(b):
                bullets.remove(b)
                score += 100
                if score > high_score:
                    high_score = score
                # gets rid of player bullets near dead enemy
                bullets = [bb for bb in bullets if not enemyhitbox.colliderect(bb)]
                enemies.remove(e)



    #player move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5


    #create new list for bullets that are on screen
    new_bullets = []

    for b in bullets:
        b.y += bullet_speed       
        if b.y > 0:               
            new_bullets.append(b)
        pygame.draw.rect(screen, (255, 255, 0), b)  

    #replace old list with only the bullets that r on screen
    bullets = new_bullets
    

    #keep player on screen
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - 40:
     player_x = WIDTH - 40  

    #invun check
    if player_invulnerable:
        player_invulnerable_timer -= 1
        player_flash_timer += 1
    
        #flash player
        if player_flash_timer >= 5:
            player_visible = not player_visible
            player_flash_timer = 0
    
        #end invincible
        if player_invulnerable_timer <= 0:
            player_invulnerable = False
            player_visible = True
    else:
        player_visible = True 
    


    #draw player
    if player_visible:
        draw_player(player_x, player_y)
        if player_invulnerable:
            red_overlay = pygame.Surface((40, 40), pygame.SRCALPHA)
            red_overlay.fill((255, 0, 0, 128))  
            screen.blit(red_overlay, (player_x, player_y))
        else:
            pass


    if len(enemies) == 0:
    # respawn a new wave of enemies
        for row in range(ENEMY_ROWS):
            for col in range(ENEMY_COLS):
                x = x_gap + col * (40 + x_gap)
                y = start_y + row * row_gap
                enemies.append(enemyclass(x, y, enemy_img))

    # draw HUD: score, high score, lives
    S = font.render(f"Score: {score}", True, (255, 255, 255))
    HS = font.render(f"High: {high_score}", True, (255, 255, 0))
    L = font.render(f"Lives: {player_lives}", True, (255, 255, 255))

    screen.blit(S, (10, 10))
    screen.blit(HS, (10, 30))
    screen.blit(L, (WIDTH - L.get_width() - 10, 10))

    pygame.display.flip()
    clock.tick(60)



    #game over screen

    if player_lives <= 0:
        game_over = True

    if game_over == True:
        font = pygame.font.Font(None, 48)
        text = font.render("GAME OVER! Press any key to restart.", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()

        waiting = True
        while waiting:
         for e in pygame.event.get():
             if e.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
             if e.type == pygame.KEYDOWN:
               
                player_x = 370
                player_y = 400
                player_lives = 3
                score = 0
                bullets.clear()
                # Reset invulnerability
                player_invulnerable = False
                player_visible = True

                waiting = False
                game_over = False


            # Reset enemies after game over
                enemies.clear()
                for row in range(ENEMY_ROWS):
                    for col in range(ENEMY_COLS):
                         x = x_gap + col * (40 + x_gap)
                         y = start_y + row * row_gap
                         enemies.append(enemyclass(x, y, enemy_img))

        

pygame.quit()
sys.exit()
