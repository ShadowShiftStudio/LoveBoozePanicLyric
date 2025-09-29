## модуль sms работает только в паре с модулем 7dots.rpy 2022 года
## для работы модуля нужно на экран "say" добавить строку:
## on "show" action SMSAdd(what)

# показать телефон на экране
# who - имя собеседника в шапке
# clear - очистить сообщения
# $ sms_show(who=None, clear=False)

# убрать телефон с экрана
# $ sms_hide()

# очистить экран телефона
# $ sms_clear()

# персонажи для переписки, собеседник
# $ sms_oksana = SMSL(_("Оксана Ш."))

# это слова получателя
# $ sms_r = SMSR(_("Я"))

# сервисные сообщения
# $ sms_c = SMSC(_("Системное сообщение"))

# имена лучше задавать, хоть их и не видно, для сохранения в истории

# чтобы переместить телефон, нужно поменять переменную:
# sms_trans = [align(.15, .5), rotate(-2.5, False)]

## НАСТРАИВАЕМЫЕ ПАРАМЕТРЫ
init python:

    # размеры всего телефона
    phone_w, phone_h = 500, 960

    # размеры экрана телефона
    scr_w, scr_h = 480, 860

    # высота статичных участков (шапка и меню)
    scr_top_h = 80
    scr_bottom_h = 80

    # цвет фона для шапки
    scr_top_color = "#09f"

    # фон экрана телефона
    scr_bg = "#fff"

    # максимальная ширина пузыря с сообщением
    sms_w = 380

    # если ширина/высота единственной в сообщении картинки больше этих,
    # то картинка преобразуется в прикреплённое фото
    sms_min_w, sms_min_h = 200, 200

    # цвета фона
    sms_left_bg_color = "#09f"
    sms_right_bg_color = "#e5e5ea"
    sms_center_bg_color = "#0000"

    # цвета текста
    sms_left_text_color = "#fff"
    sms_right_text_color = "#000"
    sms_center_text_color = "#aaa"

    # шрифт
    sms_text_size = 28
    sms_text_font = "fonts/roboto.ttf"

    # отступы текста sms от краёв пузырей
    sms_xpadding, sms_ypadding = 24, 12

    # отступы пузырей sms от краёв экрана
    sms_xmargin, sms_ymargin = 24, 4

    # фиксированные углы для пузырей с сообщениями (для Frame)
    sms_corner_w, sms_corner_h = 16, 16

    # трансформ для окна с телефоном
    # например, можно задать положение
    sms_trans = [align(.15, .5), rotate(-2.5, False)]

    # персонажи для переписки
    sms_yuli = SMSL(_("Юля"))
    sms_nadia = SMSL(_("Надя"))

    # это слова получателя
    sms_r = SMSR(_("Я"))

    # сервисные сообщения
    sms_c = SMSC(_("Системное сообщение"))

    # имя абонента
    sms_who = _("Неизвестный")

    # цвет имени в шапке
    sms_who_color = "#fff"

## остальное лучше не менять

    # показать телефон на экране
    def sms_show(who=None, clear=False):
        if not sms_current_style:
            store.sms_current_style = "sms_center"
        if who is not None:
            store.sms_who = who
        # если нужно, очистить сообщения
        if clear:
            sms_clear()
        renpy.show_screen("sms", _layer="master")

    # убрать телефон с экрана
    def sms_hide():
        renpy.hide_screen("sms", layer="master")

    # очистить экран телефона
    def sms_clear():
        store.sms_all = []
        renpy.restart_interaction()

    # текущее время читателя
    def time_now():
        return datetime.datetime.now().strftime("%H:%M")

init:
    # стиль для фрейма с телефоном
    style phone_window is empty:
        xysize(phone_w, phone_h)
        background None
        foreground Frame("phone skin", 0, 0)

    # стиль конкретно для экрана телефона
    style scr_frame is empty:
        xysize(scr_w, scr_h)
        background Frame(scr_bg, 0, 0)
        align(.5, .5)

    # стиль для шапки с именем абонента
    style top_frame is empty:
        xysize(scr_w, scr_top_h)
        background scr_top_color
        foreground Frame("phone top", 0, 0)
        align(.5, .0)

    # стиль для подвала с псевдо-полем ввода
    style bottom_frame is empty:
        xysize(scr_w, scr_bottom_h)
        background Frame("phone bottom", 0, 0)
        align(.5, 1.)

    # стиль для sms от собеседника
    style sms_left is frame:
        background Frame(At("phone mask", color(sms_left_bg_color)), sms_corner_w, sms_corner_h)
        xmaximum sms_w
        xpadding sms_xpadding
        ypadding sms_ypadding
        xmargin sms_xmargin
        ymargin sms_ymargin
        xalign .0

    # стиль для sms от получателя
    style sms_right is sms_left:
        background Frame(At("phone mask", color(sms_right_bg_color)), sms_corner_w, sms_corner_h)
        xalign 1.

    # стиль для сервисных сообщений
    style sms_center is sms_left:
        background None
        xmaximum scr_w
        xalign .5

    # стили для текста сообщений
    style sms_left_text is text:
        font sms_text_font
        size sms_text_size
        color sms_left_text_color
        text_align .0

    style sms_right_text is sms_left_text:
        color sms_right_text_color

    style sms_center_text is sms_left_text:
        color sms_center_text_color

init -1 python:
    # листать вниз при добавлении сообщений
    yadjValue = float("inf")
    yadj = ui.adjustment()

    # все sms в формате кортежей (стиль, текст)
    sms_all = []

    # здесь будет храниться стиль текущего сообщения
    sms_current_style = ""

    from functools import partial

    # определяем стиль текущего персонажа
    def call_style(smsstyle, event_name, *args, **kwarg):
        if event_name == "begin":
            store.sms_current_style = smsstyle
            # если это sms, то пикаем
            if smsstyle in sms_beep_styles:
                splay("sms")

    # функция с параметрами в качестве одного параметра
    def sms_style(*args, **kwarg):
        return partial(call_style, *args, **kwarg)

    # заготовки для невидимых на экране персонажей
    def SMS(narrator=None, smsstyle="sms_center", *args, **kwarg):
        return Character(narrator=narrator, window_style="empty", window_yoffset=config.screen_height, statement_name="say-centered", callback=sms_style(smsstyle), *args, **kwarg)
    def SMSL(narrator=None, *args, **kwarg):
        return SMS(narrator, "sms_left", *args, **kwarg)
    def SMSR(narrator=None, *args, **kwarg):
        return SMS(narrator, "sms_right", *args, **kwarg)
    def SMSC(narrator=None, *args, **kwarg):
        return SMS(narrator, *args, **kwarg)

    sms_beep_styles = ["sms_left", "sms_right"]

    # читаем сообщение, чтобы вывести на экран в общей куче
    def sms_add(what=None):
        # добавляем сообщение в список сообщений на экране
        if what is not None and sms_current_style is not None:
            store.sms_all.append((sms_current_style, what))
        # если это не системное сообщение, то пикаем
        if style in sms_beep_styles:
            splay("sms")
    SMSAdd = renpy.curry(sms_add)

    # не будет работать с пробелами, типа такого: "{ image = smile }"
    # если вместо текста только картинка, то показать её с закруглёнными краями, а не пузырь
    def sms_image(i_style, i_text):
        if "{image=" in i_text.replace(" ", "") and not del_tags(i_text, ""):
            imgs = get_tags(i_text, "image")
            if imgs:
                key = list(imgs.keys())
                if len(key) == 1:
                    img = imgs[key[0]]
                    w, h = get_size(img)
                    # если картинка больше указанных в настройках размеров
                    if w >= sms_min_w or h >= sms_min_h:
                        # вписываем картинку в сообщение
                        if w > h:
                            z = sms_w / w
                        else:
                            z = sms_h / h
                        img = Transform(img, zoom=z)
                        w2, h2 = int(w * z), int(h * z)
                        # скругляем края
                        mask = Frame("phone mask", sms_corner_w, sms_corner_h, xysize=(w2, h2))
                        return AlphaMask(img, mask)
        return None

# экран телефона
screen sms():
    $ yadj.value = yadjValue
    # окно с телефоном
    frame:
        style "phone_window"
        at sms_trans
        # фрейм с экраном телефона
        frame:
            style "scr_frame"
            # стопочкой шапка, смски и подвал
            vbox:
                xfill True
                yfill True
                # шапка с абонентом
                frame:
                    style "top_frame"
                    # имя абонента
                    text sms_who style "sms_center_text" align(.5, .7) color sms_who_color
                # смски с прокруткой
                viewport:
                    id "sms_vp"
                    # размеры окна прокрутки с учетом шапки и подвала
                    xysize(scr_w, scr_h - scr_top_h - scr_bottom_h)
                    xinitial 1.
                    yfill False
                    mousewheel True
                    draggable True
                    side_xfill True
                    transclude
                    # перематываем в конец
                    yadjustment yadj
                    # стопочкой все сообщения
                    vbox:
                        xfill True
                        for i_style, i_text in sms_all:
                            # если это единственная картинка больше пузыря
                            $ img = sms_image(i_style, i_text)
                            if img:
                                # вписываем её в пузырь
                                frame:
                                    style i_style
                                    xpadding 0
                                    ypadding 0
                                    background None
                                    add img
                            # иначе просто выводим текст в пузыре
                            else:
                                textbutton i_text style i_style
                # подвал с псевдо-полем ввода
                frame:
                    style "bottom_frame"
