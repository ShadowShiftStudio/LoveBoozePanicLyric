init python:
    from renpy.audio.sound import play
    
    class Counter:
        def __init__(self, duration):
            self.duration = duration
            self.counter = 0

        def next(self, reversed):
            if reversed: return self.decrease()
            if not reversed: return self.increase()

        def increase(self):
            if self.counter + 1 <= self.duration:
                self.counter += 1
                return self.counter == self.duration
            else:
                return True

        def decrease(self):
            self.counter -= 1;
            if  self.counter < 0:
                self.counter = 0

            return self.counter == 0

        def reset(self):
            self.counter = 0

        def reset_reverse(self):
            self.counter = self.duration
        
        def percent(self):
            return self.counter / self.duration

    class ButtonDisplayble(renpy.Displayable):
        def __init__(self, callback, image, fade_image, pos):
            renpy.Displayable.__init__(self)
            
            self.image = image
            self.fade_image = fade_image
            self.disabled_solid = Solid("#000000")

            self.width_factor = 2 / 5.0
            self.aspect_ratio = 1 / 10.0

            self.pos = pos

            self.button = None
            self.clicked = False

            self.button_x = 0
            self.button_y = 0

            self.disabled = False

            self.callback = callback

        def visit(self):
            return [ self.image ]

        def disable(self):
            self.disabled = True

        def enable(self):
            self.disabled = False

        def render(self, width, height, st, at):
            button_width = int(width * self.width_factor)
            button_height = int(button_width * self.aspect_ratio)

            r = renpy.Render(width, height)

            t = Transform(self.image, xsize=button_width, ysize=button_height)
            self.button = renpy.render(t, width, height, st, at)

            if self.pos == -1:
                self.button_x = width / 24
                self.button_y = height - self.button.height * 3 / 2.0

            if self.pos == 1:
                self.button_x = width * 23 / 24 - self.button.width
                self.button_y = height - self.button.height * 3 / 2.0
            
            r.blit(self.button, (self.button_x, self.button_y))

            if self.clicked:
                fade_t = Transform(self.fade_image, xsize=button_width, ysize=button_height)
                fade = renpy.render(fade_t, width, height, st, at)
                r.blit(fade, (self.button_x, self.button_y))
                self.clicked = False
                self.callback()

            if self.disabled:
                disabled_t = Transform(self.disabled_solid, xsize=button_width, ysize=button_height, alpha=0.2)
                disabled = renpy.render(disabled_t, width, height, st, at)
                r.blit(disabled, (self.button_x, self.button_y))

            return r
        
        def event(self, ev, x, y, st):
            import pygame

            if not self.disabled and self.button != None and ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if x >= self.button_x and x <= self.button_x + self.button.width \
                and y >= self.button_y and y <= self.button_y + self.button.height:
                    self.clicked = True
                    self.disabled = True
            
            renpy.redraw(self, 0)
    
    class BarDisplayable(renpy.Displayable):
        def __init__(self, percent, pos):
            renpy.Displayable.__init__(self)

            self.background = Solid("#ffffff")
            self.foreground = Solid("#bd3186")
            self.percent = percent
            self.pos = pos
            self.score = 0
        
        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            background_width = width / 2.5
            background_height = background_width / 20
            background = renpy.render(self.background, background_width, background_height, st, at)

            foreground_width = background_width * self.percent / 100
            foreground_height = background_height
            foreground = renpy.render(self.foreground, foreground_width, foreground_height, st, at)

            background_pos_x = 0
            foreground_pos_x = 0

            pos_y = background_height / 3

            text_pos_x = 0

            text = Text("Очков: " + str(self.score), slow=True, size=50)
            text = renpy.render(text, width, height, st, at)

            if self.pos == -1:
                background_pos_x = (width / 2 - background_width) / 2
                foreground_pos_x = background_pos_x
                text_pos_x = background_pos_x

            if self.pos == 1:
                background_pos_x = width - (width / 2 - background_width) / 2 - background_width
                foreground_pos_x = width - (width / 2 - background_width) / 2 - foreground_width
                text_pos_x = width - (width / 2 - background_width) / 2 - text.width

            r.blit(background, (background_pos_x, pos_y))
            r.blit(foreground, (foreground_pos_x, pos_y))

            r.blit(text, (text_pos_x, pos_y + background.height))

            return r

        def increase(self, value):
            self.percent += value
            if self.percent > value: self.percent = value

        def decrease(self, value):
            self.percent -= value
            if self.percent < 0: self.percent = 0

        def add_score(self, value):
            self.score += value


    class GlassDisplayable(renpy.Displayable):
        def __init__(self, buttons, pos):
            renpy.Displayable.__init__(self)
            self.counter = Counter(100)
            self.glass_image = Image("kfc_glass.png")
            self.pos = pos

            self.reverse_animation = False
            self.animation_started = False
            self.is_finished = False
            self.buttons = buttons
            #self.my_sound = renpy.audio.sound("bitenmap.mp3")
        
        def start(self):
            self.animation_started = True
            self.reverse_animation = False
            self.counter.reset()
            self.counter.increase()
        
        def start_reversed(self):
            self.animation_started = True
            self.reverse_animation = True
            self.counter.reset_reverse()

        def drink(self):
            #renpy.audio.sound("bitenmap.mp3")
            play("audio/bitenmap.mp3")
            self.start()

        def is_finished_drinking(self):
            if self.is_finished:
                self.is_finished = False
                return True
            else: return False

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            glass_width = width / 30
            glass_height = glass_width * 1.3

            default_pos_x = 0
            default_pos_y = height / 2

            if self.pos == -1:
                default_pos_x = width / 8 - glass_width

            if self.pos == 1:
                default_pos_x = width - width / 8 - glass_width - glass_width

            import math

            pos_x = default_pos_x
            pos_y = default_pos_y

            if self.animation_started:
                pos_x += 1.5 * self.pos * glass_width * math.pow(self.counter.percent(), 2)
                pos_y -= 1.5 * glass_height * self.counter.percent()

            glass_t = Transform(self.glass_image, rotate=self.pos * 45 * self.counter.percent())
            glass = renpy.render(glass_t, glass_width, glass_height, st, at)

            r.blit(glass, (pos_x, pos_y))

            if self.animation_started and not self.counter.next(self.reverse_animation):
                self.counter.next(self.reverse_animation)
                renpy.redraw(self, 0.0001)
            elif self.animation_started and not self.reverse_animation:
                self.start_reversed()
                renpy.redraw(self, 0.0001)
            elif self.animation_started and self.reverse_animation and self.counter.percent() == 0:
                self.animation_started = False
                self.is_finished = True

                for button in self.buttons:
                    button.enable()
                    renpy.redraw(button, 0.001)

            return r

    class TextDisplayable(renpy.Displayable):
        def __init__(self, glasses):
            renpy.Displayable.__init__(self)
            self.counter = Counter(50)
            self.started = False
            self.finished = False
            self.reverse = False
            self.value = ""
            self.glasses = glasses

        def start(self, value):
            self.value = value
            self.started = True
            self.reverse = False
            self.counter.reset()
            self.counter.increase()
        
        def start_reversed(self):
            self.started = True
            self.reverse = True
            self.counter.reset_reverse()

        def display(self, value):
            self.start(value)

        def is_displaying_finished(self):
            if self.finished:
                self.finished = False
                return True
            else: return False

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            text = Text(self.value, slow=True, size=100)
            text = Transform(text, alpha=self.counter.percent())

            text = renpy.render(text, width, height, st, at)
            r.blit(text, ((width - text.width) / 2, height / 2 - text.height))

            if self.started and not self.counter.next(self.reverse):
                self.counter.next(self.reverse)
                renpy.redraw(self, 0.05)
            elif self.started and not self.reverse:
                self.start_reversed()
                renpy.redraw(self, 0.05)
            elif self.started and self.reverse and self.counter.percent() == 0:
                self.started = False
                self.finished = True

                for glass in self.glasses:
                    glass.drink()
                    renpy.redraw(glass, 0.001)

            return r

    class KfcMinigameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.bite_button = ButtonDisplayble(self.on_gg_bite, Image("kfc_bite.png"), Image("kfc_button_fade.png"), -1)
            self.not_bite_button = ButtonDisplayble(self.on_gg_not_bite, Image("kfc_not_bite.png"), Image("kfc_button_fade.png"), 1)

            self.pasha_bar = BarDisplayable(100, -1)
            self.pasha_glass = GlassDisplayable([self.bite_button, self.not_bite_button], -1)

            self.gg_bar = BarDisplayable(100, 1)
            self.gg_glass = GlassDisplayable([], 1)

            self.pasha_image = Image("pasha/neutral.png")
            self.bowl_image = Image("kfc_bowl.png")
            self.ground_image = Image("kfc_ground.png")
            self.background_image = Image("kfc inside.png")

            self.round_starting_counter = Counter(100)

            self.round_text = TextDisplayable([self.pasha_glass, self.gg_glass])

            self.bite_decrease = 3
            self.not_bite_decrease = 10

            self.round_changed = True
            self.round_count = 1

            self.bite_button.disable()
            self.not_bite_button.disable()

            self.winner = ""

        def on_gg_bite(self):
            play("audio/bite.mp3")
            self.update_stats(self.bite_decrease)

        def on_gg_not_bite(self):
            play("audio/nea.mp3")
            self.update_stats(self.not_bite_decrease)

        def update_stats(self, hp_decrease):
            self.gg_bar.decrease(hp_decrease)
            self.round_changed = True
            self.bite_button.disable()
            self.not_bite_button.disable()

            import random

            is_pasha_bite = bool(random.getrandbits(1))

            if is_pasha_bite:
                self.pasha_bar.decrease(self.bite_decrease)
            else:
                self.pasha_bar.decrease(self.not_bite_decrease)

            self.pasha_bar.add_score((100 - self.pasha_bar.percent) * 10)
            self.gg_bar.add_score((100 - self.gg_bar.percent) * 10)

            if self.pasha_bar.percent <= 0:
                self.winner = "sanya"
                renpy.timeout(0.001)
                return

            if self.gg_bar.percent <= 0:
                self.winner = "pasha"
                renpy.timeout(0.001)
                return

            renpy.redraw(self.gg_bar, 0.001)
            renpy.redraw(self.pasha_bar, 0.001)

            self.round_changed = True
            renpy.redraw(self, 0.001)

        def visit(self):
            return [ self.bowl_image, self.pasha_image, self.gg_glass, self.gg_bar, self.pasha_bar, self.bowl_image, self.background_image, self.bite_button, self.not_bite_button ]

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            background_transformed = Transform(self.background_image, xsize=1920, ysize=1024)
            background = renpy.render(background_transformed , width, height, st, at)
            r.blit(background, (0, 0))

            pasha = renpy.render(self.pasha_image, width, height, st, at)
            r.blit(pasha, (width / 4 - pasha.width / 2, height - pasha.height))

            ground = renpy.render(self.ground_image, width, height, st, at)
            r.blit(ground, (0, 0))

            bowl = renpy.render(self.bowl_image, width, height, st, at)
            r.blit(bowl, ((width - bowl.width) / 2, height / 2))

            bite_button = renpy.render(self.bite_button, width, height, st, at)
            not_bite_button = renpy.render(self.not_bite_button, width, height, st, at)

            r.blit(bite_button, (0, 0))
            r.blit(not_bite_button, (0, 0))

            pasha_bar = renpy.render(self.pasha_bar, width, height, st, at)
            r.blit(pasha_bar, (0, 0))

            gg_bar = renpy.render(self.gg_bar, width, height, st, at)
            r.blit(gg_bar, (0, 0))

            pasha_glass = renpy.render(self.pasha_glass, width, height, st, at)
            r.blit(pasha_glass, (0, 0))

            gg_glass = renpy.render(self.gg_glass, width, height, st, at)
            r.blit(gg_glass, (0, 0))

            round_text = renpy.render(self.round_text, width, height, st, at)
            r.blit(round_text, (0, 0))

            if self.round_changed:
                self.round_changed = False
                self.round_text.display("Раунд " + str(self.round_count))
                self.round_count += 1
                renpy.redraw(self.round_text, 0.001)

            return r

        def event(self, ev, x, y, st):
            self.bite_button.event(ev, x, y, st)
            self.not_bite_button.event(ev, x, y, st)

            if self.winner != "":
                return self.winner


screen kfc_minigame():
    default kfc_minigame = KfcMinigameDisplayable()
    add kfc_minigame

label play_kfc_minigame:
    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    image white = "#fff"

    scene white
    with dissolve
    call screen kfc_minigame
    with fade

    $ quick_menu = True
    window show


if _return == "pasha":
    "Саня конкретно перебрал с выпивкой в этот раз... Ноги еле идут..."
else:
    "Вы выиграли! Паша конкретно перебрал с выпивкой в этот раз..."