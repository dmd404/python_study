# pong  
<br>

8 parts
- [create the screen](#1-create-the-screen)
- [create and move a paddle](#2--3-create-and-move-a-paddle)
- [create another paddle](#2--3-create-and-move-a-paddle)
  - two-player game
- [create the ball and make it move](#4-create-the-ball-and-make-it-move)
- [detect collision with wall and bounce](#5-detect-collision-with-wall-and-bounce)
- [detect collision with paddle](#6-detect-collision-with-paddle)
- [detect when paddle misses](#7-detect-when-paddle-misses)
- [keep score](#8-keep-score)
---
<br>

# 1. Create the screen
- screen has height of 600 pixels and a width of 800 pixels.
- black backgound color
- stay on the screen until clicked on

# 2 & 3 Create and move a paddle
width = 20  
height = 100  
x_pos = 350  
y_pos = 0  

- up and down arrow key moves the paddle by 20 pixels


# 4. Create the ball and make it move
- created as a separate ball class
- width = 20
- height = 20
- x_pos = 0
- y_pos = 0
- when the screen refreshes the ball moves automatically on the screen
- used time module to slow down the ball's speed


# 5. Detect collision with wall and bounce
- only need to detect collision on the top and bottom walls
  - if the ball hits left or right side edges that means score for the other side

# 6. Detect collision with paddle
- use .distance() method to check
- ball has width of 20 pixels
- paddle has width of 20 pixels
- problem occures when the ball hits off the center
  - distance measure the center of the ball from the center of the paddle
  - solution?
    - if the ball has gone past certain point on x-axis, and within 50 pixels distance




# 7. Detect when paddle misses


# 8. Keep score