**10 NOV 2025**

Setup basics ; clock , screen size

Added player variables including X,Y,Speed

Created the draw function that draws the player and tested it and it drew the player as a rectangle.


**12 NOV 2025**

Started main loop today. First created a peice of code that tracks a variable called running which can be true or false. This is so the game can be quit out of later on

I also created a background using screen.fill and put my draw_player function (which i tested yesterday) into the main loop. I also set the clock to 60. Also added the flip() command which puts the buffered frame on the display.

Began creating player movement by checking the keyboard state and moving players X in the respective direction if it was pressed. 

Added code that keeps the player from leaving the screen.


**15 NOV 2025**

Began coding today by loading my sprite into the main.py code. I fetched them from the repo. I also resized the player sprite to be shaped 40 by 40 px. 

Created a new drawing function that draws the player at their current x and y co ordinates. Added this into the main loop

**16 NOV 2025**

Started creating bullets. First I made a list to hold all active bullets. I then defined the bullet width, height and speed.

Added a new if statement in the main loop to check for key presses. If the SPACE key is pressed, it sets booletX and booletY to the player’s current position.

Used bullets.append to add a new rectangle into the bullet list at the player’s position. This will be used to draw and move bullets in future frames.

Created a new list to update bullets each frame and remove any that go off screen. Looping over bullets, I added b.y += bullet_speed to move each bullet.

Checked if bullet is still on screen (b.y > 0) and added it to the new list if so. Each bullet is drawn as a yellow rectangle.

Fixed bullet direction by changing speed to -7 so bullets go upward. Also added 17 px to bullet X so bullets roughly come out of the center of the player.

**18 NOV 2025**

Added the enemy sprite to the game and loaded it in. Decided to keep the enemy at its default size so it doesn’t get stretched.

Created the draw_enemy() function using the same logic as the player draw function. Cleaned up variable names for consistency (enemy_img).

**20 NOV 2025**

Decided to make sure a single enemy works well before creating a grid of enemies. This will help reduce bugs later.

**23 NOV 2025**

Polished player and bullet mechanics. Confirmed player can move smoothly and stay inside screen boundaries.

bullets spawn correctly from the player and move upward, disappearing when off-screen.

Cleaned up some code for clarity

**27 NOV 2025**

Considered movement patterns and interaction between enemy bullets and the player.

**01 DEC 2025**

Created enemy class including defining the variables and creating a draw function inside the class

Deleted enemy draw function outside the class

Had to fix bug where enemy was drawn as huge

**02 DEC 2025**

Created update function inside of my enemy class that will handle enemy movement and update enemy position.

Added the function into my main loop with the draw function.



