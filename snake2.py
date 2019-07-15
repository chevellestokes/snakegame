import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint


def Easy():
    WIDTH = 35
    HEIGHT = 20
    MAX_X = WIDTH - 2
    MAX_Y = HEIGHT - 2
    SNAKE_LENGTH = 5
    SNAKE_X = SNAKE_LENGTH + 1
    SNAKE_Y = 3
    Speed = 150

    class Snake(object):
        REV_DIR_MAP = {
            KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
        }

        def __init__(self, x, y, window):
            self.body_list = []
            self.hit_score = 0
            self.timeout = Speed

            for i in range(SNAKE_LENGTH, 0, -1):
                self.body_list.append(Body(x - i, y))

            self.body_list.append(Body(x, y, '{'))
            self.window = window
            self.direction = KEY_RIGHT
            self.last_head_coor = (x, y)
            self.direction_map = {
                KEY_UP: self.move_up,
                KEY_DOWN: self.move_down,
                KEY_LEFT: self.move_left,
                KEY_RIGHT: self.move_right
            }

        @property
        def score(self):
            return "Chevelle's game / your Score : {}".format(self.hit_score)

        def add_body(self, body_list):
            self.body_list.extend(body_list)

        def eat_food(self, food):
            food.reset()
            body = Body(self.last_head_coor[0], self.last_head_coor[1])
            self.body_list.insert(-1, body)
            self.hit_score += 1
            if self.hit_score % 1 == 0:
                self.timeout -= 10
                self.window.timeout(self.timeout)

        @property
        def collided(self):
            return any([body.coor == self.head.coor
                        for body in self.body_list[:-1]])

        def update(self):
            last_body = self.body_list.pop(0)
            last_body.x = self.body_list[-1].x
            last_body.y = self.body_list[-1].y
            self.body_list.insert(-1, last_body)
            self.last_head_coor = (self.head.x, self.head.y)
            self.direction_map[self.direction]()

        def change_direction(self, direction):
            if direction != Snake.REV_DIR_MAP[self.direction]:
                self.direction = direction

        def render(self):
            for body in self.body_list:
                self.window.addstr(body.y, body.x, body.char)

        @property
        def head(self):
            return self.body_list[-1]

        @property
        def coor(self):
            return self.head.x, self.head.y

        def move_up(self):
            self.head.y -= 1
            if self.head.y < 1:
                self.head.y = MAX_Y

        def move_down(self):
            self.head.y += 1
            if self.head.y > MAX_Y:
                self.head.y = 1

        def move_left(self):
            self.head.x -= 1
            if self.head.x < 1:
                self.head.x = MAX_X

        def move_right(self):
            self.head.x += 1
            if self.head.x > MAX_X:
                self.head.x = 1

    class Body(object):
        def __init__(self, x, y, char='E'):
            self.x = x
            self.y = y
            self.char = char

        @property
        def coor(self):
            return self.x, self.y

    class Food(object):
        def __init__(self, window, char='$'):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
            self.char = char
            self.window = window

        def render(self):
            self.window.addstr(self.y, self.x, self.char)

        def reset(self):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
    def letsstart():

        if __name__ == '__main__':
            curses.initscr()
            curses.beep()
            curses.beep()
            window = curses.newwin(HEIGHT, WIDTH, 0, 0)
            window.timeout(Speed)
            window.keypad(1)
            curses.noecho()
            curses.curs_set(0)
            window.border(0)

            snake = Snake(SNAKE_X, SNAKE_Y, window)
            food = Food(window, "$")
            

            while True:
                window.clear()
                window.border(0)
                snake.render()
                food.render()
                

                window.addstr(0, 5, snake.score)
                event = window.getch()

                if event == 27:
                    break

                if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                    snake.change_direction(event)

                if snake.head.x == food.x and snake.head.y == food.y:
                    snake.eat_food(food)

                if event == 32:
                    key = -1
                    while key != 32:
                        key = window.getch()

                


                snake.update()
                if snake.collided:
                    break

        curses.endwin()
    print("info: READ THE RULES")
    input("its the easy mode you should be able to handle it/ $ this symbol is your food you should eat it ")
    letsstart()
def Medium(): 
    WIDTH = 35
    HEIGHT = 20
    MAX_X = WIDTH - 2
    MAX_Y = HEIGHT - 2
    SNAKE_LENGTH = 5
    SNAKE_X = SNAKE_LENGTH + 1
    SNAKE_Y = 3
    Speed = 65

    class Snake(object):
        REV_DIR_MAP = {
            KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
        }

        def __init__(self, x, y, window):
            self.body_list = []
            self.hit_score = 0
            self.timeout = Speed

            for i in range(SNAKE_LENGTH, 0, -1):
                self.body_list.append(Body(x - i, y))

            self.body_list.append(Body(x, y, '<'))
            self.window = window
            self.direction = KEY_RIGHT
            self.last_head_coor = (x, y)
            self.direction_map = {
                KEY_UP: self.move_up,
                KEY_DOWN: self.move_down,
                KEY_LEFT: self.move_left,
                KEY_RIGHT: self.move_right
            }

        @property
        def score(self):
            return "Chevelle's game / your Score : {}".format(self.hit_score)

        def add_body(self, body_list):
            self.body_list.extend(body_list)

        def eat_food(self, food):
            food.reset()
            body = Body(self.last_head_coor[0], self.last_head_coor[1])
            self.body_list.insert(-1, body)
            self.hit_score += 1
            if self.hit_score % 1 == 0:
                self.timeout -= 15
                self.window.timeout(self.timeout)

        @property
        def collided(self):
            return any([body.coor == self.head.coor
                        for body in self.body_list[:-1]])

        def update(self):
            last_body = self.body_list.pop(0)
            last_body.x = self.body_list[-1].x
            last_body.y = self.body_list[-1].y
            self.body_list.insert(-1, last_body)
            self.last_head_coor = (self.head.x, self.head.y)
            self.direction_map[self.direction]()

        def change_direction(self, direction):
            if direction != Snake.REV_DIR_MAP[self.direction]:
                self.direction = direction

        def render(self):
            for body in self.body_list:
                self.window.addstr(body.y, body.x, body.char)

        @property
        def head(self):
            return self.body_list[-1]

        @property
        def coor(self):
            return self.head.x, self.head.y

        def move_up(self):
            self.head.y -= 1
            if self.head.y < 1:
                self.head.y = MAX_Y

        def move_down(self):
            self.head.y += 1
            if self.head.y > MAX_Y:
                self.head.y = 1

        def move_left(self):
            self.head.x -= 1
            if self.head.x < 1:
                self.head.x = MAX_X

        def move_right(self):
            self.head.x += 1
            if self.head.x > MAX_X:
                self.head.x = 1

    class Body(object):
        def __init__(self, x, y, char='='):
            self.x = x
            self.y = y
            self.char = char

        @property
        def coor(self):
            return self.x, self.y

    class obstacle(object):
        def __init__(self, window, char="#"):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
            self.char = char
            self.window = window

        def render(self):
            self.window.addstr(self.y, self.x, self.char)

        def reset(self):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)

    class Food(object):
        def __init__(self, window, char='&'):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
            self.char = char
            self.window = window

        def render(self):
            self.window.addstr(self.y, self.x, self.char)

        def reset(self):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
    def letsstart():

        if __name__ == '__main__':
                    curses.initscr()
                    curses.beep()
                    curses.beep()
                    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
                    window.timeout(Speed)
                    window.keypad(1)
                    curses.noecho()
                    curses.curs_set(0)
                    window.border(0)

                    snake = Snake(SNAKE_X, SNAKE_Y, window)
                    food = Food(window, "&")
                    obstacl = obstacle(window, "#")

                    while True:
                        window.clear()
                        window.border(0)
                        snake.render()
                        food.render()
                        obstacl.render()
                        obstacl.render()
                        
                        window.addstr(0, 5, snake.score)
                        event = window.getch()

                        if event == 27:
                            break

                        if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                            snake.change_direction(event)

                        if snake.head.x == food.x and snake.head.y == food.y:
                            snake.eat_food(food)

                        if event == 32:
                            key = -1
                            while key != 32:
                                key = window.getch()

                        if snake.head.x == obstacl.x and snake.head.y == obstacl.y:
                            break


                        snake.update()
                        if snake.collided:
                            break
        curses.endwin()
    print("info: READ THE RULES")
    input("its kinda faster/ dont touch yourself/ # this symbol kills you if you touch itx / & this symbol is your food you should eat it ")
    letsstart()
def Hard():
    WIDTH = 35
    HEIGHT = 20
    MAX_X = WIDTH - 2
    MAX_Y = HEIGHT - 2
    SNAKE_LENGTH = 5
    SNAKE_X = SNAKE_LENGTH + 1
    SNAKE_Y = 3
    Speed = 35
    
    class Snake(object):
        REV_DIR_MAP = {
            KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
        }

        def __init__(self, x, y, window):
            self.body_list = []
            self.hit_score = 0
            self.timeout = Speed

            for i in range(SNAKE_LENGTH, 0, -1):
                self.body_list.append(Body(x - i, y))

            self.body_list.append(Body(x, y, '`'))
            self.window = window
            self.direction = KEY_RIGHT
            self.last_head_coor = (x, y)
            self.direction_map = {
                KEY_UP: self.move_up,
                KEY_DOWN: self.move_down,
                KEY_LEFT: self.move_left,
                KEY_RIGHT: self.move_right
            }

        @property
        def score(self):
            return "Chevelle's game / your Score : {}".format(self.hit_score)

        def add_body(self, body_list):
            self.body_list.extend(body_list)

        def eat_food(self, food):
            food.reset()
            body = Body(self.last_head_coor[0], self.last_head_coor[1])
            self.body_list.insert(-1, body)
            self.hit_score += 1
            if self.hit_score % 1 == 0:
                self.timeout -= 5
                self.window.timeout(self.timeout)

        @property
        def collided(self):
            return any([body.coor == self.head.coor
                        for body in self.body_list[:-1]])
        
        def update(self):
            last_body = self.body_list.pop(0)
            last_body.x = self.body_list[-1].x
            last_body.y = self.body_list[-1].y
            self.body_list.insert(-1, last_body)
            self.last_head_coor = (self.head.x, self.head.y)
            self.direction_map[self.direction]()

        def change_direction(self, direction):
            if direction == Snake.REV_DIR_MAP[self.direction]:
                exit()
            elif direction != Snake.REV_DIR_MAP[self.direction]:
                self.direction = direction

        def render(self):
            for body in self.body_list:
                self.window.addstr(body.y, body.x, body.char)

        @property
        def head(self):
            return self.body_list[-1]

        @property
        def coor(self):
            return self.head.x, self.head.y

        def move_up(self):
            self.head.y -= 1
            if self.head.y < 1:
                self.head.y = MAX_Y

        def move_down(self):
            self.head.y += 1
            if self.head.y > MAX_Y:
                self.head.y = 1

        def move_left(self):
            self.head.x -= 1
            if self.head.x < 1:
                self.head.x = MAX_X

        def move_right(self):
            self.head.x += 1
            if self.head.x > MAX_X:
                self.head.x = 1

    class Body(object):
        def __init__(self, x, y, char='.'):
            self.x = x
            self.y = y
            self.char = char

        @property
        def coor(self):
            return self.x, self.y
    class obstacle(object):
        def __init__(self, window, char="#    #      #     #"):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
            self.char = char
            self.window = window

        def render(self):
            self.window.addstr(self.y, self.x, self.char)

        def reset(self):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
    class Food(object):
        def __init__(self, window, char="'"):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
            self.char = char
            self.window = window

        def render(self):
            self.window.addstr(self.y, self.x, self.char)

        def reset(self):
            self.x = randint(1, MAX_X)
            self.y = randint(1, MAX_Y)
    def letsstart():

        if __name__ == '__main__':
            curses.initscr()
            curses.beep()
            curses.beep()
            window = curses.newwin(HEIGHT, WIDTH, 0, 0)
            window.timeout(Speed)
            window.keypad(1)
            curses.noecho()
            curses.curs_set(0)
            window.border(0)

            snake = Snake(SNAKE_X, SNAKE_Y, window)
            food = Food(window, "'")
            obstacl = obstacle(window, "#     #      #    #")

            while True:
                window.clear()
                window.border(0)
                snake.render()
                food.render()
                obstacl.render()
                

                window.addstr(0, 5, snake.score)
                event = window.getch()

                if event == 27:
                    break

                if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                    snake.change_direction(event)

                if snake.head.x == food.x and snake.head.y == food.y:
                    snake.eat_food(food)

                if event == 32:
                    key = -1
                    while key != 32:
                        key = window.getch()

                if snake.head.x == obstacl.x and snake.head.y == obstacl.y:
                    break
                

                snake.update()
                if snake.collided:
                    break

            curses.endwin()
    print("info: READ THE RULES")
    input("its faster/ dont go back on your self/ dont touch yourself/ # this symbol kills you if you touch itx / ' this symbol is your food you should eat it/ maximise your window ")
    letsstart()
def mode():
    while True:
        print("what mode you want to play on? hard (h),easy(e),medium(m)(case matters): ")
        mode = input().lower()
        if mode in "hard h easy e medium m".split():
            return mode 
        else:
            print("really? i just asked if you was ready. you good?")
mode = mode()
def Themode(mode):
    if mode[0] == "h":
        
        Hard()
    elif mode[0] == "e":
        Easy()
    elif mode[0] == "m":
        Medium()
    
    else:
        print("nope")

name = input("what is your name? :")
print("wassup " + name)
ready = input("are you ready? type YES or NO (uppercase matters): ")
if ready != "YES":
    print("come back when your ready")
else:
     Themode(mode)







