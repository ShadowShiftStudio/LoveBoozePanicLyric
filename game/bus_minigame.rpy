init python:
    class BusMinigameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.bus = Image("bus top view.png")

            self.background = Image("mg1 road background.png")
            self.ground = Image("mg1 road ground.png")

            self.ground_factor = 1
            self.ground_counter = 0
            self.background_counter = 0
            self.background_factor = 5

            self.cars= [Image("car1.png"), Image("car2.png"),
                        Image("car3.png"), Image("car4.png"),
                        Image("car5.png"), Image("car6.png")]

            self.car_counter = 0
            self.car_factor = 4.1

            self.bus_y = 0;
            self.bus_y_additional = 15

            self.bus_change_line_max = 35
            self.bus_change_line_counter = self.bus_change_line_max

            self.bus_prev_line = 0
            self.bus_line = 1

            self.cars_sets = [[0], [1, 2], [2], [0, 1], [0, 2], [1], [1, 0], [2, 0], [2, 1]]

            self.distance_bitween_sets_factor = 2
            self.distance_bitween_sets_step = 0.00005
            self.counters_step = 0.001

            self.count_of_lines = 3

            self.finished = False
            self.first_render = True

        def visit(self):
            return [ self.bus, self.background, self.ground ]

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            background = renpy.render(self.background, width, height, st, at)
            background_duplicate = renpy.render(self.background, width, height, st, at)

            r.blit(background, (self.background_counter * self.background_factor, 0))
            r.blit(background_duplicate, (self.background_counter * self.background_factor - width, 0))

            ground = renpy.render(self.ground, width, height, st, at)
            ground_duplicate = renpy.render(self.ground, width, height, st, at)

            r.blit(ground, (self.ground_counter * self.ground_factor, (height - ground.height) / 2))
            r.blit(ground_duplicate, (self.ground_counter * self.ground_factor - width, (height - ground.height) / 2))

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

            if self.bus_change_line_counter + 1 <= self.bus_change_line_max:
                self.bus_change_line_counter += 1

            is_game_finished = False
            distance_bitween_sets = bus.width * self.distance_bitween_sets_factor

            for cars_set_i in range(0, len(self.cars_sets)):
                for car_line_i in self.cars_sets[cars_set_i]:
                    t = Transform(child=self.cars[car_line_i % 6], xsize=200, ysize=int(200 * 427 / 844))
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
            self.ground_factor += self.counters_step
            self.background_factor += self.counters_step
            self.car_factor += self.counters_step

            if self.finished:
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
                return ""
            else:
                raise renpy.IgnoreEvent()

screen bus():
    default bus_minigame = BusMinigameDisplayable()
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
    