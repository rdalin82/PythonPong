# Implementation of classic arcade game Pong

import simpleguitk as simplegui

import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_pos = [HEIGHT/2, (HEIGHT/2)-PAD_HEIGHT] 
paddle2_pos = [HEIGHT/2, (HEIGHT/2)-PAD_HEIGHT]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
PADDLE_LENGTH = paddle1_pos[0] - paddle1_pos[1]
score1 = 0
score2 = 0
color = "Black"
counter = 0
speeds = 100


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global color

    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 150)/90.0
        ball_vel[1] = random.randrange(50, 90)/50.0*-1
        
    elif direction == LEFT:
        ball_vel[0] = random.randrange(120, 150)*-1/90.0
        ball_vel[1] = random.randrange(50, 90)/50.0*-1 
   
    
# Timer handler
def tick():
    global color
    if color == 'Black':
       color = "Red"

    else:
       stop() 
       color = "Black"
        
    frame.set_canvas_background(color)

def start():
    timer.start()
    
def stop():
    timer.stop()
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global ball_pos
    global score1, score2  # these are ints
    ball_pos = [WIDTH/2, HEIGHT/2]
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, color
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= (PAD_WIDTH)+ BALL_RADIUS:
        if ball_pos[1] < paddle1_pos[0] and ball_pos[1] > paddle1_pos[1]:
           ball_vel[0] = - ball_vel[0] -(ball_vel[0]*0.1)
        else:
            ball_pos = [WIDTH/2, HEIGHT/2]
            spawn_ball(RIGHT)
            score2 += 1
            start()
            

    if ball_pos[0] >= (WIDTH-PAD_WIDTH) - BALL_RADIUS:
        if ball_pos[1] < paddle2_pos[0] and ball_pos[1] > paddle2_pos[1]:
            ball_vel[0] = - ball_vel[0] - (ball_vel[0]*0.1)
        else:
            ball_pos = [WIDTH/2, HEIGHT/2]
            spawn_ball(LEFT)
            score1 += 1
            start()
            
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # draw ball
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 2, "Blue", "White")
    # update paddle's vertical position, keep paddle on the screen
#paddle 1    
    if paddle1_vel[0] > 0:
        
        if paddle1_pos[0] <= HEIGHT-1:
             paddle1_pos[0] += paddle1_vel[0]
             paddle1_pos[1] += paddle1_vel[1]
        else: 
             paddle1_pos[0] -= paddle1_vel[0]
             paddle1_pos[1] -= paddle1_vel[1]
    else: 
        paddle1_pos[0] += paddle1_vel[0]
        paddle1_pos[1] += paddle1_vel[1]
    
    if paddle1_pos[1] >= 0+1:
        paddle1_pos[0] += paddle1_vel[0]
        paddle1_pos[1] += paddle1_vel[1]
    else: 
        paddle1_pos[0] -= paddle1_vel[0]
        paddle1_pos[1] -= paddle1_vel[1]
#paddle 2
    if paddle2_vel[0] > 0:
        
        if paddle2_pos[0] <= HEIGHT-1:
             paddle2_pos[0] += paddle2_vel[0]
             paddle2_pos[1] += paddle2_vel[1]
        else: 
             paddle2_pos[0] -= paddle2_vel[0]
             paddle2_pos[1] -= paddle2_vel[1]
    else: 
        paddle2_pos[0] += paddle2_vel[0]
        paddle2_pos[1] += paddle2_vel[1]
    
    if paddle2_pos[1] >= 0+1:
        paddle2_pos[0] += paddle2_vel[0]
        paddle2_pos[1] += paddle2_vel[1]
    else: 
        paddle2_pos[0] -= paddle2_vel[0]
        paddle2_pos[1] -= paddle2_vel[1]
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos[0]], [HALF_PAD_WIDTH, paddle1_pos[1]], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH, paddle2_pos[0]], [WIDTH-HALF_PAD_WIDTH, paddle2_pos[1]], PAD_WIDTH, "White")
    
    # draw scores
    canvas.draw_text("Left Player: " + str(score1), (100, 40), 20, "Red") 
    canvas.draw_text("Right Player: " + str(score2), (325, 40), 20, "Red")
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
         if (paddle1_pos + paddle1_vel) >= PAD_HEIGHT:

            paddle1_vel[0] -= 2
            paddle1_vel[1] -= 2
            
    elif key == simplegui.KEY_MAP["s"]:
        if (paddle1_pos + paddle1_vel) >= PAD_HEIGHT:
            paddle1_vel[0] += 2
            paddle1_vel[1] += 2

    if key == simplegui.KEY_MAP["up"]:
         if (paddle2_pos + paddle2_vel) >= PAD_HEIGHT:

            paddle2_vel[0] -= 2
            paddle2_vel[1] -= 2
            
    elif key == simplegui.KEY_MAP["down"]:
        if (paddle2_pos + paddle2_vel) >= PAD_HEIGHT:
            paddle2_vel[0] += 2
            paddle2_vel[1] += 2
   
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] = 0
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] = 0
        paddle1_vel[1] = 0
        
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] = 0
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] = 0
        paddle2_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background(color)
timer = simplegui.create_timer(speeds, tick)

# start frame
new_game()
frame.start()
