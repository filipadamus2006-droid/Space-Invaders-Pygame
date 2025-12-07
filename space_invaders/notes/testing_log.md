**10 NOV 2025**

Tested the drawplayer function I created. It worked fine and the player shows up on the screen in the right place.


**12 NOV 2025**

Tested the movement, I realised the player can just go off the screen so i need to add some code that stops them from doing that.

**15 NOV 2025**

When the game was played i realised the sprite i loaded had a black background that stood out against my games dark blue one so i just changed the background to black so you couldnt see it.

**16 NOV 2025**

Fired bullets and checked movement - initially moved downwards, fixed by setting speed to -7. Bullets were slightly off-center - added +17 px to X..

**18 NOV 2025**

Enemy displays correctly on screen. draw_enemy() works multiple times without error. Bullets still function normally with enemy on screen.

**20 NOV 2025**

Checked bullets with placeholder enemyv- pass through enemy (collision not implemented yet). Frame rate with player and bullets stable at 60 FPS.

**23 NOV 2025**

Player movement and shooting tested together - smooth, no bugs. Bullets disappear correctly off-screen. Minor visual issue: bullets slightly off-center if player moves quickly - acceptable for now.

**01 DECEMBER 2025**

Today i added the enemy class. I wanted to test that the enemy prints to the screen after i made the class so i tested the draw function to see if the right image is displayed and if the code even works. Some of my variables where wrongly capitalised. After i fixed that, i ran the code and the enemy took up the whole background of the screen, it was clearly too large so i had to add some code that resizes this enemy. i added it in the class so all enemys become small and not ridiciilously large.

**02 DECEMBER 2025**

Tested the new update function that moves the enemy around. the enemy moves left / right and when they hit the wall, they turn flip directions they are moving and they go down 20 px.

**04 DECEMBER 2025**
