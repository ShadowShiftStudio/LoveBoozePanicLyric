init python:
    SECONDS_PER_UPDATE = 1 / 120

    class Shift():
        def __init__(self, step):
            self.value = 0
            self.step = step

        def tick(self, bound):
            if self.value + self.step > bound:
                self.value = 0
            else:
                self.value += self.step
            
            return self.value

        def val(self): return self.value

        def update_step(self, new_step):
            self.step = new_step

    class PercentCounter():
        def __init__(self, step, default_value=0, reset_at_end=True):
            self.step = step
            self.value = default_value
            self.reset_at_end = reset_at_end
        
        def next(self):
            if self.step + self.value > 100:
                self.value = 0 if self.reset_at_end else 100
                return False 
            else:
                self.value += self.step
                return True

        def percent_val(self):
            return self.value / 100.0

        def reset(self):
            self.value = 0

        def update_step(self, step):
            self.step = step

    class Background():
        def __init__(self, speed, textures_index):
            self.image = Image(f"mg1 road background{textures_index}.png")
            self.shift_step_factor = 3
            self.shift = Shift(self.shift_step_factor * speed)

        def visit(self):
            return self.image

        def render(self, r, width, height, st, at):
            background = renpy.render(self.image, width, height, st, at)
            shift_value = self.shift.tick(width)

            r.blit(background, (shift_value, 0))
            r.blit(background, (shift_value - width, 0))

            return r

        def update_speed(self, speed):
            self.speed = speed
            self.shift.update_step(self.shift_step_factor * speed)

    class Road():
        def __init__(self, speed):
            self.image = Image("mg1 road ground.png")
            self.shift_step_factor = 3.5
            self.shift = Shift(self.shift_step_factor * speed)
            self.rendered = None
            self.__ypos = 0

        def visit(self):
            return self.image

        def render(self, r, width, height, st, at):
            self.rendered = renpy.render(self.image, width, height, st, at)
            shift_value = self.shift.tick(width)

            self.__ypos = (height - self.rendered.height) / 2

            r.blit(self.rendered, (shift_value, self.__ypos))
            r.blit(self.rendered, (shift_value - width, self.__ypos))

        def ypos(self):
            return self.__ypos

        def height(self):
            return self.rendered.height if self.rendered != None else 0

        def xpos(self): return self.shift.val()

        def update_speed(self, speed):
            self.speed = speed
            self.shift.update_step(3.5 * speed)

    class CarsLine():
        def __init__(self, speed, road):
            import random

            self.road = road
            self.count_of_tracks = 3
            self.zoom_factor = 0.7
            self.shift_step_factor = 2
            self.shift = Shift(self.shift_step_factor * speed)
            self.__xpos = 0
            self.max_car_width = 0

            self.cars = [None] * self.count_of_tracks

            for _ in range(0, self.count_of_tracks - 1):
                pos = random.randrange(0, self.count_of_tracks)
                if self.cars[pos] == None:
                    self.cars[pos] = Image(f"car{random.randrange(1, 7)}.png")

            self.cars_rects = [None] * self.count_of_tracks
        
        def render(self, r, width, height, st, at):
            shift_value = self.shift.tick(width + self.max_car_width)
            if shift_value == 0: return False
            self.__xpos = shift_value

            for track_i in range(0, self.count_of_tracks):
                if self.cars[track_i] == None: continue

                car_transformed = Transform(self.cars[track_i], zoom=self.zoom_factor)
                car = renpy.render(car_transformed, width, height, st, at)
                xpos = shift_value - car.width
                ypos = self.road.ypos() + (self.road.height() / 3 - car.height) / 2 + self.road.height() * track_i / 3
                r.blit(car, (xpos, ypos))

                if car.width > self.max_car_width: self.max_car_width = car.width
                self.cars_rects[track_i] = Rect(car.width, car.height, xpos, ypos)

            return True

        def xpos(self): return self.__xpos

        def is_intersect(self, rect):
            for car_rect in self.cars_rects:
                if car_rect != None and rect.is_intersect(car_rect):
                    return True

            return False

        def update_speed(self, speed):
            self.speed = speed
            self.shift.update_step(self.shift_step_factor * speed)

    class Cars():
        def __init__(self, speed, road):
            import math

            self.road = road
            self.speed = speed
            self.distance_counter = PercentCounter(self.calc_distance_step(speed))
            self.lines = [CarsLine(speed, road)]

        def calc_distance_step(self, speed):
            return 0.25 + 0.03*speed

        def render(self, r, width, height, st, at):
            for line_i in range(0, len(self.lines)):
                line = self.lines[line_i]
                is_available = line.render(r, width, height, st, at)

                if not is_available:
                    self.lines[line_i] = None

            filtered_lines = []
            for line in self.lines:
                if line != None:
                    filtered_lines.append(line)
            self.lines = filtered_lines

            if not self.distance_counter.next():
                self.lines.insert(0, CarsLine(self.speed, self.road))

        def update_speed(self, speed):
            self.speed = speed
            self.distance_counter.update_step(self.calc_distance_step(speed))

            for line in self.lines:
                if line != None:
                    line.update_speed(speed)

        def is_intersect(self, rect):
            for line in self.lines:
                if line.is_intersect(rect):
                    return True

            return False

    class Rect():
        def __init__(self, width, height, xpos, ypos, constriction_factor = 0):
            self.width = width
            self.height = height
            self.xpos = xpos
            self.ypos = ypos
            self.x_constriction = width * constriction_factor
            self.y_constriction = height * constriction_factor

        def is_point_intersect(self, x, y):
            return x > self.xpos + self.x_constriction and x < self.xpos + self.width - self.x_constriction \
                    and y > self.ypos + self.y_constriction and y < self.ypos + self.height - self.y_constriction

        def is_intersect(self, other):
            return self.is_point_intersect(other.xpos, other.ypos) \
                or self.is_point_intersect(other.xpos, other.ypos + other.height) \
                or self.is_point_intersect(other.xpos + other.width, other.ypos + other.height) \
                or self.is_point_intersect(other.xpos + other.width, other.ypos)

    class Bus():
        def __init__(self, speed, road, cars):
            self.road = road
            self.cars = cars
            self.image = Image("bus top view.png")
            self.prev_track_i = 1
            self.curr_track_i = 1
            self.counter_step_factor = 1.2
            self.track_counter = PercentCounter(speed * self.counter_step_factor, 100, False)
            self.max_track_index = 2

        def update_speed(self, speed):
            self.speed = speed
            self.track_counter.update_step(self.counter_step_factor * speed)

        def render(self, r, width, height, st, at):
            transformed_bus = Transform(self.image, zoom=0.38)
            bus = renpy.render(transformed_bus, width, height, st, at)

            ypos = self.road.ypos() + (self.road.height() / 3 - bus.height) / 2 + (self.prev_track_i + (self.curr_track_i - self.prev_track_i) * self.track_counter.percent_val()) * self.road.height() / 3
            xpos = width - bus.width

            r.blit(bus, (xpos, ypos))
            self.track_counter.next()

            return self.cars.is_intersect(Rect(bus.width, bus.height, xpos, ypos, 0.1))

        def __change_track(self, track_i):
            if track_i >= 0 and track_i <= self.max_track_index and track_i != self.curr_track_i and self.track_counter.percent_val() == 1:
                self.prev_track_i = self.curr_track_i
                self.curr_track_i = track_i
                self.track_counter.reset()
        
        def increase_track(self):
            if self.curr_track_i + 1 <= self.max_track_index:
                self.__change_track(self.curr_track_i + 1)

        def decrease_track(self):
            if self.curr_track_i - 1 >= 0:
                self.__change_track(self.curr_track_i - 1)
    
    class SurrenderBtn(renpy.Displayable):
        def __init__(self, on_click):
            renpy.Displayable.__init__(self)
            self.image = Image("surrender btn.png")

            self.on_click = on_click
            self.rect = None

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            btn = renpy.render(self.image, width, height, st, at)
            r.blit(btn, (0, 0))

            self.rect = Rect(btn.width, btn.height, 0, 0)

            return r

        def event(self, ev, x, y, st):
            import pygame as pg

            if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1 and self.rect != None and self.rect.is_point_intersect(x, y):
                self.on_click()

    class BusMinigameDisplayable(renpy.Displayable):
        def __init__(self, high_score, textures_index):
            renpy.Displayable.__init__(self)

            self.high_score = high_score
            self.score = 0
            self.score_step = 1
            self.score_increase_timer = PercentCounter(10)

            self.speed = 2

            self.prev_time = None
            self.background = Background(self.speed, textures_index)
            self.road = Road(self.speed)
            self.cars = Cars(self.speed, self.road)
            self.bus = Bus(self.speed, self.road, self.cars)
            self.surrender_btn = SurrenderBtn(self.surrender)

            self.finished = False

        def surrender(self):
            self.finished = True
            renpy.timeout(0)

        def render(self, width, height, st, at):
            import time 
            curr_time = time.time()
            elepsed = curr_time - (self.prev_time if self.prev_time != None else 0)
            self.prev_time = curr_time

            r = renpy.Render(width, height)
            self.road.render(r, width, height, st, at)
            self.cars.render(r, width, height, st, at)
            self.finished = self.bus.render(r, width, height, st, at)
            self.background.render(r, width, height, st, at)

            self.score_increase_timer.next()
            if self.score_increase_timer.percent_val() == 0:
                self.score += self.score_step
                self.speed += self.score_step / 250

                self.road.update_speed(self.speed)
                self.background.update_speed(self.speed)
                self.cars.update_speed(self.speed)
                self.bus.update_speed(self.speed)

                if self.score > self.high_score:
                    self.high_score = self.score

            score_text = Text("Счёт: " + '{0:,}'.format(int(self.score)).replace(',', ' '), slow=False, size=50)
            score_text = renpy.render(score_text, width, height, st, at)

            high_score_text = Text("Рекорд: " + str(self.high_score), slow=False, size=50)
            high_score_text = renpy.render(high_score_text, width, height, st, at)

            r.blit(score_text, (width / 10, height / 10-30))
            r.blit(high_score_text, (width / 10, height / 10 + 30))

            surrender_btn = renpy.render(self.surrender_btn, width, height, st, at)
            r.blit(surrender_btn, (width / 100, width / 50))

            if self.finished:
                renpy.timeout(0)
            else:
                renpy.redraw(self, SECONDS_PER_UPDATE - elepsed if elepsed < SECONDS_PER_UPDATE else 0)

            return r

        def event(self, ev, x, y, st):
            import pygame

            self.surrender_btn.event(ev, x, y, st)

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_DOWN or ev.key == pygame.K_s:
                    self.bus.increase_track()
                    renpy.restart_interaction()
                if ev.key == pygame.K_UP or ev.key == pygame.K_w:
                    self.bus.decrease_track()
                    renpy.restart_interaction()

            if self.finished:
                return str(self.score if self.score > self.high_score else self.high_score)
            else:
                raise renpy.IgnoreEvent()

screen bus():
    default bus_minigame = BusMinigameDisplayable(1000, 1)
    add bus_minigame

label play_bus:
    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    image white = "#fff"

    scene white
    with dissolve
    screen my_screen():
        text "Управление стрелочками вверх и вниз" xalign 0.5 yalign 0.5 color "#000"
    show screen my_screen with dissolve
    pause(2.0)
    hide screen my_screen with dissolve
    call screen bus 
    with fade

    $ quick_menu = True
    window show
    