init python:
    import random as ran
    global hi_score1
    def _hi_score(hi_score):
        global hi_score1
        hi_score1 = hi_score
    from renpy.audio.sound import play
    class BusMinigameDisplayable(renpy.Displayable):
        global hi_score1
    
        def __init__(self, hi_score):
            renpy.Displayable.__init__(self)
            self.hi_score = hi_score
            self.bus = Image("bus top view.png")
            self.hi_score_bus = 0

            
            background_path = "mg1 road background"+ str(ran.randrange(0, 3)) + ".png"
            self.background = Image(background_path)
            self.ground = Image("mg1 road ground.png")

            self.ground_factor = 7
            self.ground_counter = 0
            self.background_counter = 0 
            self.background_factor = 12

            self.cars= [Image("car1.png"), Image("car2.png"),
                        Image("car3.png"), Image("car4.png"),
                        Image("car5.png"), Image("car6.png")]

            self.car_counter = 0
            self.car_factor = 4

            self.bus_y = 0
            self.bus_y_additional = 15

            self.bus_change_line_max = 15
            self.bus_change_line_counter = self.bus_change_line_max

            self.bus_prev_line = 0
            self.bus_line = 1

            self.cars_sets = [[0], [1, 2], [2], [0, 1], [0, 2], [1], [1, 0], [2, 0], [2, 1], [1, 2], [], [0,2], [1], [2,0], [0], [1], [2], [0,2], [1,2], [], [0,1], [0,1], [1,2], [1,2], [0,1]]

            self.distance_bitween_sets_factor = 2
            self.distance_bitween_sets_step = 0.00005
            self.counters_step = 0.001

            self.count_of_lines = 3

            self.finished = False
            self.first_render = True

            self.score = 0
            self.score_step = 1

        def visit(self):
            return [ self.bus, self.background, self.ground ]

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            ground = renpy.render(self.ground, width, height, st, at)
            ground_duplicate = renpy.render(self.ground, width, height, st, at)

            r.blit(ground, (self.ground_counter * self.ground_factor, (height - ground.height) / 2))
            r.blit(ground_duplicate, (self.ground_counter * self.ground_factor - width, (height - ground.height) / 2))

            background = renpy.render(self.background, width, height, st, at)
            background_duplicate = renpy.render(self.background, width, height, st, at)

            

            
            self.background_counter += 1
            if self.background_counter * self.background_factor >= width:
                self.background_counter = 0

            self.ground_counter += 1
            if self.ground_counter * self.ground_factor >= width:
                self.ground_counter = 0

            t = Transform(child=self.bus, xsize=400, ysize=int(400 * 380 / 1013.0))
            bus = renpy.render(t, width, height, st, at)

            prev_bus_y = (height - ground.height) / 2 + (ground.height / 3 - bus.height) / 2 + self.bus_prev_line * ground.height / 3
            next_bus_y = (height - ground.height) / 2 + (ground.height / 3 - bus.height) / 2 + self.bus_line * ground.height / 3

            bus_y = prev_bus_y + self.bus_change_line_counter / self.bus_change_line_max * (next_bus_y - prev_bus_y)

            if self.bus_change_line_counter + self.car_factor / 5 <= self.bus_change_line_max:
                self.bus_change_line_counter += self.car_factor / 5
            else:
                self.bus_change_line_counter = self.bus_change_line_max

            is_game_finished = False
            distance_bitween_sets = bus.width * self.distance_bitween_sets_factor

            for cars_set_i in range(0, len(self.cars_sets)):
                for car_line_i, indexx in enumerate(self.cars_sets[cars_set_i]):
                    t = Transform(child=self.cars[(car_line_i+2*indexx) % 6], xsize=200, ysize=int(200 * 427 / 844))
                    car = renpy.render(t, width, height, st, at)

                    car_x = (0 if self.first_render else car.width + width / 2) + self.car_counter * self.car_factor - cars_set_i * distance_bitween_sets
                    car_duplicate_x = car_x - distance_bitween_sets * (len(self.cars_sets))

                    car_y = (height - ground.height) / 2 + ((ground.height / 3) - car.height) / 2 + car_line_i * (ground.height / 3)

                    r.blit(car, (car_x, car_y))
                    r.blit(car, (car_duplicate_x, car_y))

                    bus_hitbox_blur_y = bus.height / 15
                    bus_hitbox_blur_x = bus.width / 10

                    if (car_x >= width - bus.width + bus_hitbox_blur_x and car_x <= width - bus_hitbox_blur_x or car_x + car.width >= width - bus.width + bus_hitbox_blur_x and car_x + car.width <= width - bus_hitbox_blur_x) \
                        and (car_y >= bus_y + bus_hitbox_blur_y and car_y <= bus_y + bus.height - bus_hitbox_blur_y or car_y + car.height >= bus_y + bus_hitbox_blur_y and car_y + car.height <= bus_y + bus.height - bus_hitbox_blur_y):
                            self.finished = True

                if cars_set_i == 0 and car_duplicate_x >= car.width + width / 2:
                    self.car_counter = -1
                    self.first_render = False

            r.blit(bus, (width - bus.width, bus_y))

            self.distance_bitween_sets_factor += self.distance_bitween_sets_step
            self.ground_factor += (self.counters_step)
            self.background_factor += (self.counters_step)
            self.car_factor += (self.counters_step)
            self.score += (0.05*self.car_factor)
            #if self.car_counter % 50 == 0:
            #    self.score += round(self.car_factor)

            score_text = Text("Счёт: " + '{0:,}'.format(int(self.score)).replace(',', ' '), slow=False, size=50)
            hi_score_text = Text("Рекорд: " + str(self.hi_score), slow=False, size=50)

            r.blit(background, (self.background_counter * self.background_factor, 0))
            r.blit(background_duplicate, (self.background_counter * self.background_factor - width, 0))

            score_text = renpy.render(score_text, width, height, st, at)
            r.blit(score_text, (width / 10, height / 10-30))

            hi_score_text = renpy.render(hi_score_text, width, height, st, at)
            r.blit(hi_score_text, (width / 10, height / 10 + 30))

            if self.finished:
                play("audio/avaria.mp3")
                renpy.timeout(0)
            else:
                self.car_counter += 1
                renpy.redraw(self, 0.00001)

            return r

        def event(self, ev, x, y, st):
            import pygame

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_DOWN or ev.key == pygame.K_s:
                    if self.bus_change_line_counter == self.bus_change_line_max:
                        self.bus_prev_line = self.bus_line
                        self.bus_change_line_counter = 0
                        self.bus_line = self.bus_line + 1 if self.bus_line + 1 < self.count_of_lines else self.count_of_lines - 1
                        renpy.restart_interaction()
                if ev.key == pygame.K_UP or ev.key == pygame.K_w:
                    if self.bus_change_line_counter == self.bus_change_line_max:
                        self.bus_prev_line = self.bus_line
                        self.bus_change_line_counter = 0
                        self.bus_line = self.bus_line - 1 if self.bus_line - 1 >= 0 else 0
                        renpy.restart_interaction()

            if self.finished:
                return str(int(max(self.score, self.hi_score)))
            else:
                raise renpy.IgnoreEvent()


screen bus(hi_score1):
    default bus_minigame = BusMinigameDisplayable(hi_score1)
    add bus_minigame

label play_bus:
    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    image white = "#fff"

    scene white
    with dissolve
    screen my_screen():
        text "Управление стрелочками вверх и вниз\nТапами на верхние и нижние части экрана" xalign 0.5 yalign 0.5 color "#000"
    show screen my_screen with dissolve
    pause(2.0)
    hide screen my_screen with dissolve
    call screen bus(0)
    $ hi_score = _return 
    with fade

    $ quick_menu = True
    window show
    