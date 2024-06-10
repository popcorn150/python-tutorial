import curses
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)

# Screen dimensions
sh, sw = stdscr.getmaxyx()

# Paddle properties
paddle_y = sh - 1
paddle_x = sw // 2
paddle_w = 10

# Ball properties
ball_y, ball_x = sh // 2, sw // 2
ball_dy, ball_dx = -1, -1

# Brick properties
brick_w = 5
brick_h = 1
bricks = [(y, x) for y in range(5) for x in range(0, sw, brick_w + 1)]

# Draw bricks
def draw_bricks():
    for y, x in bricks:
        stdscr.addstr(y, x, "#####")

# Draw paddle
def draw_paddle():
    stdscr.addstr(paddle_y, paddle_x, " " * paddle_w)
    stdscr.addstr(paddle_y, paddle_x, "P" * paddle_w)

# Draw ball
def draw_ball():
    stdscr.addstr(ball_y, ball_x, "O")

# Clear ball
def clear_ball():
    stdscr.addstr(ball_y, ball_x, " ")

# Main game loop
while True:
    stdscr.clear()
    draw_bricks()
    draw_paddle()
    draw_ball()
    stdscr.refresh()
    
    # Move the paddle
    key = stdscr.getch()
    if key == curses.KEY_LEFT and paddle_x > 0:
        paddle_x -= 1
    elif key == curses.KEY_RIGHT and paddle_x < sw - paddle_w:
        paddle_x += 1
    
    # Move the ball
    clear_ball()
    ball_y += ball_dy
    ball_x += ball_dx
    
    # Check for collision with walls
    if ball_x <= 0 or ball_x >= sw - 1:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy
    
    # Check for collision with paddle
    if ball_y == paddle_y - 1 and paddle_x <= ball_x < paddle_x + paddle_w:
        ball_dy = -ball_dy
    
    # Check for collision with bricks
    for brick in bricks:
        by, bx = brick
        if by == ball_y and bx <= ball_x < bx + brick_w:
            ball_dy = -ball_dy
            bricks.remove(brick)
            break
    
    # Check for game over
    if ball_y >= sh - 1:
        stdscr.addstr(sh // 2, sw // 2 - 5, "Game Over")
        stdscr.refresh()
        stdscr.nodelay(0)
        stdscr.getch()
        break
    
    curses.napms(50)

# Clean up
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()