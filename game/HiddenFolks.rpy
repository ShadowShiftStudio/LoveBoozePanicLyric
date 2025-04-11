# hf - HiddenFolks (поиск предметов)
# используется в паре с модулем 7dots.rpy

# трансформ для фона, чтобы он был на весь экран с сохранением пропорций
transform full_screen_bg:
    size (config.screen_width, config.screen_height)
    fit "cover"  # сохраняет пропорции и заполняет весь экран

# пример использования:
init 1:
    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("sanya room", 8,
        ("backpack", 0, 0, _("Рюкзак РЕДАН")),
        ("light", 20, 0, _("Зажигалка")),
        ("marlboro1", 0, 0, _("Пачка сигарет (пустая)")),
        ("marlboro2", 1413, 850, _("Пачка сигарет (пуста)")),
        ("t-shirt", 855, 900, _("Футболка")),
        ("pants", 440, 761, _("Трусы")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
        # включаем смену курсора при наведении
        mouse=True,
        # включаем инвентарь с убиранием из него найденных предметов
        inventory=True,
        # включаем подсказки
        hint=True,
        # включаем подсветку предмета при наведении
        hover=brightness(.2),
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

# затем будет вызов игры:
    # $ hf_start()
    
    # количество несобранных предметов будет в hf_return

    # трансформ для перемещения подсказки
    transform hf_hint_at():
        anchor(.5, 1.25)
        function hf_hint_at_f

    # стиль для подсказки
    style hint_style is frame:
        # жёлтый фон растягивается под размеры текста
        background Frame("#fe9", 0, 0)
        # отступы от краёв до текста
        xpadding 20
        ypadding 15

    # стиль для текста подсказки
    style hint_style_text is text:
        color "#014"
        outlines []

init python:
    # автоматическое объявление спрайтов (включая webp)
    images_auto()

    # курсоры
    config.mouse = {"default": [("images/c/default.png", 1, 0)],
        "hand": [("images/c/hand1.png", 2, 10),
        ("images/c/hand1.png", 2, 10), ("images/c/hand1.png", 2, 10),
        ("images/c/hand1.png", 2, 10), ("images/c/hand2.png", 2, 10),
        ("images/c/hand2.png", 2, 10), ("images/c/hand3.png", 2, 10),
        ("images/c/hand3.png", 2, 10), ("images/c/hand2.png", 2, 10),
        ("images/c/hand2.png", 2, 10)],
        "finger": [("images/c/finger.png", 2, 10)]}

    # координаты мышки
    def hf_hint_at_f(trans, st, at):
        trans.pos = renpy.get_mouse_pos()
        return 0

# НАСТРОЙКИ
    # надо ли менять курсор при наведении
    hf_mouse = True

    # нужно ли выводить подсказку
    hf_hint = True

    # True - найденные предметы добавляются в инвентарь
    # False - найденные предметы исчезают из инвентаря
    # None - инвентарь не отображается
    hf_inventory = True

    # трансформ для подсвечивания при наведении
    # может быть, например, brightness(.05)
    hf_hover = None

    # имя папки со спрайтами игры в директории images плюс пробел
    hf_dir = "game"

    # размеры предметов в инвентаре
    hf_w, hf_h = 200, 200

    # размеры таймбара
    hf_t_w, hf_t_h = 1040, 32

    # отступ предметов от краёв инвентаря
    hf_xpadding = 20
    hf_ypadding = 40

    # положение окна инвентаря
    hf_xalign = .5
    hf_yalign = .05

    # положение таймбара
    hf_t_xalign = .5
    hf_t_yalign = .01

# ВНУТРЕННИЕ ПЕРЕМЕННЫЕ
    # время, за которое нужно собрать предметы
    hf_time = 8

    # время, которое нужно обнулить для анимации
    hf_bar = 100

    # режим игры (False - режим фона)
    hf_game_mode = True

    # предметы, которые нужно найти
    hf_needed = []

    # предметы, которые уже нашли
    hf_picked = []

    # фон игры
    hf_back = "black"

    # нужно ли перекрашивать таймбар (осталась четверть времени)
    hf_warning = True

    # количество несобранных предметов
    hf_return = 0

    # изначальное количество предметов
    hf_max_count = 0

    # инициализация игры
    def hf_init(bg, time, *args, **kwargs):
        global hf_needed, hf_picked, hf_back, hf_time, hf_bar, hf_max_count
        # обнуляем списки и переменные
        hf_needed = []
        hf_picked = []
        hf_back = bg
        hf_time = time
        hf_bar = 100
        # добавляем в список предметы, которые нужно найти
        for item, x, y, h in args:
            hf_needed.append((item, x, y, h))
        hf_max_count = len(hf_needed)
        # применяем необязательные параметры игры
        # по сути меняем значения похожих переменных,
        # но только они должны начинаться с hf_
        for k, v in kwargs.items():
            kk = "hf_" + k
            if kk in globals().keys():
                globals()[kk] = kwargs.get(k)

    # показать игру в виде фона на слое master
    def hf_bg():
        store.hf_game_mode = False
        show_s("HiddenFolks")

    # спрятать игру-фон
    # но сначала показать, если игра экран скрыт
    def hf_hide():
        hf_bg()
        renpy.with_statement(None)
        hide_s("HiddenFolks")

    # запустить игру
    # если задан какой-то эффект, то сначала показать игру с ним
    def hf_start(effect=None):
        store.hf_game_mode = False
        store.hf_warning = False
        hf_bg()
        renpy.with_statement(effect)
        store.hf_game_mode = True
        store.hf_return = len(hf_needed)
        renpy.call_screen("HiddenFolks")
        hf_bg()

    # клик по предмету (перенести его в инвентарь или убрать оттуда)
    def hf_click(item, x, y, h):
        store.hf_picked.append(store.hf_needed.pop(hf_needed.index((item, x, y, h))))
        splay("click")
        renpy.restart_interaction()
        # осталось собрать
        store.hf_return = len(hf_needed)
    HFClick = renpy.curry(hf_click)

    # меняем цвет таймера
    # или запускаем анимацию уменьшения времени
    def hf_go(warning=False):
        if warning:
            # меняем цвет
            store.hf_warning = True
        else:
            # запускаем анимацию
            store.hf_bar = 0
        renpy.restart_interaction()
    HFGo = renpy.curry(hf_go)

    # получить спрайт для инвентаря
    def hf_isprite(item):
        # если в папке инвентаря есть нужный предмет,
        # то берём его, а иначе - то, что на экране
        i = hf_dir + " inventory " + item
        if has_image(i):
            item = i
        # получаем размер спрайта предмета
        w, h = get_size(item)
        # коэффициенты для зума
        zoom = 1
        # если предмет больше ячейки, вычисляем новый зум
        if w > hf_w or h > hf_h:
            # по большей из сторон
            if w > h:
                zoom = hf_w / w
            else:
                zoom = hf_h / h
        # возвращаем спрайт, вписанный в размеры ячейки инвентаря
        return Transform(item, zoom=zoom)

    # текст подсказки
    hf_hint_text = ""

    # меняем текст подсказки
    def hf_set_hint(t=""):
        if hf_hint and hf_hint_text != t:
            store.hf_hint_text = t
            renpy.restart_interaction()
    SetHint = renpy.curry(hf_set_hint)

screen HiddenFolks():
    # фон игры
    add hf_back at full_screen_bg

    # все предметы на экране
    for i, x, y, h in hf_needed:

        $ item = hf_dir + " " + i
        # предмет-кнопка
        imagebutton:
            style "empty"
            # спрайт предмета
            idle item
            # положение предмета (координаты его центра)
            pos(x, y)
            # наведение на пиксель
            focus_mask True
            # все действия только в режиме игры
            if hf_game_mode:

                # меняем курсор при необходимости
                if hf_mouse:
                    mouse "hand"

                # если включено выделение при наведении
                if not hf_hover is None:
                    # если есть картинка для выделенного объекта, то выводим ее
                    if has_image(item + " hover"):
                        hover item + " hover"
                    # иначе подсвечиваем заданным в настройках трансформом
                    else:
                        hover At(item, hf_hover)

                # меняем текст подсказки при наведении курсора
                hovered SetHint(h)
                unhovered SetHint()

                # обработка клика
                action HFClick(i, x, y, h)

    # анимация таймера
    if hf_game_mode and hf_time > 0:
        # активация таймера
        timer .01 action HFGo()

        # таймер перекрашивания бара (треть общего времени)
        timer hf_time * .6666 action HFGo(True)

        # визуализация таймера в виде бара
        bar:
            # положение и размеры таймбара
            align(hf_t_xalign, hf_t_yalign)
            xysize(hf_t_w, hf_t_h)
            value AnimatedValue(hf_bar, 100, hf_time)

            # перекрашивание и мерцание левой полоски бара,
            # когда осталось меньше трети времени
            if hf_warning:
                left_bar Frame(At("gui/bar/left.png", paint2("#e02", "#e028", .2)), gui.bar_borders, tile=gui.bar_tile)

        # проигрыш по таймеру
        timer hf_time repeat True action SetHint(), SPlay("gameover"), Return()

        # всё собрали, уходим (Return()() из def больше не работает)
        if hf_return < 1:
            timer .01 repeat True action SetHint(), SPlay("gamewin"), Return()

        # инвентарь
        if not hf_inventory is None:
            # рамка инвентаря
            frame:
                style "empty"
                xysize (hf_max_count * hf_w + hf_xpadding * 2, hf_h + hf_ypadding * 2)
                # положение инвентаря
                align(hf_xalign, hf_yalign)
                background Frame("framei", 48, 48)
                # контейнер для предметов
                hbox:
                    align(.5, .5)
                    # отображаем собранные предметы
                    if hf_inventory:
                        for item, x, y, h in hf_picked:
                            # xysize(hf_w, hf_h)
                            imagebutton idle hf_isprite(item) align(.5, .5):
                                # наведение на пиксель
                                focus_mask True
                                action NullAction()
                                if hf_game_mode:
                                    # меняем курсор при необходимости
                                    if hf_mouse:
                                        mouse "hand"
                                    # меняем текст подсказки при наведении курсора
                                    hovered SetHint(h)
                                    unhovered SetHint()
                    # либо отображаем предметы, которые осталось собрать
                    else:
                        for item, x, y, h in hf_needed:
                            imagebutton idle hf_isprite(item) align(.5, .5):
                                # наведение на пиксель
                                focus_mask True
                                action NullAction()
                                if hf_game_mode:
                                    # меняем курсор при необходимости
                                    if hf_mouse:
                                        mouse "hand"
                                    # меняем текст подсказки при наведении курсора
                                    hovered SetHint(h)
                                    unhovered SetHint()

    # при необходимости выводим подсказку
    if hf_hint and hf_hint_text:
        frame:
            style "hint_style"
            text hf_hint_text style "hint_style_text" align(.5, .5)
            at hf_hint_at()
