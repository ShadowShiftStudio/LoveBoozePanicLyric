init python:
    import random
    import pygame

    class WhiteNoiseDisplayable(renpy.Displayable):
        def __init__(self, intensity=1.0, alpha=1.0, badify=4, red=255, green=255, blue=255, **kwargs):
            super(WhiteNoiseDisplayable, self).__init__(**kwargs)
            self.intensity   = max(0.0, min(1.0, intensity))
            self.alpha       = max(0.0, min(1.0, alpha))
            self.badify      = int(badify)
            self.red         = max(0, min(255, int(red)))
            self.green       = max(0, min(255, int(green)))
            self.blue        = max(0, min(255, int(blue)))
            self._pool       = []
            self._pool_index = 0

        def render(self, width, height, st, at):
            # заменяем динамический делитель на классический
            sw = width  // self.badify
            sh = height // self.badify

            # fill pool of 10 small noise surfaces
            if len(self._pool) < 10:
                surf = pygame.Surface((sw, sh), pygame.SRCALPHA)
                surf.lock()
                for y in range(sh):
                    for x in range(sw):
                        a = int(random.random() * 255 * self.intensity)
                        surf.set_at((x, y), (self.red, self.green, self.blue, a))
                surf.unlock()
                self._pool.append(surf)
                tile = surf
            else:
                tile               = self._pool[self._pool_index]
                self._pool_index   = (self._pool_index + 1) % 10

            # scale up and draw
            surf = pygame.transform.smoothscale(tile, (width, height))
            ren  = renpy.Render(width, height)
            ren.blit(surf, (0, 0))
            renpy.redraw(self, 1.0/30.0)
            return ren

    # минимальный вызов без update_rate — шум анимируется из пула
image noise medium = WhiteNoiseDisplayable(intensity=0.3, alpha=0.2)
