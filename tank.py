from random import randint

#  changeable battlefield measurements
battlefield_setting = 20
t = int(battlefield_setting/2)
s = (["North", "N", "straight"], ["East", "E", "right"], ["South", "S", "back"], ["West", "W", "left"])


class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hits = 0
        self.points = 0
        self.foe1_x = randint(-t, t)
        self.foe1_y = randint(-t, t)
        self.foe2_x = randint(-t, t)
        self.foe2_y = randint(-t, t)
        self.foe3_x = randint(-t, t)
        self.foe3_y = randint(-t, t)
        self.shots = {s[0][0]: 0, s[1][0]: 0, s[2][0]: 0, s[3][0]: 0}
        self.direction = s[0][0]  # North

    # --------------------------------------------------------------------
    # management gear
    def straight(self):
        self.y += 1
        self.direction = s[0][0]  # North
        self.points -= 1

    def right(self):
        self.x += 1
        self.direction = s[1][0]  # East
        self.points -= 1

    def back(self):
        self.y -= 1
        self.direction = s[2][0]  # South
        self.points -= 1

    def left(self):
        self.x -= 1
        self.direction = s[3][0]  # West
        self.points -= 1
    # management gear
    # --------------------------------------------------------------------

    # a description of the targeting situation ###########################
    def check_shot1(self):
        if self.x == self.foe1_x and self.direction == s[0][0] and self.y < self.foe1_y:  # North
            return True
        if self.y == self.foe1_y and self.direction == s[1][0] and self.x < self.foe1_x:  # East
            return True
        if self.x == self.foe1_x and self.direction == s[2][0] and self.y > self.foe1_y:  # South
            return True
        if self.y == self.foe1_y and self.direction == s[3][0] and self.x > self.foe1_x:  # West
            return True
        return False

    def check_shot2(self):
        if self.x == self.foe2_x and self.direction == s[0][0] and self.y < self.foe2_y:  # North
            return True
        if self.y == self.foe2_y and self.direction == s[1][0] and self.x < self.foe2_x:  # East
            return True
        if self.x == self.foe2_x and self.direction == s[2][0] and self.y > self.foe2_y:  # South
            return True
        if self.y == self.foe2_y and self.direction == s[3][0] and self.x > self.foe2_x:  # West
            return True
        return False

    def check_shot3(self):
        if self.x == self.foe3_x and self.direction == s[0][0] and self.y < self.foe3_y:  # North
            return True
        if self.y == self.foe3_y and self.direction == s[1][0] and self.x < self.foe3_x:  # East
            return True
        if self.x == self.foe3_x and self.direction == s[2][0] and self.y > self.foe3_y:  # South
            return True
        if self.y == self.foe3_y and self.direction == s[3][0] and self.x > self.foe3_x:  # West
            return True
        return False

    # getting results #####################################################
    def shot(self):
        self.shots[self.direction] += 1
        if self.check_shot1():
            print("\033[1;30;101m              first Foe  HIT !!!!      ")  # red color background
            print("\033[0m")
            self.hits += 1
            self.points += 5
            self.foe1_x = randint(-t, t)
            self.foe1_y = randint(-t, t)
        elif self.check_shot2():
            print("\033[1;30;103m             second Foe HIT !!!!      ")  # yellow color background
            print("\033[0m")
            self.hits += 1
            self.points += 5
            self.foe2_x = randint(-t, t)
            self.foe2_y = randint(-t, t)
        elif self.check_shot3():
            print("\033[1;30;104m            third Foe   HIT !!!!     ")  # blue color background
            print("\033[0m")
            self.hits += 1
            self.points += 5
            self.foe3_x = randint(-t, t)
            self.foe3_y = randint(-t, t)

    # --------------------------------------------------------------------
    # battlefield
    def battlefield(self):
        # drawing y-axis frontend
        for y in range(-t, t+1)[::-1]:
            for x in range(-t, t+1):
                # drawing x-axis frontend
                if x == self.x and y == self.y:  # main object
                    print("\033[1;100;38;2;13;7;7m X \033[0m", end="")
                elif x == self.foe1_x and y == self.foe1_y:  # define 1st target with colored fonts (red)
                    print("\033[1;100;38;2;148;23;23m 1 \033[0m", end="")
                elif x == self.foe2_x and y == self.foe2_y:  # define 2nd target with colored fonts (yellow)
                    print("\033[1;100;38;2;183;135;37m 2 \033[0m", end="")
                elif x == self.foe3_x and y == self.foe3_y:  # define 3rd target with colored fonts (blue)
                    print("\033[1;100;38;2;41;42;160m 3 \033[0m", end="")
                elif x == 0:
                    print("\033[100m ▫ \033[0m", end="")
                elif y == 0:
                    print("\033[100m ▫ \033[0m", end="")
                else:
                    print("\033[100m · \033[0m", end="")
            print()
    # battlefield
    # --------------------------------------------------------------------

    def battle_end(self):
        if self.points <= -50:
            return True
        return False

    # define frontend #####################################################
    def info(self):
        print(f"Tank position -- x: {self.x}, y: {self.y}, direction: {self.direction}, "
              f"shots: {sum(self.shots.values())}")
        print(f"First foe position -- x: {self.foe1_x}, y: {self.foe1_y}")
        print(f"Second foe position -- x: {self.foe2_x}, y: {self.foe2_y}")
        print(f"Third foe position -- x: {self.foe3_x}, y: {self.foe3_y}")
        print(f"hits: {self.hits}, points: {self.points}")
