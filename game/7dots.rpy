# чтобы str() не вылетала на линуксе
define mystr = eval("lambda i: '%s' % i")

init -2000 python:
    # деление с переводом в целочисленное для нового ренпая
    def d2(x, d=2):
        return int(x / d)

    # задаём пределы
    clip = lambda i, mini, maxi: max(min(maxi, i), mini)

    # строка в целочисленное или в дробное
    def fint(x, default=0): # можно None
        try:
            x = int(x)
            return x
        except:
            try:
                x = float(x)
                return x
            except:
                return default

    # префиксы спрайтов, теги в которых нужно делить не пробелами, а "_"
    layered_prefixes = []

init -2:
    # масштабирование
    transform zoom(zoom=1):
        subpixel True
        zoom zoom
    transform xzoom(zoom=1):
        subpixel True
        xzoom zoom
    transform yzoom(zoom=1):
        subpixel True
        yzoom zoom
    transform zooming(xzoom1=1., yzoom1=1., xzoom2=1., yzoom2=1., t=1):
        subpixel True
        xzoom xzoom1 yzoom yzoom1
        ease t xzoom xzoom2 yzoom yzoom2

    # прозрачность
    transform alpha(alpha=1.):
        alpha alpha
    transform alphing(alpha1=0, alpha2=1, t=1):
        alpha alpha1
        ease t alpha alpha2

    # размытость
    transform blur(blur=4):
        blur blur
    transform bluring(blur1=0, blur2=16, t=1):
        blur blur1
        ease t blur blur2

    # яркость
    transform brightness(brightness=.25):
        matrixcolor BrightnessMatrix(brightness)

    transform brightnessing(brightness1=0, brightness2=.25, t=2):
        matrixcolor BrightnessMatrix(brightness1)
        ease t matrixcolor BrightnessMatrix(brightness2)

    # контраст
    transform contrast(contrast=1.25):
        matrixcolor ContrastMatrix(contrast)

    transform contrasting(contrast1=1, contrast2=1.25, t=2):
        matrixcolor ContrastMatrix(contrast1)
        ease t matrixcolor ContrastMatrix(contrast2)

    # насыщенность
    transform saturation(saturation=1.):
        matrixcolor SaturationMatrix(saturation)

    transform saturationing(saturation1=1., saturation2=.5, t=2):
        matrixcolor SaturationMatrix(saturation1)
        ease t matrixcolor SaturationMatrix(saturation2)

    # подкрашивание картинок
    transform color(color="#000"):
        matrixcolor TintMatrix(color)

    # силуэт цвета color color1 переходит в color2
    transform coloring(color1="#fff", color2="#fff", t=2):
        matrixcolor TintMatrix(color1)
        ease t matrixcolor TintMatrix(color2)

    # спрайт цвета color1 переливается в color2
    transform color2(color1="#fff", color2="#def", t=2):
        matrixcolor TintMatrix(color1)
        ease_quad t*.5 matrixcolor TintMatrix(color2)
        ease_quad t*.5 matrixcolor TintMatrix(color1)
        repeat

    # силуэт цвета color
    transform paint(color="#fff"):
        matrixcolor TintMatrix(color) * InvertMatrix(1.) * TintMatrix("#000")

    # силуэт цвета color color1 переходит в color2
    transform painting(color1="#fff", color2="#fff", t=2):
        matrixcolor TintMatrix(color1) * InvertMatrix(1.) * TintMatrix("#000")
        ease t matrixcolor TintMatrix(color2) * InvertMatrix(1.) * TintMatrix("#000")

    # силуэт цвета color1 переливается в color2 циклично
    transform paint2(color1="#fff", color2="#def", t=2):
        matrixcolor TintMatrix(color1) * InvertMatrix(1.) * TintMatrix("#000")
        ease_quad t*.5 matrixcolor TintMatrix(color2) * InvertMatrix(1.) * TintMatrix("#000")
        ease_quad t*.5 matrixcolor TintMatrix(color1) * InvertMatrix(1.) * TintMatrix("#000")
        repeat

    # относительное положение
    transform xalign(xalign=.5):
        xalign xalign
    transform yalign(yalign=1.):
        yalign yalign
    transform align(xalign=.5, yalign=1.):
        align (xalign, yalign)
    transform aligning(xalign1=.5, yalign1=1., xalign2=.5, yalign2=1., t=1):
        subpixel True
        align (xalign1, yalign1)
        ease t align (xalign2, yalign2)

    # положение
    transform xpos(xpos=.5):
        xpos xpos
    transform ypos(ypos=.0):
        ypos ypos
    transform pos(xpos=.5, ypos=.0):
        pos (xpos, ypos)
    transform posing(xpos1=.5, ypos1=1., xpos2=.5, ypos2=1., t=1):
        subpixel True
        pos (xpos1, ypos1)
        ease t pos (xpos2, ypos2)

    transform zpos(zpos=0, depth=True, zzoom=True):
        gl_depth depth
        zzoom zzoom
        zpos zpos
    transform zposing(zpos=0, t=1, depth=True, zzoom=True):
        gl_depth depth
        zzoom zzoom
        ease t zpos zpos

    # якорь
    transform xanchor(xanchor=.5):
        xanchor xanchor
    transform yanchor(yanchor=1.):
        yanchor yanchor
    transform anchor(xanchor=.5, yanchor=1.):
        anchor (xanchor, yanchor)
    transform anchoring(anchor1=.5, anchor2=.5, t=1):
        anchor anchor1
        ease t anchor anchor2

    # отзеркаливание
    transform hflip(xz=-1.):
        subpixel True
        xzoom xz
    transform vflip(yz=-1.):
        subpixel True
        yzoom yz

    # поворот против часовой
    transform rotate(a=45, rotate_pad=False):
        subpixel True
        rotate_pad rotate_pad
        rotate a
    transform rotating(a1=0, a2=360, t=1, rotate_pad=False):
        subpixel True
        rotate_pad rotate_pad
        rotate a1
        ease t rotate a2

    # повороты с перспективой
    ## вверх-вниз
    transform turnx(x=45, depth=True):
        subpixel True
        perspective True
        gl_depth depth
        matrixtransform RotateMatrix(x, 0, 0)

    # повороты с перспективой
    ## вверх-вниз
    transform turnx(x=45, depth=True):
        subpixel True
        perspective True
        gl_depth depth
        matrixtransform RotateMatrix(x, 0, 0)

    ## влево-вправо
    transform turny(y=45, depth=True):
        subpixel True
        perspective True
        gl_depth depth
        matrixtransform RotateMatrix(0, y, 0)

    ## против часовой-по часовой
    transform turnz(z=45, depth=True):
        subpixel True
        perspective True
        gl_depth depth
        matrixtransform RotateMatrix(0, 0, z)

    ## по всем направлениям
    transform turn(x=0, y=45, z=0, depth=True):
        subpixel True
        perspective True
        gl_depth depth
        matrixtransform RotateMatrix(x, y, z)

    # вырезание
    transform crop(x=0, y=0, w=1., h=1.):
        crop(x, y, w, h)

    # подпрыгивание персонажа
    transform leap(dt=.4, dyz=0.01, dxz=0.005):
        subpixel True
        yzoom 1.
        easein dt*0.35 yzoom 1.+dyz xzoom 1.-dxz
        easeout dt*0.35 yzoom 1. xzoom 1.
        easein dt*0.15 yzoom 1.-dyz xzoom 1.+dxz
        easeout dt*0.15 yzoom 1. xzoom 1.

    # слева, но не у самого края
    transform left2(xa=.35):
        anchor (.5, 1.)
        align(xa, 1.)

    # справа, но не у самого края
    transform right2(xa=.65):
        anchor (.5, 1.)
        align(xa, 1.)

    # слева, за краем
    transform left0():
        anchor (1., 1.)
        pos (.0, 1.)

    # справа, за краем
    transform right0():
        anchor (1., 1.)
        pos (1., 1.)

    # сиськотряс
    transform boobs(t=2):
        subpixel True
        yanchor 0 yzoom 1
        easeout (t*.075) yzoom 1.05
        easein  (t*.1)   yzoom .95
        easeout (t*.125) yzoom 1.025
        easein  (t*.125) yzoom .975
        easeout (t*.125) yzoom 1.01
        easein  (t*.15)  yzoom .99
        easeout (t*.15)  yzoom 1.005
        easein  (t*.15)  yzoom 1.

init python:
    # переменная для хранения скорости вывода текста
    CPS = _preferences.text_cps

    # сохранить значение скорости
    def cps_save():
        global CPS
        CPS = _preferences.text_cps

    # изменить скорость
    def cps_set(cps):
        _preferences.text_cps = cps

    # восстановить сохраненное значение скорости
    def cps_restore():
        _preferences.text_cps = CPS

init -2 python:
        # единоразовый dismiss
    def skip_once():
        renpy.end_interaction(True)
    SkipOnce = renpy.curry(skip_once)

    # остановить перемотку
    def skip_stop():
        renpy.config.skipping = None
    SkipStop = renpy.curry(skip_stop)

    # нужно, чтобы включить/отключить dismiss
    can_dismiss = True

    def dismiss_block():
        global can_dismiss
        return can_dismiss

    # включить dismiss
    def dismiss_on():
        store.can_dismiss = True
    DismissOn = renpy.curry(dismiss_on)

    # отключить dismiss
    def dismiss_off():
        if config.say_allow_dismiss is None:
            config.say_allow_dismiss = dismiss_block
        store.can_dismiss = False
    DismissOff = renpy.curry(dismiss_off)

    # для отладки
    def log(*args):
        for i in args:
            print(str(i))
    Log = renpy.curry(log)

    # эффект вспышки нужного цвета для смены фонов
    def flash(color="#fff"):
        return Fade(.25, 0, .75, color=color)

    # показан ли экран (или один из экранов)
    def has_screen(*args):
        args = make_list(args)
        for i in args:
            if renpy.get_screen(i):
                return True
        return False

    # директории для хранение звуков и музыки
    audio_dir = config.play_channel
    music_dir = "music"

    # жёсткая пауза
    def pause(t=1, hard=True):
        renpy.pause(t, hard=hard)

    # получить скриншот заданного размера, по умолчанию весь экран
    def shot(w=config.screen_width, h=config.screen_height):
        renpy.take_screenshot((w, h))
        return FileCurrentScreenshot()

    # сканируем папку музыки, на выходе - список мелодий без указанного расширения и папки
    def get_music_list(folder=music_dir, ext="ogg"):
        res = []
        list = renpy.list_files()
        for i in list:
            if i.startswith(folder):
                s = i[(len(folder) + 1):]
                if s.endswith("." + ext):
                    res.append(s[:(-len(ext) - 1)])
        return res

    # сканируем папку, на выходе - список файлов нужного расширения
    # по умолчанию расширения убираются
    def get_file_list(folder="", ext="", hideext=True):
        res = []
        list = renpy.list_files()
        for i in list:
            if i.startswith(folder) or (not folder):
                if folder:
                    s = i[(len(folder) + 1):]
                else:
                    s = i
                if ext:
                    if s.endswith("." + ext):
                        if hideext:
                            s = s[:(-len(ext) - 1)]
                        res.append(s)
                else:
                    res.append(s)
        if len(res) > 1:
            # сортировка без учета регистра
            res = sorted(res, key=lambda s: s.lower())
        return res

    # окно игры в центре экрана (вызывается из init)
    def window_center():
        import os
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    # автоматическое объявление изображений (вызывается из init)
    def images_auto(folders=["images"]):
        config.automatic_images_minimum_components = 1
        config.automatic_images = [' ', '_', '/']
        config.automatic_images_strip = folders

    # остановить перемотку
    def stop_skip():
        renpy.config.skipping = None

    # строку в displayable
    def img2disp(displayable):
        if isinstance(displayable, (str, unicode)):
            return renpy.displayable(displayable)
        return displayable

    # узнать текущие размеры изображения типа displayable
    # например, после масштабирования и других операций
    # не работает в разделе init
    def get_size(displayable, w=config.screen_width, h=config.screen_height, st=0, at=0):
        w, h = renpy.render(img2disp(displayable), w, h, st, at).get_size()
        return int(w), int(h)
    def get_width(displayable):
        return get_size(displayable)[0]
    def get_height(displayable):
        return get_size(displayable)[1]

    # если это не список, то сделать единственным элементом списка
    def make_list(param):
        if param is None:
            return None
        if not isinstance(param, list):
            param = [param]
        return param

# автоматическое объявление анимации
    # описание функции Ani:
    # автоматическое объявление картинки с анимацией,
    # например есть кадры "images/neko%s.png",
    # где %s - числа от 1 до 5, тогда объявляем анимацию так:
    # image neko = Ani("neko", 5, 0.5, reverse = False)
    # где:
    # img_name - имя файла без номера (например, "neko")
    # frames - количество кадров
    # delay - пауза между кадрами в секундах
    # если delay это кортеж, например (1, 2), то скорость будет меняться от 1 до 2 секунд
    # loop - зациклить анимацию (по умолчанию включено)
    # reverse - нужно ли проигрывание анимации в обратную сторону
    # effect - эффект для смены кадров
    # start - с какой цифры начинать отсчет кадров
    # ext - расширение, если оно отлично от Null, то работаем с файлами,
    # при ext=Null - с displayable (уже объявленными или даже измененными изображениями)
    # так же можно добавлять любые стандартные для изображений параметры, типа масштабирования или прозрачности:
    # image neko = Ani("neko", 5, 0.5, zoom=2.0, alpha=0.75)
    def Ani(img_name, frames, delay=.1, loop=True, reverse=False, effect=Dissolve(.1, alpha=True), start=1, ext=None, **properties):
        args = []
        # если пауза переменная, то вычисляем ее шаг
        if isinstance(delay, tuple):
            d0 = delay[0]
            d1 = delay[1]
            f = (frames - 1)
            if f <= 0:
                dp = 0
            else:
                dp = (d1 - d0) * 1. / f
            delay = d0
        else:
            dp = 0
        # перебираем все кадры анимации
        for i in range(start, start + frames):
            if ext:
                img = renpy.display.im.image(img_name + str(i) + "." + ext)
            else:
                img = img2disp(img_name + str(i))
            img = Transform(img, **properties)
            args.append(img)
            if reverse or loop or (i < start + frames - 1):
                args.append(delay)
                delay += dp
                # добавляем эффект для смены кадров
                args.append(effect)
        if reverse: # обратная анимация, если нужна
            dp = -dp
            delay += dp
            for i in range(start + frames - 2, start, -1):
                if ext:
                    img = renpy.display.im.image(img_name + str(i) + "." + ext)
                else:
                    img = img2disp(img_name + str(i))
                img = Transform(img, **properties)
                args.append(img)
                if loop or (i > start + 1):
                    args.append(delay)
                    delay += dp
                    args.append(effect)
        return anim.TransitionAnimation(*args)

    # показать фон с именем bg указанного цвета color
    def bg(color="#000", bg="bg"):
        renpy.scene()
        renpy.show(bg, what=img2disp(color))

    # меняем стандартное время всех или некоторых эффектов для появления/исчезновения спрайтов
    def move_time(delay=.5, effects=["move", "ease"]):
        effects = make_list(effects)
        for i in effects:
            define.move_transitions(i, delay)

    def cur_time(tformat="%H:%M:%S"):
        return datetime.datetime.now().strftime(tformat)

    import datetime

    # для цифровых часиков (не менять, не вызывать)
    def clock_f(st, at, tformat="%H:%M:%S", **kwarg):
        return Text(cur_time(tformat), **kwarg), .25

    # создать цифровые часики:
    # image clock = Clock(size=48, color="#fff8", outlines=[(2, "#0008", 0, 0)], align=(.05, .05))
    def Clock(**kwarg):
        return DynamicDisplayable(clock_f, **kwarg)

    # показать экран на слое "мастер",
    # чтобы он не исчезал, когда прячем интерфейс
    def show_s(screen, *arg, **kwarg):
        renpy.show_screen(screen, _layer="master", *arg, **kwarg)

    # убрать экран со слоя "мастер"
    def hide_s(screen, **kwarg):
        renpy.hide_screen(screen, layer="master", **kwarg)

    # добавляем неубирающийся по hide_interface слой
    if not "forever" in config.layers:
        config.layers.insert(config.layers.index("screens"), "forever")

    # показать неубирающийся по нажатию "h" экран
    def show_forever(screen):
        renpy.show_screen(screen, _layer="forever")

    # спрятать неубирающийся по нажатию "h" экран
    def hide_forever(screen):
        renpy.hide_screen(screen, layer="forever")

    # получить английское название времени суток
    # если не указывать время в часах,
    # то будет взято системное время
    # можно задать начало утра, дня, вечера и ночи в часах от 0 до 23
    def time_of_day(hours=None, morning=7, day=11, evening=18, night=23):
        if hours is None:
            hours = int(datetime.datetime.now().strftime("%H"))
        res = "night" # по умолчанию ночь
        # границы любого времени суток можно поменять
        if (hours >= morning) and (hours <= day):
            res = "morning"
        if (hours > day) and (hours <= evening):
            res = "day"
        if (hours > evening) and (hours < night):
            res = "evening"
        return res

    # словарь цветов для времен суток
    color_filters = {"morning": "#8404", "day": "#0000", "evening": "#0484", "night": "#000b"}

    # получить цвет фильтра, соответствующий времени суток
    def color_of_day(hours=None):
        return color_filters[time_of_day(hours)]

    # удалить все сохранения
    def delete_saves_now():
        all = renpy.list_saved_games(fast=True)
        for i in all:
            renpy.unlink_save(i)
        renpy.restart_interaction()
    DeleteSavesNow = renpy.curry(delete_saves_now)

    # удаление всех сохранений с запросом подтверждения
    def delete_saves(confirm=True):
        if confirm:
            layout.yesno_screen(message=_("Удалить все сохранения?"), yes=DeleteSavesNow(), no=NullAction())
        else:
            delete_saves_now()
    DeleteSaves = renpy.curry(delete_saves)

    # очистить постоянные данные и сохранения
    def delete_data_now():
        # удаление сохранений
        delete_saves(False)
        # удаление ачивок
        # achievement.clear_all()
        # achievement.sync()
        # удаление постоянных данных
        persistent._clear(progress=True)
        # выход из игры
        Quit(confirm=False)()
    DeleteDataNow = renpy.curry(delete_data_now)

    # удаление всех данных и сохранений с запросом подтверждения
    def delete_data(confirm=True):
        if confirm:
            layout.yesno_screen(message="Удалить все данные?\nИгра будет закрыта.", yes=DeleteDataNow(), no=NullAction())
    DeleteData = renpy.curry(delete_data)

    # действие - продолжить игру оттуда, где закончили
    # если загружать пока нечего, то кнопка неактивна
    # textbutton _("Продолжить игру") action Continue()
    class Continue(Action, DictEquality):
        def __call__(self):
            FileLoad(1, confirm=False, page="auto", newest=True)()
        # кликабельность кнопки
        def get_sensitive(self):
            return FileLoadable(1, page="auto")

    # объявлена ли картинка с именем name
    def has_image(name):
        for i in renpy.display.image.images:
            # такая конструкция позволяет исключить пустые теги
            if name == " ".join(" ".join(i).split()):
                return True
        return False

    # проверить существование нескольких изображений через запятую
    def has_images(*args):
        res = True
        for i in args:
            # вместо какой-то картинки может быть список или кортеж
            if isinstance(i, (list, dict)):
                res = res & has_images(i)
            else:
                res = res & has_image(i)
        return res

    # задан ли курсор с таким именем
    def has_mouse(mouse):
        if config.mouse:
            if mouse in config.mouse.keys():
                return True
        return False

    # рандомный элемент из параметров на входе
    # просто сокращаем писанину
    def rnds(*args):
        return renpy.random.choice(args)

    # рандомное целое число в заданных пределах
    # второй предел НЕ включительно, как в питоне
    # (i_to можно не указывать, тогда максимум берется из i_from)
    def rnd(i_from=0, i_to=None):
        if i_to is None:
            i_to = i_from
            i_from = 0
        return renpy.random.randint(int(i_from), int(i_to - 1))

    # рандомное дробное число в заданных пределах
    # (f_to можно не указывать, тогда максимум берется из f_from)
    def rndf(f_from=0, f_to=None):
        if f_to is None:
            f_to = f_from
            f_from = .0
        return f_from + renpy.random.random() * (f_to - f_from)

    # канал для зацикленного эффекта
    renpy.music.register_channel("effect", "sfx", loop=True)

    # зацикленный звуковой эффект, не музыка
    def sfxplay(name, channel="effect", loop=True, fadein=1, fadeout=1, ext="ogg", audio_dir=audio_dir):
        if name:
            renpy.music.play(audio_dir + "/" + name + "." + ext, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # костыли для звуков и музыки - сокращают писанину
    # можно запускать музыку или звуки, не указывая папки и расширения
    # по умолчанию для музыки music/*.ogg
    # по умолчанию для звуков audio/*.ogg

    # запустить музыку или плейлист
    def mplay(mname, fadein=1, fadeout=1, loop=True, channel="music", ext="ogg"):
        list = []
        mname = make_list(mname)
        for i in mname:
            list.append(music_dir + "/" + i + "." + ext)
        renpy.music.play(list, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # запустить музыку или случайно перемешанный плейлист
    def rndplay(mname, fadein=1, fadeout=1, loop=True, channel="music", ext="ogg"):
        list = make_list(mname)
        if len(list) > 1:
            renpy.random.shuffle(list)
        mplay(list, fadein, fadeout, loop, channel, ext)

    # перезапустить музыку, даже если уже играет она же
    def mreplay(mname, fadein=1, fadeout=1, loop=True, channel="music", ext="ogg"):
        new_fn = music_dir + "/" + mname + "." + ext
        renpy.music.play(new_fn, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    # убрать из строки теги типа <from 0.2>
    def mdeletetags(str):
        return re.sub(re.compile('<.*?>'), '', str)

    # запустить музыку для имени файла и пути
    def fnplay(new_fn, fadein=1, fadeout=1, channel="music", restart=True):
        old_fn = renpy.music.get_playing()
        if restart or (mdeletetags(old_fn) != mdeletetags(new_fn)):
            renpy.music.play(new_fn, channel=channel, loop=True, fadein=fadein, fadeout=fadeout)

    # последняя сохраненная мелодия
    last_music_fn = ""

    # сохранить в памяти играющую мелодию
    def msave():
        store.last_music_fn = renpy.music.get_playing()

    # восстановить игравшую при сохранении мелодию
    def mrestore(fadein=1, fadeout=1, channel="music"):
        if last_music_fn:
            fnplay(last_music_fn, fadein=fadein, fadeout=fadeout, channel=channel, restart=False)

    # воспроизвести звук для канала audio, который поддерживает многопоточность
    def splay(mname, fadein=0, fadeout=0, channel=config.play_channel, ext="ogg", audio_dir=audio_dir):
        if mname:
            mname = make_list(mname)
            lst = []
            for i in mname:
                lst.append(audio_dir + "/" + i + "." + ext)
            renpy.play(lst, channel=channel, fadein=fadein, fadeout=fadeout)

    # воспроизвести звук
    def sndplay(mname, fadein=0, fadeout=0, channel="sound", ext="ogg", audio_dir=audio_dir):
        if mname:
            mname = make_list(mname)
            lst = []
            for i in mname:
                lst.append(audio_dir + "/" + i + "." + ext)
            renpy.play(lst, channel=channel, fadein=fadein, fadeout=fadeout)

    # голос
    def vplay(mname, fadein=0, fadeout=0, channel="voice", ext="ogg"):
        if mname:
            renpy.play("voices/" + mname + "." + ext, channel=channel, fadein=fadein, fadeout=fadeout)

    # остановить звук
    def sstop(fadeout=None, channel='audio'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить звук
    def sndstop(fadeout=0, channel='sound'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить музыку
    def mstop(fadeout=1, channel='music'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # остановить зацикленный эффект
    def sfxstop(fadeout=1, channel='effect'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    # превращаем функции в action для экранов screen
    SPlay = renpy.curry(splay)
    SFXPlay = renpy.curry(sfxplay)
    SFXStop = renpy.curry(sfxstop)
    MPlay = renpy.curry(mplay)
    FNPlay = renpy.curry(fnplay)
    VPlay = renpy.curry(vplay)
    SStop = renpy.curry(sstop)
    MStop = renpy.curry(mstop)

    import re

    # получить словарь с найденными в строке тегами и их значением
    def get_tags(text, prefix='#'):
        res = {}
        # выуживаем все теги ремарок
        tags = re.findall('{' + prefix + '([^}]+)}', text)
        # перебираем полученные теги
        for i in tags:
            parts = i.split('=')
            if len(parts) > 0:
                key = parts[0].strip()
                val = None
                if len(parts) > 1:
                    val = parts[1]
                # добавляем тэг и его значение в словарь
                res[key] = val
        # возвращаем значения тэгов в виде словаря
        return res

    # убрать все тэги из строки
    def del_tags(txt, prefix='#'):
        if txt:
            return re.sub(r'{' + prefix + '([^}]+)}', '', txt)
        else:
            return txt

    # получить тэги и вернуть их в виде списка строк
    def get_tags_str(text, prefix='#'):
        # выуживаем все теги ремарок
        return re.findall('{' + prefix + '([^}]+)}', text)

    # разделить строку на две части - до и после знака равно
    # (или другого разделителя) и убрать пробелы вокруг этих частей
    def get_key_val(text, sep='='):
        txt = text.split(sep, 1)
        val, key = None, None
        if len(txt) > 0:
            key = txt[0].strip()
        if len(txt) > 1:
            val = txt[1].strip()
        return key, val

    # поиск в строке значения невидимого читателю тега
    # пример использования:
    # $ text = "Текст текст {#image=logo.png} текст."
    # $ img = get_tag(text, 'image')
    # на выходе в img будет logo.png
    def get_tag(text, tag, default=None, prefix='#'):
        tag = tag.strip()
        tags = get_tags(text, prefix)
        if tag in tags.keys():
            return tags[tag]
        return None

    # есть ли тэг в строке
    def have_tag(text, tag, prefix='#'):
        return tag in get_tags(text, prefix).keys()

    # нужно включить автоматические сохранения, чтобы работала Continue
    config.has_autosave = True

    # список спрайтов на экране (не только тегов)
    def get_showing_sprites(layer='master'):
        images = []
        tags = renpy.get_showing_tags(layer)
        for i in tags:
            tag = i
            atrs = renpy.get_attributes(i, layer)
            for a in atrs:
                tag += " " + a
            images.append(tag)
        return images

    # показан ли спрайт на экране
    def sprite_showed(image, layer='master'):
        return image in get_showing_sprites(layer)

    # найти на экране спрайт, содержащий тег
    def get_sprite_by_tag(tag, layer='master'):
        if tag:
            # если среди всех спрайтов на экране
            images = get_showing_sprites(layer)
            for i in images:
                # есть тот, что содержит нужный тэг
                if str(tag) in str(i):
                    return str(i)
        # если на экране нет говорящего персонажа
        return None

    # получить параметры спрайта
    def get_sprite_bounds(tag, layer='master'):
        # если не нашли спрайт
        x, y, w, h = -1, -1, -1, -1
        # ищем спрайт на экране
        i = get_sprite_by_tag(tag, layer)
        # если спрайт на экране
        if i:
            x, y, w, h = renpy.get_image_bounds(i, layer=layer)
        return int(x), int(y), int(w), int(h)

    # полное копирование
    import copy as dcopy
    def copy(*args):
        return dcopy.deepcopy(*args)

    # входит ли в строку where подстрока what
    # или одна из подстрок, если what - список или кортеж
    def has_text(where, what):
        if isinstance(what, (str, unicode)):
            what = [what]
        for i in what:
            if i in where:
                return True
        return False

    # существует ли переменная с заданным именем
    def has_val(key):
        return key in globals().keys()

# БЛОК ДЛЯ РАБОТЫ С ВРЕМЕНАМИ СУТОК
# как пользоваться:

# 1) если есть нужные рисунки, то назвать файлы по временам суток:
# bg_street_night, bg_street_morning и т.д. по списку
# в противном случае будет перекрашиваться основная картинка
# например, "bg street day" или скопированная в неё "bg street"
# первый суффикс в списке времён суток можно и не указывать: bg street

# 2) воспользоваться автоматическим объявлением спрайтов в блоке init:
# $ images_auto()

# 3) указать перфиксы спрайтов, которые будут зависеть от времени суток
# например, чтобы все фоны и все спрайты eileen и pytom зависели от времени суток:
# daytime_prefix = ["bg", "eileen", "pytom"]

# 4) при необходимости задать список времён суток, по умолчанию он:
# alldaytime = ["day", "night"]

# 5) в скрипте просто задавать время суток $ setdaytime("night")
# или переключение на следующее по списку (зациклено): $ setdaytime()
# спрайты на экране сразу поменяются

init:
    # настройки нового освещения, на входе сразу матрица
    transform daytime_light(matrix):
        matrixcolor matrix

    transform daytime_empty():
        pass

init -99 python:
    # список допустимых времён суток
    # "night" - обязательно!
    alldaytime = ["day", "night"]

    # список префиксов-меток для динамических спрайтов,
    # освещение которых будет зависеть от времени суток в curdaytime
    # например, все фоны и пара героев:
    # daytime_prefix = ["bg", "eileen", "pytom"]
    # к таким именам будет добавлен суффикс из daytime_suffix
    # а потом они будут превращены в динамические уже со своими именами без суффикса
    daytime_prefix = []

    # настройки каждого времени суток для перекрашивания фонов и спрайтов
    # (color, brightness, saturation, contrast)
    day_bg_attrs = ("#000", 0, 1, 1)
    day_attrs = ("#000", 0, 1, 1)
    evening_bg_attrs = ("#9af", -.2, .8, 1)
    evening_attrs = ("#9af", 0, .9, 1)
    night_bg_attrs = ("#9af", -.475, .375, .575)
    night_attrs = ("#9af", -.1, .375, 1)
    morning_bg_attrs = ("#fca", .1, 1, 1)
    morning_attrs = ("#fca", .1, 1, 1)

    # по умолчанию первое в списке время суток
    curdaytime = alldaytime[0]

    # суффикс для динамических спрайтов - первое в списке время суток
    daytime_suffix = alldaytime[0]

    # здесь будут храниться имена изменённых спрайтов, зависимых от curdaytime
    daytime_suffixed = []

    # префикс-метка для фонов
    bg_prefix = "bg"

    # переключение времени суток на новое или на следующее, если не указывать, на какое
    def setdaytime(newdaytime=None, effect=dissolve):
        if newdaytime is None:
            # если новое время суток == None,
            # то переключаемся на следующее в списке (по кругу)
            i = alldaytime.index(curdaytime) + 1
            if i >= len(alldaytime):
                i = 0
            newdaytime = alldaytime[i]
        if effect:
            renpy.show("black", tag="daytimeblack")
            renpy.with_statement(effect)
        store.curdaytime = newdaytime
        if effect:
            renpy.hide("daytimeblack")
            renpy.with_statement(effect)

    # получить трансформ с матрицей для ночного освещения
    # по умолчанию для спрайта, True - для фона
    def atdaytime(bg=False):
        if bg:
            key = "_" + bg_prefix + "_"
        else:
            key = "_"
        key = curdaytime + key + "attrs"
        attrs = ("#000", 0, 1, 0)
        if key in globals().keys():
            color, brightness, saturation, contrast = globals()[key]
            matrix = BrightnessMatrix(brightness) * ContrastMatrix(contrast) * TintMatrix(color) * SaturationMatrix(saturation)
            return daytime_light(matrix)
        return daytime_empty()

# БЛОК ДЛЯ ДОПОЛНЕННОГО АВТООБЪЯВЛЕНИЯ СПРАЙТОВ
# стандартное автообъявление картинок, но с webp
# плюс не разбиваются на теги имена, предназначенные для LayerdImage
# вместо этого объединяются через нижний минус "_"
# префиксы, по которым определяются такие имена берутся из layered_prefixes
# выполняется после всего остального
init 1900 python hide:
    def create_automatic_images():

        seps = config.automatic_images

        if seps is True:
            seps = [ ' ', '/', '_' ]

        for dir, fn in renpy.loader.listdirfiles():

            if fn.startswith("_"):
                continue

            # только .png и .jpg и .jpeg и .webp
            if not (fn.lower().endswith(".png") or fn.lower().endswith(".jpg") or fn.lower().endswith(".jpeg") or fn.lower().endswith(".webp")):
                continue

            # убираем расширения и заменяем слеши.
            if fn.lower().endswith(".jpeg") or fn.lower().endswith(".webp"):
                shortfn = fn[:-5].replace("\\", "/")
            else:
                shortfn = fn[:-4].replace("\\", "/")

            # делим строку на части
            name = ( shortfn, )
            for sep in seps:
                name = tuple(j for i in name for j in i.split(sep))

            # выбрасываем имя папок из тегов
            while name:
                for i in config.automatic_images_strip:
                    if name[0] == i:
                        name = name[1:]
                        break
                else:
                    break

            # для проверки префиксов и суффиксов после
            # возможной склейки тегов
            prefix = name[0]
            suffix = name[len(name) - 1]

            # убираем суффикс, если это первое время суток
            if suffix == daytime_suffix:
                name = name[:-1]

            # имя без суффикса
            name0 = name

            # теги одной строкой
            sname = " ".join(name)

            # не делим на части имена, которые начинаются с префиксов для LayeredImage
            layered = False
            if prefix in layered_prefixes:
                name = "_".join(name)
                sname = name
                layered = True

            # добавляем суффикс по умолчанию, если начинается
            # с префикса из списка меток для динамических спрайтов,
            # которые будут менять освещение в зависимости от времени суток
            if prefix in daytime_prefix:
                # нельзя автоматизировать файлы с суффиксами времён суток,
                # потому что они станут частью автоматизированного спрайта
                if not suffix in alldaytime[1:]:
                    if not sname in daytime_suffixed:
                        # запоминаем имя изменённого спрайта
                        store.daytime_suffixed.append(sname)
                        # добавляем суффикс
                        if layered:
                            name = name + " " + daytime_suffix
                        else:
                            name = (*name, daytime_suffix)

            # игнорируем, если уже создана одноимённая копия с суффиксом
            if name0 in daytime_suffixed:
                continue

            # игнорируем, если не набирается указанное в переменной количество тегов
            if len(name) < config.automatic_images_minimum_components:
                continue

            # игнорируем, если такой спрайт уже есть
            if name in renpy.display.image.images:
                continue

            # если тег один, но требуется для многослойных картинок, то добавляем в конце "_"
            if layered and not "_" in name:
                name = name + "_"

            # объявляем спрайт
            renpy.image(name, fn)

    # если заданы параметры, то объявляем спрайты автоматом
    if config.automatic_images:
        create_automatic_images()

    # функция для динамического освещения спрайтов и фонов
    def def_daytime(st, at, img):
        # ищем картинку для текущего времени суток
        new = img + " " + curdaytime
        if has_image(new):
            return new, None
        # если не нашли, то берем основную
        new = img + " " + daytime_suffix
        # и перекрашиваем в соответствии с настройками
        if img.startswith(bg_prefix):
            return At(new, atdaytime(True)), None
        return At(new, atdaytime()), None

    # если заданы параметры, то создаём динамически освещённые спрайты
    if len(daytime_suffixed) > 0:
        # перебираем все спрайты, для которых нужна реакция на освещение
        for i in daytime_suffixed:
            # создаём такие спрайты
            renpy.image(i, DynamicDisplayable(def_daytime, i))
