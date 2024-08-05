# пример использования
# image test = Par("bg", "layer1", "layer2")
# или
# show expression Par("bg", "layer1", "layer2") as room

# картинки должны быть разного размера, например,
# 3130х1760, 2614х1470, 2099х1180

# либо одинакового размера, но тогда их нужно увеличивать программно:
# Par(("bg", 1.5), ("layer1", 1.3), ("layer2",1.15))

init python:
    # класс для параллакса
    class Par(renpy.Displayable):
        # инициализация класса
        def __init__(self, *args):
            super(Par, self).__init__()
            self.x, self.y = renpy.get_mouse_pos()
            # заполнение данных слоёв
            self.images = []
            for i in args:
                image, zoom = i, 1
                if isinstance(i, (tuple, list)):
                    image, zoom = i[0], i[1]
                self.images.append((renpy.displayable(image), zoom))
            return

        # отрисовка displayable
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            # перебираем слои
            for image, zoom in self.images:
                # рендерим и узнаем размеры
                cr = renpy.render(image, width, height, st, at)
                w, h = cr.get_size()
                w *= zoom
                h *= zoom
                x2 = self.x - self.x * w * 1. / width
                y2 = self.y - self.y * h * 1. / height
                # выводим слой на общую картинку
                r = renpy.render(image, int(w), int(h), st, at)
                render.blit(r, (x2, y2))
            # перерисовываем экран
            renpy.redraw(self, 0)
            return render

        # считывание позиции мышки
        def event(self, ev, x, y, st):
            import pygame
            hover = ev.type == pygame.MOUSEMOTION
            # click = ev.type == pygame.MOUSEBUTTONDOWN
            # mousefocus = pygame.mouse.get_focused()
            if hover:
                self.x, self.y = x, y
            return
