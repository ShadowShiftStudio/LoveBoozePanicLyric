define sanya = Character("[player_name] ", color="#aad2ff")
define pasha = Character('Пашка Запивон ', color="#ffc9aa")
define yuli = Character('Юля ', color="#ffaaff")
define nadya = Character('Надя ', color="#ffaab1")
define storyteller = Character('Рассказчик ', color="#b3aaff")
define valeria = Character('Валерия Владимировна', color="#aaffd7")
define grusha = Character('Агриппина Филипповна ', color="#12d69b")
define pavel = Character('Павел Геннадьевич ', color="#ffb4aa")
define skin = Character('Мыкало ', color="#e1ffaa")
define noname = Character('Незнакомец ', color="#999999")
define emily = Character('Эмилия', color="#e28cd7")

#для рекламы в будущем

# init python:
#   if renpy.android:
#     banner = yandex_ads.create_banner()

#     # первым делом необходимо установить размер баннера
#     # помните - сделать это можно только один раз
#     banner.set_sticky_size(-1)

#     # по умолчанию баннер будет находиться "под игрой"
#     # с помощью set_position можно изменить положение баннера в любое время
#     banner.set_position('above_game') # при значении above_game, баннер будет находиться "над игрой"

#     # ad_unit_id можно взять в партнёрском кабинете
#     banner.set_ad_unit_id("R-M-XXXXXX-Y")

#     # не забудьте загрузить объявление
#     banner.load_ad()

init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

        Shake = renpy.curry(_Shake)
    


init python :

    def mplay(fn, chan = "music", fin = 1.0, fout = 1.0):
        renpy.music.play(fn, channel = chan, loop = True, fadein = fin, fadeout = fout)
        # канал на паузу
    def mpause(channel = "music"):
        c = renpy.audio.audio.get_channel(channel)
        c.pause()
        # снять с паузы
    def munpause(channel = "music"):
        c = renpy.audio.audio.get_channel(channel)
        c.unpause()
        # остановить мелодию
    def mstop(chan = "music", fout=1.0):
        renpy.music.stop(channel = chan, fadeout = fout)

init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

define day1_pasha_kfc = False
define day1_sanya_wants_camp = False
define day1_pasha_lose_in_drinking = False
define day1_yuli_agreed_after_kfc = False
define day2_sanya_went_to_smoke = False
define day2_sanya_vote_for_ussr = False
define day2_nadya_bought_cigarettes = False
define day2_nadya_get_one_sigarett = False
define day2_choosen_instead_yuli = False
define day2_nadya_have_a_dialog = False
define day3_go_with_nadya = False
define day3_go_with_yuli = False
define day3_choice_yuli = False
define day3_choice_nadya = False
define day3_choice_lonely = False
define day4_smoke_after_words_valeria = False
define day4_tried_move = False
define day4_take_pill = False
define day4_drink = False
define day4_yuli_meal = False
define day4_nadya_meal = False
define day4_smoke_old_siggarete = False
define day4_walk_in_park = False
define day4_suicide = False
define day4_go_with_emily = False
define day4_smoke_with_pavel = False
define day4_fight = False
define day4_with_skin = False
define day5_good_mood = False
define day5_normal_mood = False
define day5_bad_mood = False
define day5_loneliness_in_cafe = False
define day5_nadya_in_cafe = False
define day5_emily_in_cafe = False
define day5_almost_sex_with_nadya = False
define day5_sanya_love_yuli = False
define day5_go_look_for_emilia = False
define day5_kiss_emilia = False
define day5_help_emily_panic = False
define day5_look_for_yuli = False
define day5_run_with_skin = False
define mood_counter = 0

define rel_yuli = 0
define rel_nadya = 0
define rel_pasha = 0
define rel_pavel = 0
define rel_skin = 0
define rel_valeria = 0
define rel_emily = 2
define hi_score = 0

define player_name = "Саня"
define str_for_notification = ""
image cigarette_smoke = Movie(play="images/video/loopen.webm", side_mask=True)

screen notification_popup():
    add "firstDays/notification.png" xalign 1.0 yalign 0.055 xzoom 0.6
    text "[str_for_notification]" xalign 0.99 yalign 0.06 color "#ffffff" 

screen notification_popup_big():
    add "firstDays/notification.png" xalign 1.0 yalign 0.055 
    text "[str_for_notification]" xalign 0.99 yalign 0.06 color "#ffffff" 

screen toska():
    add "firstDays/night color.png":
        at transform:
            xalign 0.5 yalign 0.5
            alpha 0.0
            linear 4.0 alpha 1.0
            block:
                linear 1.0 zoom 1.2 alpha 0.9
                linear 0.6 zoom 1.0 alpha 1.0
                repeat

screen yuli_welcome():
        add "images/yuli/welcome.jpg"
        add Movie(play="images/video/petals.webm", side_mask=True)
        add "images/yuli/welcome_focus.png":
            at transform:
                truecenter
                block:
                    easein 1.0 zoom 1.02 
                    easeout 0.6 zoom 1.0 
                    repeat

screen nadya_welcome():
        add "images/nadya/welcome.jpg"
        add Movie(play="images/video/petals.webm", side_mask=True)
        add "images/nadya/welcome_focus.png":
            at transform:
                truecenter
                block:
                    easein 1.0 zoom 1.02 
                    easeout 0.6 zoom 1.0 
                    repeat

screen emily_welcome():
        add "images/emily/welcome.jpg"
        add Movie(play="images/video/petals.webm", side_mask=True)
        add "images/emily/welcome_focus.png"

screen busday1():
        default bus_minigame = BusMinigameDisplayable(hi_score, 0)
        add bus_minigame


label splashscreen:
    play sound "audio/intro_sound.mp3" 
    image temp_m = Movie(play="gui/splashscreen_sanya.webm", loop=False, start_image="gui/sanya.jpg")
    image back = "#272727"
    image log_o = "gui/logotype.png"
    image sanya_first_frame = "gui/sanya.jpg" 
    scene back
    with dissolve

    show logo studio logo at center with Dissolve(1.6)
 
    pause 2.0

    scene back 
    with Dissolve(1.5)

    show logo disclaimer with dissolve
    
    pause 100.0
    stop sound
    scene temp_m with Fade(0.0, 0.1, 0.06, color="#272727")
    show log_o:
        xalign 0.02 yalign 0.1 alpha 0.0
        linear 0.16 alpha 1.0

    pause 0.16

    return

label start:
    jump first_day

label first_day:
    image night = "firstDays/night color.png"
    scene firstDays black scen
    
    play music "audio/alarm-sound.mp3" volume 0.2
    "*Звук будильника*"
    stop music
    play sound "audio/alarm-sound-end.mp3" volume 0.5
    $ renpy.pause(2, hard=True)
    stop sound

    scene sanya room 
    with fade

    play sound "audio/deep-moan.mp3"
    "*Вздох*"
    $ renpy.pause(1, hard=True)

    play music "audio/einaudi_nefeli.mp3" volume 0.21

    "Ну что, день первый пошёл..."
    "Как же меня это всё достало: эти бесконечные лабораторные работы, сдачи курсачей..."
    "A экзамены так вообще смех какой-то: ты забиваешь на учёбу болт весь семестр, а потом в поте лица пыхтишь без сна над какой-нибудь электротехникой, которая тебе нахрен не сдалась!"
    "Всё бы ничего, но я, конечно, далеко не такого ожидал, когда поступал в универ."
    "Эх, как же хочу вернуться в школьные годы, когда ты вечно ищешь способы поднять бабок на алкашку." 
    "Затем идёшь в \"проверенный ларёчек\" и покупаешь литр водки на литр колы в обычные дни или же литр водки на литр апельсинового сока по праздникам."
    "Сейчас это звучит ужасно, но в этом явно есть своя романтика подростковых лет..."
    "А теперь я уже совсем старый стал, – 20 лет ёпте! Сменил вот недавно паспорт, теперь даже над фоткой в нём не поржать."
    "Господи, как ссать-то охота..."

    stop music fadeout 2.0
    pause (0.5)

    scene sanya toilet day without water
    with fade
    
    play sound "audio/toilet-sound.mp3" volume 0.1
    "*Звук смыва унитаза*"
    stop sound

    scene firstDays black scen 
    with fade

    play sound "audio/street-music.mp3" volume 0.4 
    pause (2.0)
    scene firstDays bus station 
    with fade

    "Когда я иду ранним тихим утром по улице, мне кажется, что в голове у меня нескончаемый каскад мыслей." 
    "\"Не слишком ли много я пью в последнее время?\"" 
    "Cпрашиваю я себя, и в голове зарождается нотка беспокойства."
    stop sound fadeout 10.0
    play music "audio/bad_dream.mp3" volume 0.5 fadein 10.0
    image nc = "firstDays/night color.png"
    show nc:
        xalign 0.5 yalign 0.5
        alpha 0.0
        linear 10.0 alpha 0.6
        block:
            linear 1.0 zoom 1.2 alpha 0.5
            linear 0.6 zoom 1.0 alpha 0.6
            repeat
    "Я как будто уже и не помню себя трезвым...."
    "Что со мной происходит? Как я допустил, чтобы всё дошло до такого состояния?" 
    "Раньше я был гораздо ответственнее и отдавал себе отчёт в своих поступках." 
    "Сейчас же кажется, что каждый день становится похож на предыдущий," 
    extend " и я даже не помню, когда последний раз был настоящим собой — трезвым и ясно мыслящим."
    "Я делаю глубокий вдох, пытаясь очистить голову, но мысли продолжают метаться."
    "Может быть, мне стоит отказаться от алкоголя, – размышляю я, пытаясь найти подобие равновесия."
    "Речь идет не только о здоровье, но и о восстановлении контроля над своей жизнью."
    stop music fadeout 0.5
    play sound "audio/bus.mp3" volume 0.07 fadein 1.4
    hide nc 
    "Из бесконечного потока мыслей меня смог вытащить только гудок подъезжающего ЛИАЗа."
    "А вот и мой автобус подъезжает."    
    sanya "Ладно, пора и честь знать."

    play sound "audio/sound-in-bus.mp3" volume 0.05

    scene firstDays bus 
    with fade
    "Даже матушку свою довёл."
    "Вчера с мужиками пришли пиво пить, последний день лета проводить, скажем так, а она меня поджидает у туалета и говорит:"
    "\"Хоть бы раз домой вернулся с девчонкой какой-нибудь красивенькой, а не как обычно с парнями в зассаных майках\", — \"Мама, ну мы же панки\"..."
    "Впрочем, ладно. У меня есть немного времени, чтобы поспать. Надо было ночью не заниматься хернёй..."
    
    scene black with fade
    if renpy.mobile:
        centered "{size=+24}Нажимайте на вверхнюю и нижнюю части экрана{/size}" 
    else:
        centered "{size=+24}Используйте стрелочки вверх-вниз или клавиши W, S{/size}" 
    window hide
    call screen busday1


    if int(_return) > int(hi_score):
        scene black
        centered "{size=+50}Новый рекорд!{/size}"
        centered "{size=+50}Счёт: [_return]{/size}"


    $ hi_score = max(hi_score, int(_return))
    

    scene firstDays black scen 
    with fade
    "Какой странный сон мне приснился..."
    "Бесконечно едешь прямо... Как далеко можно так уехать?"
    play sound "audio/bus.mp3" volume 0.03
    $ renpy.pause (7.5)
    stop sound fadeout 1.5
    play music "audio/street-sound.mp3" volume 0.1
    scene firstDays bus station near nstu 
    with fade

    show pasha neutral:
        alpha 0.0 xalign 0.5 yalign 1.0
        # Take 1.0 seconds to move things back to the left.
        linear 1.0 xalign 0.6 alpha 1.0

    "Только вышел из автобуса, как тут мне навстречу идёт крупный парень, он явно меня узнал, а вот я его не очень..."
    "Ба-а, так это же Пашка Запивон так за лето подкачался!"
    pasha "Дарова, Саня, как сам, как жизнь? Целое лето тебя не видел же!"
    sanya "Паша, а я тебя и не узнал сперва, накачался за лето я вижу!"
    pasha "Да так, самую малость."

    show pasha smiles with dissolve

    pause 2.0

    pasha "Слышь, Саня, говорили ты фамилию себе изменил, женился что ли?"
    sanya "Да там свои приколы с этим, ну захотелось мне просто фамилию новую, начать жизнь, знаешь, с чистого листа."
    pasha "А чё имя-то не сменил тогда?"
    sanya "А чё с ним не так? Имя Саня – Заебись!"
    
    $ player_name = "Саня "
    $ player_name_buf = renpy.input("Во дела. Ладно, меченый, как звать-то тебя теперь? \nСаня ...", length=16, allow="ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю")
    $ player_name_buf = player_name_buf.strip()
    $ player_name_buf = player_name_buf.lower().title()
    
    if player_name_buf == "" :
        $ player_name = "Саня Юрченко"
        $ player_name_buf = "Юрченко"
        $ player_name_tmp = player_name_buf
    else :
        $ player_name += player_name_buf
        $ player_name_tmp = player_name_buf

    sanya "[player_name]"
    pasha "О-о-о, панковская фамилия, я вижу! Ну такое дело надо отметить!!"
    pasha "[player_name_buf], пошли сегодня в кефас пиво пить, я тебя ещё за двадцатилетие за уши не тягал!"
    sanya "Ну смотри, у меня одна пара, а потом никаких планов. Пошли, конечно, без проблем."
    pasha "Ну всё, патлатый, жду тебя возле курилки после пар. Если че, у меня мобила скоро сядет. Так что давай без сюрпризов."

    hide pasha smiles 
    with dissolve

    $ renpy.pause(1.5)

    show pasha sad 
    with dissolve

    pasha "Сань, я, походу, уже забыл..."
    pasha "Как там тебя зовут, ещё раз?"
    
    $ player_name = "Саня "
    $ player_name_buf = renpy.input("Ну я же говорю  \nСаня ...", length=16, allow="ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю")
    $ player_name_buf = player_name_buf.strip()
    $ player_name_buf = player_name_buf.lower().title()

    if player_name_buf == "" :
        $ player_name = "Саня Юрченко"
        $ player_name_buf = "Юрченко"
    else :
        $ player_name += player_name_buf
    
    if player_name_buf != player_name_tmp :
        pasha "А-а-а, а я почему-то запомнил [player_name_tmp], ну ладно, [player_name_buf], теперь никогда не забуду!"
    else :
        pasha "А-а-а, ну я так и запомнил! Давай, [player_name_buf], бывай!"
    
    hide pasha sad
    with dissolve
    stop music
    $ renpy.pause(1.0)

    scene firstDays lecture scen 
    with fade
    play sound "audio/table_punch.mp3"
    $ renpy.pause(2)
    "Преподаватель" "Встаём, студенты. Здравствуйте, поздравляю вас с началом нового учебного года, меня зовут..."
    stop sound

    $ mplay("audio/lecture-sound.mp3")
    pause (1.0)

    "Какая же скукота, вроде новый предмет, а начинается всё по-старому:"
    "\"Фсем привет, я Такой-то Такойтович. М-м-мой претмет будет непрасты-ы-ым, но я вас фсе-ему научу, в-вот только на ле-екции обязательно ходите!!!\""
    "Заебало..."
    play music "music/tchaikovsky-Hymn_of_the_Cherubim.mp3" fadein 0.0 fadeout 5.0 volume 0.1
    

    show screen yuli_welcome with Fade(2.0, 2.0, 4.0)
    "Рядом со мной сидит удивительно прекрасная девушка, облаченная в откровенно свежее платье." 
    "Вероятно, не только мне душно на этой лекции." 
    "Её присутствие словно дарит ветерок летнего утра, и взгляд на неё вызывает неподдельное восхищение."
    stop music fadeout 5.0

    with None
    hide screen yuli_welcome
    scene firstDays lecture scen 
    show yuli happy at right 
    with Fade(3.0, 1.0, 2.0)
    
    $ mplay("audio/lecture-sound.mp3")

    "Ой, похоже, она заметила, что я пялюсь на неё..."
    "Девушка справа" "Приветики, занят?"
    sanya "Занят? Ага, как же. Пришел просто сон утренний досмотреть. А что, хочешь присоединиться к просмотру?.."
    "Бог ты мой, насколько же это была плохая и несуразная шут..."

    play voice "audio/girl_laugh2.mp3"
    show yuli horny at right 
    with Dissolve(2.0)

    "О боже, она словила смешинку с моей дурацкой шутки!"
    "Возможно, это и есть мой шанс!"
    sanya "А меня Саша зовут!"
    yuli "Я Юля, очень приятно познакомиться! Ах-хах"

    show yuli happy at right 
    with dissolve

    sanya "Юля, ты перевелась откуда-то? Я почему-то тебя раньше никогда не видел!"

    show yuli happy at center 
    with move

    yuli "(шёпотом) А потому что на лекции надо чаще ходить, я тебя тоже за целый год ни разу не видела!"
    "Тут она права, я вообще на эту лекцию по схемотехнике попал лишь потому что где-то надо было дождаться Пашу," 
    extend " у него-то, видите ли, пра-а-актика, надо прийти-и-и!"

    show yuli sad at center
    with dissolve

    yuli "(шёпотом) Я вот никогда не понимала, зачем нам постоянно ставят предметы, которые практически бесполезны для нашего направления?"
    sanya "Согласен!"
    $ mpause()
    play sound "audio/table_punch.mp3"
    $ renpy.pause(2)
    pause (1.0)
    "Преподаватель в этот момент прекратил говорить, и я крикнул \"Согласен!\" на всю аудиторию."

    show yuli sad at right 
    with move

    "Преподователь" "Мужчина! На моём предмете разговоры могу вести только я!"

    $ munpause()
    pause (0.5)

    "Ну что же поделать, раз такая красивая мадам будоражит мои нейроны прямо сейчас!" 
    extend " Повезло ещё, что я в этот самый момент не решил крикнуть слово \"ПИСЬКА!\""
    
    show yuli sad at center 
    with move

    sanya "(уже шёпотом) Согласен..." 
    extend " Особенно сильно раздражает, когда по этим бесполезным предметам, как, например, этот, нужно потом ещё и полноценный экзамен сдавать, билеты к нему учить и чего похуже."
    yuli "(шёпотом) У этого предмета ещё и такое дурацкое название, – ..."
    extend " Блин, забыла, ну это, как его..."
    sanya "Схемотехника!!"

    show yuli sad at right 
    with move

    $ mpause()
    play sound "audio/table_punch.mp3"
    $ renpy.pause(2)
    pause (0.5)

    "Преподаватель" "Молодой человек, я вам в последний раз делаю замечание! Прекратите разговаривать на лекции!"

    $ munpause()
    pause (0.5)

    show yuli sad at center 
    with move

    show yuli empathy at center 
    with dissolve

    yuli "(шёпотом) История лингвистических учений же!"
    sanya "Стоп, что?"
    "В эту минуту я осмотрел всю аудиторию. Вокруг меня были одни девушки... "
    extend "О нет, кажется, я перепутал кабинеты... "  
    extend "И теперь вместо бесполезной схемотехники я сижу... " 
    extend "Я сижу в компании приятных дам! Что за день!"

    show yuli sad at center  
    with dissolve

    yuli "Ты что, перепутал лекторные? Бедняжка..."
    "Какие ещё лекторные, правильно же лектории! Тебе бы точно не помешало послушать про лингвистические уче..."
    "Ох... Она назвала меня бедняжкой... Такая скромная..."
    "Её взгляд такой сочувствующий, видно, что она не пытается мне посочувствовать, а именно это и делает!"
    "Сейчас она мне кажется милой до безобразия."
    extend " Такая естественная и простая."
    "Одевается вызывающе, но при этом стеснительная..."

    show yuli disappointed at left
    with Dissolve(1.0)

    "Ой, сколько времени я уже молча просто пялюсь на неё? Надо срочно что-то сказать!!"
    sanya "У тебя лямки майки слезли, но я вижу, (шёпотом) как выступает ещё и вторая линия обороны!"

    show yuli shy at center 
    with dissolve

    yuli "(шёпотом) Что ты такое говоришь, дурачок?"
    sanya "(шёпотом) До этого мне казалось, что я сижу на самом бесполезном для меня предмете, но теперь я понимаю, насколько же я ошибался."
    yuli "Я тоже совсем не понимаю, что я тут забыла-то?"
    "Разговор, кажется, заходит в тупик. Нельзя же вечно обсуждать скукоту лекции, иначе сам разговор начнёт отдавать душниной!"
    sanya "Юля, а ты чем любишь заниматься обычно?"

    show yuli horny at center 
    with dissolve

    yuli "Не знаю, чем я люблю заниматься обычно, но после этой пары я свободна на все четыре стороны!"

    sanya "Ого, какой темперамент!"
    "Я за эти 10 минут на лекции по лингвистике уже такие слова, как \"темперамент\" начал использовать? А что, весьма продуктивно!"
    sanya "Вот этот настрой мне нравится!"

    show yuli horny at right 
    with move 

    $ mstop()
    play sound "audio/table_punch.mp3"
    $ renpy.pause(2)
    pause (0.5)

    "Преподаватель" "Так, молодой человек на камчатке! ..."
    sanya "В тебе есть искринка, Юль, я это вижу!"
    "Преподаватель" "Вы меня слышите вообще?"
    sanya "И вообще ..."
    "Преподаватель" "Стукните его там кто-нибудь рядом!"

    show yuli horny:
        linear 1.0 xalign 0.5 zoom 1.3 yalign 0.6
        linear 1.0 xalign 0.1 zoom 1.0 yalign 1.0

    "*Юля легко проводит рукой по моему подбородку, поворачивая голову в сторону преподавателя*"

    "Преподаватель" "Молодой человек, ну наконец-то! Попрошу Вас немедленно покинуть лекционный зал! "
    "Я было оторопел от такой наглости со стороны преподавателя настолько, что начал даже собирать свои вещи, как тут меня взяла за руку Юля и обратилась ко мне."
    show yuli horny:
        linear 0.3 center
    play music "audio/love.mp3" volume 0.1 fadein 4.0
    yuli "Саша, я тоже уже устала от этой душной лекции, хочешь, мы сейчас же вместе куда-нибудь сходим вместо неё? Время с тобой мне ведь явно понравится больше..."
    "Согласиться погулять с Юлей, значит кинуть Пашу с пивом, а ведь я уже договорился с ним, будет некрасиво так поступить."
    "Да и к тому же Паша просил без сюрпризов. У него и телефон сел, я не смогу его даже предупредить..."
    "С другой стороны, сколько я уже пил с Пашей, а с девочкой погулять не приходилось уже очень давно..."
    "Да и мама уже прям настаивает с кем-то познакомиться. Такой шанс всрать могу. Я ведь ей явно симпатичен!"
    "Может, Паша меня и поймёт..."

    menu :
        "Согласиться" :
            $ rel_yuli += 3
            $ rel_pasha -= 3
            $ str_for_notification = "Юля и Паша запомнят это"
                
            show screen notification_popup_big
            with dissolve
            sanya "Юля, да я же с радостью! Собирайся, мы уходим!"
            "Тут я заметил, что Юле и собираться не из чего, просто встала и пошла за мной!"
            $ day1_pasha_kfc = False
            

        "Отказаться" :
            
            $ str_for_notification = "Это действие имеет последствия"
                
            show screen notification_popup_big
            with dissolve

            sanya "Юля, давай погуляем завтра, я сегодня никак не могу – с другом уже договорился встретиться! Мы с ним тысячу лет не виделись!"
            sanya "Ты знаешь, что сделай, напиши мне свой ник в телеграме, я тебе сегодня вечером ещё напишу обязательно!"
            $ day1_pasha_kfc = True
    hide screen notification_popup_big
    with dissolve
    stop music fadeout 2.0


    if day1_pasha_kfc :
        play sound "audio/forest-sound.mp3" loop volume 0.2 fadein 2.0
        hide yuli happy
        scene firstDays nstu enter 
        with fade
        
        "Наконец-то лекция закончилась..."
        extend " Как обычно она была душной, зато на ней я познакомился с прекрасной Юлей"

        show pasha neutral 
        with dissolve

        "У входа я сразу встретил Пашку, который уже ждал меня."
        pasha "Ну чё, [sanya]идёт в кефас?"
        sanya "Обижаешь, конечно!"

        hide pasha neutral 
        with dissolve
        scene firstDays black scen 
        with fade

        $ renpy.pause(1.0)

        "Вспомнив про намеченные планы, я согласился, и в скором времени мы уже были на месте."
        stop sound fadeout 2.0
        play music "audio/kfc-sound.mp3" fadein 3.0 volume 0.4

        scene firstDays kfc inside 
        with fade

        "Когда я вошёл внутрь, меня сразу же окутал сладкий аромат курочки, я переглянулся с Пашей и поспешил сделать заказ."
        "Людей было не так много, хотя, казалось бы, вечер – час-пик!"

        show pasha neutral 
        with dissolve

        pasha "Слушай, ты уже записался на дополнительную физру? У нас в зале ещё есть свободные места."
        sanya "Я даже не думал об этом, всё, что я выбирал до этого, было полной хернёй, – занятия скучные, а преподы – мудаки"
        pasha "Заебись, записывайся тогда к нашему тренеру в подвальчике. Ты его сразу узнаешь, он больше меня в два раза."
        "Куда больше-то, блядь?"

        show pasha smiles
        with dissolve
        "Мне быстро принесли мой заказ: баскет дуэт и три бутылки бада."
        "Пару минут спустя принесли и заказ Паши: чикен моблан, три чизбургера, цезарь ролл, большая фри, большая деревенская, ещё и соус ёпте!"

        pasha "Ну что, Санёк, сейчас нам будет весело."

        "Сказав это, Пашка непонятно откуда достал бутылку коньячка."
        sanya "Ах-ха-ха, бля-я-ядь, сука, ну, Пашка, а ты умеешь поднять настроение!"
        pasha "А я умею!"
        pasha "Ну что, выпьем?"

        stop music

        hide pasha smiles
        with dissolve

        play music "audio/deadline_music.mp3" volume 0.13

        call play_kfc_minigame from _call_play_kfc_minigame
        stop music fadeout 2.0
        if _return == "pasha":
            $ day1_pasha_lose_in_drinking = False
        elif _return == "sanya":
            $ day1_pasha_lose_in_drinking = True
            
        
        play sound "audio/street-sound.mp3" volume 0.5 fadein 2.0   
        scene firstDays kfc outside 
        with Fade(0.0, 0.0, 2.0, color="#fff")
        
        show pasha neutral:
            alpha 0.0 center
            linear 1.0 alpha 1.0

        "Знатно накидавшись, мы вышли из кефаса и решили перекурить."

        show pasha giggles
        with dissolve

        pasha "После вкусного обеда, по закону Архимеда, чтобы жиром не заплыть, нужно срочно покурить!"
        sanya "А ты не подкинешь сигаретки?"

        show pasha smiles 
        with dissolve

        pasha "Конечно, братка, держи."
        "После пары затягов у меня сдавило горло и сразу захотелось блевать."
        sanya "Ебаный винстон синий, блядь!!"

        "Мы с Пашком так много выпили, а я ещё даже и не думал рассказать ему о моём знакомстве с Юлькой."
        "Да просто все мысли были о том, как же я"
        if not day1_pasha_lose_in_drinking :
            extend " жестко его перепил сегодня, что-что, а вот пил Пашка всегда слабенько"
        else :
            extend " жестко напился сегодня, что даже Пашка меня перепил. Явно сдаю позиции. Говорю же – старость!"

        sanya "Паша, кстати, сегодня я на лекции совершенно случайно познакомился с девочкой одной..."

        show pasha neutral
        with dissolve

        pasha "О-о-о-о!! Ну, рассказывай, как она в плане секса?"
        sanya "Паш, я с ней на лекции последней только познакомился, а сейчас вот сидел с тобой пил, как ты думаешь, когда бы я успел там?"
        pasha "Ну ты же на схемотехнике сидел, придумал бы там что-то на задних рядах такое..."

        show pasha giggles

        extend " схемотичное!"

        sanya "Паша, ты дурак, тебе часто это говорят?"
        pasha "Ну, а ты мне почаще об этом напоминай."
        extend " И вообще, я вижу ты уже начинаешь с девочками взлетать!"
        pasha "Когда они за тобой хвостами ходить будут, ты только не забывай, с кем ползал!!!"
        "Паша явно намекал на себя."
        sanya "Короче, я скучал на лекции, а потом смотрю направо... и оп! там она сидит вся такая довольная..."
        pasha "Наверное, потому что тебя заметила, такого красавца, да?"
        "А Паша то умеет засмущать"
        sanya "Она ещё ходит в такой очень облегающей маечке, знаешь, с вырезом в виде сердечка ниже груди. Очень мило выглядит, немного даже вызывающе..."
        sanya "Её Юля зовут, очень красивое имя между прочим! Мы с ней совсем недолго проболтали, а потом меня препод по беспределу выгонять начал. Видите ли, я шумлю тут!"
        sanya "Ну, она мне и предложила прогуляться вместо пары, но я-то знаю, что тёлок много, а друзей не выбирают! Сразу вспомнил, что на сегодня я занят. Ну и я вежливо ей..."

        show pasha angry 
        with dissolve

        pasha "ТАК, не понял, то-есть ты познакомился с симпотной девочкой, она позвала тебя сразу же гулять, а ты, такой дурной, решил вместо этого пойти пить пиво со мной?"
        sanya "Паш, мы же с тобой раньше договорились..."

        show pasha sad
        with dissolve

        pasha "Да ты совсем дурак? Тебе золото с неба упало, а ты что-то про договорились мне тут талдычишь!"
        sanya "Ну я взял её номер, сказал, что завтра ещё погуляем..."
        pasha "А ну! Пиши ей прямо щас, говори, что передумал, что ты мужик и хочешь видеть её!"
        sanya "Паша, ну я ж ..."
        extend " ну я ж того ... в зюзю!"

        show pasha angry
        with dissolve

        pasha "Пи-ши я те-бе ска-зал!"
        "Последняя трезвая частичка меня просто кричит, что это всё не к добру..."
        "Я достал телефон, нашёл её контакт и написал ей следующее, считай, любовное послание:"
        
        image message_yuli_background = "firstDays/message yuli background.png"
        image message_yuli_messages = "firstDays/message yuli messages.png"
        stop sound fadeout 0.5

        window hide

        $ sms_show(_("Юлолия"), True)

        sms_c "Сегодня"

        sms_r "поивет юлтчка!!!"

        sms_r "{image=emoji rofl}"

        sms_r "п мы можкм с тобой скйчас прямо встетитсья?б"

        sms_r "{image=emoji sweat}"

        sms_r "посто я очень ну хряу тебя видеть!"

        sms_r "мяу)"
        $ sms_hide()


        show pasha neutral with dissolve
        "Ну, вроде получилось неплохо, даже смайлики добавил к месту!"
        sanya "Ой, ответила!"
        pasha "Что пишет? Не томи!"
        hide pasha sad
        window hide
        $ sms_show(_("Юлолия"), True)
        with dissolve

        sms_yuli "Привет, Саша, я сразу и не поняла, кто мне пишет такие романсы)))"
        $ sms_hide()

        show pasha neutral
        sanya "– скобочка, скобочка, скобочка, –"
        window hide
        hide pasha neutral

        $ sms_show(_("Юлолия"), True)
        sms_yuli "Я сейчас на набережной стою, скучаю как раз"
        sms_yuli "Хочешь, приходи"
        $ sms_hide()
        $ quick_menu = True
        
        show pasha neutral
        sanya " – подмигивающий смайлик."
        $ sms_hide()
        play sound "audio/street-sound.mp3" volume 0.5 fadein 2.0 

        with dissolve
        show pasha angry
        with dissolve

        pasha "Ну и чего ты ждёшь? Беги к ней обниматься-целоваться!"

        menu :
            "Согласиться" :
                show screen notification_popup 
                with dissolve
                $ mood_counter += 1
                $ rel_yuli += 3
                show pasha smiles with dissolve
                pasha "Саня, Саня, не теряй такие возможности! Я тоже уже как раз до хаты собираюсь. Давай, расскажешь завтра, как оно там!"
                $ day1_yuli_agreed_after_kfc = True
            "Отказаться" :
                show screen notification_popup 
                with dissolve
                $ rel_yuli -= 3
                $ mood_counter -= 1;
                
                sanya "Паша, да... Мне уже в любом случае пора бы домой идти. Если случайно встретимся, то встретимся, если нет, то не суждено значит."
                show pasha sad with Dissolve(0.2)
                $ day1_yuli_agreed_after_kfc = False

        hide screen notification_popup
        with dissolve

        if day1_yuli_agreed_after_kfc :

            scene firstDays black scen
            with fade
            play music "audio/love_music.mp3" fadein 4.5 volume 0.4 fadeout 5.5
            scene firstDays bridge
            with fade

            
            show yuli greeting
            with dissolve

            storyteller "Саня нервно пробирался к набережной, надеясь, что не споткнется о собственные ноги. Он был ещё немного пьян от выпитого с Пашей. Однако он был рад встрече с Юлей."

            storyteller "Когда он увидел её, она стояла у перил и смотрела на воду. Саня подошёл к ней, и она повернулась, чтобы поприветствовать его улыбкой."

            yuli "Привет, Саша! Очень рада наконец-то с тобой познакомиться!"

            sanya "Привет, Юля. Я тоже рад тебя видеть."

            "Вау, она выглядит ещё красивее, чем я помнил."
            show yuli wet disappointed 
            with dissolve
            yuli "На улице идет сильный дождь, но я подумала, что мы всё равно можем прогуляться по мосту."

            sanya "Конечно, звучит неплохо."

            yuli "Итак, что ты думаешь о сегодняшней лекции?"

            sanya "Если честно, я не особо обращал внимание. Я был слишком занят разговором с тобой."

            storyteller "Слова Сани только укрепили у Юли уверенность в приятности его компании." 
            "Её сердце забилось немного быстрее, ведь она тоже чувствовала, что с ним так легко и приятно общаться."

            show yuli wet neutral 
            with dissolve
            yuli "Ха-ха, ну надеюсь, я не сильно тебя отвлекала."

            yuli "Мне тоже было очень интересно общаться с тобой," 
            storyteller "ответила она, слегка покраснев." 
            "Такое чувство, будто мы давно знакомы."

            storyteller "Внутренние мысли Сани подтверждали слова Юли. Он действительно ощущал какую-то особенную связь с ней, будто они уже давно были знакомы." 
            "Взглядом я следовал за каждым её движением и улыбкой, чувствуя, что эта встреча могла изменить что-то в моей жизни."

            storyteller "Пока они шли по мосту, Саня и Юля болтали о своих интересах и увлечениях. Они обнаружили, что у них много общего, и вскоре дождь прекратился, и солнце выглянуло из-за туч."

            storyteller "Словно подчеркивая природное слияние этих двух молодых сердец. Внешняя атмосфера отражала их чувства – свежесть, новизну и радость."
            yuli "Саша, а не хочешь перекусить где-нибудь?"

            sanya "Конечно, звучит здорово! Тут неподалеку есть очень милое кафе."
            scene firstDays black scen
            with Fade(2.0, 0.0, 1.0)
            
            "Я не могу поверить, как хорошо всё идет. Она потрясающая. Кажется, она мне действительно нравится."
            image foreground_cafe = "firstDays/foreground cafe.png"
            play sound "audio/kfc-sound.mp3" volume 0.1 fadein 3.0
            scene firstDays background cafe
            show yuli happy:
                xalign 0.7
                yalign 0.5
                zoom 0.77
            show foreground_cafe
            show black
            hide black  with Fade(2.0, 0.0, 2.0)
            

            storyteller "Пока они сидели в уютном кафе, наслаждаясь едой и компанией друг друга, Саня чувствовал себя на вершине мира. Он не мог поверить, как ему повезло, что он встретил такую девушку, как Юля."
            show yuli horny2 with dissolve:
                xalign 0.7
                yalign 0.5
                zoom 0.77
            yuli "Саша, я сегодня отлично провела время. Спасибо, что вышел ко мне под дождь."

            sanya "Нет, это тебе спасибо, Юля. Я тоже прекрасно провел время. Мы обязательно должны повторить это как-нибудь."
            show yuli horny with dissolve:
                xalign 0.7
                yalign 0.5
                zoom 0.77
            yuli "С удовольствием."

            "Не могу дождаться, когда увижу её вновь. Это начало чего-то особенного."
            hide yuli happy with dissolve
            hide foreground_cafe
            scene firstDays black scen
            with fade
            stop sound

        else :
            play music "audio/slow_sad_classical_music.mp3"  fadein 4.5 volume 0.4 fadeout 5.5
            scene firstDays black scen
            with fade
            "Я действительно не хотел встречи с Юлей, поэтому решил пробираться через закрытый мост."
            "Юля ждала меня совсем в другом месте. Скажу ей, что просто передумал встречаться, или побоялся, что слишком пьян..."
            "Прогуливаясь по ночным улочкам, я дошёл до моста. Передо мной воцарилась та самая, уже классическая надпись:"

            scene firstDays bridge
            with fade

            "Мост временно закрыт для пеших прогулок, приносим свои извинения."
            "Это временное закрытие длиться уже буквально год! Дыра справа от надписи как бы намекает, что мост закрыт только на словах."
            "Пробравшись через дырку на карачках, по ту сторону я увидел Юлю. Она меня сразу заметила и приветливо улыбнулась мне."

            show yuli greeting
            with dissolve

            yuli "О, ты пришёл! Так быстро!"
            sanya "Да, Юля, привет..."

            "Я же не хотел её видеть, как так получилось? Специально же пошёл через закрытый мост..."

            sanya "Набережная большая, Юля, а ты... такая маленькая на её фоне."

            show yuli wet disappointed 
            with dissolve
            
            yuli "Саш, ты порой такую чепуху несёшь..."
            sanya "Прости, я сегодня немного выпил..."
            yuli "Блин, Саш, мне не очень нравится тереться с пьяненькими мужчинами. Они меня пугают, если честно."
            
            sanya "Не переживай, Юля! *ик* Я тебя в обиду никому не дам!"

            show yuli wet sad with dissolve
            yuli "Защити меня сперва от себя, пожалуйста..."

            yuli "Я же вижу, что ты меня не рад видеть уже. Мы с тобой не друзья даже..."

            sanya "Юля, конечно, знакомы мы совсем недолго, но я уже вижу в тебе отличного товарища!"

            yuli "Ты даже не захотел пойти со мной гулять. Мне пришлось ошиваться одной... Под дождём..."

            sanya "Боже, Юля, ты ведь вся промокла насквозь! "

            sanya "И ведь это даже не самое главное..."

            yuli "Не говори этого, Саша. Я знаю, что ты хотел сказать, но это неправда. Мы едва знаем друг друга. "
            yuli "Давай просто наслаждаться видом."

            show yuli wet neutral

            "Мы стояли молча, смотрели на темную воду и отражающиеся на её поверхности огни."

            sanya "Юля, извини, если я что-то не так сказал. Я не хотел тебя напугать или ещё что-то."

            yuli "Все нормально, Саша. Я просто немного нервничаю. Я не привыкла к таким вещам."

            sanya "К чему?"

            yuli "Ну, знаешь, знакомиться с кем-то новым. Идти куда-то ночью. Это не то, что я часто делаю."

            sanya "Понятно. Ну, мы можем не оставаться здесь, если ты не хочешь."

            yuli "Нет, все в порядке. Я рада, что вырвалась из своей зоны комфорта. Приятно, что мне есть с кем поговорить."

            "Мы поговорили ещё немного, о школе, о наших интересах, о наших семьях. Это было приятно, но было заметно, что Юля не интересуется мной в романтическом плане."

            scene firstDays black scen
            with fade

            "В конце концов, мы попрощались, и я пошёл домой один. Это была грустная прогулка, но, по крайней мере, у меня появился новый друг."

    else :

        "Мы молча вышли из лекторной."

        play music "audio/strauss-festival.mp3" fadein 4.5 volume 0.1 fadeout 1.5

        hide yuli happy

        scene firstDays nstu enter 
        with fade

        sanya "На улице сейчас такой прекрасный закат, давай прогуляемся в сторону набережной?"
        yuli "Конечно, давай!"
        storyteller "Юля согласилась, и они направились в сторону набережной, шагая рядом друг с другом."

        scene firstDays black scen
        with fade

        storyteller "На набережной они оказались перед захватывающим видом. Солнце медленно клонилось за реку, раскрашивая небо оттенками розового и золотистого"
        storyteller "Конечно, они ещё не держались за ручку и не шли в обнимку, но уже явно были ближе друг к другу."

        scene firstDays promenade yuli
        with Dissolve(1.5)
        sanya "Да, дух захватывает..."
        yuli "Какое удивительное зрелище! "
        extend "Это похоже на произведение искусства!"
        storyteller "Восхитилась Юля"
        storyteller "Саня кивнул, соглашаясь"
        sanya "Не могу не согласиться. "
        extend "Знаешь, редко встретишь человека, который так ценит мелочи жизни"
        yuli "Я понимаю, о чем ты. "
        extend "Иногда кажется, что люди слишком сильно заняты своими проблемами, чтобы замечать красоту вокруг"
        sanya "Именно! Будто вдыхаешь глоток свежего воздуха, когда встречаешь кого-то, кто видит вещи так же, как и ты."
        yuli "Да, кажется, что мы на одной волне"
        sanya "И это так здорово, когда можешь разговаривать с кем-то новым и совсем не испытывать дискомфорта"
        yuli "Мы с тобой точно на одной волне"
        storyteller "подтвердила Юля, улыбаясь"
        sanya "А хочешь пойти со мной куда-нибудь? Может быть, выпьем кофе?"
        yuli "С удовольствием. Звучит замечательно"

        "Довольно резво тучи закрыли всё небо."
        "Начал собираться дождь."
        stop music fadeout 6.0
        scene firstDays rain yuli
        with Fade(2.0, 0.0, 2.0)
        play sound "audio/rain.mp3" fadein 15.0 volume 0.06 loop
        show yuli neutral
        with dissolve
        
        "Она подошла к забору и молча смотрела на правый берег."
        play music "audio/Love.mp3" fadein 0.5 volume 0.1 fadeout 1.5
        yuli "Саша, здесь так красиво..."

       

        sanya "Мне тоже очень нравится."

        show yuli horny
        with dissolve

        yuli "Обнимемся?"
        storyteller "Саня на мгновение замешкался, испытывая чувство вины за то, что он так плохо поступил по отношению к Паше"
        storyteller "Но, в то же время, он не мог устоять перед соблазном провести больше времени с Юлей"
        storyteller "Он наклонился и крепко обнял её"
        sanya "Конечно, давай обнимемся"
        
        hide yuli horny
        
        scene firstDays bridge
        with fade

        storyteller "Пока они шли по мосту, Саня не мог отделаться от ощущения кома в горле. Он понимал, что неправильно обошёлся с товарищем"
        storyteller "Но компания Юли была так приятна, что он отогнал эту мысль на задворки сознания"
        storyteller "Когда они дошли до середины моста, Саня увидел, что к ним приближается Паша. Он ощутил приступ вины и тревоги, когда понял, что его друг ждал его всё это время"
        
        show pasha angry at center with dissolve:
            blur 5.0
        show yuli disappointed at right with dissolve
        
        show pasha angry at center with Dissolve(0.1):
            blur 0.0
        show yuli disappointed at right with Dissolve(0.1):
            blur 7.0

        pasha "Эй, мужик, что происходит? Я ждал тебя в кефасе больше часа!"
        sanya "А, привет, Паша. Извини, я что-то закрутился..."
        

        show pasha angry at center with Dissolve(0.1):
            blur 7.0
        show yuli shy at right with Dissolve(0.6):
            blur 0.0

        "Юля смутилась и начала возиться с телефоном."

        stop music fadeout 10.0
        
        show pasha angry at center with Dissolve(0.1):
            blur 7.0
        show yuli sad at right with Dissolve(0.7):
            blur 0.0

        yuli "Эм, мне, наверное, пора. Только что написала мама, ей нужно, чтобы я скорее возвращалась домой."


        storyteller "Саню грызло изнутри. Настолько неприятный финал свидания и представить страшно"
        sanya "Хорошо, хорошо. Я был рад встретиться с тобой, Юля"
        "Потерял я Юлю. Она мне и не напишет больше."
        pasha "Мужик, ну и чего ты замер-то? В кайф под дождём стоять одному что ли? "
        extend "Пошли назад"

        hide yuli sad with Dissolve(0.5)
        show pasha angry at center with Dissolve(0.5):
            blur 0.0

        scene firstDays black scen
        with fade

        storyteller "Когда они шли обратно к университету, Саня не мог отделаться от чувства вины за то, что только что произошло."
        storyteller "Он понимал, что подвел друга и совершил ошибку, решив пойти на свидание с Юлей вместо того, чтобы встретиться с Пашей."

        scene firstDays nstu night 
        with fade
        stop sound fadeout 3.0
        show pasha sad at center
        with dissolve

        play music "audio/einaudi_nefeli.mp3" fadein 2.0 fadeout 2.0 volume 0.15
        pasha "Знаешь, Саня, так дела не делаются. Но, похоже, для тебя кидаться словами просто."
        pasha "Буквально пару часов назад же договорились встретиться в кефасе. А ты? Забыл об этом с лёгкой руки."
        sanya "Да нет же, Паша, всё не так. Извини, я просто увлёкся..."
        pasha "Да какая разница, чем ты там увлёкся. Я не хочу больше об этом говорить. Просто не делай так больше."

        hide pasha angry
        with Fade(1.5, 1.0, 1.5)


        storyteller "С этими словами Паша ушёл, оставив друга стоять одного на улице. Герой понимал, что совершил ошибку, но он также знал, что не может вернуть то, что уже произошло."
        storyteller "Он поклялся как-нибудь загладить свою вину перед Пашей и больше никогда не предавать его доверие."
        "После всех мыслей, я не нашел ничего лучше, чем поехать домой."

        scene firstDays black scen 
        with Fade(2.0, 0.0, 0.0)

    if not day1_pasha_kfc:
        play sound "audio/sound-in-bus.mp3" volume 0.03

        scene firstDays bus night with Fade(0.0, 0.0, 3.0)

        "Как обычно, по пути домой я глубоко погрузился в себя. Мои мысли перескакивали со скучных лекций и лаб на Пашку, на новую подругу Юлю и обратно."
        
        stop sound fadeout 0.5
        play sound "audio/bus.mp3" volume 0.03

        pause(2.0)

        stop sound fadeout 0.5
        play music "audio/home-sad.mp3" fadein 2.0  volume 0.2

        
        scene black with Fade(1.0, 0.0, 1.0)
        play sound "audio/footsteps.mp3"
        "Открыв дверь домой, я первым делом пошёл к окну."
        scene sanya cry
        with Fade(2.0, 0.0, 2.0)
        sanya "За столько лет я так и не смог бросить."
        "Достав последнюю сигаретку из пачки ванильного чапмана, я пару раз затянулся."
        play sound "audio/cigarette.mp3"
        pause 8.3
        show cigarette_smoke with dissolve
        sanya "Фух, сразу полегчало. На днях надо будет купить ещё пару пачек в кб."
        
        "Странный день вышел сегодня. "
        extend "Кажется, какое решение я бы не принял, всё пошло бы через жопу..."
        hide cigarette_smoke with dissolve

        "Почему я не могу не вести себя как идиот хотя бы на первом свидании?"
        
    else:
        play music "audio/einaudi_nefeli.mp3" volume 0.2
    scene sanya notification 
    with fade

    "Затушив сигарету, я было направился на кухню, но меня прервало уведомление на телефоне."
    "Система информированния студентов" "Здравствуйте, Александр Артёмович!\nПриглашаем вас в санаторий–профилакторий. Оздоровительное лечение, двухразовое питание и проживание. Путёвка на неделю за счёт Университета."

    menu :
        "Отличная идея!" :
            $ str_for_notification = "У этого действия будут последствия"
            
            show screen notification_popup_big 
            with dissolve

            sanya "Звучит как отличная идея, может хотя бы там смогу вернуть краски в жизнь."
            $ day1_sanya_wants_camp = True

            $ mood_counter += 1; 
        "Какой-то отстой." : 
            $ str_for_notification = "У этого действия будут последствия"
            
            show screen notification_popup_big 
            with dissolve

            sanya "Да блядь, опять спам от университета, как же он бесит."
            $ day1_sanya_wants_camp = False
            $ mood_counter -= 1;
        
    hide screen notification_popup_big
    with dissolve

    "Родители" "Саша, мы можем оплатить санаторий, тебе будет полезно развеяться."
    "Ладно, это и правда неплохая возможность отдохнуть. Говорить о том, что он бесплатный я, конечно, не буду."

    scene sanya bed with dissolve: 
        linear 35 zoom 1.1
        linear 35 zoom 1.0
        repeat

    if not day1_yuli_agreed_after_kfc:
        "Почистив зубы, я быстро вернулся в свою комнату. Было тяжело найти силы даже на то, чтобы раздеться. Я упал на кровать."
        "Семестр только начался, а я уже так устал. Честно говоря, я давно начал замечать, что жизнь становится все серее и серее."
        extend " Уже нет такого озорного взгляда у меня в глазах, как был раньше."

        "В университете я вижу одни и те же безразличные и скучные лица."
        extend " Ни с кем из них я не был знаком, ни то чтобы оно мне было нужно, мне так даже легче. "
        
        "Преподы как обычно валят на сессии, заставляя снова и снова приходить на пересдачи, ради которых приходится  учить тонны бесполезного материала."
        "Единственное положительное событие за последние дни было знакомство с Юлей. Для меня удивительно, что она вообще со мной заговорила."
        "Но даже с Юлей я не мог избавиться от чувства пустоты, которое преследовало меня уже долгое время. "
        extend "Может быть, дело было во мне, может быть, это я изменился. "
        extend "А может, это мир вокруг меня потерял свои краски."
        "Я тупо уставился в потолок, мои мысли бесцельно блуждали. "
        extend "В чем был смысл всего этого? "
        extend "Почему я вообще здесь оказался?"
        "Я знал, что должен вырваться из этого состояния, но это было легче сказать, чем сделать. "
        extend "Груз моей собственной печали, казалось, раздавил меня."
        "Так я и лежал, погруженный в свои мысли, пока, наконец, усталость не взяла верх и я не погрузился в беспокойный сон, надеясь, что завтра наступит какое-то облегчение."
    else:
        "Когда я лежал в постели той ночью, я не мог не думать о Юле. Она была умной, красивой и доброй. Но я знал, что между нами никогда ничего не будет."
        "Я уснул с тяжелым сердцем, зная, что никогда не найду любовь."

    stop music fadeout 3.0

    show black with Fade(3.0, 0.0, 2.0)

    jump second_day

label second_day :

    play sound "audio/typewriter-sound.mp3" volume 0.5 loop
    centered "{size=+30}{font=fonts/sfpro_semibold.ttf}{cps=3.8}День второй.  {nw}{/cps}{/font}{/size}"
    stop sound
    with fade

    "И опять же... {w}Я проснулся с ощущением тяжкого груза на сердце."
    "Господи, какой же срач. " 
    extend "Как вообще отыскать здесь то, что мне нужно?"
    play music "audio/space-floating.mp3" fadein 2.5 loop fadeout 3.0 volume 0.1
    # определим фон игры, время игры в секундах
    # и зададим параметры игры – спрайты и положение для собираемых предметов
    $ hf_init("sanya room", 30,
        ("backpack", 1232, 436, _("Рюкзак ЖУК-РЕДАН")),
        ("light", 610, 930, _("Зажигалка")),
        ("marlboro1", 1147, 927, _("Пачка сигарет (пустая)")),
        ("marlboro2", 1610, 690, _("Пачка сигарет (пуста)")),
        ("t-shirt", 1038, 798, _("Футболка")),
        ("pants", 568, 200, _("Трусы")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
        # включаем смену курсора при наведении
        mouse=True,
        # включаем инвентарь с убиранием из него найденных предметов
        inventory=True,
        # включаем подсказкиD
        hint=True,
        # включаем подсветку предмета при наведении
        hover=brightness(.1),
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

    # покажем вместе с фоном и фигурки на нём
    with dissolve
    

    if renpy.mobile:
        centered "{size=+24}{color=#fff}Найдите все предметы за 30 секунд.\nНажмите, чтобы начать.{/color}{/size}"
    else:
        centered "{size=+24}{color=#fff}Найдите все предметы за 30 секунд.\nНажмите ЛКМ, чтобы начать.{/color}{/size}"
    $ hf_bg()
    window hide
    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)
    play music "audio/einaudi_nefeli.mp3" fadein 1.0 fadeout 2.0 volume 0.2
    # результаты
    $ hf_hide()
    if hf_return == 0:
        centered "{size=+24}Предметы собраны успешно.\n Но все пачки пусты..{/size}"
    else:
        if hf_return == 1:
            centered "{size=+24}{color=#fff}GAME OVER\nНе нашёлся 1 предмет.{/color}{/size}"
        else:
            centered "{size=+24}{color=#fff}GAME OVER\nНе нашлось [hf_return] предмета(-ов){/color}{/size}"

    
    with dissolve

    "Вот дерьмо..."
    "Единственное, что мне нужно прямо сейчас, – это чапа."
    extend " Только сигарета поможет мне забыться."
    
    
    scene sanya cry blue
    with fade

    "Подойдя к окну, я достал уже изрядно потрепанную пачку сигарет, но единственное, что я в ней нашел, – это затхлый запах табака."
    "Пиздец... " 
    extend "День только начался, а я уже лишился самого важного."
    "Придется сходить в кб за сигами. " 
    extend "Ведь говорил же себе вчера купить пару пачек, но всё равно забыл."

    scene firstDays black scen
    with fade
    
    play sound "audio/footsteps_asphalt.mp3" fadein 0.2 fadeout 0.2
    play music "audio/street-sound.mp3" fadein 2.0 fadeout 2.0 volume 0.2

    pause 4.0

    scene firstDays red white
    with fade

    "Наконец-то купил сиги. Жизнь продолжается."
    "Итак, раз уж я решил ехать в санаторий, то лучше бы не затягивать со всем этим бюрократическим адом и собрать все документы за раз."
    "{i}-Примечание: перед тем, как Вы отправитесь в наш великолепный санаторий, вам нужно принести следующие документы: {/i}"
    "{i}Копию паспорта, свидетельство о рождении, книжку со всеми проставленными прививками...-{/i}"    
    sanya "Ебись оно все в рот!"
    "{i}Выписка из ЕГРН, 2-НДФЛ, 3-НДФЛ...{/i} бла-бла-бла... {i}Справка о целостности заднего прохода...{/i}"
    extend " Так, стоп, а это им для чего?"
    "Выбора у меня всё равно нет. Нужно развеяться, сменить обстановку. " 
    extend "Иначе я могу просто не выдержать..."
    "Придётся ехать в универ."

    scene firstDays bus station
    with fade

    "Снова эта убитая и дряхлая остановка. "
    extend "Быть может, ещё в СССР она выглядела нормально, но сейчас... "
    extend "Это просто пиздец."

    scene firstDays black scen 
    with fade
 
    play sound "audio/bus.mp3" fadein 0.5 fadeout 1.5 volume 0.1

    pause 4.0

    stop sound fadeout 1.0

    scene firstDays bus 
    with fade

    play music "audio/sound-in-bus.mp3" fadein 1.5 fadeout 2.5 volume 0.1

    "Этот автобус вообще меняется? " 
    extend "Хотя да... С каждым годом он всё хуже и хуже."
    "Город, который когда-то казался мне бесконечным простором для приключений, теперь выглядел иначе"
    "Перед моими глазами проплывали старые дома, сложенные веками истории, и разбитые дороги, которые, казалось, уже и не помнили гладкой молодости"
    "Взгляд мой устремлялся вдаль, где рождался рассвет, но серость бытия словно окутывала меня туманом"
    "Что-то внутри моей души тревожно колебалось, будто желая пробудить меня от безразличия"
    
    "После этих мыслей я начал погружаться в сон."
    scene black with Fade(2.0, 0.0, 2.0)

    screen bus_day2():
        default bus_minigame = BusMinigameDisplayable(hi_score, 1)
        add bus_minigame
    window hide
    call screen bus_day2

    if int(_return) > int(hi_score):
        scene black
        play music "audio/slow_sad_classical_music.mp3" fadein 2.0 fadeout 1.0 volume 0.6
        centered "{size=+50}Новый рекорд!{/size}"
        centered "{size=+50}Счёт: [_return]{/size}"
        "И всё же, среди всей серости дней случаются прекрасные моменты," 
        "Когда лучи восходящего солнца пробиваются сквозь облака, озаряя улицы золотым сиянием, и даже обветренные фасады домов кажутся оживающими"
        "В эти моменты серость уступает место теплым оттенкам, а в моей душе возникает надежда, что в этом городе ещё есть место для перемен," 
        "что он может возродиться, обрести новую жизнь и расцвести, словно редкая красочная картина, привлекающая взгляды и вызывающая восхищение"
    else:
        scene firstDays bus with Fade(0.0, 0.5, 2.5)

        play music "audio/bad_dream.mp3" fadein 1.0 fadeout 1.0 volume 0.6
        play sound "audio/heart.mp3" fadein 0.9 fadeout 0.2
        image nc = "firstDays/night color.png"
        show nc:
            xalign 0.5 yalign 0.5
            alpha 0.0
            linear 1.5 alpha 0.6
            block:
                linear 1.0 zoom 1.2 alpha 0.5
                linear 0.6 zoom 1.0 alpha 0.6
                repeat
        "Тягостное ощущение того, что время в этом городе остановилось или потихоньку утекает, сковывает мои мысли"
        "В молчаливом хоре окружающих меня домов и улиц я словно теряю себя"
        "Тот город, который когда-то вдохновлял меня своей суетой, сейчас кажется утратившим свою яркость"
        "Может быть, это я потерял способность видеть краски жизни, но они всё ещё присутствуют вокруг меня," 
        "Но я их упускаю, забившись в собственную повседневность и рутину"
        stop sound fadeout 1.0
 
        hide nc with dissolve

    $ hi_score = max(hi_score, int(_return))
    

    stop music fadeout 2.0
    
    scene firstDays black scen
    with fade

    "Ох, блядь! Чуть не проспал свою же остановку."

    play sound "audio/bus.mp3" fadein 0.5 fadeout 1.5 volume 0.1

    pause 7.0

    stop sound

    scene firstDays bus station near nstu
    with fade
    show pasha neutral
    with dissolve

    play sound "audio/street-sound.mp3" loop volume 0.2
    "Первое, что я увидел, когда вышел из автобуса, – это огромную фигуру Паши. Да его и сложно не заметить..."
    sanya "Паша! Привет. Я хотел тебе кое-что сказать..."

    if day1_pasha_kfc :
        "Паша быстро меня заметил и подошёл ко мне"

        show pasha smiles
        with dissolve

        pasha "Санек, привет. Как поспал? "
        extend "Хотя... "
        extend "Можешь не отвечать. Как всегда херово, я знаю."
        sanya "Да, бошка трещала не по-детски."
        sanya  "Мне вчера письмо пришло с приглашением в санаторий. "
        extend "Я тут подумал и решил, что стоило бы съездить, подлечиться..."
        pasha  "О, Саня, тебе это сейчас больше всего, можно сказать, не хватает."
        pasha "Я конечно, с тобой туда ни ногой, ты меня знаешь, я и так здоров как бык. "
        extend "Но за тебя пальчики мы с ребятами скрестим!"
        
    else :

        sanya "Извини меня за вчерашнее... " 
        extend "Я совсем замотался. Вылетело из головы."
        pasha "Не парься. "
        extend "Я ещё вчера сказал, что больше это обсуждать не хочу. " 
        extend "Просто забей. Но я надеюсь ты понимаешь, что так лучше больше не делать!"

        show pasha smiles
        with dissolve

        pasha "А ещё, ты мне за это теперь пива торчишь!"
        extend " И минимум три литра бада!"

        pasha "Ладно, ты сам как вообще?"
        sanya "Как и всегда. "
        extend "Абсолютно хуево."
        sanya "Кстати, тебе вчера не приходило письмо с приглашением в санаторий?"

        show pasha neutral
        with dissolve

        pasha "Может и приходило. "
        extend "Ты же знаешь, что я весь спам от универа даже не читаю. "
        extend "Тем более про санатории, которые каждый год предлагают."
        sanya "Бесплатно же. "
        extend "Чего бы не скататься. "
        extend "Так ещё можно родакам сказать, что универ не оплачивает поездку. "
        extend "Денег получить."

        show pasha giggles
        with dissolve
        pasha "Бесплатный сыр только в мышеловке, запомни!"

        pasha "Они тебе, может, там вообще зонд в жопу запихнут, пока ты спать будешь!"
        "А-а-а, так вот для чего им справка о целостности ануса нужна..."
        sanya "Не хочешь со мной съездить? "
        extend "Бухла купим, будем по вечерам пить."
        "Если и ломать целостность ануса, то хотя бы не одному!"

        show pasha sad
        with dissolve

        pasha "Извини, но желания ехать в этот старый санаторий у меня нет."
        pasha "Но ты, как вернёшься, расскажи, как там оно проходит."
        pasha "Если там правда могут поставить на ноги, то в следующем году уже вместе можем и поехать!"

        show pasha smiles
        with dissolve

        pasha "Ладно, Санёк, был рад повидаться! " 
        extend "Мне на пары пора."

        hide pasha smiles
        with dissolve

    
    if not day1_yuli_agreed_after_kfc and day1_pasha_kfc :

        pasha "Кстати, а как там с девочкой твоей дела обстоят?"
        image night = "firstDays/night color.png"
        sanya "Ну ты же знаешь, что я тебе сейчас ничего хорошего не расскажу..."

        play sound "audio/heart.mp3" fadein 4.0 fadeout 0.5 volume 0.3
        show night:
            alpha 0.0
            linear 4.0 alpha 1.0
            block:
                linear 1.0 zoom 1.2 alpha 0.9
                linear 0.6 zoom 1.0 alpha 1.0
                repeat

        "Ужасно неудобно вышло с Юлей, на самом деле. Бедный человек, у неё же и правда проблемы в жизни, мы с ней практически незнакомы, а она мне так открылась на эмоциях. А я то и дело избегаю её."

        "Хотя, с другой стороны, Может это и к лучшему, мне и своих проблем в жизни сейчас хватает по горло, разве я готов хранить в себе ещё и её проблемы?.."

        "Я человек сентиментальный. Я всё принимаю близко к сердцу. Ну не могу я слушать о проблемах других, не перенимая их переживания."

        "Ловлю себя порой на мысли, что с подобной особенностью мне точно не стоит подаваться в психотерапевты, подобная профессия мне строго противопоказана."

        show pasha sad
        with dissolve

        hide night with dissolve
        stop sound

        pasha "Алё-ё, Саня, ты завис тут немного!"
        pasha "Я тебя понял, тебе даже тяжело вспоминать, что было? Я этот твой взгляд сразу узнаю!"

        show pasha giggles
        with dissolve

        pasha "У тебя точно такой же был, когда твоя мама вернулась с дачи раньше времени, а тебе 16, и у тебя вся хата заблёвана!"

        "Паша умудрился вытащить меня из ямы самокопания своим подколом"

        "Я заулыбался"

        sanya "Да уж, Паша, было же время! Лучшие мои годы, честно признаться! Я порой так по ним скучаю..."

        show pasha neutral
        with dissolve

        pasha "Брат, да не загоняйся ты о прошлом! Думай о будущем! Тебе всего 20 стукнуло только! Вся жизнь ведь впереди!"

        show pasha smiles
        with dissolve

        pasha "Заставь дряхлого старика из будущего жалеть ещё больше о сегодняшнем дне!"

        sanya "А ты прав, Паша!!"

        "Ты, как всегда, прав..."

    elif day1_yuli_agreed_after_kfc and day1_pasha_kfc :
        play music "audio/keys-of-moon-a-little-fantasy.mp3" fadein 3.5 fadeout 1.0 volume 0.1
        sanya "Паша, помнишь, когда я написал Юле и пошёл к ней?"

        show pasha neutral
        with dissolve

        pasha "Да, не думай, что я от бухла сразу память теряю!"
        sanya "Ладно-ладно. Так вот, мы с ней встретились и поболтали. Этот разговор я точно запомню надолго..."
        sanya "Я подошёл к набережной. Мы решили прогуляться."
        sanya "Мы очень славно гуляли, я даже подумывал уже взять её за ручку."
        sanya "Через некоторое время ей набрала мама и позвала домой."
        sanya "Я проводил её до лифта и обнял, мы попрощались, и она сказала, что этот день ей представлялся очередным скучным деньком, который я скрасил своим появлением!"
        sanya "У меня чуть сердце не взорвалось от таких речей..."

        show pasha smiles 
        with dissolve

        pasha "Ах ты ж красавец-то! А! Всё правильно сделал. Идеальнее некуда."
        pasha "Видишь же? Не зря я тебя заставил ей написать. Радуйся, что у тебя такой друг есть."
        pasha "Напомню ещё раз: \"Когда будешь летать, не забывай с кем ползал!\""

        show pasha neutral
        with dissolve

        pasha "Так, ладно, мне уже пора идти на пару. А ты, как я понял, только за документами в универ приехал?"
        sanya "Ну, да."
        pasha "Удачи тебе тогда, Саня! И в санатории приятно отдохнуть. Я тебе ещё вечером напишу, мемов в телеграм накидаю!"
        pasha "Увидимся через неделю, значит? На этом же месте?"
        sanya "Верно, верно, на этом же месте, ровно через неделю!"

        hide pasha neutral 
        with dissolve
    
        "Всё-таки хорошо, что я смог увидеть Пашу. Теперь как-то даже веселее. Пора идти в универ..."

    scene firstDays black scen 
    with fade

    "Распрощавшись с Пашкой, я направился прямиком в деканат. "
    extend "Желания возиться с документами у меня не было совсем."
    sanya "Ненавижу, блядь, бюрократию..."
    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene firstDays nstu que
    with fade

    play sound "audio/people-noise.mp3" fadein 2.0 loop volume 0.05
    "Возле деканата меня повергла в шок необычайно длинная очередь. Видимо, второкурсники пришли брать допуск на пересдачу."
    "Моё ожидание продлилось больше часа, в конце концов я зашёл в деканат."
    
    "В момент, когда я уже должен был заходить следующим, сзади в меня влетела какая-то рыжая девчонка."
    "От чего все мои документы рассыпались по всему холлу."
    play music "audio/space-floating.mp3" fadein 2.5 loop fadeout 3.0 volume 0.1
    "Боже, парень передо мной уже вот-вот выйдет. Надо как можно быстрее собрать всё обратно!"
    window hide
    # ивент со сбором документов
    # определим фон игры, время игры в секундах
    # и зададим параметры игры – спрайты и положение для собираемых предметов
    
    $ hf_init("nstu que", (9 if not renpy.mobile else 25),
        ("a1", 413, 780, _("1-НДФЛ")),
        ("a2", 918, 980, _("2-НДФЛ")),
        ("a3", 630, 710, _("3-НДФЛ")),
        ("a4", 413, 900, _("Справка об усыновлении")),
        ("a5", 555, 950, _("Справка о целостности ануса")),
        ("a6", 990, 711, _("Скан паспорта")),
        ("a7", 733, 894, _("Скан свидетельства о рождении")),
        ("a8", 900, 780, _("Направление на анализы кала")),
        ("a9", 885, 694, _("Справка об отсутствии судимостей")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
        # включаем смену курсора при наведении
        mouse=True,
        # включаем инвентарь с убиранием из него найденных предметов
        inventory=True,
        # включаем подсказки
        hint=True,
        # включаем подсветку предмета при наведении
        hover=brightness(.17),
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

    # покажем вместе с фоном и фигурки на нём
    scene black
    with dissolve

    centered "{size=+24}Подберите раскиданные справки за 8 секунд.\nНажмите, чтобы начать.{/size}"
    $ hf_bg()
    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)
    $ hf_hide()
    # результаты
    if hf_return == 0:
        centered "{size=+24}Все справки собраны!{/size}"
        
        with dissolve
        "Фух, теперь можно со спокойной душой заходить в кабинет..."
    else:
        if hf_return == 1:
            centered "{size=+24}GAME OVER\nНе нашлась одна справка...{/size}"
        else:
            centered "{size=+24}GAME OVER\nНе нашлось [hf_return] справки(-ок){/size}"
        "Ай, да и чёрт с ним, может и так примут, кто вообще эти документы смотреть-то будет?"
        "Идиотская бумажная волокита!"
    scene black with fade
    stop music fadeout 3.0

    stop sound fadeout 0.5
    "Уже вечерело, времени ушло куда больше, чем я ожидал. "
    extend "У выхода из корпуса я заметил несколько одногруппников, по разговору было понятно, что они направляются в курилку."
    "Может, мне тоже сходить? Пообщаться с одногруппниками. Встретить знакомые лица."
    "Хотя, с другой стороны, сегодня хорошая погода, можно пойти домой через парк..."
    
    scene firstDays nstu enter
    with Fade(0.0, 0.0, 0.3)

    menu :

        "Пойти в курилку" :
            $ str_for_notification = "У этого действия будут последствия"
            $ rel_yuli += 3
            show screen notification_popup_big
            with dissolve

            $ day2_sanya_went_to_smoke = True

        "Прогуляться по парку" :
            $ str_for_notification = "У этого действия будут последствия"

            show screen notification_popup_big
            with dissolve

            $ day2_sanya_went_to_smoke = False

    hide screen notification_popup_big
    with dissolve

    if day2_sanya_went_to_smoke :
        scene firstDays black scen 
        with fade

        "Поприветствовав одногруппников, я с ними направился в сторону курилки."

        play music "audio/street-sound.mp3" fadein 1.5 fadeout 2.5 volume 0.3

        scene firstDays kyrilka
        with fade
        show cigarette_smoke with dissolve

        "Одногруппник" "Как же бесит препод по схемотехнике, мы с ним только первый день, а он уже показал себя полным мудаком."
        "Одногруппник" "Да уж, он точно будет валить на сессии. Кстати, Саня, тебя вроде не было на лекции."
        sanya "Да я проебался немного, пришёл не на свою."
        "Потянувшись за пачкой сигарет, неожиданно для себя я её не обнаружил."
        "Порывшись получше в рюкзаке, я пришел только к одному выводу: я ..."
        extend " должен стрельнуть сигу."
        sanya "Слушайте, а у вас сигаретки не будет? Видимо свои я где-то посеял."
        "Стоявший справа от меня парень с неодобрительным взглядом протянул мне сижку шоколадного чапмана."
        play sound "audio/cigarette_one_shot.mp3" volume 0.4
        "Сделав пару затягов, мне приятно ударило по горлу, а никотин немного меня расслабил."
        "Парни в основном обсуждали прошедшую лекцию и скорую лабораторную по электротехнике."
        "По их словам препод требовательный, но справедливый. На практиках он часто смеется со студентов, которые ничего не понимают, но тем не менее старается понятно донести материал."
        "Одногруппник" "Бля, недавно видел на ютубе видео про СССР, как же  тогда хреново было, не то что сейчас. Вы как вообще к нему относитесь?"
        "Мне так нравится СССР, на самом деле..." 
        extend " Я восхищаюсь его историей и достижениями. Это было время больших перемен и сильных людей." 
        "Но что-то мне подсказывает, что эти ребята явно негативно настроены..."
        "Все посмотрели на меня. "
        extend "Они ждут моего мнения по этому поводу? Надо что-то сказать..."

        menu :
            "СОЮЗ НЕРУШИМЫХ..." :
                $ mood_counter -= 1;
                $ str_for_notification = "У этого действия будут последствия"

                show screen notification_popup_big
                with dissolve

                $ day2_sanya_vote_for_ussr = True
            "На хуй СССР!" :
                $ mood_counter += 1;
                $ str_for_notification = "У этого действия будут последствия"

                show screen notification_popup_big
                with dissolve

                $ day2_sanya_vote_for_ussr = False

        hide screen notification_popup_big
        with dissolve

        if day2_sanya_vote_for_ussr:
            play music "audio/cherry-metal.mp3" volume 0.05 fadein 10.0 fadeout 5.0
            sanya "Честно говоря, мне кажется, что в СССР было лучше, чем сейчас. Жизнь была проще, люди добродушнее..."
            "Сказав это, я заметил на себе неодобрительные взгляды одногруппников."
            "Одногруппник" "Пхахаха, ты что, в атомик харт переиграл, доходяга? Давай-ка мы национализируем твои денюжки, пионер."
            "Они накинулись на меня толпой, противостоять им я никак не мог."
            "Каждый удар и пинок приходился как из нескончаемой лавины, заставляя меня чувствовать ушибы и жгучую боль." 
            "Я пытался оправдать свои идеи, объяснить, что это всего лишь мои мысли и желание размышлять о прошлом, но они не желали слушать." 
            "Вместо этого в их глазах горела неистовая ярость, словно я представлял угрозу для всего, во что они верили."
            "Внезапно, один из них сильно ударил меня в живот, заставив меня задохнуться и прижаться к стене." 
            "Я смотрел на своих одногруппников, бывших друзей, и не мог понять, как они могут быть такими жестокими." 
            "Мои слова и мольбы лишь подливали масло в огонь и усиливали их агрессию."
            play music "audio/slow_sad_classical_music.mp3" volume 0.3 fadein 10.0 fadeout 10.0

            "Кое-как отбрыкавшись, я направился в сторону универа."
            "Моя одежда была слегка оборвана, лицо покрыто ссадинами, а тело болело в каждой клеточке." 
            "Шаги были неуверенными, но я старался идти вперед, не глядя назад на это ужасное событие. "

            "Состояние у меня было хуже некуда, хотелось просто уйти как можно дальше от этого мира."
            "Возможно, я должен был просто притворяться, соглашаться с общепринятыми мнениями и не поднимать дискуссию?" 
            "Но это было бы ложью перед самим собой, и я не мог отказаться от своих убеждений ради внешнего признания."
            "После этих унижений я уже не хотел курить. "
            extend "Я выкинул сигарету. "
            extend "Хотел плакать. "
            extend "Хотел заорать на всю улицу, но сдержался."

            scene firstDays black scen
            with fade
            play sound "audio/footsteps_asphalt.mp3" volume 0.5 noloop fadein 0.2 fadeout 0.2
            "У выхода из корпуса я заметил Юлю, смотрящую в мою сторону. "
            extend "Она подбежала ко мне, явно заметив моё паршивое настроение."

            scene firstDays nstu enter
            with fade
            show yuli afraid
            with dissolve

            play music "audio/keys-of-moon-a-little-fantasy.mp3" fadein 3.5 fadeout 2.5 volume 0.1

            yuli "Саша, что с тобой случилось? Выглядишь ужасно подавленным."
            sanya "Да так, ничего серьезного, день с самого утра не задался, не стоит так беспокоиться."
            show yuli happy
            with dissolve
            yuli "Ну, раз ты так говоришь... Главное помни, что ты всегда можешь ко мне обратиться."
            yuli "пойдём, я провожу тебя до дома, может тебе полегчает в моей компании."
            sanya "пойдём, конечно."

            hide yuli happy
            scene firstDays black scen
            with fade

            "Как же приятно идти по улице в компании такой красивой и весёлой девушки..."
            yuli "Сань, может у тебя всё-таки что-то случилось?"
            sanya "Нет, всё в порядке, Юля. Ты лучше расскажи, как у тебя дела."
            "Поболтав немного, я решил предложить зайти за сигаретами. Свои новенькие я уже успешно проебал."

            scene firstDays red white
            with fade

            show yuli empathy
            with dissolve

            yuli "Я подожду тебя снаружи. Не люблю такие магазины..."
            sanya "Хорошо! Скоро буду."

            hide yuli empathy
            scene firstDays magazine inside
            with fade
            
            sanya "Можно, пожалуйста, пачку чапы ванильной."
            "Немного погодя, я добавил:"
            sanya "И два советских пломбира в вафельном стаканчике!"
            "Кассир" "Да, с вас..."

            scene firstDays red white
            with Fade(2.0, 0.0, 1.0)
            show yuli empathy
            with dissolve

            sanya "Ну всё, пойдём дальше. Мне что-то захотелось мороженого, я и тебе взял!"
            show yuli horny
            with dissolve
            yuli "Советское! Обожаю!"

            
            scene firstDays black scen
            with Fade(2.0, 0.0, 2.0)

            "Через пять минут мы уже были около моего дома."

            scene sanya home
            with fade
            show yuli shy
            with dissolve

            yuli "Ого! Я и не знала, что мы так близко живем!"
            yuli "Не задумываешься, почему мы друг друга ещё ни разу не видели?"
            "Пока мы шли, я думал позвать её с собой в санаторий"
            "Конечно, знакомы мы не так долго, но с ней мне легко и приятно. Почему нет?.."
            "Жаль, правда, что Паша не захотел"
            sanya "Слушай, а ты не хочешь съездить со мной в санаторий на недельку?"
            "Чёрт, я же перебил её. Надеюсь не обидится."

            show yuli horny
            with dissolve

            yuli "Ура, мы поедем в санаторий, мы отлично проведем время вместе!"
            "Она же, блядь, даже не успела подумать. Да и пофиг."
            sanya "Не хочешь ко мне зайти, можем посмотреть кино или чем-то ещё интересным заняться?"
            #"Учитывая, как она думает над своими действиями, мне может что-нибудь да перепасть."
            "Юля не успела ответить, как у неё зазвонил телефон."

            show yuli horny2
            with dissolve

            yuli "Прости, Саш. Мама уже зовёт домой, сегодня не получится, — поздновато."
            "Мы обнялись на прощание."
            sanya "Тогда завтра в 8:00 встретимся у университета!"
            yuli "Конечно, буду ждать с нетерпением!"
            "Да... Снова не повезло."

            stop music fadeout 3.0

            hide yuli horny2
            show firstDays black scen
            with Fade(2.0, 0.0, 1.0)

        else:
            sanya "Согласен, сейчас жизнь куда лучше, ни то что в совке, посмотреть только на то, куда он нас привел, в кошмарную перестройку."

            "Одногруппник" "Да, ты прав, в то время был полный пиздец."
            "Одногруппник" "Слышали, недавно версию разработчиков атомик харт выпустили. Кто-нибудь уже играл?"
            "Одногруппник" "Да, там совок прямо таки восхваляется."

            "Докурив, мы попрощались друг с другом и разошлись. Я направился в сторону универа."

            "Может и зря я так отозвался о СССР... "
            "Говорят, там советское мороженное и квас в бочках были вкусными!"

            scene firstDays black scen
            with fade

            "У выхода из корпуса я заметил Юлю, смотрящую в мою сторону. Она подбежала ко мне явно заметив моё паршивое настроение."

            scene firstDays nstu enter
            with fade
            show yuli greeting
            with dissolve

            yuli "Са-а-аш, привет. Как у тебя дела? Выглядишь немного грустным."
            sanya "Да все хорошо, целый день убил на сбор документов для санатория."
            yuli "Ого, ты собираешься в санаторий? Тебе тоже пришло письмо от университета? Я как раз хотела тебе предложить съездить."

            show yuli horny
            with dissolve

            yuli "Ура мы поедем в санаторий, мы отлично проведем время вместе."
            yuli "Ты не против пройтись со мной до моего дома?"
            "Такое предложение не могло пройти мимо моих ушей."
            sanya "Да, конечно, пойдём!"

            hide yuli horny
            scene firstDays black scen
            with fade

            pause 3.0
            
            scene sanya home
            with fade
            show yuli happy
            with dissolve

            "Мы уже приближались к дому Юли, я был сильно удивлен тем, что мы живем совсем рядом."

            sanya "Я и не знал, что мы живем так близко друг к другу."
            sanya "Почему я тебя до этого ни разу не видел?"
            yuli "Потому что нужно почаще выходить на улицу и побольше общаться с самим собой... Кхм, ну и с людьми, конечно."
            sanya "Да... Наверно, ты права."
            "Может пригласить её куда-нибудь."
            sanya "Не хочешь ко мне зайти, можем посмотреть кино или заняться чем-то ещё заняться?"
            "После этих слов у Юли зазвонил телефон."

            show yuli horny2
            with dissolve

            yuli "Прости, Саш. Мама уже зовёт домой, сегодня никак получится."

            "Мы обнялись на прощание..."

            sanya "Тогда завтра в 8:00 встретимся у университета!"
            yuli "Конечно, буду ждать с нетерпением!"

            stop music

            hide yuli horny2
            show firstDays black scen
            with fade

        $ day2_sanya_vote_for_ussr = True

    else :
        
        scene firstDays nstu enter
        with fade

        "Выйдя из корпуса, я потянулся за пачкой сигарет, но тут же обнаружил, что её там нет."
        "Осмотрев все карманы рюкзака, сигарет я так и не нашёл. Видимо, где-то посеял. Придется заглянуть в кб на обратном пути."
        "А ведь только утром покупал. Может, спиздил кто?"
        "Ладно, в этот раз пойду пешком до дома. Сэкономлю хотя бы на проезде."

        scene firstDays black scen
        with fade

        "Пройдя пару кварталов, я заметил вход в парк, который находится недалеко от моего дома. Чем не отличное место, чтобы привести мысли в порядок?"
        play sound "audio/forest-sound.mp3" fadein 1.0 loop 
        scene firstDays park
        with fade

        "Великолепный парк, утопающий в природной красоте." 
        "Однако, прежде чем окунуться в его волшебную атмосферу, необходимо сделать краткий перерыв и совершить маленькое увлекательное приключение" 
        "– отправиться за сигаретами."

        scene black
        with fade
        stop sound fadeout 3.0
        pause 2.0

        
        play music "music/tchaikovsky-Hymn_of_the_Cherubim.mp3" fadein 0.0 fadeout 5.0 volume 0.1
        show screen nadya_welcome with Fade(0.0, 0.0, 3.0)

        "В тихий и благосклонный вечер, где небольшая очередь таяла в магазинах, я невольно оказался перед дивной красотой молодой девушки."
        "Её рыжие пряди волнились легко, словно играли в танце с ветерком."
        "Невероятные зелёные глаза, словно два изумруда, притягивали взгляд своей загадочностью."
        "Сердце замирало на мгновение, увидев гармонирующий с цветом волос зелёный свитер, который располагал к себе и создавал гармонию с её прекрасными глазами."
        "Моментом я заметил, что её эмоции, выраженные на лице,"
        extend " словно художественная палитра, отражали смесь чувств – страсть в перемешку с досадой." 
        "Гнев в её глазах явно говорил, что она ведёт захватывающий спор с кассиром."
        "Бесшумно устремившись к прослушиванию их разговора, я не мог не поколебаться перед этой магнетической личностью," 
        "Которая словно расцветала в окружающем пространстве."

        stop music fadeout 5.0
        with None
        hide screen nadya_welcome
        scene firstDays magazine inside
        show nadya angry
        with Fade(3.0, 0.5, 1.5)
        
        "Девушка" "Сейчас-сейчас, дайте минутку, я найду паспорт."
        "Кассир" "Да ты уже пять минут пытаешься его найти, не продам я тебе сигареты. По закону нельзя."

        show nadya light sad
        with dissolve

        "Девушка" "Может тогда по студенческому продадите?"
        "Кассир" "Разуйте глаза, на кассе чётко написано, что продажа только с 18-ти лет при предъявлении паспорта."

        show nadya angry
        with dissolve

        "Девушка" "Ухх, ну я тебе ещё покажу, злюка!"

        "Развернувшись, девушка увидела меня и попросила выйти с ней ненадолго."
        scene firstDays red white
        with fade
        play sound "audio/forest-sound.mp3" fadein 2.0 loop
        show nadya flirting
        with dissolve

        "Девушка" "Слушай, не мог бы ты купить мне чапу ванильную? Я забыла паспорт, а кассир ни в какую не продаёт. Меня, если что, Надя зовут."
        nadya "А, погоди, я тебя же видела сегодня уже в деканате со спины?.."
        sanya "Ага, вспомнил. Это же ты мне в спину тогда влетела, что все бумаги по полу разлетелись."
        show nadya light sad with dissolve
        nadya "Прости пожалуйста! Это могло случиться с каждым! Я не растеряха!"
        show nadya smiles with dissolve
        nadya "Ну вот, значит ты знаешь, что я учусь с тобой в одном университете, а значит мне точно есть 18!"
        nadya "Так ку-упишь сижки-сигаретки, а?"

        menu :

            "Купить сиги." :
                $ str_for_notification = "Надя запомнила это"
                $ mood_counter += 1;
                show screen notification_popup
                with dissolve
                $ rel_nadya += 2
                $ day2_nadya_bought_cigarettes = True

            "Да малолетка ты. Домой иди." :
                $ mood_counter -= 1;
                $ str_for_notification = "Надя запомнила это"
                $ rel_nadya -= 2
                show screen notification_popup
                with dissolve

                $ day2_nadya_bought_cigarettes = False

        hide screen notification_popup
        with dissolve

        if day2_nadya_bought_cigarettes :
            hide nadya flirting 
            with dissolve

            sanya "Ладно. Сейчас куплю тебе чапу."

            scene firstDays magazine inside
            with fade
            stop sound fadeout 2.0

            sanya "Добрый вечер, пару пачек ванильного чапман."
            "Кассир оценивающим взглядом оглядел меня с ног до головы."
            "Кассир" "Паспорт, пожалуйста."
            "Недолго думая, я показал его, на что он утвердительно кивнул и начал рыться за прилавком."
            "Оплатив покупку, я подошёл  к девушке и протянул ей пачку."

            show nadya happy
            with dissolve

            nadya "Большое спасибо, ты меня правда спас. Кстати говоря, мне кажется мы ещё где-то виделись."
            "Я попытался вспомнить где же я её ещё мог видеть, но ничего в голову так и не пришло."

            show nadya smiles
            with dissolve

            nadya "А-а, вспомнила, ты был вчера на лекции по лингвистике, тебя ещё препод выгнал."
            sanya "Да, было такое, даже не знаю, чего он так взъелся на меня."
            nadya "Ха-ха, меньше кричать на всю аудиторию надо."
            sanya "Ты права, моя вина."
            nadya "Ты бы ещё \"ПИСЬКА\" крикнул бы во всю"
            "Усмехнулась Надя"
            nadya "Я хотела по парку прогуляться, составишь мне компанию?"
            sanya "Ну давай пойдём, мне всё равно нечем заняться."

            scene firstDays black scen
            with fade
            play sound "audio/forest-sound.mp3" fadein 4.0 loop 
            pause 3.0

            scene firstDays park
            with fade

        else :

            hide nadya flirting 
            with dissolve

            "Поразмыслив над просьбой девушки, я решил не покупать ей сигареты, выглядит она совсем молодо, может быть ей и 18-ти лет-то нет."
            stop sound fadeout 2.0
            scene firstDays magazine inside
            with fade
            
            sanya "Добрый вечер, ванильный чапмен, пожалуйста."
            "Кассир оценивающим взглядом оглядел меня с ног до головы."
            "Кассир" "Паспорт гони."
            "Недолго думая, я показал его, на что он утвердительно кивнул и начал рыться за прилавком."
            "Оплатив покупку, я вышел на улицу. Девушки я там так и не увидел."
            sanya "Интересно, куда она так неожиданно ушла."
            "Оставив размышления, я направился в сторону парка, где присел на ближайшую лавочку."
            play sound "audio/forest-sound.mp3" loop fadein 1.0
            scene firstDays park
            with fade

            "Достав сигаретку, я уже было потянулся в карман за зажигалкой, как осознал, что и её я успешно посеял"
            "Я хотел было возвращаться в магазин, как какой-то незнакомец дал мне прикурить."
            "Разглядев появившийся передо мной силуэт, я заметил ту же девушку, которую видел в магазине."

            show nadya flirting
            with dissolve

            nadya "Парень, я тебя спасла, но в благородство играть не буду, дашь мне сижку и мы в расчёте."

            menu :

                "Стрельнуть сижку, оторвать её от своей души." :
                    $ str_for_notification = "Надя запомнила это"
                    $ mood_counter += 1;
                    $ rel_nadya += 2
                    show screen notification_popup_big
                    with dissolve
                    $ day2_nadya_get_one_sigarett = True

                "Обойдешься без сиги." :
                    $ str_for_notification = "Надя запомнила это"
                    $ mood_counter -= 1;
                    $ rel_nadya -= 2
                    show screen notification_popup_big
                    with dissolve
                    $ day2_nadya_get_one_sigarett = False

            hide screen notification_popup_big
            with dissolve

            if day2_nadya_get_one_sigarett :

                "Недолго думая, я достал ещё одну сигаретку и протянул милой даме."
                
                show nadya smiles
                with dissolve

                nadya "Спасибо большое!"

                show nadya flirting
                with dissolve

            else :

                "Немного подумав я не стал давать ей сигарету, она выглядит слишком молодо, я даже не уверен есть ли ей 18 лет."
                sanya "Прости, я даже не знаю сколько тебе лет, не могу же я просто так дать сигарету ребенку."

                show nadya angry
                with dissolve

                nadya "Ну и иди ты, злюка!"

                hide nadya angry
                with dissolve

                "Надя ушла, оставив меня в одиночестве. В я поступил как мудак, может быть мы бы стали с ней хорошими друзьями или ещё чего больше."
                "Опять я расстроил человека, неужели я ни разу не могу поступить правильно?"
                "Надеюсь хоть что-то хорошее придет в мою жизнь, завтра всё таки поеду в санаторий."
                "Заниматься самобичеванием, раскуривая сигарету, мне не хотелось. Затушив её, я незамедлительно отправился домой."

        if day2_nadya_bought_cigarettes or day2_nadya_get_one_sigarett :
            
            $ day2_nadya_have_a_dialog = True
            show nadya handson 
            with dissolve

            nadya "Ну вот и отлично, как ты? Выглядишь уставшим."
            sanya "Да не волнуйся, просто замотался сегодня, лучше о себе расскажи."
            nadya "Честно и рассказывать то нечего, учусь в ... на гуманитарном факультете."
            sanya "Видимо, на лингвистической специальности?"
            nadya "Да, так и есть. Ты, я так понимаю, тоже? Мы, вроде, раньше не встречались, перевёлся что-ли?"

            nadya "А-а, вспомнила, ты был вчера на лекции по лингвистике, тебя ещё препод выгнал."
            sanya "Да, было такое, даже не знаю, чего он так взъелся на меня."
            nadya "Ха-ха, меньше кричать на всю аудиторию надо."
            nadya "Сам препод очень жесткий, говорят, и злопамятный."
            extend " Смотри, как бы он тебя за эту выходку не завалил на экзамене!"

            sanya "Да мне на этого препода начхать, скажу больше, я вообще не на свою лекцию попал."

            show nadya laughs
            with dissolve

            nadya "Ну ты даешь, как так получилось-то?"
            sanya "Случайно как-то, я вообще друга ждал и решил заглянуть на лекцию."
            sanya "Слушай, а чем ты увлекаешься?"

            show nadya giggles
            with dissolve

            nadya "В свободное время читаю, люблю вышивать, время от времени я не прочь поиграть во что-нибудь."
            nadya "Сегодня в деканат кстати ходила подавать документы на поездку в санаторий от нашего ВУЗа."
            "Ничего себе, я ж тоже туда еду!"

            show nadya flirting
            with dissolve

            nadya "Мне кажется, или ты там был с той же целью?"

            "Я был бы не прочь поехать с ней на автобусе."

            if rel_yuli >= 3:
                extend " Но как тогда быть с Юлей?"


            menu :

                "Согласиться" :
                    $ day2_choosen_instead_yuli = True
                    $ mood_counter += 1;
                    $ rel_nadya += 1
                    $ str_for_notification = "Надя запомнила это"

                    show screen notification_popup_big
                    with dissolve

                    sanya "Да, я тоже еду! Можем вместе поехать на одном автобусе!"

                    show nadya smiles
                    with dissolve

                    nadya "Отлично, а я-то боялась, что без друзей совсем там окажусь!"

                    "Мы продолжили разговаривать на различные темы, пока у Нади не зазвонил телефон."

                    nadya "Прости, мне уже пора, добавишь меня в телеграме?"
                    sanya "Да, конечно."
                    nadya "Класс, мой номер: ..."
                    nadya "Ладно, мне пора идти. Ещё увидимся."

                    show nadya flirting
                    with dissolve

                    "Она неожиданно крепко стиснула меня в своих объятиях."

                    hide nadya flirting
                    with dissolve

                    "На такой приятной ноте прервалось наше знакомство."
                    extend " Уже было достаточно поздно, поэтому, недолго думая, я направился прямиком к своему дому."

                "Нейтральный ответ" :
                    $ day2_choosen_instead_yuli = False
                    $ mood_counter -= 1;
                    $ str_for_notification = "Надя запомнит это"
                    
                    show screen notification_popup_big
                    with dissolve

                    sanya "Ну, да."

                    if not day1_sanya_wants_camp:
                        extend " Меня вообще туда родители загнали, я б в жизни по своей воле туда не пошёл."

                        nadya "Бывает же. Ну, может ещё в санатории пересечёмся!"
                    else:
                        nadya "Ой, ну, может ещё в санатории пересечёмся!"

                    show nadya light sad
                    with dissolve

                    

                    "Мы продолжили разговаривать на различные темы, пока у Нади не зазвонил телефон."
                    nadya "Прости, мне уже пора, добавишь меня в телеграме?"
                    sanya "Да, конечно."
                    nadya "Класс, мой номер: ..."
                    nadya "Ладно, мне пора идти. Ещё увидимся."

                    hide nadya light sad
                    with dissolve

                    "Уже было достаточно поздно, поэтому, недолго думая, я направился прямиком к своему дому."
            
            hide screen notification_popup_big
            with dissolve
    
    scene firstDays black scen
    with fade

    if not day2_nadya_get_one_sigarett and not day2_nadya_bought_cigarettes and not day2_sanya_went_to_smoke:
        "Зайдя в квартиру, я сразу достал сигарету и пошёл к окну."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry blue
        with fade

        "Настроение было, мягко говоря, отвратительным."
        "Весь день потратил на эти гребаные документы, отказал девушке в парке."
        "Так мог поступить только настоящий мудак."
        "Сигарета в моих руках все тлела, а я смотрел на проезжающие мимо автомобили."
        "Весь город кипит жизнью, люди куда-то торопятся, один я с каждым днём все больше стагнирую."
        "Только Юля делает мою жизнь светлее."
        
        "Достав телефон я быстро набрал её номер и стал ждать ответа."

        stop music
        play music "audio/cell-phone-ring-simple.mp3" fadein 1.5 fadeout 2.0 volume 0.1

        scene sanya notification
        with fade

        "Как же я волнуюсь."
        "Что ей сказать?"
        "Я просто хочу чтобы она меня поддержала."
        "Пожалуйста, ответь..."
        "Гудки тянулись очень долго, каждый из них отдавался во мне глухим гулом."
        sanya "Возьми трубку, пожалуйста!"
        "Мне кажется, что моё сердце сейчас выпрыгнет из груди. Я еле стою на ногах, руки вспотели."
        "Я еле стою на ногах, руки вспотели."

        stop music

        pause 0.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        yuli "Саша, привет, как я рада тебя слышать!"
        "После услышанного мне сразу полегчало, я облокотился на балкон и прикурил ещё одну сигарету."
        sanya "Юля, я так хотел тебя услышать, мне очень тяжело сейчас."
        yuli "Саш, что случилось, я тебя искала, но так и не смогла найти. Где ты был?"
        sanya "Прости меня. Я был в парке, решил прогуляться после пар."
        yuli "В следующий раз найди меня. пойдём домой вместе, как раз узнаешь где я живу. И вообще, мы можем почаще видеться."
        sanya "Спасибо, я очень рад это слышать. С этого дня мы будем ходить домой вместе."
        
        "Следующие пятнадцать минут мы болтали о том, о сем."
        yuli "Саш, я никогда тебя не спрашивала, а когда у тебя день рождения?"
        sanya "Ха-ха, попробуй угадать, уверен у тебя не получится."
        yuli "Может быть тридцатого июля?"
        sanya "Как так? Оно именно в этот день!"
        yuli "Правда?! У меня тоже. Видишь как мы похожи, даже день рождения одинаковый."
        sanya "И правда, мы очень похожи."
        yuli "Ой, прости, уже поздно пора бы нам закругляться."
        yuli "Спокойной ночи, Саш, очень жду нашей с тобой поездки!"
        sanya "Юль, спасибо ты очень помогла. Встретимся завтра возле универа. Спокойной ночи!"
        "Мне и правда сильно полегчало после разговора с Юлей, она как будто оживила меня."

        scene sanya bed with dissolve :
            linear 35 zoom 1.1
            linear 35 zoom 1.0
            repeat

        "Улёгшись в кровать меня посетила одна мысль."
        sanya "А откуда я вообще знаю её номер?"
        "Я слишком устал за этот день, размышлять над этим уже не было сил."

    elif not day2_sanya_vote_for_ussr and not day2_nadya_have_a_dialog:
        "Зайдя в квартиру, я сразу достал сигарету и пошёл к окну."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry blue
        with fade

        "Настроения не было даже ужинать."
        "Весь день потратил на эти гребаные документы, так ещё и наврал самому себе, сказав что СССР всё было херово."
        "Так мог поступить только настоящий мудак."
        "Сигарета в моих руках все тлела, а я смотрел на проезжающие мимо автомобили."
        "Весь город кипит жизнью, люди куда-то торопятся, один я с каждым днём все больше стагнирую."
        "Наверное стоило сказать правду про СССР, я бы смог им доказать что тогда было лучше."
        "В детстве мой дедушка часто рассказывал истории о пионерах и октябрятах, насколько в лагерях тогда было классно."
        "Я всю жизнь хотел посетить Артек, но так ни разу не смог туда попасть, путевки очень дорогие, а пробраться через заслуги в учёбе для меня было невозможно."
        "Так я и оставил эту идею, а сейчас мне уже 20..."
        "Вспомнив про заначку, оставленную мне дедом, я полез в шкаф и обнаружил там пару пачек сигарет \"Космос\"."
        "Взяв пару сигарет, я вернулся к окну и закурил."
        sanya "Ух, крепкая."
        "Слезы так и хотели побежать от нахлынувших воспоминаний, но почему-то не могли."
        "Они оставляли жгучую горечь внутри меня. Она была настолько сильна, что я на миг упал на колени и схватился за грудь."
        "Через пару минут меня отпустило."
        sanya "Как же меня все заебало."
        "Я облокотился на балкон, чуть-ли не свисая с него. В миг, когда моя жизнь могла закончиться в мыслях передо мной предстала Юля."

        "Отхлынув от балкона я сразу лёг в кровать в надежде прийти в себя."

        scene sanya bed with dissolve :
            linear 35 zoom 1.1
            linear 35 zoom 1.0
            repeat

    elif day2_nadya_have_a_dialog and not day2_sanya_went_to_smoke:
        "Зайдя в комнату, я сразу пошёл на балкон. Достав сигаретку из пачки вишнёвого чапмана, я сразу вспомнил о Наде."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry blue
        with fade

        "Наше знакомство в парке было очень неожиданным, но очень приятным."
        if day2_choosen_instead_yuli :
            "Надя мне сразу понравилась, она очень умная и необычная. В добавок курит чапу, так же, как и я. Интересно, она ответит, если я ей позвоню?"

            stop music
            play music "audio/cell-phone-ring-simple.mp3" fadein 1.5 fadeout 2.0 volume 0.1

            scene sanya notification
            with fade

            "Спустя пару протяжных гудков в трубке послышался знакомый голос."

            stop music
            play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

            nadya "Привет, Саш, чего ты звонишь так поздно?"

            sanya "Надь привет. Ну так что, железно едем вместе до санатория?"
            sanya "Думаю, нам было бы весело вместе."

            nadya "Конечно, я только рада буду составить тебе компанию."
            sanya "Приятно это слышать, может, тогда завтра встретимся в 8:00 у универа?"
            nadya "Да, в 8:00 будет как раз. Ладно, Саш, я пойду, а то мне уже спать пора."
            nadya "Сладких снов!"
            sanya "Спасибо ещё раз, тебе того же!"
            
            "Мои мысли были только о Наде."
            "Надеюсь мы будем жить в соседних комнатах. Гулять вместе." #пошлость
            "А по ночам может даже проводить оздоровительные процедуры по улучшению кровообращения в области таза." #(что за ебанавт это писал?! исправить!)

        else :
            "Надя мне сразу понравилась, она очень умная и необычная. В добавок курит чапу, так же как и я. Интересно, она ответит, если я ей позвоню?"

            stop music
            play music "audio/cell-phone-ring-simple.mp3" fadein 1.5 fadeout 2.0 volume 0.1

            scene sanya notification
            with fade

            "Спустя пару протяжных гудков в трубке послышался знакомый голос."

            stop music
            play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

            nadya "Привет, Саш, чего ты звонишь так поздно?"

            sanya "Надь привет, просто было интересно, как у тебя дела..."

            nadya "Отлично. Я была очень рада познакомиться с тобой сегодня!"
            sanya "Я очень рад это слышать..."
            nadya "И я рада, что тебе приятно. Уже поздно, Сань... Я пойду спать."
            nadya "Спокойной ночи!"
            sanya "Спасибо ещё раз, тебе тоже спокойной!"

        "С этими словами я положил трубку и достал ещё одну сигарету."

        scene sanya cry blue
        with dissolve


        "Я достал наушники и включил недавно добавленную в плейлист музыку."
        "Ей оказалась \"Несогласие – Жду любви\"."
        "Ещё минут пятнадцать я сидел на балконе, курил и наслаждался музыкой."
        "В скором времени меня начало клонить в сон и я решил перебраться на кровать."

        scene sanya bed with dissolve :
            linear 35 zoom 1.1
            linear 35 zoom 1.0
            repeat

        "Спать на ней будет явно удобнее, чем на балконе."
        
    elif day1_pasha_kfc and not day1_yuli_agreed_after_kfc and day2_sanya_vote_for_ussr:
        "Зайдя в квартиру, я сразу пошёл к окну."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry blue
        with fade

        "Настроение было, мягко говоря, ужасным."
        "Конченые одногруппники, все деньги забрали, даже на курево не оставили... Ничего они не понимают!"
        "С этими словами я пошёл к шкафу и достал оттуда пачку сигарет \"Космос\", припасённую ещё дедушкой."
        "Встав у окна, я прикурил сигарету. Она оказалась весьма крепкой, аж горло сковало."
        "После пары затяжек я привык."
        sanya "Вот это сигареты, не то что сейчас, махорка какая-то..."
        "Временами мне кажется, что сам мир отвергает меня, будто я какая-то сломанная деталь в механизме часов, от которой нужно просто избавиться."
        "Да и хочу-ли я продолжать существовать?"
        "За что бы я не взялся, всё рушиться, будто песок вытекающий из рук."
        "Сигарета в моих руках все тлела, а я смотрел на проезжающие мимо автомобили."
        "Весь город кипит жизнью, люди куда-то торопятся, один я с каждым днём все больше стагнирую."
        "Какое-же я ничтожество."
        "Подвел Юлю, она ещё меня и до дома провела."

        scene sanya toilet night withh water
        with fade

        "Затушив сигарету, я направился в ванну."
        "Раздевшись и набрав воды я улегся в неё. Голова была совсем пуста, желание думать о чем-то совсем отпало."
        "Я повернулся в сторону двери и на тумбочке увидел некий блестящий предмет. Им оказалось лезвие."
        sanya "Как кстати."
        "Взяв одно из них в руку и подставив к запястью, я понял насколько же я жалок."
        "Просто хочу уйти от проблем самым кратчайшим путем, даже не попытавшись решить их..."
        "В такой позе я просидел несколько секунд, в конце-концов я решился и надавил на лезвие."
        "В этот миг передо мной возник образ Юли."

        show yuli sad
        with dissolve

        yuli "Саш, ты правда хочешь сделать это, ты ничего не забыл?"
        sanya "О чём это ты говоришь?"
        yuli "А как же наша поездка в санаторий, как я буду без тебя? Ты решил оставить меня совсем одну?"
        "Я резко отдёрнул руку, почувствовав жгучую боль."
        "На ней остался неглубокий, но явно заметный порез. Он ещё долго будет мне напоминать о моей беспомощности."
        sanya "Спасибо, Юля, даже в такой момент ты спасла меня..."

        yuli "..."

        hide yuli sad
        with dissolve

        "Выбравшись из ванны я направился прямиком в кровать."

        scene sanya bed with fade :
            linear 35 zoom 1.1
            linear 35 zoom 1.0
            repeat

        "Я всё пытался понять, что со мной не так."
        "Почему у меня ничего не получается?"
        "Последнее время я будто смотрю свою жизнь, как фильм или театральную пьесу."
        "Что же вершит судьбой человека в этом мире? Некое незримое существо или закон? По крайне мере истинно то, что я не властен даже над своей волей."
        "С этими мыслями я погрузился в глубокий сон."

    elif (day1_yuli_agreed_after_kfc or not day1_pasha_kfc) and day2_sanya_vote_for_ussr:

        "Зайдя в квартиру, я сразу достал сигарету и пошёл к окну."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry blue
        with fade

        "Настроение было, мягко говоря, в подвешенном состоянии."
        "Вспомнив, что я почти весь день не курил, я потянулся за сигаретой. {w}И правда, сегодня вся голова была забита Юлей. {w}Целый день я думал только ней."
        "Я облокотился на подоконник и закурил."
        "Честно говоря, я так рад встрече с Юлей, она смогла разукрасить мою жизнь... {w}Придать ей смысл."
        "За прошедшие пару дней она разделяла со мной как радости, так и неудачи."
        "Лучше неё нет никого на свете."
        "Я хочу быть с ней постоянно."
        "Поскорее бы настало завтра, я так хочу её увидеть."
        "Для меня она единственный лучик счастья в этом бренном мире."
        sanya "Может, позвонить ей?"
        sanya "Хотя... {w}уже поздно... {w}Она, наверное, спит."

        "Затушив сигарету, я сразу лёг в кровать, надеясь, что завтра наступит как можно скорее."

        scene sanya bed with Dissolve(3.0):
            linear 35 zoom 1.1
            linear 35 zoom 1.0
            repeat
    stop music fadeout 7.0
    scene firstDays black scen 
    with Fade(3.0, 0.0, 3.0)

    jump third_day

label third_day :
    play music "audio/noise_ambient_Otixx - Nostalgia.mp3" volume 0.2 fadein 3.0
    play sound "audio/typewriter-sound.mp3" volume 0.5 loop
    centered "{size=+30}{font=fonts/sfpro_semibold.ttf}{cps=3.8}День третий.  {nw}{/cps}{/font}{/size}"
    stop sound
    scene sanya bed with Fade(0.0, 1.0, 4.0):
        linear 35 zoom 1.1 center
        linear 35 zoom 1.0 center
        repeat

    "Проснувшись, я понял что ничуть не отдохнул за прошедшую ночь."
    "Гул в голове всё не утихал, подняться с кровати я не мог."
    "Через пятнадцать минут боль немного утихла, и я смог подняться. Я достал телефон и проверил время."
    sanya "Блядь, я опаздываю!"

    "Я быстро собрался, захватил заранее заготовленные вещи и пачку новокупленных сигарет. "
    "Выйдя на улицу, я достал одну сигаретку и глубоко затянулся, головная боль ушла, а мысли переключились на вчерашний день."

    scene sanya home
    with Fade(1.0, 1.0, 1.9)

    "С кем же мне поехать в итоге?"

    menu :
        "Юля" if not day1_pasha_kfc or day2_sanya_vote_for_ussr or day1_yuli_agreed_after_kfc :
            if day2_nadya_have_a_dialog :
                $ rel_nadya -= 3
            $ mood_counter += 1;
            $ rel_yuli += 3

            $ str_for_notification = "У этого действия будут последствия"
            stop music fadeout 3.0
            show screen notification_popup_big
            with dissolve

            $ day3_choice_yuli = True

            "Первым в голове возник образ Юли. Вчерашняя прогулка оставила приятное послевкусие."
            "Я и не ожидал что мы всего за пару дней так сблизимся, мы удачно совпали характерами, временами мне кажется, что мы с ней очень похожи."
            "Интересно, смогу ли я ещё встретиться с ней?"

        "Надя" if day2_nadya_have_a_dialog :
            $ mood_counter += 1;
            $ rel_yuli -= 3
            $ rel_nadya += 3

            $ str_for_notification = "У этого действия будут последствия"
            stop music fadeout 3.0
            show screen notification_popup_big
            with dissolve

            $ day3_choice_nadya = True

            "Первым в голове возник образ Нади. Наше знакомство оказалось для меня неожиданностью. Мы встречались только один раз, но она всем видом показывала, что я ей симпатичен."

        "Один" :
            $ mood_counter -= 5;
            $ str_for_notification = "У этого действия будут последствия"

            show screen notification_popup_big
            with dissolve


            "А ведь и ехать не с кем... Поеду тогда один."

    hide screen notification_popup_big
    with dissolve

    scene firstDays bus station
    with fade

    "Заебала эта остановка. Когда её уже снесут к хуям собачьим?"
    "А вот и моя развалюшка..."

    play sound "audio/bus.mp3" fadein 1.5 fadeout 1.5 volume 0.1

    scene firstDays black scen 
    with fade

    pause 6.0
    stop sound

    play music "audio/sound-in-bus.mp3" fadein 1.5 fadeout 2.0 volume 0.1

    scene firstDays bus
    with fade

    "Посплю пока. Главное не проспать остановку..."

    screen bus_day3():
        default bus_minigame = BusMinigameDisplayable(hi_score, 2)
        add bus_minigame
    window hide
    call screen bus_day3

    if int(_return) > int(hi_score):
        scene black
        centered "{size=+50}Новый рекорд!{/size}"
        centered "{size=+50}Счёт: [_return]{/size}"


    $ hi_score = max(hi_score, int(_return))
    

    "Снова тот же сон..."

    
    scene firstDays black scen 
    with fade

    stop music
    play sound "audio/bus.mp3" fadein 1.5 fadeout 1.5 volume 0.1

    pause 6.0
    stop sound

    scene firstDays bus station near nstu
    with fade

    "Кажется, по времени всё нормально. Можно уже не торопиться."

    scene firstDays black scen
    with fade

    "На часах было без пяти восемь, а в конце улицы уже виднелся ждавший меня автобус."
    "Подойдя ближе, я был приятно удивлен, передо мной открылся вид не на старенький и потрепанный ЛИАЗ, а на красивый Икарус, он выглядел так, будто только сошёл с конвейера."

    scene firstDays neew bus
    with fade

    if day3_choice_lonely :
        play sound "audio/noise_reverb_ambient_harris cole & aso - safe now (slowed & reverb).mp3" fadein 8.5 fadeout 11.5 volume 0.2
        pause 3.0
        if day2_nadya_have_a_dialog and (not day1_pasha_kfc or day2_sanya_vote_for_ussr or day1_yuli_agreed_after_kfc):
            show nadya angry at right
            with dissolve
            $ day3_choice_lonely = False
            $ day3_choice_nadya = True
            nadya "Привет! Я не понимаю, а почему ты сел один-то?!"
            sanya "Прости... Я не очень хотел садиться к кому-то. Не было настроения."

            show yuli sad at left
            with dissolve

            yuli "Ты почему не со мной сел, Саш? Мы же так мило общались..."
            yuli "Погоди, девочка слева от меня это вообще кто?"

            show yuli angry at left
            with dissolve

            yuli "Ты что, сразу нескольким девочкам пообещал сесть, а теперь вообще садишься один?!"

            scene black 
            with dissolve

            sanya "Девочки, давайте не будем ссориться! Ляжем спать, погоняем автобус во сне..."

            window hide
            screen bus_day0():
                default bus_minigame = BusMinigameDisplayable(hi_score, 0)
                add bus_minigame
            
            call screen bus_day0

            if int(_return) > int(hi_score):
                scene black
                centered "{size=+50}Новый рекорд!{/size}"
                centered "{size=+50}Счёт: [_return]{/size}"


            $ hi_score = max(hi_score, int(_return))
    

            "Проснувшись, автобус уже тронулся и я не застал Юлю на своём месте."
            "Я поднялся и прошёся по рядам... Нашёл Надю и обратился к ней"
            sanya "А ты не видела Юлю? Она же с нами садилась? Неужели из-за меня решила не ехать вовсе..."
            $ mood_counter -= 1;
            "Надя что-то буркнула в ответ, явно не желая  даже разговаривать со мной сейчас."
            "Я молча сел рядом. Будь что будет"



        if day2_nadya_have_a_dialog :
            show nadya angry
            with dissolve
            $ day3_choice_lonely = False
            $ day3_choice_nadya = True
            nadya "Привет! Я не понимаю, а почему ты сел один-то?!"
            sanya "Прости... Я не очень хотел садиться к кому-то. Не было настроения."
            nadya "Мы же с тобой договаривались! Разве это правильный поступок?"

            hide nadya angry
            with dissolve

            "Надя молча села рядом. Говорить дальше она ничего не хотела. Я же побоялся сделать всё ещё хуже"

            jump _sanatorium

        elif not day1_pasha_kfc or day2_sanya_vote_for_ussr or day1_yuli_agreed_after_kfc :
            $ day3_choice_lonely = False
            $ day3_choice_yuli = True
            show yuli angry
            with dissolve

            yuli "Привет! Я не понимаю, а почему ты сел один то?!"
            sanya "Прости... Я не очень хотел садиться к кому-то. Не было настроения."
            yuli "Мы же с тобой договаривались! Разве это правильный поступок?"

            hide yuli angry
            with dissolve

            "Юля молча села рядом. Говорить дальше она ничего не хотела. Я же побоялся сделать всё ещё хуже"

            jump _sanatorium

        else :
            
            $ day3_choice_lonely = True
            jump _alone


    elif day3_choice_nadya :
        play music "audio/sound-in-bus.mp3" fadein 4.0 fadeout 5.0 volume 0.10
        sanya "Привет, в этот раз запаслась чапой? А то мне кажется, я взял маловато!"

        show nadya smiles
        with dissolve

        nadya "Ха-ха-ха, конечно взяла, если будем жить рядом, можем вместе ходить курить."
        "Она такая необычная – можно говорить, что правда думаешь, и не стеняться, хотя бы в плане сигарет."
        sanya "Кстати, а зачем тебе ехать в санаторий?"

        show nadya giggles
        with dissolve

        nadya "А ты как думаешь? Не с отитом же!"
        "Зато, зная какие справки она собирала, можно не сомневаться в здоровье её ануса..."
        sanya "Не знаю... может что-то с легкими?"
        "Курит-то она много..."
        nadya "Шерлок Холмс нервно курит, конечно, с твоей дедукцией! А ты зачем едешь-то?"
        sanya "Да как-то отвлечься надо и здоровье поправить. Тяжело так после лета сразу на учёбу, тем более когда все лето занимался хуйнёй."

        menu :
            "Да ладно..? Слушай, а какой у тебя любимый цвет?" :
                nadya "Цвет?.. {w}Зелёный, наверное..."
                nadya "Слушай, а ты тоже не выспался?{w} Давай поспим, пока едем?{w} Не могу соображать ничего,{w} что ты говорил? Сплю уже."

            "Меньше бы курила, сейчас бы дома отдыхала. Полной грудью дышала бы, ха-ха." :
                $ rel_nadya -= 1
                "Надя обиделась и мне пришлось отсесть. Не думаю, что мы серьезно поссорились."
                jump _sanatorium
        
        stop sound fadeout 2.0
        jump _sanatorium

    elif day3_choice_yuli :

        $ is_bad_ask = False

        play music "audio/sound-in-bus.mp3" fadein 4.0 fadeout 5.0 volume 0.10
        "Сяду-ка я к Юле – проверенный вариант, так скажем."
        sanya "Юль, привет..."

        show yuli happy
        with dissolve

        if day1_pasha_kfc == True :
            yuli "Приветик! Хоть здесь ты побудешь без своего Пашки-алкашки"
            show yuli sad
            with dissolve

        else :

            sanya "Жалко конечно, что Паша не поехал, мне будет его не хватать"
            yuli "Да ладно тебе, нужен тебе этот качок-харчок!"
            sanya "Паша мне очень помогал в жизни, иногда как прихватит – так только его шутка в себя приведет."

        if day1_pasha_kfc == False and day2_sanya_vote_for_ussr == True :

            yuli "Как думаешь, мой поцелуй..."
            play music "audio/heart.mp3" fadein 0.3 fadeout 0.3 volume 0.2
            "Что...?! Что она говорит! Я не готов!!"

            show yuli horny
            with dissolve

            yuli "смог бы привести тебя в чувство?"
            "Блядь! Что отвечать?"

            menu :
                "У нас ещё весь вечер впереди, Юлечка!" :
                    $ rel_yuli += 1
                    stop music fadeout 0.1
                    play music "audio/sigma.mp3" volume 0.7
                    camera: 
                        linear 1.5 zoom 1.0 center
                        ease 0.5 zoom 1.5 yalign 0.01
                        linear 2.0 zoom 1.5 yalign 0.99
                        linear 0.9 zoom 1.0 center
                    pause 4.0

                "Ну если только мне искусственное дыхание нужно будет..."  :
                    $ rel_yuli -= 1
                    stop music fadeout 0.1
                    play music "audio/fail.mp3" volume 0.2
                    scene black
                    centered "{w=1.3}{nw}"
                    centered "{size=+24}Участие принимали:{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nAsind{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nDarlingInSteam{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nDanilka108{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nXpomin{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nTheNorth{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nArtsBer{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nJuravl{fast}{w=1.3}{nw}{/size}"
                    centered "{size=+24}\nrero{fast}{w=1.3}{nw}{/size}"
                    scene firstDays neew bus
                    
        stop music fadeout 0.5 
        play music "audio/sound-in-bus.mp3" fadein 3.0 fadeout 5.0 volume 0.10

        show yuli shy
        with dissolve

        yuli "На самом деле, я рада, что ты тоже едешь в санаторий!"
        yuli "Кстати, а у тебя какие-то проблемы со здоровьем или ты просто так?"
        sanya "Да у меня последнее время что-то ночи становятся все длиннее, а дни все тусклее. Надо отвлечься как-то, природа, думается мне, – самое то!"

        if day1_sanya_wants_camp == True:
            "Главное не говорить, что меня мамка сюда отправила, а то не видать мне ничего с юлькой."

        sanya "А ты почему едешь? Учёбу прогулять хочешь?"
        
        if day1_sanya_wants_camp == False :
            yuli "Да меня мама отправила, говорит, что отвлечься пора бы, а то я все лето проварилась в делах"
        else :
            yuli "Да пришло уведомление, я долго не думала, решила – надо ехать"

        "Мы так похожи! Но я чувствую, что сил больше на разговор у меня нет, слишком уж рано мы едем, надо бы отдохнуть"
        

        if (day1_pasha_kfc == True and day1_yuli_agreed_after_kfc == False) or day2_sanya_vote_for_ussr == False :
            sanya "Ты не хочешь поспать? Я чуть не умер так рано вставать"
            "Пока я говорил, Юля уже сладко спала, не дожидаясь моего предложения"

        hide yuli shy
        with dissolve

        jump _sanatorium

label _alone :
    play sound "audio/heart.mp3" fadein 4.0 fadeout 0.5 volume 0.3
    show night:
        alpha 0.0 center
        linear 4.0 alpha 1.0
        block:
            linear 1.0 zoom 1.2
            linear 0.6 zoom 1.0
            repeat
    "Смотря на пустой автобус, я понял лишь одно – я никому не нужен."
    "Впрочем, оно и не удивительно, последние дни я всё делал не так, как нужно было бы."
    "Пустота автобуса, предначертанная жизнью, будто говорила мне, что я неудачник, что я никому не был нужен и не буду."

    play music "audio/sound-in-bus.mp3" fadein 1.5 fadeout 2.0 volume 0.1 

    "Всё, что мне оставалось, – это молча смотреть в окно и наблюдать на проезжающие леса, дома,"
    
    screen bus_day0():
        
        default bus_minigame = BusMinigameDisplayable(hi_score, 0)
        add bus_minigame

    scene black with Fade(3.0, 0.0, 0.0)
    $ hi_score = 1000
    centered "{size=+24}Избежать трагедии нереально. Нет смысла даже что-то предпринимать.{/size}"
    window hide
    call screen bus_day0

    if int(_return) > int(hi_score):
        scene black
        centered "{size=+50}Новый рекорд!{/size}"
        centered "{size=+50}Счёт: [_return]{/size}"
        jump _sanatorium

    $ hi_score = max(hi_score, int(_return))

    play sound "audio/diskoteka_avaria.mp3"
    extend " ИКАРУС????"
    window hide

    play music "audio/rock_live_music.mp3" fadein 5.5 fadeout 1.5 volume 0.2

    centered "{size=+24}Автобус попал в аварию.\nПогибло два человека.\nЕдинственный Пассажир и водитель.{/size}"
    $ renpy.pause(1, hard=True)
    stop sound
    jump _end

label _sanatorium :
    stop music
    stop sound
    scene black with fade
    play sound "audio/typewriter-sound.mp3" volume 0.5 loop
    centered "{size=+30}{font=fonts/sfpro_semibold.ttf}{cps=4.5}День четвёртый.  {nw}{/cps}{/font}{/size}"
    stop sound

    scene firstDays black scen
    with dissolve

    pause 2.0   
    
    play music "audio/sound-in-bus.mp3" fadein 1.0 fadeout 2.0 volume 0.06
    play sound "audio/forest-sound.mp3" fadein 3.0 fadeout 2.0 volume 0.06


    "Мы наконец-то подъезжаем к \"Новомысу\" – санаторию, в котором мне придётся провести целую неделю. Надеюсь, это будет стоить того."

    scene sanatorium forest neer san with dissolve:
        block:
            linear 1.9 zoom 1.01 center
            linear 1.9 zoom 1.0 center
            repeat


    "Красивая природа дала понять, что санаторий находится в глуши. Всё вокруг отдавало зелёными оттенками и говорило о первозданности."
    "Высокие и пушистые деревья рядом с обочиной заставляли каждую часть тела расслабиться, почувствовать себя свободным."
    "Река, которая проходила под небольшим мостом, текла в неизвестную мне даль, я ощущал потрясающую энергетику этого удивительного места."
    "Наблюдая за этой природой, я не заметил, как мы начали заезжать на территорию санатория."
    stop music fadeout 2.0
    stop sound fadeout 2.0

    play sound "audio/bus.mp3" noloop fadein 1.5 fadeout 1.0 volume 0.1
    pause 2.0

    valeria "Так, выгружаемся!"
    
    stop music fadeout 1.5

    scene sanatorium sanatorium
    with dissolve

    play sound "audio/forest-sound.mp3" loop fadein 1.5 fadeout 3.0 volume 0.1

    "Конструктивный стиль, полный острых углов и кубических форм."
    "Никаких архитектурных излишеств, но много зелени, клумб"
    "Вся эта свистопляска буйной цветастой зелени, бесцветных стен, да и общая атмосфера легкой запущенности – все это веяло легкой меланхолией, словно весь этот санаторий – отражение моей жизни."
    "Человек из толпы" "Будто в прошлое попал!"
    "Не могу не согласиться, вид старенького санатория оставлял приятные, душевные чувства где-то в глубине меня."
    "Мне сразу вспомнились рассказы моего уже почившего дедули, о том, как он был сначала октябрёнком, а потом и пионером."
    "Встав, я в числе первых вышел на воздух. Он мне показался необычайно свежим, видимо, годы жизни в городе дали о себе знать."
    "Водитель уже открыл багажное отделение и, с неохотой доставал наши сумки, ставя их прямо на пыльный бетон."
    "Достав пачку чапмана и вынув сигарету, я сунул сладковатый фильтр в рот, планируя как следует затянуться после долгой дороги."
    
    show valeria happy
    with dissolve

    valeria "Так, молодые люди, одно из правил санатория гласит, что курить можно только в строго отведенных местах, чтобы не мешать другим отдыхающим!"
    valeria "А лучше и вовсе не курить. Вы, как-никак, на лечение приехали!"
    
    menu :
        "Жестко раскурить чапу" :
            $ day4_smoke_after_words_valeria = True
            $ rel_valeria -= 3
            "Поездка была настолько долгая, что отказать в сигаретке себе я никак не мог, даже не смотря на запрет со стороны вожатой."
            
            play sound "audio/cigarette.mp3" noloop fadein 0.5 fadeout 0.5
            pause 3.0

            "Проигнорировав её, я с удовольствием втянул ароматный дым любимого чапмана."
            "Никотин приятно ударил в голову, лёгкие разжались и я, с удовольствием, продолжил смаковать сигаретку."

            show valeria angry
            with dissolve

            $ str_for_notification = "{size=-12}Валерия запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            "Валерия Владимировна неодобрительно глянула на меня."
            sanya "Мне пиздец..."   

            "От этого взгляда мурашки пошли по спине. Надеюсь она не заставит таскать мешки с сахаром по всему санаторию."
            valeria "А сейчас, давайте я вам проведу небольшую экскурсию, пока мы идём до ваших комнат."

            hide valeria angry 
            with dissolve

        "Сдержаться" :
            $ day4_smoke_after_words_valeria = False

            "Валерия Владимировна неодобрительно посмотрела на тех, кто её проигнорировал и с вежливой улыбкой произнесла."

            $ str_for_notification = "{size=-12}Валерия запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            valeria "А сейчас, давайте я вам проведу небольшую экскурсию, пока мы идём до ваших комнат."

            hide valeria happy
            with dissolve
        
        "Снести кабину" if day3_choice_lonely :
            $ day4_smoke_after_words_valeria = True
            $ rel_valeria -= 10
            
            play sound "audio/punch.mp3" noloop fadein 0.5 fadeout 0.5
            with hpunch
            pause 2.0
            
            show valeria angry
            with dissolve
            "Въебав ей, я с удовольствием втянул ароматный дым любимого чапмана."
            "Никотин приятно ударил в голову, лёгкие разжались и я, с удовольствием, продолжил смаковать сигаретку."
            
            $ str_for_notification = "{size=-12}У этого действия будут ебать какие последствия{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            "Валерия Владимировна неодобрительно глянула на меня."
            sanya "Да похуй чё." 

            "От этого взгляда мурашки пошли по спине. Надеюсь она не заставит таскать мешки с сахаром по всему санаторию."
            valeria "Хуй с тобой, давайте я вам проведу небольшую экскурсию, пока мы идём до ваших комнат."

            hide valeria angry 
            with dissolve

    scene black
    with dissolve

    stop music fadeout 0.4
    play sound "audio/footsteps_asphalt.mp3" fadein 0.5 fadeout 0.5 volume 0.8
    pause 2.0
    
    "Валерия Владимировна бодро шла вперед, громко информируя нас о том, как же хорош этот санаторий и как же качественно мы тут отдохнем. "

    scene sanatorium sanatorium park
    with dissolve

    play sound "audio/forest-sound.mp3" loop fadein 1.0 fadein 2.0 volume 0.1

    "Я плёлся без особого энтузиазма, лениво поглядывая по сторонам, но вот семьи, — молодые и не очень, с детьми и адекватные..."
    "Весело шагали в ногу, следуя за энергичной сопровождающей."
    "Среди всей когорты приехавших на лечение, было мало молодых, что тоже отнюдь не добавляло мне настроения."
    "Старость, думал я, подступает незаметно. Как и всякая другая болезнь." 
    "Вот ты здоров, силен, молод и можешь выдуть чекушку всухую, а на утро выпить крепкого чаю и быть в строю."
    "А потом раз – и вот ты уже хрустишь коленками и боишься лишний раз наклониться, потому что темнеет в глазах." 
    "Ну, рядом хотя бы есть парочка жгучих красоток, которые вполне могут скрасить мои оздоровительные процедуры. "
    extend "А может и не просто скрасить... Хе-хе."

    play music "music/life_blossom.mp3" fadein 2.5 fadeout 3.0 volume 0.3
    
    if day3_choice_yuli :
        "Я незаметно оглянулся в поисках Юли, в мыслях уже готовый пригласить её на совместное принятие грязевой ванны."
        "Как бы я не крутил головой, никак не мог найти её. Юли нигде видно не было. Может, она пошла к себе в комнату, минуя экскурсию? А может ей стало плохо?"
        "Гадать бессмысленно, в любом случае мы встретимся – санаторий небольшой. Может и вовсе процедуры проходить вместе будем, хе-хе..."
        "Но всё равно неприятно, с ней бы в любом случае экскурсия была бы веселее."
        "Разочарованно вздохнув, я ускорил шаг, догоняя наш отряд молодых и не очень. Поправив рюкзак, с ещё более дерьмовым настроением, поплелся в самом конце."
    elif day3_choice_nadya :
        "Я незаметно оглянулся в поисках Нади, в мыслях уже готовый пригласить её на совместное принятие грязевой ванны."
        $ mood_counter -= 1
        "Найдя искомую в компании какого-то парня, я приветливо махнул ей." 
        "Надя помахала в ответ, и продолжила щебетать с этим пацанчиком, что в довесок со своей сумкой, тянул и её вещи. Что-то не помню его в автобусе."
        "Где-то под сердцем неприятно затянуло, а изнутри начала подниматься тихая волна жгучей злобы. Но я тут же одернул себя, немного удивившись порыву."
        "Мы с ней даже толком не знакомы, что это я тут начал. К тому же, не факт, что это её парень."
        "Может знакомый или родственник? Да и вообще какое мне дело!"
        "Потряся головой, словно отгоняя наваждение, я поправил рюкзак и с ещё более дерьмовым настроением, поплелся в самом конце."
           
    "Фоном неслась складная, явно много раз произнесенная, речь Валерии Владимировной."
    "Там мелькали объяснения режима, правил и процедур, но я особо не слушал, обращая внимание больше на окружение."
    "В конце концов, мне тут жить ещё неделю."
    "Территория санатория была поистине огромной, но зданий на нем было мало. Да и сами здания были довольно компактными, явно не рассчитанными на большое количество людей."
    
    show valeria happy at center
    with dissolve

    valeria "Вот тут у нас медпункт, если кому-то станет плохо."

    scene sanatorium medical post
    with dissolve

    "Выхватил я из общего потока речи конкретику, и,  ради интереса, взглянул в указанном направлении."
    "Медпунктом оказалось бетонное побеленное здание, формой напоминающее коробку из под спичек."

    show grusha happy
    with dissolve
    
    "На крыльце, в удобном с виду кресле, сидела женщина крепкого телосложения в белом халате, курящая трубку."
    sanya "Значит ей, сука, можно, а нам, простым людям, нельзя?"
    "Но в ответ моим мыслям раздался полный возмущения голос Валерии Владимировной."
    valeria "Агриппина Филипповна! Сколько раз я вас просила не курить около медпункта?!"

    show grusha neutral
    with dissolve

    "Названная меланхолично посмотрела на пышущую праведным гневом женщину и спокойно продолжила попыхивать задорно дымящейся трубке."
    "Валерия Владимировна ещё постояла, негодующим взглядом обжигая стойкую старушку, и в конце-концов сдалась, продолжив экскурсию."
    
    hide grusha
    with dissolve
    "Ха! А мне нравится эта бабка, надо будет с ней скорешиться."

    scene sanatorium park
    with fade

    "Я стал больше прислушиваться к болтовне Валерии Владимировной, но усталость и голод брали своё."
    "Идти стало тяжеловато, и, видимо, не только мне."
    "Послышалось недовольное ворчание, и Валерия Владимировна, поняв общее настроение стала закругляться."
    
    show valeria happy
    with dissolve
    
    valeria "Что ж, я думаю пора проводить вас по комнатам!"
    "Недовольное ворчание сменилось одобрительным гоготом. В том числе и моим."
   
    hide valeria
    with dissolve

    "Комнаты располагались в отдельном здании, самом большом из всех."
    "Четыре этажа, с обширными балконами, и, надеюсь, с такими же обширными комнатами."
    "Выглядело оно, конечно, побито, словно за ним почти не ухаживали, но, тем не менее, весьма добротно. Хорошо бы внутри было получше."
    "Ну, лучше, чем можно было ожидать..."
    
    scene black
    with dissolve
    
    play sound "audio/footsteps.mp3" noloop fadein 0.3 fadeout 0.3 volume 0.8
    pause 4.0

    play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1 volume 1.0
    pause 2.0

    scene sanatorium dormitory room
    with Fade(0.3, 0.4, 0.3, color="#000")

    "Все было достаточно светлым, но каким-то устаревшим, что ли..."
    extend " Или просто очень дешёвым."

    "Но при этом таким родным и знакомым, что захотелось вдохнуть полной грудью и сказать: "
    stop music fadeout 0.1
    extend "Этот амбал будет моим соседом?!"
    play sound "audio/pavel_cough.mp3"
    
    show pavel pavel neutral:
        ypos 0.1
        linear 0.9 xalign 0.9
    with Dissolve(1.0)
 
    show valeria happy:
        linear 0.1 xalign 0.1
    with Dissolve(0.5)
    
    "Вслед за мной в комнату зашел мужик. Конкретный такой мужик, будто бы только что вышедший из жесткого запоя. Пахло от него соответствующе."
    
    valeria "Это Пал Генадьич."
    "Терпеливо пояснила Валерия Владимировна."
    valeria "Он очень хороший мужчина, и теперь он ваш сосед по комнате."

    menu:
        "А можно мне другого соседа...":
            $ str_for_notification = "{size=-12}Павел запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            $ day4_tried_move = True;
            $ rel_pavel -= 1
            play music "audio/cherry-metal.mp3" fadein 2.5 fadeout 3.0 volume 0.09
                    
        "Да мы с ним два сапога пара!":
            $ str_for_notification = "{size=-12}Павел запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve


            $ day4_tried_move = False;
            $ rel_pavel += 1
            play music "music/start-kevin-macleod-hall-of-the-mountain-king.mp3" fadein 2.5 fadeout 3.0 volume 0.22
    
    if day4_tried_move == True:

        "Смотря на это вонючее нечто, что уже по-хозяйски развалилось на кровати, раскидав носки с тапочками в разные стороны, я понял одно."
        sanya "Я не собираюсь с ним жить."
            
        show valeria angry
        with dissolve

        valeria "Ну как же это! Павел Генадьевич очень хороший молодой человек! Культурный, аккуратный, чистоплотный..."
        "В этот момент этот культурный молодой человек, успевший зайти проведать туалет, как следует высморкался в раковину." 
        "От звука его хобота, казалось, затряслись стены во всех зданиях санатория."
        "Красноречиво глянув на Валерию Владимировну, я получил полный непонимания взгляд."
        sanya "Я не собираюсь с ним жить!"
        valeria "Ну, как же это! Ну..."
        sanya "Я требую другую комнату!"

        if day4_smoke_after_words_valeria :
            $ day4_fight = True
            $ day4_take_pill = True
            $ mood_counter -= 2
            $ rel_pavel -= 2

            valeria "К сожалению, у нас сейчас нет свободных комнат"
            "Она беспомощно развела руками, с вежливой улыбкой глядя на меня. Однако, судя по злорадным огонькам в глазах, это было неправдой. "
            sanya "Вы что, хотите, чтобы я жил... вот с этим?!"
            "Я махнул рукой в сторону алкаша, уже раздевшегося до трусов."
            "Тот, поняв, что речь идет о нём, поднял на меня своё пропитое лицо." 
            "Пару секунд на его лице отражался мучительный умственный процесс. Потом морда мужика побагровела."

            hide valeria angry
            with dissolve

            show pavel angry:
                linear 0.9 xalign 0.4
            with dissolve

            stop music fadeout 0.5
            play music "audio/fight.mp3" fadein 3.0 fadeout 2.0 volume 0.1

            pavel "Ты это мне, щенок?!"
            "Он вскочил, причем очень резво, что было неожиданно для его грузной комплекции."
            "Меня его порыв никак не впечатлил. Уж с кем я точно справлюсь, так это с пропитым алкашом. "
            sanya "Тебе, морда пропитая."
            "Руки чуть задрожали, а дыхание предательски ускорилось, по спине пробежал холодный пот. Не от страха, нет – от прилива адреналина."
            "Я корпусом повернулся к приблизившегося вплотную алкашу, едва сдерживаясь, чтобы не поморщиться от запаха перегара. "
            "Я, конечно, тоже не трезвенник, бывало и на улице засыпал. Но чтобы вот так... "
            "Алкаш возвышался надо мной, как Голиаф над Давидом, но так же как и Давид, я не дрогнул перед великаном."
            pavel "Ты меня что, алкашом назвал?"
            "Глаза его опасно сузились, но меня таким точно не напугаешь. Видывали и пострашнее."

            play sound "audio/punch.mp3" noloop fadein 0.1 fadeout 0.1
            with sshake
            "Неожиданно челюсть взорвалась болью, а сознание поплыло в неведомые дали."
            "Я даже не успел заметить, как этот ублюдок прописал мне оплеуху!"

            play sound "audio/punch.mp3" noloop fadein 0.1 fadeout 0.1   
            with hpunch
            "На ногах устоять я смог, хоть ноги и подкосились, однако челюсть дала отбой."
            
            play sound "audio/Fall.mp3" fadein 0.1 fadeout 0.2
            scene firstDays black scen
            with Fade(0.5, 0.5, 0.5, color="#000")
            
            "Вот тут у нас проблемы, Ватсон! Бухнувшись на колени, я судорожно пытался вздохнуть, царапая пальцами плитку." 
            stop music fadeout 3.0
            "Но мучился я не долго – висок взорвался болью и я потерял сознание."
            "Очнулся я от резкого запаха, чуть ли не вскочив с  кушетки.  Но чьи-то стальные руки крепко прижали меня к жесткой поверхности, не давай двинуться лишний сантиметр. "

            scene firstDays medicina
            with fade
            
            play music "audio/medicine_sound.mp3" noloop fadein 1.0 fadeout 1.0
            play sound "audio/pressure_apparat.mp3" noloop fadein 1.0 fadeout 1.0 volume 0.2
            
            show grusha happy
            with dissolve

            with hpunch

            grusha "Ишь, какой резкий драчун! Да стой ты!" 
            "Вырываться я перестал только тогда, когда понял, что нахожусь в медицинском кабинете, а передо мной медсестра, а не тот бугай. "
            "Посветив мне фонариком в глаза, и поводим им же перед носом, Агриппина Филипповна (а это была именно она, я её хорошо запомнил) осталась довольна осмотром. "
            "Засунув руку в карман халата, она сунула мне под нос таблетку."
            grusha "На! Выпьешь после обеда, чтобы голова быстрее прошла."
            sanya "Спасибо..."
            grusha "Пожалуйста. Идти можешь?"
            
            stop sound fadeout 0.3            
            sanya "Могу..."
            show grusha angry
            with sshake

            

            grusha "Ну так и иди на хуй отсюда!"

            
            "Не став больше нужного занимать эту колоритную женщину, я пружиной подскочил с кушетки, охнув от резкой вспышки боли в голове. "
            "Баба Груша на это только хмыкнула, доставая из второго кармана огромную трубку. Глазами она указала на выход."
            "Поняв всё без лишних слов, я ретировался из кабинета."
            
            stop music fadeout 0.3            
            
            show black
            with dissolve
            
            play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
            pause 1.5
            
            play sound "audio/footsteps.mp3" noloop fadein 0.2 fadeout 0.3
            pause 2.0 
            
            scene medical post
            with fade

            "Вот же ж гад! Не ожидал я от пропитого алкаша такой силы и скорости. Ну, сам виноват... "
            "Достав из кармана чапу, я закурил."
            
            play sound "audio/cigarette.mp3" fadein 0.5 fadeout 0.5 volume 0.6
            pause 4.0

            "Мда-а-а... Весело первый день здесь начинается, ничего не скажешь. "
            "Я посмотрел на время. "
            sanya "Ну, хотя бы на обед не опоздал... Может даже с девчонками встречусь."
            "Подбодрив себя подобным образом я поплелся в сторону столовой. "

            scene sanatorium canteen
            with fade

        else:

            $ day4_fight = False
            $ day4_with_skin = True

            "Явно через силу, но Валерия Владимировна все же произнесла:"
            valeria "Ну, у нас есть одна свободная комната... Можем заселить вас туда. Но только в качестве исключения."
            sanya "Было бы неплохо."
            "Покивал я важно."
            "Надеюсь, там будет девочка..."
            stop music fadeout 1.5
            valeria "Прошу за мной."

            play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.0
            
            scene sanatorium walkway
            with fade
            
            play sound "audio/door_close.mp3" noloop fadein 0.1 fadeout 0.1

            show valeria angry at center
            with dissolve

            play sound "audio/footsteps.mp3" noloop fadein 0.1 fadeout 0.1

            "Шли мы недалеко, комната была буквально через пару дверей."
            valeria "Вот ваша комната, располагайтесь. А я пойду проверю остальных заселяющихся."
            
            hide valeria angry
            with dissolve

            "Полный предвкушения, я открыл дверь. "
            play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.0
            play music "audio/skin_music.mp3" fadein 5.0 fadeout 2.0 volume 0.1
            scene sanatorium skin dormitory room
            with fade
            
            play sound "audio/door_close.mp3" noloop fadein 0.1 fadeout 0.1

            "Меня встретил бардак и разбросанные везде носки с футболками, а на кровати, в позе йога, сидел бритый паренек, явно скинхедской наружности."
            extend " Облом..."
            "Услышав шум, он открыл глаза."
            
            show skin angry
            with dissolve
            
            
            skin "Тихо, блядь! ты мешаешь моему слиянию с бесконечно вечным!"
            "Знатненько прихуев от такого приветствия, я пробурчал извинения и виновато прошёл к свободной кровати, поставив сумку."
            
            hide skin
            with dissolve
            
            "Заебись, из огня да в полымя, охуенно переселился. "
            "Раскладывая свои вещи, я украдкой посматривал на скинхеда. "
            "Выглядел он, конечно, колоритно. Кожанка на чёрную кофту, джинсы, абсолютно лысый череп. "
            "Находиться в комнате с этим чудаком было не очень комфортно. Решение переселиться от вонючего, но заурядного алкаша, уже не выглядело хорошим. "
            
            show skin angry
            with dissolve

            skin "Да бля, че ты на меня зыришь?"
            "От неожиданности я вновь оторопел, не зная, что ответить. Он же с закрытыми глазами был, как он увидел?"
            skin "Ладно, бля, похуй..." 
            "Он резко вскочил с кровати и замер в странной позе, постояв так пару секунд, он потянулся, хрустнув костями, и неожиданно протянул руку."

            show skin neutral
            with dissolve

            skin "Меня Мыкало звать!"
            sanya "Саня..."
            skin "Здрав будь, Саня!"
            sanya "Здрав..." 
            "Вот это имечко конечно.."
            skin "Располагайся, че замер-то, помочь чем что ли?"
            "Я осознал, что я неприлично долго разглядываю своего необычного соседа, так что резко одернув руку, я буркнул:"
            sanya "Все нормально, я сам как-нибудь."
            "Развернувшись, я продолжил разбирать свои вещи, стараясь сделать это как можно быстрее, чтобы смыться из комнаты на обед."

            show skin happy at center
            with dissolve

            skin "Странный ты какой-то..."
            "На себя посмотри, древняя реликвия... Вслух я это, конечно, не сказал. "
            skin "О, я тебя вспомнил, ты с кислой мордой шёл позади всех на экскурсии."
            sanya "Ну, было дело..."
            skin "А все потому, что у тебя энергетика загрязнена!" 
            sanya "Чего?"
            skin "Прочиститься тебе надо, вот что! Где-то у меня тут была одна штука..."
            "Он чуть ли не с головой зарылся в свою сумку, увлеченно там что-то разыскивая."
            sanya "Слабительное что ли?"
            skin "Во!"
            "Он воздел руку в потолок, в ней было зажато что-то, что было подозрительно похоже на самокрутку..."

            skin "По древним рецептам наших славных предков! Сушеные листья клена, березы, акации и куча разных полезных трав! Вмиг встанешь на ноги!"
            
            "Это он мне древнерусский косячок предлагает?"

            menu :
                "Жестко вспомнить предков" :
                    $ day4_smoke_old_siggarete = True
                    $ day4_take_pill = True
                    $ mood_counter -= 1
                    $ rel_skin += 3

                    $ str_for_notification = "{size=-12}Мыкола запомнит это{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve


                    show skin neutral at center:
                        linear 0.1 ypos 1.2
                        linear 0.3 zoom 1.2
                    pause 0.3

                    "Я с сомнением посмотрел на протянутую руку, потом на честную морду панка."
                    "Тот, заметив мои душевные метания, доверительно произнес: "
                    skin "Сам собирал и набивал, точно по рецепту!"
                    sanya "И где ты эти рецепты откопал?"
                    "Не то, чтобы мне было интересно, но иногда забавно слушать вот таких вот... индивидов. Мыкало, услышав вопрос по теме, радостно начал объяснять."
                    skin "Я когда у бабушки на чердаке убирался, одну книгу нашел, можно сказать, манускрипт!"
                    extend " Русскими рунами писано было, Родом клянусь! И бумага такая, будто из кожи сделана, ну, ты понимаешь, о чем я..."
                    sanya "Ну как сказать..."
                    skin "Короче, я на один форум зашел, там мне все и объяснили. Сказали, это древний травник, возможно, созданный ещё при Рюриковичах, представь!"
                    sanya "А ты, оказывается, не один такой..."
                    skin "Вот, я его изучил поподробнее, там некоторые слова знакомы были, и понял, что медицина в сравнении с этим – чепуха полная! Ты знал, что все проблемы со здоровьем – от нестабильной связи с землей идут?"
                    sanya "Ну хоть не с Нибиру..."
                    skin "Я тоже сначала смеялся, а потом попробовал – и прозрел!"
                    
                    show skin happy at center:
                        ypos 1.2
                        linear 0.3 zoom 1.2
                    with dissolve

                    "Он вновь протянул мне скрутку, причем с таким одухотворенным лицом, что я просто не смог отказать. Вот так в секты и попадают."
                    sanya "Ну, ладно, давай своё чудодейственное средство."
                    "Он с готовностью сунул мне в руку скрутку, кажется, в сушеном лопухе, и достал зажигалку."
                    
                    show skin happy at center:
                        zoom 1.0
                    with dissolve
                    
                    sanya "У меня своя."

                    stop music fadeout 2.0

                    play sound "audio/cigarette.mp3" noloop fadein 0.2 fadeout 0.2
                    pause 3.0

                    "Я достал из кармана жигу и, чиркнув кремнем, подпалил краешек травяной папиросы."
                    "По комнате распространился запах горелой травы, но не то, чтобы он неприятно пах. Ободренный этим фактом, я затянулся. "
                    
                    play sound "audio/pavel_cough.mp3" noloop fadein 0.1 fadeout 0.1

                    sanya "Кха-кха-кха-кха!" 
                    "Легкие обожгло огнем, а в голове зашумело. Кашель был настолько сильный, что меня чуть не вырвало. "
                    extend "Дышать я не мог, так что очень скоро начал задыхаться."
                    skin "Ой, я тебе, кажется, не ту дал! Щас, подожди... Где же она..."
                    "Под мой нестерпимый кашель он вновь принялся копаться в своей сумке, и в скором времени извлек оттуда новую скрутку. "
                    
                    play sound "audio/pavel_cough.mp3" noloop fadein 0.1 fadeout 0.1
                    
                    skin "Держи! Это то, что надо!"
                    sanya "И... Иди... Помоги...."
                    "Я даже не смог послать его на хуй, из-за того, что очень сильно задыхался."
                    "Сознание плыло, а я всё ещё не мог вздохнуть. Липкий страх пополз по спине и с каждой секундой без воздуха он становился сильнее."
                    sanya "Вра... Врача..."
                    "Паника захлестнула меня, и к кашлю прибавилась ещё и одышка. Настоящее комбо и фаталити для дыхательных путей."
                    "В глазах темнело, от кашля меня вырвало, что отнюдь не способствовало поступлению кислорода. "
                    "Да чтоб ещё раз я что-то пробовал из рук незнакомцев! "

                    stop music fadeout 2.0 

                    play sound "audio/Fall.mp3" noloop fadein 0.1 fadeout 0.1
                    
                    scene black
                    with Fade(0.4, 0.5, 0.4, color="#000")
                    
                    "С такими мыслями я и ушел в отруб."
                    
                    "Ох-х-х, как же мне хуево..."
                    "Перед глазами все вертелось и кружилось, а во рту будто бы насрали кошки. Причем несколько раз."
                    "Легкие болели так, будто бы их прострелили. Нахуй я согласился?.. Щас бы сидел в столовой, пил чаек с девчонками и в ус не дул."

                    scene firstDays medicina
                    with Fade(0.4, 0.5, 0.4, color="#000")
                    
                    play music "audio/medicine_sound.mp3" fadein 1.0 fadeout 1.0

                    play sound "audio/pressure_apparat.mp3" noloop fadein 1.0 fadeout 1.0 volume 0.2

                    show grusha happy
                    with dissolve

                    grusha "О, ты очнулся!"
                    "Я попытался рассмотреть источник голоса, но адский калейдоскоп перед глазами мешал это сделать. "
                    grusha "Рот открой."
                    "Но не успел я послушаться, как губ что-то коснулось и я почувствовал, что мне впрыснули что-то прямо в горло. "
                    "Закашлявшись от жуткой горечи, попавшей не в то горло, я блеванул в заботливо подставленный кем-то тазик. "
                    "Как следует прочистив желудок, я с облегчением откинулся на кушетке. "
                    
                    show grusha neutral
                    with dissolve

                    grusha "Полегчало?"
                    "Я снова не успел ответить – в рот опять что-то впрыснули, но не такое неприятное и не так резко, так что с трудом, но я смог проглотить препарат."
                    sanya "Вы кто? Где я?"
                    grusha "Я Агриппина Филипповна, твой ангел хранитель на случай, если опять будешь принимать сомнительные вещества."
                    extend "А находишься ты в раю, где ставят на ноги таких как ты."
                    sanya "А-а-а."
                    grusha "Бэ-э, дурында, ещё раз тут появишься – я палец о палец не ударю. Такой молодой, а уже... эх!"
                    "Бурчание продолжалось, но уже так невнятно, что разобрать было сложно. "
                    "С каждой минутой мне становилось все лучше и лучше. По крайней мере, вертолетики кончились, да и легкие не так сильно болели. "
                    "Наконец, я смог нормально осмотреться. "
                    "Обычный процедурный кабинет. В дальнем углу звенела колбами низенькая женщина, видимо, это и есть Агриппина Филипповна. "
                    "Обернувшись, она просканировала меня своим орлиным взглядом и что-то решив для себя сунула руку в карман. "
                    grusha "На! Выпьешь после обеда чтобы до конца все токсины вывести."
                    sanya "Спасибо..."
                    grusha "Пожалуйста, идти можешь?"
                    sanya "Могу..."

                    show grusha angry
                    with sshake

                    grusha "Ну так иди на хуй отсюда!" 
                    "Бодро вскочив, я вылетел пробкой из процедурного кабинета. "
                    
                    stop music fadeout 1.0                    
                    
                    play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1

                    show sanatorium medical post
                    with Fade(0.4, 0.5, 0.4, color="#000")

                    pause 0.3
                    
                    play sound "audio/door_close.mp3" noloop fadein 0.1 fadeout 0.1 

                    extend "Никогда так быстро в себя не приходил, хотя считай при смерти был. Баба Груша реально волшебница! "
                    "В животе заурчало, но аппетита как такового не было, поскольку чувство насранности во рту не пропало. Хотелось чем-то прополоскать рот, желательно пивком..."

                "Я ещё не обедал, закон Архимеда не работает" :
                    $ day4_smoke_old_siggarete = False
                    $ day4_take_pill = False
                    $ mood_counter += 1
                    $ rel_skin -= 1

                    $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    "Я с сомнением посмотрел на протянутую руку, потом на честную морду панка."
                    "Тот, заметив мои душевные метания, доверительно произнес:"
                    skin "Сам собирал и набивал, точно по рецепту!"
                    sanya "Ну сам и употребляй, а я кушать пойду"
                    skin "Э-э, я от сердца, считай, отрываю"
                    sanya "Считай, я сберег твое сердце, покеда"
                    skin "Ладно, но потом сам ко мне прибежишь!"
                    "Ничего не ответив, я вышел в коридор. Многовато чудиков что-то вокруг меня крутиться в последнее время. "
                    "Чувствуя легкий голод, я спустился в столовую, находящуюся на первом этаже."
    
    else:
        "Я решил не спорить с Валерией Владимировной и направился прямо к свободной кровати." 
        "На соседней в этот же момент развалился пластом жира Павел с тройным подбородком и тройным одеколоном."
        valeria "Вот и прекрасно! Надеюсь, вы подружитесь!"

        hide valeria happy
        with dissolve
        
        show pavel neutral:
            linear 0.5 xalign 0.5
        with dissolve

        "С этими словами неунывающая Валерия Владимировна ушла, оставив меня наедине с Павлом Геннадьевичем."
        pavel "Досданья, Влерья Ладимирна!"
        "Что-то нечленораздельное раздалось из уст Павла."
        "Ладно, возможно, что я слишком категоричен. В конце-концов это же не просто кусок жира, а ещё и кусок мышц проглядывается?"
        "За этим всем явно что-то стоит. Мужик понакачанней меня будет, чего это я."

        hide pavel neutral
        with dissolve

        "Может скорешимся с ним, кто знает? Но сначала надо разобрать вещи."
        "У меня их было немного, поэтому я быстро управился, рассовав всё по тумбочкам и единственному шкафу в комнате."
            
        "Павел Геннадьевич даром времени не терял, и от его кровати на всю комнату раздался богатырский храп."
        "Кажется, даже окна задрожали."

        play sound "audio/door_open.mp3" noloop fadein 0.3 fadeout 0.3 

        scene sanatorium balcony
        with Fade(0.3, 0.2, 0.3, color="#000")

        play music "audio/forest_walk.mp3" fadein 2.0 fadeout 3.0 volume 0.13

        "Выйдя на балкон, я невольно залюбовался открывшейся передо мной картиной."

        "Никогда не был особым ценителем ландшафтного дизайна, но этот вид и у меня вызывает восторг."

        "Множество клумб и цветов, которые складывались в незамысловатые узоры. Много беседок поодаль, изумрудные поляны и {w=0.2}{cps=8}{i}очень много деревьев.{/i}{/cps}"
        "Я глубоко вздохнул свежий воздух, пахший холодной рекой и мокрыми камнями, и у меня даже немного закружилась голова."

        "И курить не хотелось! Вот настолько плодотворно воздействовала на меня местная природа."

        play sound "audio/chair_crack.mp3" noloop fadein 0.2 fadeout 0.2  

        "Плюнув на всё, я плюхнулся в кресло и, любуясь видом, всё-таки достал свой ванильный чапман."

        play sound "audio/cigarette.mp3" noloop fadein 0.3 fadeout 0.3

        pause 4.0

        "Красота! Лепота!"
        "Кажется, я понимаю, что чувствовал Иван Васильевич, когда смотрел на Москву."
        "Всё-таки, есть в созерцании бесконечно вечного что-то великое, вдохновляющее, настраивающее на определённый умственный лад..."
        stop music
        play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.2
        play music "music/start-kevin-macleod-hall-of-the-mountain-king.mp3" fadein 5.5 fadeout 3.0 volume 0.22

        "{i}~Хр-р-р~{/i}"
        sanya "Да блядство!"
        
        "Вышло это неожиданно громко даже для меня."

        play sound "audio/pavel_cough.mp3" noloop fadein 0.1 fadeout 0.1

        "За стеной послышался громкий кашель, такой сильный, что я даже испугался."
        "Заглянув в окно, обнаружил, что Павел Геннадьевич сидит на кровати и пытается вздохнуть."
        "Голова его покраснела как помидор, а изо рта вырывался жуткий хрип."

        "Ой... " 
        extend "Как бы не вышло чего."

        "Но, слава богу, всё обошлось."
        "Казалось, что это даже пошло на пользу Павлу Геннадьевичу." 
        "По крайней мере, с кровати он встал очень резво."

        "Выйдя на балкон, он через нос вздохнул местный воздух. И со словами: \"Пиздато!\" достал сигареты."

        show pavel smile:
            ypos 0.1
            linear 0.3 xalign 0.1
        with dissolve        

        play sound "audio/chair_crack.mp3" noloop fadein 0.2 fadeout 0.2
        
        "Плюхнувшись на свободное кресло, которое жалобно скрипнуло под ним, но все же стоически выдержало, он закурил."
        
        play sound "audio/cigarette_one_shot.mp3" noloop fadein 0.2 fadeout 0.2
        hide pavel smile
        with None
        show cigarette_smoke
        show pavel smokes
        with dissolve
        
        "Мы оба наслаждались видом, тишиной и возможностью просто спокойно посидеть."
        "Никуда не нужно идти. Нет вечно давящей ответственности, горящих дедлайнов, беспокойства и стресса."
        "Тут по настоящему можно ощутить течение времени. Понять его силу, почувствовать мощь."

        pavel "Модные у тебя сигареты."
        "Павел Геннадьевич докурил свою и забычковал оранжевый фильтр."
        
        sanya "Да обычные, вроде. Чапман ванильный."
        pavel "С кнопкой, что ли?"

        "В его взгляде появилась насмешка."

        sanya "Нет, просто фильтр такой." 
        pavel "Дашь попробовать? А я тебе свои."

        "Он протянул пачку красного Мальборо."
        "Мы обменялись сигаретами и закурили."
        
        play sound "audio/cigarette.mp3" fadein 0.3 fadeout 0.3
        pause 4.0
        
        "После Чапмана, Мальборо показалось более крепкой, однако, я к ним быстро привык."
        "Голова немного закружилась, так что я старался делать более редкие тяжки."

        sanya "Хороший табак, впечатляет."
        pavel "Меня другой не берет."

        "Он сделал очередную тяжку, втянув сигарету чуть ли не в половину. Мощный мужик, зря я на него бузил."
        pavel "Неплохие сигареты."
        "Одобрительно проговорил он, выдыхая дым."
        pavel "А есть без лишних запахов? Не люблю я все эти ванили, вишни-хуишни, мне б нормального крепкого табачку."
        sanya "Да, вроде, есть классический чапман, но я его никогда не пробовал."
        pavel "Это хорошо, надо бы попробовать."
        "Он кинул сигарету в пепельницу. За пару тяг он дошёл до самого фильтра, и уже доставал следующую из своей пачки."
        "Я же понял, что многовато в себя никотина принял, так что тоже положил выкуренную наполовину сигарету."

        pavel "Я люблю чистый запах табака, без всяких примесей. Только так раскрывается его уникальный вкус."
        pavel "А если всякие вишни, арбузы, ванили добавлять, то в чем смысл? Иди салата наверни, если фрукты так нравятся."
        scene balcony
        show pavel smokes
        sanya "Ну не всем нравится чистый запах табака, некоторые пытаются его смягчить."
        pavel "Да-а-а, и так во всем! Все что-то пытаются смягчить, замаскировать, замылить. Зачем?!"
        pavel "Почему бы не наслаждаться тем, что-есть? Не зря же оно нам дано, правильно?"

        sanya "Но если совсем невмоготу, если так получилось, что не можешь привыкнуть и наслаждаться чем-то, то зачем это терпеть?"
        sanya "Можно же адаптировать под себя. В конце-концов любой человек стремиться к комфорту. Именно благодаря ему мы сейчас здесь сидим."

        pavel "Твоя правда, да. Тебя, кстати, как зовут-то?"
        sanya "Саня. Александр."
        
        "Я пожал протянутую руку."

        pavel "Меня Пал Генадич, будем знакомы."

        "Я посмотрел на время. Близился обед, так что пора бы собираться."
        "Поднявшись, я размял спину, затекшую от жестких кресел."
        pavel "Ты, вроде, хороший мужик, Саня, может быть тут посидим?"
        pavel "Что туда идти траву есть, я курочку привез с собой, картошечку."
        pavel "Тут стол есть, на нем расположимся, отметим, так сказать приезд."
        
        menu:
            "Отметим":
                
                $ str_for_notification = "{size=-12}Павел запомнит это{/size}"
                        
                show screen notification_popup_big
                with dissolve

                pause 2.0

                hide screen notification_popup_big
                with dissolve

                $ day4_drink = True
                $ rel_pavel += 3
                $ mood_counter -= 1

                "Ну, почему бы и не посидеть с хорошим человеком?"
                sanya "А давайте!"

                show pavel smile
                with dissolve
                
                pavel "Во-о-от! Вот это по-нашему!"

                scene sanatorium dormitory room
                with Fade(0.3, 0.4, 0.3, color="#000")

                play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                pause 1.0
                play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2 

                stop music fadeout 2.0

                "Вернувшись в номер, мы стали накрывать поляну. Павел Геннадьевич достал из своей сумки курочку, бережно завернутую в фольгу."
                "Потом пару контейнеров с салатами, жареной картошкой, нарезал сыр и колбасу."
                "Буквально через десять минут в нашем номере красовался добротный холостяцкий стол, венчала который бутылка армянского коньяка, бережно вынутая Павлом Геннадьевичем из отдельной сумки."
                "Разлив по складным стопарикам на два пальца, мы не чокаясь опрокинули их."
                
                show pavel smile
                with dissolve
                
                pavel "Ну, за знакомство!"

            "Да ну его":

                $ day4_drink = False
                $ rel_pavel -= 1
                $ mood_counter -= 1

                $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                    
                show screen notification_popup_big
                with dissolve

                pause 2.0

                hide screen notification_popup_big
                with dissolve

                sanya "Извините, Пал Геннадьич, но меня там кое-кто ждем в столовой, давайте в следующий раз?"
                "Взгляд мужчины погрустнел, но он всё равно протянул мне руку."
                pavel "Ничего, Саня, все нормально. Мы же тут неделю будем, ещё успеется!"

                hide pavel neutral

                "С этими словами он встал, хрустнув коленями, и прошёл в комнату."
                "Я, чувствуя легкий голод, спустился в столовую, находящуюся на первом этаже."

                scene black
                with dissolve

                play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                pause 1.0
                play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2 

                scene sanatorium walkway
                with Fade(0.2, 0.3, 0.2, color="#000")

                play sound "audio/footsteps.mp3" noloop fadein 0.2 fadeout 0.2
                pause 1.0

                scene black
                with dissolve

                pause 2.0

        if day4_drink == True:

            $ day4_take_pill = True

            "За первой бутылкой последовала вторая, за ней третья. Казалось, сумка Павлка Геннадьевича была бездонной."
            pavel "Ты, Санька, хороший парень! Тока тощий, шо тростинка." 
            pavel "Тебе бы ко мне в деревню на недельку, в поля, сразу в нормального мужика превратишься!"
            "Я в ответ промычал что-то нечленораздельное, всеми силами стараясь держать себя в вертикальном положении."
            pavel "Задохлик, как есть задохлик! Ну ничо, дядя Паша научит тебя как эту жизнь жить!"
            "Он хлопнул меня по плечу, что стало критическим для моего вестибулярного аппарата."
            "Перед глазами все поплыло. Пол и потолок поменялись местами и я со всего маху брякнулся об плиточный пол."
            
            play sound "audio/Fall.mp3" noloop fadein 0.1 fadeout 0.1
            with hpunch

            hide pavel smile
            with dissolve

            scene firstDays black scen
            with fade

            "Голова адски кружилась, меня штормило даже лежа."
            "Сквозь пелену и мельтешащие круги надо мной появилось обеспокоенное лицо Павла Геннадьича, а голос его доносился как из под земли."
            pavel "Санька, Санька! Ты голову расшиб!"
            "Он говорил что-то ещё но я уже не слышал. Сознание постепенно затухало."
            "Ох-х-х, как же мне хуево..."
            "Перед глазами все вертелось и кружилось, а во рту будто бы насрали кошки. Причем несколько раз."
            "Живот болел так, будто бы его прострелили, а пищевод саднил, будто я хлестал кислоту, а не коньяк."
            "Нахуй я согласился?.. Щас бы сидел в столовой, пил чаек с девчонками и в ус не дул."
            
            scene firstDays medicina
            with fade

            show grusha happy
            with dissolve

            grusha "О, ты очнулся!"
            "Я попытался рассмотреть источник голоса, но адский калейдоскоп перед глазами мешал это сделать."

            show grusha angry
            with dissolve

            grusha "Рот открой."
            "Но не успел я послушаться, как губ что-то коснулось и я почувствовал, что мне впрыснули что-то прямо в горло."
            "Закашлявшись от жуткой горечи, попавшей не в то горло, я блеванул в заботливо подставленный кем-то тазик."
            "Как следует прочистив желудок, я с облегчением откинулся на кушетке."
            
            show grusha happy
            with dissolve

            grusha "Полегчало?"
            "Я снова не успел ответить – в рот опять что-то впрыснули, но не такие неприятное и не так резко, так что с трудом, но я смог проглотить препарат."
            sanya "Вы кто? Где я?"
            grusha "Я Агриппина Филипповна, твой ангел хранитель на случай, если опять перепьешь. А находишься ты в раю, где ставят на ноги таких как ты."
            sanya "А-а-а-а."
            grusha "\"Б\", дурында, ещё раз тут появишься – рассолом буду отпаивать. Такой молодой, а уже... эх!"
            "Бурчание продолжалось, но уже так невнятно, что разобрать было сложно."
            "С каждой минутой мне становилось все лучше и лучше."
            "По крайней мере, вертолетики кончились, да и живот не так сильно болел."
            "Наконец, я смог нормально осмотреться."
            "Обычный процедурный кабинет. В дальнем углу звенела колбами низенькая женщина, видимо, это и есть Агриппина Филипповна."

            "Обернувшись, она просканировала меня своим орлиным взглядом и что-то решив для себя сунула руку в карман."
            grusha "На! Выпьешь после обеда чтобы до конца все токсины вывести."
            sanya "Спасибо..."
            grusha "Пожалуйста, идти можешь?"
            sanya "Могу..."

            show grusha angry
            with sshake
            
            grusha "Ну так иди на хуй отсюда!"
            "Бодро вскочив, я вылетел пробкой из процедурного кабинета."

            scene sanatorium medical post
            with fade

            "Никогда так быстро в себя после попойки не приходил, да ещё и такой жесткой. Баба Груша реально волшебница!"

            "В животе заурчало, но аппетита как такового не было, поскольку чувство насранности во рту не пропало."
            "Хотелось чем-то прополоскать рот, желательно пивком..."

    scene sanatorium canteen
    with dissolve

    stop music fadeout 0.5

    play music "audio/kfc-sound.mp3" fadein 1.0 fadeout 2.0 volume 0.2

    "Зайдя в столовую, я сразу почувствовал приятный запах котлеток."
    "Тут было немноголюдно, так что свободных столов было навалом. Видимо, некоторые решили пропустить в этот раз обед и отдохнуть с дороги."
    "Впрочем, я их понимал."
    "Сегодня подавали самое классическое блюдо из всех возможных: котлетку с пюрешкой, от которых поднималось настроение."
    "Кружка ароматного кофейного напитка или какао на выбор, пара кусочков хлеба с маслом и салат цезарь, с крупными кусочками жареной курицы."
    "Как бы слюной не истечь пока несу..."
    sanya "Балдёж!..."
    "Поместив пищу на поднос, я осмотрелся, выбирая куда сесть. Места было много, но в одиночестве сидеть не хотелось."
    "В дальнем углу приметил Юлю, сидящую в одиночестве." 

    if day2_nadya_have_a_dialog:
        "а также Надю, которая сидела в противоположной стороне у окна, и тоже, к счастью, одна."
        "К кому бы мне подсесть?"
    
    menu:
        "Подсяду к Юле":

            $ day4_yuli_meal = True
            $ rel_yuli += 2
            $ mood_counter += 2

            $ str_for_notification = "{size=-12}Юля запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            sanya "Юль, привет, здесь не занято?"

            show yuli greeting
            with dissolve
            
            yuli "Ой, Сашенька, привет, конечно присаживайся."

            play sound "audio/chair_crack.mp3" noloop fadein 0.1 fadeout 0.1

            pause 1.0

            sanya "А где ты была? Я тебя искал во время экскурсии."

            show yuli horny
            with dissolve
            
            yuli "Прости, я немного отвлеклась и потеряла группу. Пришлось самой всё осматривать."
            sanya "А-а-а, ну, ничего, я, тогда, давай позже тебе все покажу? После процедур можем погулять."

            show yuli happy
            with dissolve

            yuli "Да, конечно, я только рада буду."
            "На этой ноте наша небольшая беседа подошла к концу и мы оба принялись за еду."
            "Ну, что сказать, еда тут знатная! Давненько я не ел такой вкусной котлетки, а пюрешка вообще во рту таяла!"
            "Идеально солёная, без комочков с приятным молочным послевкусием."
            "Масло, уже успевшее подтаять, легко размазалось по ароматному, ещё теплому хлебу, наверное, его пекут прямо здесь."
            "А салатик идеально сочетал в себе свои ингредиенты, и этот баланс создавал прекрасную гармонию вкуса."
            
            play sound "audio/deep-moan.mp3" fadein 0.2 fadeout 0.2

            "Откинувшись на спинку стула, я с удовольствием выдохнул, чувствуя приятную сытость."

            pause 1.0

            "Сверху шлифанул плотным какао, не слишком сладким и не водянистым, прямо как я люблю!"
            
            sanya "Блаженство, не ожидал что еда здесь будет настолько вкусная."

            pause 2.0

            yuli "И не говори."
            "Мы оба развалились на стульях и потягивали наши напитки, наслаждаясь обществом друг друга."
            sanya "Как говорит один мой друг: после сытного обеда, по законам Архимеда..."
            extend "Чтобы жиром не заплыть – надо срочно покурить!"
            
            show yuli happy
            with dissolve

            sanya "Курить! Ты не против составить мне компанию?"
            yuli "Ну, не против, пойдём проветримся."
            "Я протянул ей руку, и мы направились прямиком в курилку."
            stop music fadeout 2.0
            
            scene black
            with dissolve
            
            play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.0
            
            play sound "audio/door_close.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.0
            
            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.5

            scene sanatorium alcove
            with dissolve

            play music "audio/forest-sound.mp3" fadein 0.3 fadeout 0.3 volume 0.3

            "Ей служила отдаленная беседка на живописном берегу реки. На столе стояли пепельницы, однако, в них не было ни одного окурка."
            "Видимо, это место пользуется особой популярностью."

            play sound "audio/cigarette.mp3" fadein 0.2 fadeout 0.2

            "Достав сигаретку, я закурил."

            pause 3.0

            show yuli empathy
            with dissolve
            
            yuli "Как тебе тут?"
            sanya "Ну, пока сложно сказать... В целом, нравится. Чистый воздух, вкусная еда."
            sanya "Скоро всякие процедуры начнутся. Поживём-увидим, как говорится."
            
            yuli "Тут очень спокойно и тихо. После шумного и грязного города – истинное наслаждение."
            sanya "И не говори..."
            "Так, в тишине, в которой так нуждались, мы и пробыли пару минут, пока я докуривал."
            
            show yuli shy
            with dissolve

            yuli "Ой, знаешь, мне уже пора. Процедуры там, всё такое. Давай вечером у меня встретимся?"
            sanya "Конечно, я только за."
            yuli "Тогда, до вечера?"

            show yuli horny
            with dissolve

            yuli "До вечера..."
            "На прощание мы слегка обнялись."
            "Режим есть режим, так что попрощавшись, мы разбрелись в разные стороны."

        "Подсяду к Наде" if day2_nadya_have_a_dialog:
            $ day4_nadya_meal = True
            $ rel_nadya += 2
            $ mood_counter += 2

            $ str_for_notification = "{size=-12}Надя запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            sanya "Надь, привет, здесь не занято?"
            
            show nadya giggles
            with dissolve

            nadya "Ой, Сашенька, привет, конечно присаживайся."
            play sound "audio/chair_crack.mp3" noloop fadein 0.1 fadeout 0.1 
            sanya "А где ты была? Я тебя искал во время экскурсии."

            show nadya light sad 
            with dissolve

            nadya "Прости, я немного отвлеклась и потеряла группу. Пришлось самой все осматривать."
            sanya "А-а-а, ну, ничего, я тогда давай позже тебе все покажу? После процедур можем погулять."

            show nadya smiles
            with dissolve

            nadya "Да, конечно, я только рада буду."
            "На этой ноте наша небольшая беседа подошла к концу и мы оба принялись за еду."
            
            "Ну, что сказать, еда тут знатная! Давненько я не ел такой вкусной котлетки, а пюрешка вообще во рту таяла!"
            "Идеально соленая, без комочков с приятным молочным послевкусием."
            "Масло, уже успевшее подтаять, легко размазалось по ароматному, ещё теплому хлебу, наверное, его пекут прямо здесь."
            "А салатик идеально сочетал в себе свои ингредиенты, и этот баланс создавал прекрасную гармонию вкуса."
            
            play sound "audio/deep-moan.mp3" fadein 0.2 fadeout 0.2

            "Откинувшись на спинку стула, я с удовольствием выдохнул, чувствуя приятную сытость."

            pause 1.0

            "Сверху шлифанул плотным какао, не слишком сладким и не водянистым, прямо как я люблю!"
            sanya "Блаженство, не ожидал что еда здесь будет настолько вкусная."
            
            nadya "И не говори."
            "Мы оба развалились на стульях и потягивали наши напитки, наслаждаясь обществом друг друга."
            sanya "Как говорит один мой друг: после сытного обеда, по законам Архимеда..."
            
            show nadya laughs
            with dissolve
            
            nadya "Чтобы жиром не заплыть – надо срочно покурить!"
            "Закончила за меня Юля и звонко рассмеялась. Я невольно залюбовался её искренней улыбкой, что так мягко сияла на нежно девичьем личике."
            sanya "Точняк! Ты не против составить мне компанию?"
            
            show nadya smiles
            with dissolve

            nadya "Не против, пойдём проветримся."
            "Она протянула мне руку и я с радостью взял её."
            
            "Чтобы лишний раз не нарушать местные уставы, мы направились прямиком в курилку."

            stop music fadeout 2.0
            
            scene black
            with dissolve
            
            play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.0
            
            play sound "audio/door_close.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.0
            
            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.1 fadeout 0.1
            pause 1.5
           
            scene sanatorium alcove
            with dissolve
            
            play music "audio/forest-sound.mp3" fadein 1.0 fadeout 2.0 volume 0.3 

            "Ей служила отдаленная беседка на живописном берегу реки. На столе стояли пепельницы, однако, в них не было ни одного окурка."
            "Видимо, это место пользуется особой популярностью."

            
            play sound "audio/cigarette.mp3" noloop fadein 0.2 fadeout 0.2
            pause 3.0
            
            "Достав сигаретку, я закурил."
            "Надя, помяв в руках тонкий ванильный чапман, попросила ей подкурить."
            nadya "Забыла зажигалку дома."
            "Я понятливо хмыкнул."

            show nadya happy
            with dissolve

            nadya "Как тебе тут?"
            sanya "Ну, пока сложно сказать... В целом, нравиться. Чистый воздух, вкусная еда."
            sanya "Скоро всякие процедуры начнутся. Поживём – увидим, как говорится."
            nadya "Тут очень спокойно и тихо. После шумного и грязного города – истинное наслаждение."
            sanya "И не говори..." 
            "Так, в тишине, в которой так нуждались, мы и пробыли пару минут, пока я докуривал."
            
            show nadya flirting
            with dissolve

            nadya "Ладно, мне уже пора. Скоро процедуры. Встретимся после ужина?"
            sanya "Конечно, я только за."
            nadya "Тогда, до вечера?"

            show nadya handson
            with dissolve

            sanya "До вечера..."
            "На прощание мы крепко обнялись, замерев так на несколько минут."
            "Никто не хотел отстраняться первым, но нам пришлось. Режим есть режим, так что попрощавшись, мы разбрелись в разные стороны."
    scene black
    with Fade(0.2, 0.3, 0.2, color="#000")
    
    stop music fadeout 2.0 
    
    if day4_take_pill:

        play music "audio/love_music.mp3" fadein 1.0 fadeout 2.0 volume 0.4

        "По пути на процедуры, вспомнил про таблетку. Забежав в столовую, кинул её в рот и запил водой из под крана."
        
        "Ну вот! Другое дело, теперь можно и в грязевую ванную залезть, и зонд в жопу засунуть."
        "Шутка! "
        extend "Надеюсь..."
        
        scene black 
        with Fade(0.2, 0.3, 0.2, color="#000")
   
        if day4_yuli_meal:

            $ mood_counter -= 1
            $ rel_yuli -= 1

            "Процедуры оказались... "
            extend "довольно приятными."
            "Горячая сауна, грязевая ванна, массажик, пускай делала его и не сексапильная девочка, а огромная женщина, руки которой были толщиной с мою голову."
            "А также прочие приколдесы, после которых ты чувствуешь себя человеком."
            
            scene sanatorium evening park
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Расслабленный, отдохнувший и довольный я шёл по парку в сторону курилки, намереваясь шлифануть всё ароматной сигареткой чапмана, и провести время в компании прекрасной девушки."
            "Эх, жить хорошо и жизнь хороша!"

            scene sanatorium alcove
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Зайдя в курилку, я присел на лавочку и, любуясь открывающимися видами, открыл стремительно пустующую пачку."
            sanya "Жить – пиздато!"
            "Однако шёл час, второй. Пачка пустела, а Юля всё не приходила."
            
            "Не вытерпев, я пошёл искать её."
            
            scene sanatorium evening park
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Прошелся по парку, заглядывая во всякие укромные места. "
            extend "пошёл к корпусу, надеясь встретить её по пути. "
            extend "Но ни в парке, ни в корпусе не было и следа моего романтического интереса."
            "Отчаявшись, я даже спросил парочку встречных, не видели ли они девушку, похожую на неё. " 
            extend "Большинство просто пожимало плечами."

            scene sanatorium night
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Расстроившись, я вышел из корпуса на свежий воздух. " 
            extend "Достал из пачки последнюю сигарету, и поднес ко рту."

            noname "Эй! Здесь нельзя курить!"
            "Обернувшись, я увидел какую-то тетку в белом халате. Раздраженно выдохнув, убрал сигарету обратно."
            
            menu :
                "Прогуляюсь по парку..." :
                    
                    $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    $ day4_walk_in_park = True
                "Пойду посплю..." :

                    $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    $ day4_walk_in_park = False
            
            if day4_walk_in_park:

                scene black
                with Fade(0.2, 0.3, 0.2, color="#000")

                "Хотелось побыть одному, в комнате сто процентов был Павел Геннадьевич, так что выбор пал на вечернюю прогулку по парку. "
                extend "Там обычно никого не бывает, да и созерцание красивых видов успокаивает."
                "Так что, кинув прощальный взгляд на злую тетку, не разрешающую курить где попало, я медленно побрёл в своё сакральное место."
                
                scene sanatorium evening park
                with Fade(0.2, 0.3, 0.2, color="#000")

                "Топая по красивому парку, я размышлял о тленности бытия и бессмысленности существования. "
                "Честно говоря, мне уже изрядно надоело курить, да и виды тут такие красивые, лучше погуляю здесь подольше."
                "Исчезновение Юли больно ударило по настроению и самооценке, что сказывалось и на \"светлости моего лика\"."
                "Думаю, такой хмурой рожи у меня давненько не было. "
                extend "Наверное, если я посмотрюсь в зеркало – оно треснет нахуй."
                
                stop music fadeout 2.0
                noname "Извини, у тебя что-то случилось?"
                "Тоненький голосок, раздавшийся сзади, застал меня врасплох. Неловко дернувшись, я обернулся."
                scene black with Fade(2.0, 1.0, 0.0)

                play music "music/tchaikovsky-Hymn_of_the_Cherubim.mp3" fadein 4.0 fadeout 2.5 volume 0.2  
                

                show screen emily_welcome with Fade(1.0, 1.0, 3.0)

                "Я столкнулся с превосходством творения природы – милая девушка, дивнейшая особа с очаровательными синими, как два океана, глазами," 
                "Что, казалось, они вечно манят меня своим загадочным сиянием." 
                "Её длинные волосы, словно мягкий розовый вуаль, обрамляли её изящное лицо," 
                extend " и мастерски подобранный оттенок придал им такую натуральность, будто они сами сотканы из лучей рассвета."
                sanya "Что-что, извини?"

                noname "У тебя что-то случилось? Выглядишь грустным."
                "Она спросила это настолько искренне, что я растерялся. Никогда не думал, что люди могут обращаться так к незнакомцу."
                play music "music/life_blossom.mp3" fadein 4.0 fadeout 2.5 volume 0.5  
                menu :
                    "Красивая... Но настроения нет. Лучше пойду мимо.":
                        
                        $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                            
                        show screen notification_popup_big
                        with dissolve

                        pause 2.0

                        hide screen notification_popup_big
                        with dissolve

                        $ day4_smoke_with_pavel = True
                        $ rel_emily -= 1
                        $ mood_counter += 1

                        "Мне льстило, что о моем психическом здоровье кто-то поинтересовался, но слишком уж много девушек за последнее время сделали мне от ворот поворот, не хочется обжигаться снова. "
                        "Ладно, всё таки я не против сейчас перекурить."
                        "Оставив розоволосую позади, я поспешил к беседке."

                        if day4_drink:

                            $ rel_pavel += 1
                            $ mood_counter += 1
                            with None
                            hide screen emily_welcome
                            scene sanatorium alcove
                            with Fade(0.2, 0.3, 0.2, color="#000")
                            play sound "audio/cigarette.mp3" fadein 2.0 fadeout 2.0 

                            "Кажется, эта беседка становится мне роднее дома. Сев на скамейку, я закурил."
                            "Первая глубокая тяжка немного прочистила сознание, освободив места для разных мыслей. Далеко не самых приятных."

                            play music "audio/Love.mp3" fadein 2.0 fadeout 2.0 volume 0.1
                            
                            show pavel smile at center:
                                xpos 1.0
                                linear 0.7 xalign 0.5
                            with dissolve

                            pavel "О, какие люди, я думал ты в медблоке отлеживаешься." 
                            "Я хмыкнул."
                            sanya "Баба Груша настоящая волшебница."
                            pavel "Это врач местный?"
                            sanya "Да, не слишком приветливая, зато лечит хорошо."

                            show pavel smokes at center
                            with dissolve

                            "Павел Геннадьевич сел рядом, достав свою пачку красного Мальборо."
                            pavel "Выглядишь мрачно"
                            sanya "Со всеми бывает"
                            pavel "Не поспоришь"
                            "Помолчали. Каждый думал о своем, смотря на природу."
                            pavel "Когда я был в твоем возрасте, после каждой более-менее серьезной проблемы мне казалось, что жизнь окончена."
                            pavel "Однако стоило немного подумать, приложить усилия, как решение находилось." 
                            pavel "И так всю жизнь. Кажется, что жизнь сложна." 
                            pavel "Ну, отчасти так и есть, каждый день приходится решать кучу маленьких и больших проблем, однако это входит в привычку и не доставляет особых неудобств."
                            sanya "А что, без проблем жить совсем нельзя?"
                            pavel "Нет. Мы начинаем их придумывать из воздуха, потому что нам становиться скучно."
                            pavel "У взрослых, на самом деле, не так много развлечений."
                            sanya "И смысл тогда в такой жизни?"
                            pavel "Огромный. Ты стремишься жить без проблем, постоянно их наживая. " 
                            extend "Ты решаешь их, создавая новые, решаешь уже их и так далее."
                            pavel "Это замкнутый круг, уроборос во плоти. "
                            extend "Вечный дискомфорт и вечное развитие. " 
                            extend "Разве не в этом смысл жизни?" 
                            pavel "Проходить испытания для создания лучшей версии себя?"
                            sanya "Не все нравятся трудности. Иногда людям хочется обычного комфорта."
                            pavel "Возможно. Однако обычно такие люди долго не живут. Естественный отбор в действии."
                            sanya "Я думаю, это работает немного не так..."
                            pavel "Считай как знаешь. В любом случае помни, что жизнь это сплошные испытания и их преодоления." 
                            pavel "И миг, когда ты проходишь определённый порог – твоя лучшая награда."
                            sanya "Сомнительное удовольствие"
                            pavel "Вот и узнаешь."
                            "Павел Геннадьевич затушил сигарету и поднялся."
                            pavel "Не вешай нос, студент. В мире миллионы свободных девушек, открытых к предложениям." 
                            pavel "В мире миллион возможностей. " 
                            extend "Конечно, иногда непросто осознать это или даже отпустить человека, но всегда держи это в голове. " 
                            extend "Бывай, я пойду прогуляюсь."
                            "Мужчина сунул руки в карманы и вышел из беседки."
                            "Посидев ещё немного, я выбросил окурок и пошёл в сторону корпуса."
                            "Жизнь – миллион возможностей. Надо просто осознать это."
                            "Эти мысли вертелись у меня все время, пока я шёл в корпус. "
                            extend "С этой мыслью я ложился в кровать. Эта мысль была последней перед сном."
                            "Она стала моей мантрой. Она стала той ниточкой, что держала мое настроение в \"зеленой зоне\"."
                            "Нужно просто осознать..."

                            stop music fadeout 2.0

                            jump _day5

                        else:
                            
                            $ rel_pavel += 1
                            $ mood_counter += 1
                            with None
                            hide screen emily_welcome
                            scene sanatorium alcove
                            with Fade(0.2, 0.3, 0.2, color="#000")
                            
                            "Кажется, эта беседка становится мне роднее дома. Сев на скамейку, я закурил. Первая глубокая тяжка немного прочистила сознание, освободив места для разных мыслей. Далеко не самых приятных."

                            play sound "audio/cigarette.mp3" fadein 2.0 fadeout 2.0 

                            show pavel smile at center:
                                xpos 1.0
                                linear 0.7 xalign 0.5
                            with dissolve

                            play music "audio/Love.mp3" fadein 2.0 fadeout 2.0 volume 0.3

                            pavel "О, какие люди."
                            "Я хмыкнул."
                            sanya "Баба Груша настоящая волшебница."
                            pavel "Это врач местный?"
                            sanya "Да, не слишком приветливая, зато лечит хорошо."

                            show pavel smokes at center
                            with dissolve

                            "Павел Геннадьевич сел рядом, достав свою пачку красного Мальборо."
                            pavel "Выглядишь мрачно."
                            sanya "Со всеми бывает."
                            pavel "Не поспоришь."
                            "Помолчали. Каждый думал о своем, смотря на природу."
                            pavel "Когда я был в твоем возрасте, после каждой более-менее серьезной проблемы мне казалось, что жизнь окончена. Однако стоило немного подумать, приложить усилия, как решение находилось."
                            pavel "И так всю жизнь. Кажется, что жизнь сложна. "
                            extend "Ну, отчасти так и есть, каждый день приходится решать кучу маленьких и больших проблем, однако это входит в привычку и не доставляет особых неудобств."
                            sanya "А что, без проблем жить совсем нельзя?"
                            pavel "Нет. Мы начинаем их придумывать из воздуха, потому что нам становиться скучно. "
                            extend "У взрослых, на самом деле, не так много развлечений."
                            sanya "И смысл тогда в такой жизни?"
                            pavel "Огромный. Ты стремишься жить без проблем, постоянно их наживая. " 
                            extend "Ты решаешь их, создавая новые, решаешь уже их и так далее. Это замкнутый круг, уроборос во плоти. Вечный дискомфорт и вечное развитие."
                            pavel "Разве не в этом смысл жизни? Проходить испытания для создания лучшей версии себя?"
                            sanya "Не все нравятся трудности. Иногда людям хочется обычного комфорта."
                            pavel "Возможно. Однако обычно такие люди долго не живут. Естественный отбор в действии."
                            sanya "Я думаю, это работает немного не так..."
                            pavel "Считай как знаешь. В любом случае помни, что жизнь это сплошные испытания и их преодоления. "
                            extend "И миг, когда ты проходишь определённый порог – твоя лучшая награда."
                            sanya "Сомнительное удовольствие."
                            pavel "Вот и узнаешь."
                            "Павел Геннадьевич затушил сигарету и поднялся."
                            pavel "Не вешай нос, студент. В мире миллионы свободных девушек, открытых к предложениям. "
                            extend "В мире миллион возможностей."
                            pavel "Конечно, иногда непросто осознать это или даже отпустить человека, но всегда держи это в голове. "
                            extend "Бывай, я пойду прогуляюсь."
                            "Мужчина сунул руки в карманы и вышел из беседки. Посидев ещё немного, я выбросил окурок и пошёл в сторону корпуса."
                            "Жизнь – миллион возможностей. Надо просто осознать это."
                            "Эти мысли вертелись у меня все время, пока я шёл в корпус. С этой мыслью я ложился в кровать. Эта мысль была последней перед сном."
                            "Она стала моей мантрой. Она стала той ниточкой, что держала мое настроение в \"зеленой зоне\"."
                            "Нужно просто осознать..."

                            stop music fadeout 2.0

                            scene black
                            with Fade(0.4, 0.5, 0.4, color="#000")
                            
                            jump _day5

                        if day4_tried_move:   

                            $ mood_counter -= 1


                            scene sanatorium balcony night
                            with Fade(0.2, 0.3, 0.2, color="#000")
                            
                            play music "audio/love_music.mp3" fadein 1.5 fadeout 2.5 volume 0.15
                            
                            "Смеркалось. Был поздний вечер и солнце уже почти закатилось за горизонт. Сквозь темнеющее небо пробивались первые, самые яркие звезды. А может быть лишь их предсмертный свет, созданный взрывом."
                            "Звезды действительно достойны восхищения. Даже после смерти, многие годы их свет виден нам. Возможно, некоторые из них умерли тысячелетия назад, а мы всё ещё их видим, думаем о них."
                            "В сравнении с ними смерть человека – пустота. Ничего.  Меньше чем миг, меньше чем ноль."
                            "Даже вся эта бравада, про память и пока нас помнят – мы живы полнейший бред."
                            "О звездах не помнят. Звезды видят и они кажутся живыми. Человек жив, пока его видит и его видят. А воспоминания о нем... Они такие же эфемерные."
                            "Субъективные. Это ведь даже не слепок, не фото. Это частичка, которую к тому же можно трактовать совершенно по-разному."
                            "Можно ли это назвать жизнью после смерти? Нет. Очевидно, что нет."
                            "От сигареты осталась половина."
                            "Звезд на небе стало больше."
                            "Я подошёл к окну."
                            "Темно."
                            "Глядя в небесную бесконечность, я думал над тем, что мне делать дальше. Какая вообще у меня жизненная цель?"
                            "Отучиться, получить работу? А дальше? В чем смысл этого? Зачем мне это нужно?"
                            "Каждый день по восемь часов пахать, чтобы в конце месяца получить зарплату. Потом слить её быстрые удовольствия и все по новой."
                            "У меня нет хобби, нет собственной семьи, да и появится она вообще у меня?"
                            "Та девушка, с которой я действительно захочу прожить жизнь. А не вариант попроще, как у сотен других."
                            "Какое же дерьмо... Двадцать лет жизни... Кажется, так мало, только начал жить, но по факту..."
                            "Кажется, я уже заруинил свои характеристики персонажа и мне придётся жить на костылях всю мою жизнь."
                            "Сигарета дотлела. Дотлели и мои мысли. Полностью опустошенный и разбитый я выкинул бычок."
                            "Навалилась ужасная усталость, но пересиливая себя я побрёл в корпус."
                            "Жить – пиздато. Пизже некуда."
                            
                            stop music fadeout 3.0

                            jump _day5

                    "Мне одиноко. Быть может, она составит мне компанию?" :
                        
                        $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                        show screen notification_popup_big
                        with dissolve

                        pause 2.0

                        hide screen notification_popup_big
                        with dissolve

                        $ day4_go_with_emily = True
                        $ rel_emily += 3
                        $ mood_counter += 2

                        sanya "Да так..."
                        "Я смутился и отвел взгляд от огромных голубых глазищ, которые, казалось, отражали само небо."
                        with None
                        hide screen emily_welcome
                        scene sanatorium evening park
                        show emily green neutral
                        with Fade(2.0, 0.5, 2.0)

                        noname "Если ты хочешь, я могу тебя выслушать!"
                        sanya "Э-э-э..."
                        noname "Но я, конечно, не настаиваю!"
                        sanya "Спасибо..."
                        
                        
                        noname "Меня Эмилия зовут!"
                        sanya "Саша..."
                        emily "Приятно познакомиться! Так что у тебя случилось?"

                        hide emily
                        with dissolve

                        scene black
                        with dissolve

                        "Я, конечно, не выложил Эмилии всё как есть. " 
                        extend "Обтекаемыми фразами, не вдаваясь в подробности рассказал о насущных проблемах."
                        "И, удивительно, но мне стало немного легче. Впервые за долгое время я почувствовал, что кому-то не плевать на меня."
                        "Тем страннее, что этот кто-то первая встречная девушка."
                        "Эмилия тоже немного рассказала о себе. " 
                        extend "Рассказ, к слову, вышел как бы не грустнее моего."
                        "Строгие родители, отсутствие свободного выбора, распланированная жизнь и дни по жёсткому расписанию."
                        "Поездка в санаторий стала небольшой отдушиной для девушки, где можно немного отдохнуть от постоянной учёбы и тирании родителей."
                        "Будучи стеснительной, но до ужаса сердобольной, она не смогла пройти мимо хмурого парня, то-есть меня."
                        "Однако, сама растерявшись от своей смелости, решила действовать весьма напористо. "
                        extend "Что, в общем-то, не было плохо."
                        "Она оказалось приятной и весёлой девушкой, так что настроение начало подниматься из глубин моего внутреннего мира."
                        
                        scene sanatorium alcove
                        with Fade(0.3, 0.4, 0.3, color="#000")

                        show emily green cute
                        with dissolve

                        "Придя в курилку и зависнув там, мы обсуждали совершенно разные темы, порой, даже с неожиданным жаром для тех, кто был незнаком до этого."
                        
                        sanya "Ты правда никогда раньше не пила алкоголь?"
                        "Моему удивлению не было предела."
                        sanya "Тебе же уже двадцать!"
                        
                        show emily green sad
                        with dissolve 
                        
                        emily "Мне мама запрещает..."
                        "Смущается она, конечно, убийственно мило."
                        sanya "Но ведь тебе двадцать! "
                        extend "Ты же можешь просто уйти из дома и делать всё, что захочешь."
                        "Эмилия на это лишь грустно улыбнулась, медленно покачав головой."
                        "Поняв, что это не лучшая тема для разговора, я поспешил её сменить."
                        sanya "А шаурму ты ела?"
                        "Еба-а-а-а-а, а ещё тупее вопрос не мог задать?"
                        "Девушка смутилась, став расправлять складки платья на коленях."

                        show emily green happy
                        with dissolve

                        emily "Нет, но мне подружка сказала, что она очень вкусная."
                        sanya "Ты серьезно не ела шаурму?"
                        "Моему удивлению не было предела."
                        "Эмилия покачала головой."
                        emily "У меня диета. Я кушаю только дома..."
                        sanya "Капец, подруга, твоя жизнь проходит зря! "
                        extend "Как только выйдем отсюда, я тебе покажу насколько прекрасна юность и шаурма!"
                        play voice "audio/girl_laugh2.mp3"

                        show emily green flirting
                        with Dissolve(2.0)

                        emily "Ловлю на слове!"
                        "Эмилия звонко рассмеялась. Потом чуть грустно произнесла:"

                        show emily green kind
                        with dissolve

                        emily "Надеюсь, мы сможем видеться, когда я вернусь на учёбу..."
                        sanya "Пф! Конечно! Как говориться, кто школу... " 
                        extend "то-есть универ не гулял, тот жизни не видал! " 
                        extend "В конце концов, впереди новогодние каникулы, да и выходные есть."
                        emily "Ну да."
                        "Эмилия вновь улыбнулась, но глаза её остались грустными."
                        "Не желая больше расстраивать новую знакомую, я перевел разговор на более приятные темы. "
                        extend "Но зарубку себе в памяти сделал – во что бы то ни стало, найти Эмилию после санатория и угостить её шаурмой!"

                        hide emily

                        scene black
                        with dissolve

                        "Сгущались сумерки, солнце заходило за горизонт, но мы продолжали болтать."
                        "Лишь когда Эмили начала зевать и клевать носом, мы поняли, что пора закругляться."
                        
                        
                        scene sanatorium night
                        with Fade(0.3, 0.4, 0.3, color="#000")

                        show emily green neutral
                        with dissolve

                        "Дойдя до корпуса, мы тепло попрощались, направившись в разные стороны. "

                        pause 2.0

                        hide emily green neutral
                        with dissolve

                        "Настроение возвратилось в норму, курить совсем не хотелось."
                        "Вдохнув пьянящий ночной воздух, я улыбнулся сам себе и новой встрече."
                        "Жизнь – продолжается!"

                        stop music fadeout 2.0

                        jump _day5

            else :
                $ mood_counter -= 2 
                "Идти никуда не хотелось. Настроение упало в ноль, так что я поплелся в свою комнату."
                
                play sound "audio/footsteps.mp3" noloop fadein 0.3 fadeout 0.3
                
                scene sanatorium walkway
                with Fade(0.4, 0.3, 0.7, color="#000")

                pause 2
                
                play sound "audio/door_open.mp3" noloop fadein 0.3 fadeout 0.3

                pause 1.0

                play sound "audio/door_close.mp3" noloop fadein 0.3 fadeout 0.3

                scene sanatorium dormitory room
                with Fade(0.4, 0.3, 0.7, color="#000")

                "Павла Геннадьевича не было, что немного меня порадовало. "
                extend "Видеть никого не хотелось. " 
                extend "Пройдя на балкон, я упал в кресло и достал последнюю сигарету чапы."

                play sound "audio/door_open.mp3" noloop fadein 0.3 fadeout 0.3

                pause 1.0

                play sound "audio/door_close.mp3" noloop fadein 0.3 fadeout 0.3

                scene sanatorium balcony night
                with Fade(0.3, 0.4, 0.3, color="#000")

                play music "audio/love_music.mp3" fadein 1.5 fadeout 2.5 volume 0.25

                play sound "audio/cigarette.mp3" noloop fadein 0.2 fadeout 0.2

                pause 2.0

                "Смеркалось. Был поздний вечер и солнце уже почти закатилось за горизонт. "
                extend "Сквозь темнеющее небо пробивались первые, самые яркие звезды. "
                extend "А может быть лишь их предсмертный свет, созданный взрывом."

                "Звезды действительно достойны восхищения. Даже после смерти, многие годы их свет виден нам. "
                extend "Возможно, некоторые из них умерли тысячелетия назад, а мы всё ещё их видим, думаем о них."

                "В сравнении с ними смерть человека – пустота. Ничего. Меньше чем миг, меньше чем ноль."
                "Даже вся эта бравада, про память и пока нас помнят – мы живы полнейший бред."
                "О звездах не помнят. Звезды видят и они кажутся живыми. Человек жив, пока он видит и его видят."
                "А воспоминания о нем... "
                extend "Они такие же эфемерные. Субъективные. Это ведь даже не слепок, не фото."
                "Это частичка, которую к тому же можно трактовать совершенно по-разному."
                "Можно ли это назвать жизнью после смерти? Нет. Очевидно, что нет."

                play sound "audio/cigarette_one_shot.mp3" noloop fadein 0.2 fadeout 0.2

                "От сигареты осталась половина."
                "Звезд на небе стало больше."
                "Я подошёл к краю балкона."
                "Темно."
                "Глядя в небесную бесконечность, я думал над тем, что мне делать дальше. Какая вообще у меня жизненная цель?"
                "Отучиться, получить работу? А дальше? В чем смысл этого? Зачем мне это нужно?"
                "Каждый день по восемь часов пахать, чтобы в конце месяца получить зарплату. Потом слить её быстрые удовольствия и все по новой."
                "У меня нет хобби, нет собственной семьи, да и появится она вообще у меня?"
                "Та девушка, с которой я действительно захочу прожить жизнь. А не вариант попроще, как у сотен других."

                play sound "audio/cigarette_one_shot.mp3" noloop fadein 0.2 fadeout 0.2

                "Какое же дерьмо... Двадцать лет жизни... Кажется, так мало, только начал жить, но по факту... Кажется, я уже заруинил свои характеристики персонажа и мне придётся жить на костылях всю мою жизнь. "
                "Или не придется?"
                "Сигарета почти догорела, бычок жег пальцы, но я не обратил на это внимание."
                "Облокотился на бортик балкона."
                "Я ничего не хочу. Ни искать смысл жизни, ни что-то ещё."
                "Я просто хочу, чтобы все это закончилось. Может даже сейчас."
                
                stop music fadeout 3.0

                "Просто перенести усилие чуть вперед и мое бессмысленное существование наконец закончиться."

                play music "audio/heart.mp3" fadein 1.0 fadeout 2.0 volume 0.2

                show screen toska
                
                menu :
                    "Шаг вперед." :
                        
                        $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                        show screen notification_popup_big
                        with dissolve

                        pause 2.0

                        hide screen notification_popup_big
                        with dissolve

                        $ day4_suicide = True
                    "Пойти спать" :
                        
                        $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                        show screen notification_popup_big
                        with dissolve

                        pause 2.0

                        hide screen notification_popup_big
                        with dissolve

                        $ day4_suicide = False

                if day4_suicide :
                    
                    "Чуть наклонившись вперед, я всмотрелся в темноту. Она зачаровывала, тянула к себе. Обещала покой, тишину, уют и отсутствие проблем."
                    "Я, повинуясь наитию, сделал движение вперед."
                    noname "КТО В НЕПОЛОЖЕННОМ МЕСТЕ КУРИТ?!"
                    
                    hide screen toska
                    with dissolve

                    stop music fadeout 0.5
                    
                    play music "audio/fall.mp3" fadein 0.3 fadeout 0.5 volume 0.3

                    pause 1.0

                    stop music
                    
                    "Я дернулся назад от неожиданности. Бычок улетел в темноту."
                    "Тут же вспотели ладони, от осознания того, что я сейчас хотел сделать."
                    "Вытерев их о штаны, я поспешил в кровать."
                    
                    play sound "audio/door_open.mp3" noloop fadein 0.3 fadeout 0.3

                    pause 1.0

                    play sound "audio/door_close.mp3" noloop fadein 0.3 fadeout 0.3
    
                    scene sanatorium dormitory room
                    with Fade(0.2, 0.3, 0.2, color="#000")
                    
                    sanya "Какой же я долбоеб."
                    "Как ни странно, но это придало мне сил. С мрачными мыслями и плохим настроением, я все же смог уснуть."

                    stop music fadeout 3.0

                    jump _day5

                else :
                    "Темнота внизу зачаровывала. И в этой темноте появилось лицо родителей и Пашки."
                    sanya "Блять!.."
                    
                    play sound "audio/door_open.mp3" noloop fadein 0.3 fadeout 0.3

                    pause 1.0

                    play sound "audio/door_close.mp3" noloop fadein 0.3 fadeout 0.3

                    hide screen toska
                    with dissolve
                    
                    stop music fadeout 0.5

                    scene sanatorium dormitory room
                    with Fade(0.2, 0.3, 0.2, color="#000")

                    "Я резко отпрянул. Кинул бычок в пепельницу и зашел в комнату. На кровати похрапывал Павел Геннадьич, и когда только успел войти?"
                    "Раздевшись, я лег в кровать. В груди что-то болело, но я не обращал на это внимания."
                    "Наверное, все же зря я так. Кто знает, что преподнесет мне следующий день?"
                    "Отрешившись от всех мыслей, я постарался заснуть."

                    jump _day5
        else:

            $ rel_nadya += 2
            $ mood_counter += 1

            "Процедуры оказались..."
            extend "довольно приятными."

            play music "audio/love_music.mp3" fadein 2.0 fadeout 2.0 volume 0.3
            
            scene sanatorium evening park
            with Fade(0.4, 0.5, 0.4, color="#000")

            "Горячая сауна, грязевая ванна, массажик, пускай делала его и не сексапильная девочка, а огромная женщина, руки которой были толщиной с мою голову."
            "А также прочие приколдесы, после которых ты чувствуешь себя человеком."
            
            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.2 fadeout 0.2

            "Расслабленный, отдохнувший и довольный я шёл по парку в сторону курилки, намереваясь шлифануть всё ароматной сигареткой чапмана, и провести время в компании прекрасной девушки."
                        
            "Эх, жить хорошо и жизнь хороша!"

            scene sanatorium alcove
            with Fade(0.4, 0.5, 0.4, color="#000")

            "Надю я заметил издалека."
            "Махнув ей приветливо рукой, я достал новую сигарету из пустеющей пачки."

            play sound "audio/cigarette_one_shot.mp3" noloop fadein 0.2 fadeout 0.2

            show nadya happy
            with dissolve

            nadya "Идут года, сменяются сезоны, а Саня также смОлит и смолИт."
            sanya "Че это это ты поэтизируешь тут надо мной..."
            nadya "Настроение хорошее просто."
            "Мы обнялись, когда она зашла в беседку, и плюхнулись на лавочку."
            "Надя тут же достала свою пачку ванильного Чапмана."
            sanya "Кто бы говорил."
            "Я кивнул на сигареты в её руках, на что она лишь неловко пожала плечами."

            show nadya handson
            with dissolve

            nadya "Ну, рассказывай, как твой день прошёл."
            sanya "Да че рассказывать, обычный день..."
            "Удивительно, но вот этого неловкого чувства, будто разговариваю с красивой девушкой, не было."
            "Было так же комфортно, как, например, на посиделках с пацанами или с тем же Пашкой."
            "Когда мы выходили на улицу, чтобы перекурить и перетереть. Свободное общение, простые темы." 
            "Всё что нужно, чтобы скинуть лишнее эмоциональное напряжение и расслабиться."
            sanya "Ты думала, чем будешь заниматься после университета?"
            nadya "Не-а. Я, если честно, и поступила-то сюда, потому что тут проходной балл невысокий был, а я читать люблю." 
            nadya "Но, как это обычно бывает, ожидания не совпали с реальностью. Эта лингвистика, как оказывается, мало похожа на литературу."
            "Она рассмеялась."
            nadya "Думаю, поработаю в кофейне, родители, если что, помогут. А там, может быть, пройду курсы сценаристики или режиссера какого-нибудь."
            extend " Посмотрим, в общем, впереди ещё куча времени, чтобы понять, чем заняться по жизни."
            sanya "Ты удивительно легко относишься к этому."

            show nadya neutral
            with dissolve

            nadya "В смысле?"
            sanya "Все девушки, с которыми я общался, конкретно так заморачиваются насчёт своего будущего."
            sanya "Типа: \"вот я отучусь, потом туда, через год сюда, замуж дети или там карьера, путешествия, слава и прочее\"."
            "Она пожала плечами."
            
            show nadya smiles
            with dissolve

            nadya "Я просто пока не знаю, чего хочу от жизни." 
            nadya "Я не очень люблю путешествовать. Это, конечно, интересно, но лично для меня тяжело." 
            nadya "Работать и делать карьеру хочется в том деле, которое интересно, иначе какой смысл?" 
            nadya "Работать на нелюбимой работе – это какой-то особенный вид мазохизма, помоему." 
            nadya "Мы ещё молоды, нам свойственно искать свой путь, нынешние реалии это позволяют."
            "Я молча кивнул. Действительно, в наших реалиях мы ещё можем подумать о том, чем заняться в жизни. У наших родителей, такой возможности не было."
            nadya "А ты чем планируешь заниматься?"
            sanya "Может пойду работать по профессии, может в армию, может ещё куда-нибудь. Пока не знаю."

            show nadya giggles
            with dissolve

            nadya "В общем, как и у всех сверстников наших."
            nadya "Не знаю, плохо это или хорошо, что мы в двадцать всё ещё не можем определиться с жизненным путём." 
            nadya "Меня мама родила в девятнадцать, папа уже тогда работал." 
            nadya "И вот, я на год старше своей тогдашней мамы, но ни отношений, ни планов на жизнь у меня нет."
            "Я вспомнил парня, который нёс сумки Нади, и осторожно спросил:"
            sanya "Кстати, на экскурсии я видел, что твою сумку нес какой-то парень..."
            nadya "Это парень моей подруги, они сюда вдвоем приехали. Он наши сумки нес."
            sanya "А."

            show nadya flirting
            with dissolve
            
            nadya "А что это ты спросил? Ревнуешь?"
            sanya "Ну разве что чуть-чуть."
            "Смущенно пробормотал я, желая увидеть реакцию девушки."
            "Надя же сначала чуть покраснела, а потом, видя мою красную мину, звонко рассмеялась." 
            "Закончив, она утерла выступившие в уголках глаз слезы и наклонилась чуть ближе к моему лицу."
            
            show nadya flirting
            with dissolve

            nadya "Пока ты ближе всех подобрался к роли моего парня."
            "Она произнесла это таким чарующим голосом, что у меня по спине пробежали мурашки, а в штанах началось бодрое шевеление."
            "Однако, не растерявшись, я наклонился в ответ."
            sanya "Это радует."
            "Мы смотрели друг на друга пару секунд. Пара секунд в сантиметре друг от друга. Очень волнительные пару секунд."
            "Одновременно отпрянув друг от друга, мы смущенно посмотрели в стороны."

            show nadya happy
            with dissolve

            nadya "Холодает..."
            sanya "Есть немного... Может, в корпус?"
            nadya "пойдём."
            "Пока мы шли до корпуса, то не проронили ни единого слова. Атмосфера неловкости, царящая между нами, как-то не настраивала на беседу."
            "Однако эта неловкость была какой-то романтичной..."

            scene sanatorium night 
            with fade

            show nadya smiles
            with dissolve
            
            nadya "Спасибо, что погулял со мной."
            sanya "Тебе спасибо, было весело."
            "Мы постояли, смотря в стороны. Вдруг Надя взяла меня за футболку и притянула к себе, чмокнув в щёку. И тут же, не оборачиваясь и не смотря на меня, прошмыгнула в свою комнату."
            "От неожиданности я впал в ступор. Отмерев, я потёр щёку, которую поцеловала Надя."
            sanya "День закончился определённо удачно..."
            "По-дурацки улыбаясь, я пошёл в комнату."

            scene black 
            with fade

            stop music fadeout 3.0

            "Жить – пиздато!"
            

            jump _day5
    else:

        $ rel_yuli += 2
        $ mood_counter += 1

        "Процедуры оказались... "
        extend "довольно приятными."
        "Горячая сауна, грязевая ванна, массажик, пускай делала его и не сексапильная девочка, а огромная женщина, руки которой были толщиной с мою голову."
        "А также прочие приколдесы, после которых ты чувствуешь себя человеком."
        "Расслабленный, отдохнувший и довольный я шёл по парку в сторону курилки, намереваясь шлифануть всё ароматной сигареткой чапмана, и провести время в компании прекрасной девушки."
        "Эх, жить хорошо и жизнь хороша!"

        scene sanatorium alcove
        with Fade(0.2, 0.3, 0.2, color="#000")

        "Зайдя в курилку, я присел на лавочку и, любуясь открывающимися видами, открыл стремительно пустующую пачку."
        sanya "Жить – пиздато!"

        noname "Скучал?"

        play music "audio/love_music.mp3" fadein 4.0 fadeout 2.0 volume 0.3

        show yuli happy
        with dissolve

        "Я обернулся на голос, улицезрев одетую в легкий сарафан Юлю, которая легко мне улыбалась."
        "У меня защемило сердце от её красоты, и я, повинуясь наитию, выпалил..."
        sanya "Какая же ты красотка!"
        
        show yuli horny
        with dissolve
        
        "Юля смутилась."
        yuli "Ты тоже ничего..."
        
        "Повисло неловкое молчание, длившееся пару секунд."
        "Потом мы одновременно рассмеялись и Юля, счастливо улыбаясь, бросилась ко мне в объятия."

        show yuli happy
        with dissolve

        yuli "Я так скучала! Наконец-то мы встретились"
        "Я лишь кивнул, наслаждаясь теплом горячего девичьего тела."
        "Сразу же пошли определенные подвижки в районе второго мужского мозга, но слава богу на мне сегодня плотные джинсы и ничего, кроме физических неудобств, это не принесет."
        "П – продуманность!"
        "Мы сели на лавочку, держась за руки."
        "Курилка почти всегда пустовала и рядом никто не шастал, так что лучшего места для посиделок мы и придумать не могли."
        
        show yuli shy
        with dissolve
        
        yuli "Ну, что, как тебе сегодняшний день?"
        sanya "Да особенно рассказывать и не о чем..."
        "Я рассказал о том, как заселился, что произошло потом, выглядело это уныло, но Юля слушала с интересом, что внушало мне осторожный оптимизм."
        "Девушка больше спрашивала и слушала, что в корне отличалось от того, к чему я привык."
        "Так что вскоре я расслабился и, кажется, впервые получал удовольствие от долгой беседы с девушкой."

        show yuli horny2
        with dissolve

        yuli "Может сходим на берег?"
        "Неожиданно спросила Юля, когда мы на секунду замолчали."

        show yuli happy
        with dissolve

        yuli "Речка тут недалеко... Можем ножки помочить"
        "О мысли о голых девичьих лодыжках меня бросило в жар."
        sanya "Давай, как раз разомнемся"
        "Юля вскочила и весело крикнув: \"кто последний тот лошара\", припустила по тропинке в лес."
        "Приняв вызов, я рванул за весело хохочущей девушкой."

        play sound "audio/footsteps_asphalt.mp3" fadein 0.2 fadeout 0.2

        scene sanatorium path
        with Fade(0.4, 0.5, 0.4, color="#000")
        
        "Юля оказалась настоящим спринтером!"
        "Ловко уворачиваясь от веток и перепрыгивая ухабы, корни и рытвины, она не давала сократить расстояние между нами, переливаясь хохотом где-то впереди."
        "Я, будучи не особо спортивным, но очень упорным, пыхтел и задыхался, но бежал изо всех сил."
        "Однако, как бы я не я не старался, догнать Юлю мне никак не удавалось."

        sanya "Вот же ж..." 
        extend "Коза..."

        with hpunch
        stop music fadeout 3.0

        "Неудачно поставив ногу, я оступился, подворачивая лодыжку."
        sanya "Блядство!"
        
        play music "audio/heart.mp3" fadein 3.0 fadeout 2.0 volume 0.7
        with vpunch
        "Упав на землю, я пару раз перекатился, набивая синяки везде, где только можно."
        "Но это было ничто в сравнении с жгучей болью в растянутой бабочке."
        
        sanya "Добегался нахуй..." 
        extend "Юль!"
        
        "Судя по смеху, она не заметила, что я упал."
        sanya "Ю-юль!"
        "Она вновь не ответила. Но и смех не удалялся, словно она замерла на месте, смеясь где-то в кустах."
        sanya "Юля! Иди сюда, я, кажется, ногу подвернул!"
        "Смех прервался, и я услышал шум травы и кустов. Наконец-то, блин."
        sanya "Заебись, свидание, баба Груша жди..."
        noname "Саша?"
        "Отвлекшись от ноги, я поднял голову."
        "В кустах стояла Юля..."

        $ mood_counter -= 2
        $ rel_yuli -= 1

        show screen toska
        with dissolve

        show yuli empty
        with dissolve

        with pixellate
        yuli "Саша?"
        "По телу пробежали мурашки от того, насколько она была... не Юлей."        
        yuli "Саша?"
        "Она произнесла это не открывая рта и не моргая, смотря как будто бы сквозь меня."
        "Отсутствующий, скорее даже мертвый взгляд."
        
        with pixellate
        show yuli empty glitch
        with dissolve 
        
        yuli "Саша?"
        yuli "СашаСашаСашаСашаСашаСашаСашаСаша СашаСашаСашаСашаСашаСашаСашаСаша СашаСашаСашаСашаСашаСашаСаша"
        sanya "кх-къх"

        "Крик застрял в горле."
        "Воздух сгустился и перестал быть прозрачным, превратившись в туман. Из него потянулись черные щупальца."
        "Дыхание становилось быстрее и быстрее с каждой секундой. Сердце, казалось, сломает грудную клетку."
        "Туман подползал ближе. Лицо Юли становилось ближе."
        
        scene black
        with Fade(0.2, 0.3, 0.2, color="#000")
        
        show yuli empty glitch at center:
            zoom 1.4
            ypos 1.3
        with dissolve 

        "Паническая атака накрыла с головой. Я забыл, как дышать. Чувства отключились, я словно попал в сонный паралич."
        "Перед глазами – мертвое лицо Юли."
        "Кислородное голодание – я теряю сознание."

        hide screen toska
        with dissolve

        hide yuli
        with dissolve
        
        stop music fadeout 3.0

        jump _day5

label _day5 :

    play sound "audio/typewriter-sound.mp3" volume 0.5 loop
    centered "{size=+30}{font=fonts/sfpro_semibold.ttf}{cps=3.8}День пятый.  {nw}{/cps}{/font}{/size}"
    stop sound
    scene black
    with dissolve
    window hide
    pause(3.0)

    #пока нет продолжения в сюжете
    if day4_suicide :
        "Утро красит нежным светом... стены санатория. На новом месте спалось неплохо. Хотя ночь выдалась... Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."
        
        if day4_with_skin :

            scene sanatorium dormitory room
            with dissolve

            play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.3 volume 0.4
            
            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. Встав с кровати, я протер веки. На соседней кровати похрапывал Мыкало."

        else :

            scene sanatorium skin dormitory room
            with dissolve

            play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.3 volume 0.4
            
            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. Встав с кровати, я протер веки. На соседней кровати похрапывал Павел Геннадьевич."
        
        "Потянувшись, я вышел на балкон."

        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2

        pause 1.0

        scene sanatorium balcony
        with Fade(0.3, 0.4, 0.3)
        
        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 0.4

        "Прохладный свежий воздух взбодрил. Пускай сейчас начало сентября, но погода держалась всё ещё летняя. Хотя ночами и утром было довольно прохладно. Листья пока только начали желтеть и в основном везде было зелено. Красота! "
        "Вдохнув полной грудью пьянящий лесной воздух, я посмотрел вниз."
        sanya "В темноте земля казалась дальше..."
        "Зайдя внутрь, пошёл выполнять утренние процедуры. До завтрака ещё пара часов, так что торопиться некуда."
        
        scene black 
        with Fade(0.3, 0.4, 0.3, color="#000")

        stop music fadeout 2.0

    #пока нет продолжения в сюжете
    elif day4_smoke_with_pavel:

        "Утро красит нежным светом... стены санатория. На новом месте спалось неплохо. Хотя ночь выдалась... Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."

        if day4_tried_move:

            scene sanatorium dormitory room
            with dissolve

            play music "audio/snore_big.mp3" fadeout 2.0 volume 0.4

            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. Встав с кровати, я протер веки. На соседней кровати похрапывал Мыкало."

            stop music
            
        else :
            
            scene sanatorium skin dormitory room
            with dissolve

            play music "audio/snore_big.mp3" fadeout 2.0 volume 0.4
            
            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. Встав с кровати, я протер веки. На соседней кровати похрапывал Павел Геннадьевич."

            stop music

        "Хмыкнув, я поднялся и вышел на балкон."

        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2

        pause 1.0

        scene sanatorium balcony
        with Fade(0.3, 0.4, 0.3)
        
        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 0.4


        "Прохладный свежий воздух взбодрил. Пускай сейчас начало сентября, но погода держалась всё ещё летняя."
        "Хотя ночами и утром было довольно прохладно. Листья пока только начали желтеть и в основном везде было зелено. Красота!"
        
        scene black 
        with Fade(0.3, 0.4, 0.3, color="#000")

        stop music fadeout 2.0

    elif day4_go_with_emily :

        "Утро красит нежным светом... стены санатория. "
        extend "На новом месте спалось неплохо. "
        extend "Хотя ночь выдалась... "
        extend "Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."

        if day4_tried_move and not day4_fight:

            scene sanatorium skin dormitory room
            with Fade(0.3, 0.4, 0.3, color="#000")

            play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.3 volume 0.4

            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. "
            extend "Встав с кровати, я протер веки. "
            extend "На соседней кровати похрапывал Мыкало."
        else :

            scene sanatorium dormitory room
            with Fade(0.3, 0.4, 0.3, color="#000")

            play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.3 volume 0.4

            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. "
            extend "Встав с кровати, я протер веки. "
            extend "На соседней кровати похрапывал Павел Геннадьевич."

        "Потянувшись, я вышел на балкон."

        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2

        pause 1.0

        scene sanatorium balcony
        with Fade(0.3, 0.4, 0.3)
        
        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 0.4
        
        "Прохладный свежий воздух взбодрил. "
        extend "Пускай сейчас начало сентября, но погода держалась всё ещё летняя."
        "Хотя ночами и утром было довольно прохладно. "
        extend "Листья пока только начали желтеть и в основном везде было зелено. "
        extend "Красота!"

        scene black 
        with Fade(0.3, 0.4, 0.3, color="#000")

        stop music fadeout 2.0

        play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.1 fadeout 0.1

        pause 2.0

    elif day4_nadya_meal :

        "Утро красит нежным светом... стены санатория. "
        extend "На новом месте спалось неплохо. "
        extend "Хотя ночь выдалась... Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."

        if day4_tried_move and not day4_fight:

            scene sanatorium skin dormitory room
            with Fade(0.3, 0.4, 0.3, color="#000")

            play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.3 volume 0.4

            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. "
            extend "Встав с кровати, я протер веки. "
            extend "На соседней кровати похрапывал Мыкало."

        else :

            scene sanatorium dormitory room
            with Fade(0.3, 0.4, 0.3, color="#000")

            play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.3 volume 0.4

            "Немного гудела голова, да и глаза слипались, но спать дальше желания не было. "
            extend "Встав с кровати, я протер веки. "
            extend "На соседней кровати похрапывал Павел Геннадьевич."

        "Потянувшись, я вышел на балкон."

        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2

        pause 1.0

        scene sanatorium balcony
        with Fade(0.3, 0.4, 0.3)
        
        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 0.4
        
        "Прохладный свежий воздух взбодрил. "
        extend "Пускай сейчас начало сентября, но погода держалась всё ещё летняя."
        "Хотя ночами и утром было довольно прохладно. "
        extend "Листья пока только начали желтеть и в основном везде было зелено. "
        extend "Красота!"
        
        scene black 
        with Fade(0.3, 0.4, 0.3, color="#000")

        stop music fadeout 2.0
        
    scene sanatorium canteen
    with Fade(0.3, 0.4, 0.3, color="#000")

    play music "audio/kfc-sound.mp3" fadein 1.0 fadeout 1.0 volume 0.1 

    "В столовой было немноголюдно. "
    extend "Видимо, ещё рановато для общего завтрака, но так даже лучше. "
    extend "Посидеть в тишине всегда комфортнее, чем толкаться в очереди."
    "Подойдя к раздаче, я оценил сегодняшнее меню."
    "Молочный суп, сырники со сгущенкой и кофейный напиток. "
    extend "Как в лагере, честное слово. "
    extend "Взяв свою порцию, я огляделся, выбирая куда сесть."

    if day4_go_with_emily :

        show emily green neutral at right
        with dissolve

    if day2_nadya_have_a_dialog:

        show nadya neutral at left
        with dissolve

    "К сожалению, Юли всё ещё не было видно. "
    
    extend "Ладно... К кому бы сесть?"

    menu :
        "Сяду один." :

            $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            $ day5_loneliness_in_cafe = True
            $ mood_counter -= 2

            hide emily green neutral
            with dissolve

            hide nadya light sad
            with dissolve

        "Подсяду к Наде." if day4_nadya_meal or day2_nadya_have_a_dialog and rel_nadya >= 3:

            $ str_for_notification = "{size=-12}Надя запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 0.5

            hide screen notification_popup_big
            with dissolve

            $ day5_nadya_in_cafe = True
            $ rel_nadya += 1

            hide emily green neutral
            with dissolve

            show nadya happy at center
            with dissolve

        "Подсяду к Эмилии" if day4_go_with_emily and rel_emily >= 3:
            show emily green happy
            with dissolve
            $ str_for_notification = "{size=-12}Эмилия запомнит это{/size}"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            $ day5_emily_in_cafe = True
            $ rel_emily += 2

            hide nadya light sad
            with dissolve

            

    if day5_nadya_in_cafe :
        "Поскольку одному сидеть не очень весело, особенно когда поодаль сидит девушка, с которой интересно общаться, мною было решено подсесть к Наде."
        sanya "Привет!"
        "Издали помахал ей рукой. "
        extend "Она махнула в ответ, почти не подняв лица от тарелки."
        "Поставив ей на стол поднос с едой, я поинтересовался:"
        play sound "audio/chair_crack.mp3" noloop fadein 0.2 fadeout 0.2
        sanya "Как дела?"
        "Девушка прожевала, посмотрела на меня и выдала:"
        show nadya laughs
        with dissolve
        nadya "Когда я ем – я глух и нем! "
        extend "Так что извини, но я не люблю болтать за столом."
        "С этими словами она закинула себе в рот новую порцию молочного супа и принялась активно жевать."
        "Что ж... "
        extend "Справившись с оторопью, я пожал плечами. "
        extend "Мало ли какие у людей причуды бывают."
        "Спокойно продолжил завтрак в тишине, прерываемой лишь постукиваем ложек о тарелки."
        "Лишь, прожевав всё полностью, Надя посмотрела на меня."
        nadya "Что ты там говорил?"
        sanya "Может прогуляемся после процедур?"

        show nadya happy 
        with dissolve

        nadya "Давай, почему бы и нет, всё равно по вечерам тут делать нечего."
        sanya "Ну, старики играют в шашки и шахматы по беседкам, им есть чем заняться."
        "Надя лишь фыркнула."
        nadya "Я думала тут веселее будет, когда ты меня приглашал. "
        extend "А тут вон как..."
        sanya "Раз я тебя пригласил, мне тебя и развлекать."
        "Я поиграл бровями, заставив Надю чуть смутиться."
        nadya "Что ж... "
        extend "Надеюсь, на твою помощь. "
        extend "Вечером в нашей беседке!"
        "Она резко встала и, загремев стулом, пошла сдавать грязную посуду. "
        extend "Проводив взглядом её обтянутые джинсами бедра, я сам встал из-за стола." #пошлость 

        hide nadya happy
        with dissolve
        
        "Пора бы и на процедуры."
        
        scene firstDays black scen
        with fade

        stop music fadeout 1.0

        if rel_yuli >= 3:
            "Процедуры проходили спокойно. Массажик, солевая ванна, витаминчики и прочее. "
            #extend "Вот только мое внутреннее умиротворение было далеко от этого самого умиротворения."
            "Что-то не давало мне покоя, какое-то зудящее чувство на периферии сознания раздражало своей навязчивостью."
            "Словно я что-то сделал не так, что-то упустил или проигнорировал."
            "Терзаемый непонятным чувством, я переходил с процедуры на процедуру, как вдруг прозвучал такой знакомый голос, заставивший меня вздрогнуть."
            noname "Саша..."

            show yuli empty glitch at right
            with dissolve

            pause 1.5

            hide yuli empty glitch
            with dissolve

            "Я обернулся в поисках источника голоса, но никого не обнаружил."
            "Поежился, поймав заинтересованный взгляд какого-то взрослого мужика, что проходил мимо моей ванной."
            "Иди, иди, не глазей, не мешай мне шизеть."
            noname "Саша..."

            show yuli empty glitch at left
            with dissolve

            pause 1.5

            hide yuli empty glitch
            with dissolve

            "Да блять! "
            extend "Я вновь закрутил головой, силясь найти шутника."
            "Однако в маленькой комнате с кучей ванн был только я и тот мужик, что погрузился в ванную на противоположной стороне комнаты."
            "Вряд ли это он... "
            extend "Да ещё и женским голосом. "
            extend "Есть, конечно, такие умельцы, но не думаю, что это наш случай."
            "Да и голос подозрительно знаком."
            "Тут у меня в голове что-то как будто бы щелкнуло. "
            extend "Это же Юлин голос. "
            extend "По спине пробежали мурашки, а в ванной как будто бы стало холодно."
            "Погрузившись в воду по шею, я вновь поежился. "
            extend "Кажется, этим неприятным чувством была вина. "
            extend "Вина за то, что я не поговорил с ней после вчерашнего. " 
            extend "Не нашел, не написал даже."
            "Ы-ы-х... "
            extend "Но ведь она сама вчера не пришла! "
            extend "Да и сегодня её видно не было. "
            extend "Так почему же я чувствуя себя так, будто предал кого-то."
            noname "Потому что так и есть..."

            show yuli empty glitch
            with dissolve

            pause 1.5

            hide yuli empty glitch
            with dissolve

            "Так! "
            extend "Вскочив из ванной и расплескивая воду я пошлепал в раздевалку."
            "ещё бы меня совесть Юлиным голосом стыдила. "
            extend "Нафиг, нафиг, пойду подышу, что ли..."
            "Придя в пустую комнату и зайдя на балкон, я задумался. Чувство, похожее чем-то на совесть. Но откуда бы она взялась, особенно у такого как я?"
            "Но какой-то червячок сомнения грыз меня, наводя на разные мысли. Может, все-таки, найти Юлю, чтобы нормально спросить в чем дело? А то как то не по-пацански получается..."

        stop music fadeout 2.0
        "Наступил вечер. "
        extend "Процедуры кончились. "
        extend "Кто-то разошёлся по комнатам, кто-то по беседкам играть в домино и шашки."
        "Я же, надев свои самые лучшие шмотки, готовился к встрече."


        if day4_tried_move and not day4_fight :
            scene sanatorium skin dormitory room
            with fade
        else :
            scene sanatorium dormitory room
            with fade

        "Прихорошившись, я подошёл к зеркалу, стоящему у входа."

        play music "audio/bad_dream.mp3" fadein 1.0 fadeout 1.0 volume 0.6
        play sound "audio/heart.mp3" fadein 0.2 fadeout 0.2
        noname "И куда это ты такой красивый вырядился?"


        show yuli empty glitch at left:
            alpha 0.0
            linear 0.15 alpha 0.5
            linear 0.15 alpha 0.0
        pause 0.3

        show yuli empty glitch at right:
            alpha 0.0
            linear 0.15 alpha 0.5
            linear 0.15 alpha 0.0

        pause 0.78

        hide yuli empty glitch

        show yuli empty glitch:
            alpha 0.0 zoom 3.0 ypos -500 xpos -500
            linear 0.5 alpha 0.99
            linear 0.2
            linear 0.3 alpha 0.0

        pause 1.5

        hide yuli empty glitch

        "Вздрогнув от неожиданности, я резко обернулся."

        stop sound fadeout 0.3 
        "На моей кровати беззаботно болтая ножками сидела улыбающаяся Юля."

        show yuli empathy
        with dissolve

        sanya "Ты как сюда попала?"
        yuli "Я первая свой вопрос задала!"
        "Она легко вспорхнула с кровати и прошлась мягким шагом по комнате."
        "Почему-то, глядя на её расслабленное лицо, я напрягся. "
        extend "Какой-то иррациональный страх пробирался под кожу."
        sanya "Гулять я пошёл..."
        yuli "О! Супер, куда пойдём?"
        "Она подошла ближе, ожидающе уставившись на меня своими огромными глазищами."
        sanya "В парк мы идём, я уже договорился со знакомой, но думаю, она не будет против, если мы..."
        yuli "C кем договорился?"
        "Юля резко переменилась в лице. "

        show yuli angry
        with dissolve

        extend "От прежней расслабленности не осталось и грамма, сейчас её моську украшало достаточно злое выражение лица."
        sanya "С Надей..."
        with sshake
        yuli "С этой сукой... "
        extend "Понятно. "
        extend "Вот значит как."
        sanya "А что такого?"
        yuli "Ты ещё спрашиваешь?"
        "Кажется этот вопрос действительно взбесил её. "
        extend "Она даже не нашла сразу, что ответить."

        menu:
            "Пойти на свидание с Надей." :

                $ str_for_notification = "{size=-12}Юля запомнит это{/size}"
                    
                show screen notification_popup_big
                with dissolve

                pause 2.0

                hide screen notification_popup_big
                with dissolve

                yuli "Ну и вали с этой сукой хоть на все четыре стороны!"

                $ day5_nadya_date = True
                $ rel_yuli -= 3

                hide yuli angry
                with dissolve

            "Остаться и успокоить Юлю." :
                
                $ str_for_notification = "{size=-12}Юля запомнит это{/size}"
                    
                show screen notification_popup_big
                with dissolve

                pause 2.0

                hide screen notification_popup_big
                with dissolve

                $ day5_nadya_date = False
                $ rel_nadya -= 3
        
        if day5_nadya_date :
            
            play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1
            
            scene firstDays black scen
            with Fade(0.3, 0.4, 0.3, color="#000")
            
            play sound "audio/door_close.mp3" noloop fadein 0.1 fadeout 0.1

            pause 1.0
            
            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.1 fadeout 0.1

            pause 2.0

            stop music fadeout 0.5

            play music "audio/nadya_theme.mp3" fadein 1.5 fadeout 1.5 volume 0.2

            
            "Мрачное настроение сразу же исчезло, как только я встретил Надю."
            
            scene nadya white meet art
            with Fade(0.3, 0.4, 0.3, color="#000")

            "Легкое серое платье, босоножки и легкая походка."
            "Эх... "
            extend "Кажется, именно этого не хватало мне в моей серой и бессмысленной жизни."
            noname "Да что ты!"
            stop music fadeout 0.3
            show screen toska
            play sound "audio/heart.mp3" fadein 1.0 fadeout 2.0 volume 0.8

            "Голову пронзила резкая вспышка боли, причем такой силы, что потемнело в глазах."
            "Покачнувшись, я все-таки смог устоять на ногах. "
            extend "Однако пульсирующие навязчивое томление в голове осталось."
            nadya "Что-то случилось?"

            stop sound fadeout 0.3

            hide screen toska
            with dissolve

            play music "audio/nadya_theme.mp3" fadein 0.6 fadeout 2.0 volume 0.25

            "Меня подхватила Надина тонкая, но удивительно сильная рука."
            sanya "Да, да, все нормально, голова просто закружилась..."
            nadya "Давай присядем?"

            play sound "audio/chair_crack.mp3" noloop fadein 0.3 fadeout 0.3
            
            scene sanatorium alcove
            with Fade(0.3, 0.4, 0.3, color="#000")

            show nadya white shy
            with dissolve

            "Мы сели на скамейку в курилке. "
            extend "Головокружение отпустило и в глазах прояснилось."
            sanya "Надо просто меньше чапы курить..."

            play voice "audio/girl_laugh3.mp3"
            show nadya white happy
            with Dissolve(2.0)

            "Надя сдержано посмеялась. "
            extend "Неловкая шутка помогла немного разрядить атмосферу, и вскоре мы уже свободно болтали о том и сем."
            
            "Несмотря на то, что сидели мы в курилке, к сигам нас не тянуло."
            
            hide nadya
            with dissolve
            scene firstDays black scen
            with dissolve

            pause 2.0

            "Мы спокойно общались на разные отвлеченные темы, вскоре и вовсе переместившись в парк. "

            scene sanatorium evening park
            with dissolve
            show nadya white happy
            with dissolve

            "Решили, так сказать, размять ноги. "
            nadya "Я думаю, эпоха барокко снова возвращается к нам. " 
            extend "Вся эта театральная напыщенность, интерес к культуре смерти, да и в целом некая мрачность проявляется и сейчас."
            nadya "Раньше барокко считали чем-то низким. Тем, что нельзя, так сказать, упоминать. "
            extend "Любовь, эмоции на показ, всё такое – сейчас же то же самое!"
            nadya "Да я даже больше скажу – это никуда не уходило..."
            nadya "Разве что, добавилась некая религия вокруг вредных привычек."
            nadya "Вот и получается, что современное общество — это отражение старого стиля."
            nadya "Вся эта любовь, выпивка, паника, лирика — всё то, что окружает нас в течение всей нашей жизни."
            "Слушая Надю, я кивал головой и поддакивал в нужных моментах."
            "На самом деле, мне было совершенно побоку на все эти эпохи Ренессанса, барокко и прочих Возрождений." 
            "Я просто получал удовольствие смотря на неё, пока она с таким огоньком в глазах говорит о чем-то. "
            nadya "А ведь что самое главное? "
            extend "Главное то, что многие говорили, что культура вырождается, население тупеет и прочее, прочее, прочее. "
            extend "А сейчас?"
            nadya "Сейчас же происходит то же самое, старперы говорят, что раньше было лучше, бла-бла-бла, но ведь темы те же, содержание то же, лишь форма меняется, трансформируется..."
            sanya "М-м-м..."

            play sound "audio/pain.mp3" noloop fadein 0.2 fadeout 0.2 volume 2.0
            stop music
            "Голову пронзила резкая вспышка боли, которая была даже сильнее, чем предыдущая. "

            show screen toska

            play music "audio/heart.mp3" fadein 1.0 fadeout 2.0 volume 0.5
            
            show nadya white open mouth
            with dissolve

            nadya "Саш?"
            "Голос Нади звучал словно через пелену. "
            extend "Голова кружилась, боль пульсировала в висках, подняв взгляд, я с трудом смог его сфокусировать."

            show yuli empty glitch:
                ypos 0.05
                alpha 0.7 
            pause 0.1
            hide yuli
            with dissolve

            "Вдруг передо мной на секунду возникло ухмыляющееся лицо Юли, а боль словно усилилась. "
            "Я не смог сдержать стон."
            nadya "Саш, что случилось?" 
            "Кажется, в её голосе проскочили нотки паники. "
            sanya "Голова... болит."
            "Слова давались с большим трудом."
            nadya "Тебе нужно в медпункт!"

            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.2 fadeout 0.2
            show nadya:
                linear 0.6 zoom 1.1
                linear 0.6 ypos 1.15
            pause 1.2
            "Я почувствовал, что она взяла меня под руку и мягко, но настойчиво потянула вверх."
            
            show nadya:
                linear 0.6 ypos 1.0
                linear 0.6 zoom 1.0

            nadya "Давай, тут как раз недалеко."

            scene black
            with dissolve 

            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.1 fadeout 0.1
            
            "Каждый шаг отдавался болью в затылке, но с помощью Нади все-таки смог кое-как пойти."
            
            scene sanatorium medical post
            with Fade(0.3, 0.4, 0.3, color="#000")

            "Агриппина сидела около своей вотчины и, попыхивая трубку, смотрела с задумчивым видом вдаль. "
            "Однако, увидев меня, идущего на прицепе у Нади, Агриппина сузила глаза и встала с кресла, потушив трубку."

            show grusha grusha neutral at left
            with dissolve
            show nadya white open mouth at right:
                zoom 1.2
                ypos 1.2
            with dissolve
            grusha "Что с ним?"
            nadya "Голова резко заболела!" 
            with hpunch
            "Тут у меня вновь случился приступ, от которого я чуть не потерял сознание."
            with vpunch
            "Все поплыло, ноги начали подкашиваться, но меня тут же кто-то подхватил и куда-то повел. "

            hide grusha grusha neutral
            with dissolve

            scene firstDays black scen 
            with dissolve

            pause 2.0

            scene firstDays medicina
            with dissolve
            
            play sound "audio/chair_crack.mp3" noloop fadein 0.3 fadeout 0.3

            "Все кружилось и вертелось, меня посадили на что-то мягкое и сунули в рот таблетку. "
            grusha "Пей!" 

            show grusha angry
            with dissolve

            "В зубы ударился стакан, и я смог проглотить до жути горькую таблетку. "
            grusha "Лежи, сейчас пройдет."
            "Однако не проходило, становилось только хуже, и калейдоскоп перед глазами приобрел такое вращательное движение, что меня начало штормить уже сидя. "
            grusha "Ясно..."
            "До слуха донеслось какое-то копошение и в рот вдруг что-то вбрызнули. "
            extend "Что-то до жути горькое. "
            "Закашлявшись, я чуть не брякнулся с кушетки, но меня держала крепкая женская рука. "
            hide screen toska
            with dissolve
            stop sound fadeout 1.0
            play music "audio/medicine_sound.mp3" noloop fadein 1.8 fadeout 0.2 volume 0.7
            "Калейдоскоп начал замедлятся, пульсирующая боль становилась слабее. "
            sanya "Спасибо..."
            "Агриппина Владимировна ничего не ответила, подняв мне веко и посветив туда фонариком."
            grusha "Будешь каждое утро приходить ко мне за лекарством, понял?" 
            "Произнесла она приказным тоном, так что выбора у меня не было."
            sanya "Я чем-то болен?"
            grusha "Возможно. "
            extend "Полегчало? "
            extend "Можешь идти."
            "Посмотрев на хмурую женщину, я кивнул. "
            extend "Благо, боль полностью прошла."

                        
            stop music
            
            hide grusha angry
            with dissolve

            scene sanatorium medical post
            with dissolve

            "На улице меня ждала обеспокоенная Надя. "
            extend "Увидев, что я выхожу на своих ногах, она сразу расцвела."

            play music "audio/nadya_theme.mp3" fadein 1.5 fadeout 2.0 volume 0.25
            
            show nadya white shy at center:
                ypos 1.2
                linear 0.5 zoom 1.3
            with dissolve

            nadya "Ну, как ты?" 
            sanya "Всё нормально, Агриппина Владимировна сказала завтра ещё к ней зайти."
            nadya "Хорошо."

            show nadya white happy
            with dissolve

            "Кажется, она облегченно выдохнула."
            nadya "А что это было? Она не сказала?"
            sanya "Нет, но со мной такое впервые. "
            extend "Наверное, акклиматизация."
            nadya "Продолжим гулять или ты комнату пойдешь?"
            sanya "Конечно погуляем! "
            extend "Разве я могу терять шанс провести время с такой интересной и красивой девушкой?"
            play voice "audio/girl_laugh4.mp3"
            "Надя звонко рассмеялась, а я галантно предложил свой локоть, на который она с готовностью оперлась."
            
            scene nadya white river art
            with Fade(0.3, 0.4, 0.3, color="#000")

            "Все-таки осень начинала входить в свои права, поэтому после заката температура опускалась достаточно низко."
            "Гулять в легкой одежде было можно, но и риск заболеть присутствовал. "

            extend "Именно из-за этого погуляли мы не очень долго, в конце-концов придя к корпусу."

            scene sanatorium night
            with Fade(0.3, 0.4, 0.3, color="#000")

            show nadya white happy
            with dissolve

            "Остановившись около его входа, мы замерли в нерешительности. "
            extend "Расставаться не хотелось, но и продолжать дальше гулять на улице тоже."

            menu :
                "Предложить пойти к Наде" :

                    $ str_for_notification = "{size=-12}Надя запомнит это{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    if day4_nadya_meal :
                        $ day5_almost_sex_with_nadya = True
                        $ rel_nadya += 3

                        sanya "Может, зайдем к тебе? "
                        extend "Ты вроде говорила у тебя никого нет..."

                        show nadya white shy
                        with dissolve

                        nadya "Только ненадолго, не хочу завтра долго спать..."
                        "Воодушевившись до опизденения, я со счастливой улыбкой пошёл за Надей."
                        
                        hide nadya
                        with dissolve

                        play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.1 fadeout 0.1

                        pause 1.6
                        
                        show sanatorium walkway
                        with dissolve

                        play sound "audio/footsteps.mp3" noloop fadein 0.1 fadeout 0.1

                        pause 1.6

                        play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1

                        "У комнаты она остановилась и, бросив через плечо \"Подожди здесь\", юркнула за дверь."

                        play sound "audio/rustle.mp3" noloop fadein 0.3 fadeout 0.7 volume 0.15

                        "Послышался шорох и шум, словно что-то передвигали."

                        pause 2.0

                        play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1
                        
                        scene sanatorium nadya room
                        with Fade(0.2, 0.3, 0.2, color="#000")

                        "Через пару минут дверь открылась, и чуть растрепанная девушка впустила меня."
                        "Тут царил легкий беспорядок, видимо не успела до конца убраться."
                        "На полу лежало пару носков, которые она тут же убрала, кровать была наспех заправлена, на столе стояла косметика."
                        
                        show nadya white happy
                        with dissolve
                        
                        nadya "Извини за беспорядок, я не ожидала, что ты придешь."
                        sanya "Да все нормально."
                        nadya "Был бы чай, угостила бы."
                        "Я разулся."
                        sanya "Я схожу в ванную?"
                        
                        show nadya white shy
                        with dissolve

                        nadya "Конечно, тогда можешь ещё подождать там, я переоденусь?"
                        sanya "Давай."

                        scene black
                        with dissolve

                        hide nadya
                        with dissolve

                        play sound "audio/tap.mp3" noloop fadein 0.5 fadeout 0.5 volume 0.2
                        
                        "Помыв руки и умывшись, я пригладил свои вихрастые волосы. "
                        extend "Ждать долго не пришлось, уже через пять минут Надя позвала меня."
                        "Весь в предвкушении, я вышел из ванной."

                        stop sound fadeout 1.0
                        
                        scene nadya pijamas evening art
                        with Fade(2.0, 1.0, 3.0)

                        "На кровати, в зеленой пижаме сидела Надя, сжимая в руках подушку."
                        nadya "Садись на вторую."
                        "Она указала на соседнюю кровать, на которую я и приземлился."
                        sanya "Тебе идет эта пижама, подходит к твоим волосам."
                        
                        "Надя немного зарделась."
                        nadya "Спасибо."
                        "Посидели, помолчали, глядя друг на друга. И тут я выдал:"
                        sanya "На самом деле, я считаю тебя самой красивой девушкой, которая только есть в моем окружении."
                        "Повисла тишина. "
                        extend "Надя покраснела до кончиков ушей, но хитро мне улыбнулась."
                        nadya "Ты тоже ничего."
                        "И только тут я осознал, что ляпнул."
                        sanya "Нет, ты не подумай, я не подкатываю..."
                        nadya "Жаль..."
                        sanya "Что?"
                        nadya "Что?"
                        sanya "Что?"
                        nadya "Что?"
                        "Тут она сделала такое невинное лицо, что я невольно рассмеялся. "
                        play voice "audio/girl_laugh3.mp3"
                        extend "Через секунду к моему смеху присоединилась и Надя."
                        nadya "Если хочешь... "
                        extend "Можешь остаться у меня, соседняя кровать все равно не занята."
                        "Я замер, не веря своим ушам. "
                        extend "Посмотрел на Надю, ожидая увидеть улыбку, но та была серьезной."
                        sanya "Почту за честь, моя леди..."
                        jump _day6
                        
                    else :
                        sanya "Может, зайдем к тебе? Ты вроде говорила у тебя никого нет..."
                        
                        show nadya white expressionless
                        with dissolve

                        nadya "Извини, мне завтра рано вставать, я хочу выспаться."
                        "Иголочка разочарования кольнула грудь, но я отнесся с пониманием. "
                        extend "В конце-концов, мы слишком мало знакомы."
                        sanya "Хорошо, тогда спокойной ночи. "
                        extend "Было весело!"

                        show nadya white happy
                        with dissolve

                        "Улыбнувшись, Надя ушла в свою комнату. Я же пошёл в свою. "
                        hide nadya 
                        with dissolve

                        play sound "audio/footsteps.mp3" noloop fadein 0.2 fadeout 0.2
                        scene sanatorium walkway
                        with dissolve
                        pause 1.0
                        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                        pause 0.5
                        
                        if day4_tried_move and not day4_fight :
                            scene sanatorium skin dormitory room
                            with fade

                            play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
                            
                            "В целом, день прошел очень неплохо. "
                            extend "Отдохнул, пообщался, эх, пивка бы и вообще шикарно было бы..."
                            "Мыкало не было, так что умывшись, я лег в кровать. "
                            extend "Спокойной мне ночи!"
                        else :
                            scene sanatorium dormitory room
                            with fade

                            play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
                            
                            "В целом, день прошел очень неплохо. "
                            extend "Отдохнул, пообщался, эх, пивка бы и вообще шикарно было бы..."
                            "Павла Геннадьевича не было, так что умывшись, я лег в кровать. "
                            extend "Спокойной мне ночи!"
                        
                        scene firstDays black scen
                        with dissolve
                        jump _day6

                "Пойти к себе в комнату" :

                    $ str_for_notification = "{size=-12}Надя запомнит это{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    $ rel_nadya -= 3
                    sanya "Спокойной ночи. "
                    extend "Завтра ещё встретимся?"

                    show nadya white happy
                    with dissolve

                    nadya "Конечно! "
                    extend "Все равно тут заняться нечем."
                    "Она удалилась в свою комнату, я же пошёл в свою. "
                    extend "В целом, день прошел очень неплохо. "
                    extend "Отдохнул, пообщался, эх, пивка бы и вообще шикарно было бы..."

                    hide nadya
                    with dissolve

                    if day4_tried_move and not day4_fight :
                        
                        play sound "audio/footsteps.mp3" noloop fadein 0.3 fadeout 0.3
                        
                        scene sanatorium walkway
                        with Fade(0.3, 0.4, 0.3, color="#000")

                        pause 1.5

                        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                        pause 1.0

                        scene sanatorium skin dormitory room
                        with Fade(0.3, 0.4, 0.3, color="#000")

                        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
                        pause 1.0                        

                        "Мыкало не было, так что, умывшись, я лег в кровать. "
                        extend "Спокойной мне ночи!"
                    else :
                        play sound "audio/footsteps.mp3" noloop fadein 0.3 fadeout 0.3
                        
                        scene sanatorium walkway
                        with Fade(0.3, 0.4, 0.3, color="#000")

                        pause 1.5

                        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                        pause 1.0

                        scene sanatorium dormitory room
                        with Fade(0.3, 0.4, 0.3, color="#000")
                        
                        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
                        pause 1.0                        

                        "Павла Геннадьевича не было, так что умывшись, я лег в кровать. "
                        extend "Спокойной мне ночи!"

                    scene firstDays black scen
                    with dissolve

                    pause 2.0

                    jump _day6

            hide nadya
            with dissolve

        else :
            
            if day4_tried_move and not day4_fight :
                scene sanatorium skin dormitory room
                with fade
            else :
                scene sanatorium dormitory room
                with fade

            sanya "Юль, пожалуйста, успокойся..."

            show yuli angry
            with dissolve

            yuli "Ты ещё спрашиваешь? "
            extend "Я к тебе подошла, я с тобой заговорила, а ты вот так со мной поступаешь?"
            sanya "И что? "
            extend "Мы разве друг другу что-то обещали?"
            yuli "В смысле? "
            extend "Разве это не очевидно?"
            sanya "Нет!"
            "Глаза Юли опасно сузились, она лёгким движением переместилась ко мне, заглядывая прямо в глаза."

            show yuli sad with Dissolve(0.2):
                xpos 0.5 ypos 1.0 zoom 1.0
                linear 0.4 ypos 1.4 zoom 1.4
                linear 0.6 ypos 1.5 zoom 2.0

            yuli "Скажи, ты меня любишь?"
            sanya "Что?"
            "Сказать по правде, я очень растерялся от этого вопроса. "
            extend "В данной ситуации он был совершенно не к месту."
            yuli "Я тебе нравлюсь? "
            extend "Да или нет?"

            menu :
                "Да." :

                    $ str_for_notification = "{size=-12}Юля запомнит это{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    $ day5_sanya_love_yuli = True

                "Прости, но нет..." :

                    $ str_for_notification = "{size=-12}Юля запомнит это{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    $ day5_sanya_love_yuli = False

            if day5_sanya_love_yuli :

                sanya "Ну... думаю, что скорее да, чем нет..."

                show yuli horny:
                    linear 0.9 zoom 1.1
                with dissolve
                pause 1.0
                
                hide yuli
                with dissolve
                
                play sound "audio/heart.mp3" fadein 0.2 fadeout 0.2

                show screen toska
                with dissolve 

                "Юля загадочно улыбнулась и сделала шаг вперед, истаяв туманом."
                yuli "Это правильный ответ..."
                "И тут я почувствовал, что будто куда-то падаю. "
                extend "Чувство невесомости во всем теле, бабочки в животе и отсутствие ощущения пространства."

                show yuli wet crying
                with dissolve

                "Зажмурившись, я увидел перед собой плачущую Юлю."
                yuli "Однако за то, что ты меня расстроил, пообщавшись с той девкой, придется тебя немного наказать."
                play audio "audio/pain.mp3" noloop fadein 0.2 fadeout 0.2 volume 3.0
                "Я почувствовал острую боль на запястьях. "
                extend "Посмотрев на них, обнаружил глубокие кровоточащие царапины, которые появлялись прямо на глазах."
                "Руки онемели от боли, однако вставший в горле ком страха помешал закричать."

                show yuli empathy
                with dissolve

                yuli "Так-то лучше! "
                extend "Теперь, каждый раз когда будешь думать об измене, посматривай на них. "
                extend "И будь хорошим мальчиком. "
                extend "Отдыхай."

                hide yuli
                with dissolve

                with vpunch
                play audio "audio/Fall.mp3" noloop fadein 0.2 fadeout 0.2
                
                "Меня словно затянуло в водоворот, выплюнув прямо на пол в комнаты. "
                extend "Кое-как поднявшись, я осмотрелся. "
                extend "Руки болели и плохо слушались."
                "Сознание плыло, да и в целом ощущения были не самые приятные."
                
                hide screen toska
                with dissolve
                
                sanya "Это что нахуй было..."
                "Юли в комнате уже не было. "
                extend "Забравшись на кровать, я осмотрел руки. "
                extend "Кровь идти перестала, раны закрылись."
                "Несмотря на то, что я очнулся на полу – крови не было."
                sanya "Галлюцинации?"
                "В виски отдало легкой болью. "
                extend "Нарастающий страх, подстегиваемый болью в руках, помутнил сознание. "
                extend "Из-за всех сил сжав одеяло, я повернулся на бок."
                sanya "Это Юля сделала?"
                "Как она смогла исчезнуть? "
                extend "Почему говорила такие странные вещи? "
                extend "И почему у меня руки порезаны?"
                "Тысячи вопросов роились в моей голове, не давая уснуть. "
                extend "Но вдруг по телу прошла волна расслабления."
                sanya "А, собственно, какая разница? "
                extend "Главное, что Юля довольна, а остальное неважно..."
                "Подумал об этом я уснул. "
                extend "Не обращая внимания на боль и то, что случилось до этого."

                jump _day6

            # концовка
            else :

                sanya "Юль, что за бред? "
                extend "Говоришь так, будто бы это просто катастрофически важно. "
                extend "Мы же просто знакомые, что за трагедии."
                
                show yuli neutral
                with dissolve

                "Она смотрела на меня пару секунд."
                yuli "Ясно. "
                extend "Я поняла тебя."

                hide yuli
                with dissolve

                play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                pause 0.7
                play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
                
                "С этими словами она вышла из комнаты. "
                extend "Я проводил её взглядом и уставился в закрытую дверь. "

                "Какая же она всё-таки странная, а раньше казалась идеальной."
                "Жаль, конечно, но я и правда ничего ей не обещал, так что доёб, как говорится, непонятен."
                "Надо бы уже выходить, иначе опоздаю на встречу."
                
                play sound "audio/Fall.mp3" noloop fadein 0.1 fadeout 0.1 
                pause 0.3
                show screen toska
                with sshake
                
                
                noname "ТЫ НИКУДА НЕ ПОЙДЁШЬ!"
                play sound "audio/pain.mp3" noloop fadein 0.1 fadeout 0.2 volume 2.0
                
                "Голову пронзила сильнейшая вспышка боли. "
                
                
                
                extend "Ноги подкосились, и я рухнул на пол, схватившись за голову."
                
                play music "audio/strashilka_rero.mp3" volume 0.5 noloop

                image yuliinsult:
                    block:
                        "images/yuli/empty glitch.png"
                        pause 0.2
                        "images/yuli/insult.png"
                        pause 2.0
                        repeat


                show yuliinsult:
                    zoom 0.8 center alpha 0.0
                    linear 3.0 zoom 1.0 alpha 1.0
                with dissolve

                "За моей спиной, как ни в чём не бывало, на кровати сидела Юля."
                yuli "Саша, Сашенька, почему ты так считаешь? "
                extend "Я думала, мы уже пара!"
                "Как? Она же только что ушла из комнаты?!"
                "Боль усилилась."
                yuli "Я, на самом деле, очень стеснительная по природе. "
                extend "Ты не представляешь, каких трудов мне стоило подойти к тебе, заговорить. "
                extend "Потом ещё встретиться."
                show yuliinsult:
                    zoom 1.1 truecenter
                yuli "И ты сейчас говоришь, что между нами ничего нет? "
                if day3_choice_yuli:
                    extend "А автобус? "
                if day4_yuli_meal or not day1_pasha_kfc or day1_yuli_agreed_after_kfc:
                    extend "А наши прогулки? "
                extend "Знаешь кто ты? Ты – предатель!"
                show yuliinsult:
                    zoom 1.2 center
                sanya "А-а-а-а-а-а!!!"
                "Боль была такая, что мне хотелось умереть."
                "Стало тяжело сопротивляться Юле. "
                extend "Она словно захватила мой разум, подчинила меня себе."
                show yuliinsult:
                    zoom 1.3 truecenter
                yuli "Ты просто бабник. "
                extend "Как только на тебя обратило внимание парочка шлюх, так всё? "
                extend "Я была первой. "
                extend "Я влюбилась в тебя первой. "
                extend "Я обязана стать твоей первой!!!"
                

                
                yuli "Саша, я очень люблю тебя. "
                extend "И мне больно, что ты не отвечаешь мне взаимностью."
                yuli "Я прекрасно чувствую, что сейчас больно и тебе."
                yuli "Ну ты же понимаешь меня, да? Ты всё давно уже понял."
                show yuliinsult:
                    zoom 1.35 truecenter
                yuli "Я — твоя совесть. "
                show yuliinsult:
                    zoom 1.4 truecenter
                extend "Я — твоя страсть. "
                show yuliinsult:
                    zoom 1.45 truecenter
                extend "Я появилась в твоей жизни именно тогда, когда нужна была больше всего."
                yuli "И что теперь? " 
                extend "Ты меня больше не любишь?"

                "Не желая больше терпеть эту боль, я пополз в сторону балкона. "
                extend "В принципе, высота достаточная, чтобы это всё прекратилось."
                show yuliinsult:
                    zoom 1.5 truecenter
                yuli "Ты предпочел меня другим тёлкам, и это печально. "
                extend "Думаю, ты плохой человек, а плохие люди не должны жить на этом свете."

                hide yuli
                with dissolve

                scene sanatorium balcony
                with dissolve
                "Открыв дверь на балкон, я навалился на перегородку. "
                extend "Я уже не мог соображать. "
                extend "Хотелось просто покончить с этим."
                "Совершив последнее усилие, я оттолкнулся от пола."
                
                scene black
                with dissolve
                pause 2.0
                play sound "audio/Fall.mp3" noloop fadein 0.3 fadeout 0.3
                pause 2.0

                hide screen toska
                show yuli wet sad
                with dissolve

                yuli "Прощай, Сашенька."
                yuli "Теперь мы с тобой вместе. Навсегда."
                hide yuli with Fade(3.0, 0.0, 0.0)
                pause 3.0
                stop music fadeout 1.0

                jump _end


            
    elif day5_emily_in_cafe :
        "Я решил подсесть к Эмилии. "
        extend "Наш вчерашний разговор был настолько приятным, что я всю ночь не мог не думать о ней."
        sanya "Привет, Эмилия! "
        extend "Я подсяду?"
        
        show emily green flirting at center
        with dissolve

        emily "О, Саша, привет! " 
        extend "Конечно, садись!"

        play sound "audio/chair_crack.mp3" noloop fadein 0.1 fadeout 0.1

        "Я сел напротив Эмилии, поставив поднос. "
        extend "Эмилия уже почти закончила свою порцию, видимо пришла вовремя, в отличии от меня."
        sanya "Эмилия, как спалось?"

        show emily kind
        with dissolve

        emily "Неплохо. "
        extend "Правда, из-за того, что спала с открытым окном, под утро замёрзла. "
        extend "Надеюсь, не простужусь." 
        emily "А ты как ночь провел?" 
        "\"Думая о тебе\" – чуть было не ляпнул я, но вовремя остановился. "
        extend "Рановато, думаю, для таких откровений."
        sanya "Тоже неплохо, хотя, обычно, я не очень хорошо сплю на новых местах."
        emily "Понимаю, хотя я уже немного привыкла. "
        extend "Часто приходится туда-сюда мотаться по региону."
        sanya "Да?"

        show emily green happy
        with dissolve

        emily "Ну, я типа активистка-комсомолка-спортсменка, езжу туда-сюда по вузовским мероприятиям. "
        extend "Они иногда на несколько дней затягиваются, так что проиходится ночевать."
        sanya "А как ты учишься? "
        extend "Ты успеваешь вообще?"
        emily "Приходится, иначе родители загрызут – они могут у меня. "
        extend "Папа офицер флота, а мама преподаватель бывший!"
        sanya "Серьезно!"
        "Я уважительно покивал."

        show emily green neutral
        with dissolve

        emily "Мне не очень нравится дома находится, а родители запрещают квартиру снимать, говорят \"что нам на неё деньги тратить, у тебя есть уже где жить\"."
        emily "И плевать, что мне до ВУЗа на другой конец города надо ехать, да по пробкам."
        emily "Нет, чтобы университет выбрать поближе, они в самый дальний отправили!"
        "Ого, как у неё всё серьёзно. "
        extend "Не хотел бы я таких родителей."
        sanya "Тебя родители заставили поступить?"
        emily "Ну, да. "
        
        show emily green sad
        with dissolve

        extend "Они уже всё за меня продумали. "
        extend "Даже куда я работать пойду."
        sanya "Жёстко..."
        "Помолчали, думая о своем. "
        extend "Кажется, Эмилия расстроилась, но кто же знал, что так получиться. "
        extend "Я лихорадочно искал вопрос, который можно задать, но девушка меня опередила."

        show emily green kind
        with dissolve

        emily "А ты чем увлекаешься?"
        sanya "Да, как и все. Спорт там, видеоигры..."
        "Мне стало немного стыдно, за то что как таковых увлечений у меня нет. "
        extend "Но Эмилия, кажется, даже не заметила этого."
        emily "А я люблю петь! "
        extend "Правда, пока не очень хорошо получается, да и времени учиться нет, но главное это же желание, да?"
        "Ответить я не успел, она меня опередила."
        emily "Ещё, я хочу когда-нибудь поехать в путешествие! "
        extend "Родители меня, конечно, не отпустят, но вдруг случится так, что получится, было бы очень круто!"
        "Я кивал в такт её словам. "
        extend "Эмилию понесло, видимо, у неё давно не было нормальных собеседников. "
        extend "А лучший собеседник кто? "
        extend "Тот кто не мешает говорить."
        "Но вдруг она опомнилась, и слегка смутилась."
        emily "Извини, я много говорю, да?"
        sanya "Ну, немного."

        show emily green sad
        with dissolve

        "Произнеся, я понял какую ошибку совершил. "
        extend "Глаза Эмилии заблестели, и я поспешил добавить:"
        sanya "Да все нормально! "
        extend "Я просто молчаливый и люблю слушать. "
        extend "Всё хорошо."

        show emily green cute
        with dissolve

        "Кажется, немного подействовало. "
        extend "Эмилия чуть повеселела."
        "Но дальше у нас разговор не пошёл – настало время процедур."

        sanya "Может встретимся вечером?"

        show emily green flirting
        with dissolve

        emily "Давай! Я тут погуляла, пару интересных мест нашла. "
        extend "Могу показать."

        "Она хитро мне подмигнула, и я не смог отказаться. "
        extend "Забившись на встречу, мы разошлись довольные друг другом."

        scene black
        with Fade(0.5, 0.5, 0.5, color="#000")
        stop music fadeout 1.0
        if rel_yuli >= 3 :
            "Процедуры проходили спокойно. "
            extend "Массажик, солевая ванна, витаминчики и прочее. "
            extend "Вот только мое внутреннее умиротворение было далеко от этого самого умиротворения."
            "Что-то не давало мне покоя, какое-то зудящее чувство на периферии сознания раздражало своей навязчивостью. "
            "Словно я что-то сделал не так, что-то упустил или проигнорировал. "
            extend "Терзаемый непонятным чувством, я переходил с процедуры на процедуру, как вдруг прозвучал такой знакомый голос, заставивший меня вздрогнуть."
            noname "Саша..."
            "Я обернулся в поисках источника голоса, но никого не обнаружил."
            "Поежился, поймав заинтересованный взгляд какого-то взрослого мужика, что проходил мимо моей ванной."

            "Иди, иди, не глазей, не мешай мне шизеть."

            noname "Саша..."

            "Да блять! "
            extend "Я вновь закрутил головой, силясь найти шутника. "
            extend "Однако в маленькой комнате с кучей ванн был только я и тот мужик, что погрузился в ванную на противоположной стороне комнаты."

            "Вряд ли это он... "
            extend "Да ещё и женским голосом. "
            extend "Есть, конечно, такие умельцы, но не думаю, что это наш случай. "
            extend "Да и голос подозрительно знаком."

            "Тут у меня в голове что-то как будто бы щелкнуло. "
            extend "Это же Юлин голос. "
            extend "По спине пробежали мурашки, а в ванной как будто бы стало холодно."
            "Погрузившись в воду по шею, я вновь поежился. "
            extend "Кажется, этим неприятным чувством была вина. "
            extend "Вина за то, что я не поговорил с ней после вчерашнего. "
            extend "Не нашел, не написал даже."

            "Ы-ы-х... "
            extend "Но ведь она сама вчера не пришла! "
            extend "Да и сегодня её видно не было. "
            extend "Так почему же я чувствуя себя так, будто предал кого-то."

            noname "Потому что так и есть..."

            "Так! "
            extend "Вскочив из ванной и расплескивая воду я пошлепал в раздевалку."

            "ещё бы меня совесть Юлиным голосом стыдила. "
            extend "Нафиг, нафиг, пойду подышу, что ли..."

            "Придя в пустую комнату и зайдя на балкон, я задумался. Чувство, похожее чем-то на совесть. Но откуда бы она взялась, особенно у такого как я?"
            "Но какой-то червячок сомнения грыз меня, наводя на разные мысли. Может, все-таки, найти Юлю, чтобы нормально спросить в чем дело? А то как то не по-пацански получается..."

            menu :
                "Разыскать Юлю.":
                    $ day5_look_for_yuli = True
                "Пойти к Эмилии":
                    $ day5_look_for_yuli = False
        
        if not day5_look_for_yuli :
            if day4_tried_move and not day4_fight:
                scene sanatorium skin dormitory room
                with dissolve
            else:
                scene sanatorium dormitory room
                with dissolve

            "Почилив в комнате, отдыхая от процедур, я поднялся, морально готовясь на встречу с Эмилией. "
            "Надев свои лучшие шмотки, я пригладил волосы, подмигнул себе в зеркало и пошёл блатной походкой в назначенное место встречи."

            play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
            pause 0.5
            show sanatorium walkway
            with dissolve
            pause 0.5
            play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
            pause 1.0
            play sound "audio/footsteps.mp3" noloop fadein 0.2 fadeout 0.2
            pause 2.0
            
            scene sanatorium
            with dissolve

            "На улице было довольно тепло, пускай и вечерело. "
            extend "Хотя, вот это прохладное дуновение ветра, заставляющее желтеть листья и закутываться теплее, присутствовало."
            "Это дыхание осени, такое тоскливое и грустное, но при этом удивительно приятное. "
            extend "Может быть, осень – это душа этих мест?"

            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.2 fadeout 0.2
            
            pause 2.0

            scene sanatorium alcove
            with dissolve
            
            "Курилка пустовала, как и всегда. "
            
            play sound "audio/chair_crack.mp3" noloop fadein 0.2 fadeout 0.2

            extend "Сев на лавочку, я достал Чапман. "
            extend "Но, подумав немного, убрал его обратно. Курить не хотелось." 
            "Зато хотелось как следует вдохнуть этот чистый воздух, чтобы прояснилась голова и очистились легкие."
            "В данном случае дым лишний. "
            extend "Все лишнее, кроме этой прекрасной природы."
            "Вечерело. "
            extend "Становилось прохладнее, так что моя одежда уже не спасала от пронизывающего дыхания осени."
            "Эмилии все не было, а написать я ей не мог – мы не обменивались контактами."
            "Беспокойство сменилось раздражением. Неужели, я ошибся второй раз?"
            "Грудь кольнуло, а в ухо будто бы кто-то прошептал: \"Ты просто обычный неудачник...\""

            menu:
                "Пойти искать Эмилию":

                    $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    $ day5_go_look_for_emilia = True

                "Пойти в комнату":

                    $ str_for_notification = "{size=-12}У этого действия будут последствия{/size}"
                        
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    $ day5_go_look_for_emilia = False
                    "Продолжения нет."

            if day5_go_look_for_emilia :

                "Эмилия не похожа на человека, который просто забывает или кидает, по крайней мере, мне хочется в это верить."
                "Собрав всю свою волю в кулак я направился на её поиски. И, к счастью, долго в детектива играть не пришлось."
                "Первый же работник подсказал мне номер её комнаты, и доверительно сообщил, что как она зашла, так и не выходила."
                play sound "audio/footsteps_asphalt.mp3" fadein 0.2 fadeout 0.2
                pause 1.5

                scene sanatorium walkway
                with dissolve

                "Стараясь не забивать голову мыслями по типу: зачем вообще работникам знать кто куда ходил или не выходил, я направился по заданным координатам."
                "Эмилия жила этажом выше, прямо над моей комнатой. Уж не судьба ли это?"

                play sound "audio/door_knock.mp3" noloop fadein 0.5 fadeout 0.5

                "Постучавшись, я прислушался. "
                extend "В комнате послышалась какая-то возня, но никто не открыл. "
                play sound "audio/door_knock_hard.mp3" noloop fadein 0.5 fadeout 0.5
                extend "Постучав настойчивее, я прибавил голос."
                sanya "Эмилия, открой! "
                extend "Я знаю, что ты там!"

                play music "audio/emily_sad.mp3" fadein 1.0 fadeout 1.0 volume 0.3
                play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                
                "Какое-то время было тихо. И когда я уже было планировал уходить, дверь, легко скрипнув, открылась."

                show emily green sad at right 
                with dissolve

                show emily:
                    linear 0.5 xalign 0.75 zoom 1.1 yalign 0.8
                    linear 0.5 xalign 0.5 zoom 1.0 yalign 1.0

                "Передо мной предстала растрепанная Эмилия, с красными заплаканными глазами."
                emily "Привет..."
                sanya "Оу, привет..."
                "Несколько неожиданно было видеть Эмилию... "
                extend "такой."
                emily "Извини, что я в таком виде.... "
                extend "Просто..."
                "Кажется, она едва сдерживала себя, чтобы не заплакать."
                sanya "Извини, если помешал, я могу пойти..."
                
                show emily:
                    linear 0.3 zoom 1.15
                with hpunch

                emily "Нет-нет! "
                extend "Не уходи!"
                "Она сделал шаг вперед, схватив меня за руку."
                emily "Может... "
                extend "Посидишь со мной? "
                extend "Мне так будет спокойнее."
                "Утешать девушек мне ещё не приходилось. "
                extend "Ну, все бывает в первый раз."
                sanya "Конечно! "
                extend "Мне зайти?"
                "Девушка кивнула, потянув меня за собой."

                play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2
                
                scene sanatorium emily room
                with dissolve
                
                "её комната была одноместной и на вид выглядела обставленной, видимо, по платной путевке предоставляют такие апартаменты."
                "Все было чисто и аккуратно, только кровать была расправлена, что выбивалась из общей опрятности."
                "Эмилия потянула меня как раз к этому островку беспорядка, заставив сесть. "
                
                show emily green neutral at left:
                    zoom 1.1
                    ypos 1.0
                    linear 0.5 zoom 1.0 ypos 1.1  
                with dissolve

                "Сама примостилась рядом, все так же не отпуская рукав моей кофты."
                "Поняв, что Эмилия не планирует начинать разговор первой, я осторожно спросил:"
                sanya "Что-то случилось?"
                "Она кивнула, крепче сжав мою руку."
                sanya "Хочешь рассказать мне?"
                "Эмилия неуверенно кивнула, чуть расслабившись."
                "Я не стал продолжать допрос, захочет – расскажет, но и просто сидеть не хотелось."
                sanya "Может я могу что-то сделать для тебя? "
                extend "Может, как-то помочь?"
                "Как же вести себя в таких ситуациях?.."
                "Она неуверенно посмотрела мне в глаза."
                emily "Ну... "
                extend "Ты можешь меня поцеловать?"
                sanya "Что, прости?"
                "Сказать, что я опешил, ничего не сказать."
                emily "Я хочу, чтобы ты меня поцеловал!"
                "Уже уверенней произнесла она, смотря мне прямо в глаза."

                menu :

                    "Поцеловать Эмилию." :
                        $ str_for_notification = "{size=-12}Эмилия запомнит это{/size}"
                            
                        show screen notification_popup_big
                        with dissolve

                        pause 2.0

                        hide screen notification_popup_big
                        with dissolve

                        $ day5_kiss_emilia = True
                    "Дать понять, что ещё рано для этого." :
                        $ str_for_notification = "{size=-12}Эмилия запомнит это{/size}"
                            
                        show screen notification_popup_big
                        with dissolve

                        pause 2.0

                        hide screen notification_popup_big
                        with dissolve

                        $ day5_kiss_emilia = False

                if day5_kiss_emilia :
                    "Воу... Вот это мне свезло."
                    "Не веря своим ушам, я переспросил:"
                    sanya "Что, прости?"
                    emily "Я хочу поцеловаться."
                    "Она произнесла это так серьезно, что я не смог устоять."
                    sanya "Ну, желание дамы – закон."

                    show emily at center
                    with dissolve
                    
                    camera:
                        center
                        linear 0.5 zoom 1.1 center 

                    "Я подсел ближе и наклонился к резко покрасневшей Эмилии. "
                    extend "Цвет её лица слился с цветом волос, а широко раскрытые глаза, кажется, неверяще смотрели на меня."
                    camera:
                        linear 0.5 zoom 1.2 yalign 0.4 

                    "Вот между нашими лицами осталась пара сантиметров, я уже почувствовал её теплое дыхание на своих губах."
                    
                    camera:
                        center
                        linear 0.5 zoom 1.0 center 
                    with hpunch
                    
                    play sound "audio/Fall.mp3" noloop fadein 0.2 fadeout 0.2

                    hide emily
                    with dissolve

                    "Как вдруг Эмилия резко меня оттолкнула."
                    "Причем с такой силой, что я слетел с кровати, больно ударившись об пол."
                    emily "Нет! Нет-нет-нет!"
                    "Громкий крик сменился всхлипами, которые вскоре переросли в громкий вой."
                    sanya "М, блядь...."

                    menu :
                        "Постараться успокоить." :
                            $ day5_help_emily_panic = True


                        "Стыдливо побежать домой." :
                            $ day5_help_emily_panic = False

                    if day5_help_emily_panic :
                        "Бля-я-я-я..."

                        show emily green sad
                        with dissolve

                        "Поднявшись с пола, я попытался подойти к Эмилии, но у неё случилась настоящая истерика."
                        "Она металась на кровати, кричала и рыдала. "
                        extend "Выглядело это пугающе, а что делать, я не знал совершенно."
                        "Я попытался к ней приблизиться, но в меня тут же полетела подушка, а истерика, кажется, усилилась."
                        "Но пересилив себя, я всё-таки смог подойти к сжавшейся в комочек Эмилии."
                        sanya "Я не буду приставать. "
                        extend "Извини, за то, что я сделал."
                        "Я попытался придвинуться ещё ближе, но Эмилия, укуталась сильнее. "
                        extend "Так что я оставил попытки. "
                        "Просто сидел рядом, говоря какую-то успокаивающую белеберду."
                        "Через какое-то время она чуть успокоилась. "
                        extend "Из кокона одеяла доносились лишь редкие всхлипы."
                        "ещё через пару минут, она раскуталась и равнодушно посмотрела на меня."

                        show emily green neutral
                        with dissolve

                        emily "Извини за это. Не знаю, что на меня нашло."
                        sanya "И ты прости, я повел себя как мудак..."
                        emily "Да нет, вполне естественно."
                        "Неловкая пауза затягивалась."
                        emily "Ты можешь идти, все в порядке."
                        sanya "Уверена?"
                        emily "Да, приму ванну, успокоюсь. "
                        extend "Спасибо, что посидел со мной."
                        sanya "Да не за что..."

                        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2

                        scene sanatorium walkway
                        with Fade(0.3, 0.4, 0.3)

                        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2

                        "Я поднялся и в полнейшей тишине вышел из комнаты."

                        play sound "audio/footsteps_loop.mp3" fadein 0.2 fadeout 0.2

                        "Настроение пробило все пределы, так что я просто поплелся в комнату."
                        "На душе было гадко, хотя я, вроде, ничего такого и не сделал. "
                        extend "Кажется, у меня судьба такая, быть неудачником. Эх..."
                        stop sound fadeout 0.5
                        pause 0.5
                        
                        play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2

                        if day4_tried_move and day4_fight:
                            scene sanatorium dormitory room 
                            with Fade(0.3, 0.4, 0.3)
                        else:
                            scene sanatorium skin dormitory room 
                            with Fade(0.3, 0.4, 0.3)

                        play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2

                        "Зайдя в пустую комнату, я бухнулся на кровать."
                        "Неприятная усталость накинулась на тело, даже думать не хотелось. "

                        scene black
                        with dissolve

                        jump _day6
                    else :
                        
                        "Бля-я-я-я..."
                        "Поднявшись с пола, я попытался подойти к Эмилии, но у неё случилась настоящая истерика. Она металась на кровати, кричала и рыдала. Выглядело это пугающе, а что делать я не знал совершенно."
                        "Я попытался к ней приблизиться, но в меня тут же полетела подушка, а истерика, кажется, усилилась."
                        "Решив не искушать судьбу, я просто пробормотал извинения и вышел из комнаты."
                        "Дверь приглушила громкий плачь, но даже отойдя от комнаты на достаточное расстояние, я слышал его в ушах."
                        sanya "Что же мне так не везет на девушек..."
                        "Настроение пробило все пределы, так что я просто поплелся в комнату. На душе было гадко, хотя я, вроде, ничего такого и не сделал. Кажется, у меня судьба такая, быть неудачником. Эх..."
                        "Зайдя в пустую комнату, я бухнулся на кровать. Неприятная усталость накинулась на тело, даже думать не хотелось."
                        "Так что перевернувшись на бок, я просто закрыл глаза и уснул. Прямо в одежде. День – дерьмо..."
                        "Проснувшись утром, я, полностью разбитый, пошел в ванную, чтобы умыться и почистить зубы."
                        "Но вдруг меня привлек какой-то странный шум с улицы – балкон был открыт, так что звуки отлично проникали в комнату. Заинтересованный, я глянул вниз."
                        "Там, в окружении кучи людей, в огромной лужи крови лежала сломанной куклой Эмилия."
                        "В тот же миг люди, стоящие внизу подняли свои головы. Несмотря на то, что между нами было расстояние в пару этажей, я отчетливо увидел в их глазах презрение, смешанное с осуждением."
                        "Шок, сковавший члены, не давал двинуться. Я смотрел вниз, на Эмилию и не мог поверить своим глазам."
                        "Вдруг она повернула голову и посмотрела прямо на меня."
                        emily "Смотри, что ты сделал. Это только твоя вина"
                        "И тут я закричал. Сильно, до хрипоты. Отказываясь верить происходящему."
                        "И тут же проснулся. Проснулся, продолжая кричать."
                        "Пот покрыл все тело, горло болело, а сердце бешено колотилось. Вскочив, я подбежал к балкону. Посмотрел вниз. Никого. Облегчение разлилось по телу, и я чуть расслабился. Сон... Всего лишь сон..."
                        
                        jump _day6 
                else :
                    sanya "Я не думаю, что это хорошая идея, учитывая то, что мы знакомы два дня."
                    "Серьезно, кто вообще предлагает такую близость через два дня общения?"
                    "Хотя, я думаю, для кого-то это покажется нормальным, разные же люди есть. "
                    extend "Но точно не в данной ситуации."
                    "Губы Эмилии затряслись, а глаза заблестели. "
                    extend "Кажется, она была готова вновь разрыдаться."
                    
                    show emily green sad at center:
                        ypos 1.1
                        linear 0.5 zoom 1.3
                    with dissolve
                    
                    "Не дав ей это сделать, повинуясь порыву, я её обнял."
                    sanya "Но дружеские объятия я могу тебе устроить."

                    show emily green crying
                    with dissolve

                    "Пара мгновений и плотину прорвало."
                    "Она разрыдалась так, что мне стало не по себе. "
                    extend "Она ничего не говорила, просто рыдала навзрыд несколько минут подряд."
                    "Это же сколько в себе надо копить, чтобы вот так в один момент все вылить."
                    "Через какое-то время она чуть успокоилась. "
                    extend "Уткнувшись мне в грудь она тихонько всхлипывала и вздрагивала."
                    
                    show emily green sad at center:
                        ypos 1.0
                        zoom 1.0
                    with dissolve

                    "Погладив её по неожиданно мягким волосами, я осторожно отнял её от своей груди и положил на кровать."
                    "Она лениво сопротивлялась, но, видимо, эта вспышка забрала у неё много сил."
                    "Прикрыв её одеялом, я сел рядышком, вытерев своей кофтой остатки слез с её лица."
                    
                    emily "Спасибо."
                    sanya "За что?"
                    emily "За то, что посидел со мной. "
                    extend "Извини, за это. Просто... "
                    extend "Не было сил сдерживаться."
                    sanya "Не переживай. "
                    extend "Мне это ничего не стоило."
                    
                    show emily green neutral at center
                    with dissolve

                    "Она слабо улыбнулась."
                    emily "У меня довольно строгие родители. И не особо чуткие. "
                    extend "Для них я – идеальная дочь. Отличница, спортсменка, всегда и везде первая."
                    emily "В общем, все как у всех подобных людей. "
                    extend "Мне, в целом, и самой нравится заниматься спортом, активничать, побеждать. "
                    extend "Это приятно, когда ты чувствуешь, что становишься лучше."
                    emily "Переступаешь через ступень, так сказать."
                    emily "Но когда твои родители считают, что ты делаешь недостаточно, когда все твои достижения обесценивают, а тебя саму считают стальной и непробиваемой – это грустно. "
                    extend "Принес пятерку?"
                    emily "Почему не пятерку с плюсом? " 
                    extend "Победил на региональной олимпиаде? " 
                    extend "Почему не на международной?"
                    emily "И так во всем. Даже в отдыхе. " 
                    extend "Ты устала решать тест? "
                    extend "Иди в зал! " 
                    extend "Ты устала в зале? "
                    extend "Садись за уроки. "
                    emily "Когда вечно крутишься, есть риск, что закружиться голова."
                    emily "В последнее время это моя вечная проблема."
                    sanya "А почему ты не переедешь? "
                    extend "Ты тогда сможешь жить как хочешь?"

                    show emily green sad
                    with dissolve

                    "Эмилия горько улыбнулась."
                    emily "Если бы это было так просто."
                    emily "Думаю, как у всех родителей подобного типа есть такое, что они не хотят отпускать своё дитя, опасаясь, что оно перестанет быть таким, каким его хотят видеть родители."
                    emily "Мне не дают денег на карманные расходы и заставляют вести отчет о каждой трате. "
                    extend "Лишние деньги сразу забирают, так что копить я не могу."
                    emily "Если устроюсь на работу – то родители сразу об этом узнают, так как планы на день пишет мама, прописывая мои действия буквально до секунды."
                    emily "Если задержусь – спросят где. "
                    extend "Не появлюсь на паре – накажут. " 
                    extend "У моей мамы знакомая в деканате, так что и в вузе я под колпаком."
                    emily "Снизиться успеваемость – накажут. Начну общаться с кем-то без одобрения – накажут."
                    sanya "Мне кажется, ты все немного утрируешь..."
                    "Серьезно, звучит все немного... бредово."
                    emily "Хех. Поверь, возможно я что-то даже упустила, так как для меня это уже давно стало нормой."
                    emily "Они даже хотели поехать в этот санаторий со мной, боясь отпускать одну."
                    emily "Но не получилось – папу вызвали в командировку, а маму я смогла убедить. "
                    extend "её главным условием было, чтобы я каждый день, утром днем и вечером звонила по видеосвязи."
                    sanya "Бывают же родители..."
                    emily "Я думаю, мои не самые худшие в мире. "
                    extend "Да и делают они это их лучших побуждений."
                    sanya "Мне показалось или ты сейчас переобулась?"
                    play voice "audio/girl_laugh2.mp3"

                    show emily green happy
                    with Dissolve(2.0)
                    

                    "Эмилия хихикнула... "
                    extend "Красиво, ярко и так искренне, что сердце будто бы свело."

                    emily "Да нет, просто говорю про мотивы. "
                    extend "Конечно, мне хочется сбежать из под их душной опеки, пожить так, как мне хочется. "
                    extend "С тем, кем мне хочется."
                    "Тут она стрельнула глазками в меня. "
                    extend "Я сделал вид, что не заметил этого."
                    sanya "Ну, если то, что я услышал правда от и до, то это будет весьма трудной задачей. "
                    extend "Но если у тебя есть цель – стремись к ней, и все в таком роде."
                    "Кажется, она немного обиделась..."

                    show emily green kind
                    with dissolve

                    emily "Извини за мою вспышку. "
                    extend "Просто... я немного устала держать все в себе и делать вид, что я робот."
                    sanya "Все нормально, не бери в голову."
                    sanya "Пускай мы знакомы пару дней, я уже могу назвать тебя подругой. "
                    extend "Думаю, я мог это сделать ещё в парке, когда ты подошла ко мне, чтобы спросить, как у меня дела."
                    
                    show emily green love
                    with dissolve

                    emily "Просто ты выглядел таким хмурым, будто бы у тебя случилось что-то серьезное."
                    sanya "Можно и так сказать. "
                    extend "Так что вот, ты мне, я – тебе. "
                    extend "В благородство играть не буду!"
                    
                    show emily green neutral
                    with dissolve

                    emily "Что?"
                    "Кажется в её голосе мелькнула паника."
                    sanya "Ничего, не волнуйся. "
                    extend "Просто шутка."
                    
                    show emily green cute
                    with dissolve

                    emily "Ну, ладно. "
                    extend "Слушай, может посидишь со мной ещё немного? "
                    extend "C тобой как-то спокойнее."
                    sanya "Без проблем, время ещё детское."
                    emily "Извини, что так получилось..."
                    sanya "Да все нормально! "
                    extend "Мы же все-равно хотели погулять, а тут считай в гости зашел, на улице же холодно. "
                    extend "Да и в комнате нечего делать."
                    emily "Если хочешь, то ты можешь остаться."
                    emily "Я могу подвинуться..."
                    sanya "Не стоит. "
                    extend "Не хочу доставлять тебе неудобства."
                    "Её можно понять, но пока что не стоит так торопиться. "
                    extend "Видимо, опыта у неё совсем нет..."
                    "Эмилия больше не пыталась затащить меня в постель и вскоре уснула. "
                    extend "Оставив мерно сопящую девушку, я тихо вышел из комнаты."

                    play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2
                    
                    scene sanatorium walkway
                    with Fade(0.4, 0.5, 0.4, color="#000")
                    pause 1.0

                    play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2 
                    
                    "Да-а-а, существуют же люди!"
                    "Как она вообще с ума не сошла с такими родителями. "
                    extend "Ладно, надеюсь, ей хоть немного полегчало. "
                    extend "Лично мне, когда я посидел с ней в обнимку, точно стало лучше."

                    play sound "audio/footsteps.mp3" noloop fadein 0.5 fadeout 0.5
                    pause 1.5
                    play sound "audio/pain.mp3" noloop fadein 0.2 fadeout 0.2

                    "Так что спокойный и удовлетворенный я шёл в комнату, как вдруг в голове словно что-то стрельнуло."
                    "Вспышка боли в висках, резкая, сильная, но быстро прошедшая. "
                    extend "Словно меня что-то покинуло, решив напоследок немного пошалить. "
                    extend "Ну, ладно, главное не болит."

                    stop music fadeout 1.5

                    play sound "audio/door_open.mp3" noloop fadein 0.2 fadeout 0.2

                    if day4_tried_move and not day4_fight:
                        scene sanatorium skin dormitory room
                        with Fade(0.4, 0.5, 0.4, color="#000")
                    else:
                        scene sanatorium dormitory room
                        with Fade(0.4, 0.5, 0.4, color="#000")
                    
                    play sound "audio/door_close.mp3" noloop fadein 0.2 fadeout 0.2

                    "Придя в комнату я сразу улегся спать. "
                    extend "Устал я знатно, так сон пришел быстро. "
                    extend "День, определенно удался."

                    jump _day6
            
            else :
                "Ой, да в пизду все это!"
                "Без девок, так без девок, сам справлюсь, не впервой."
                "Достав предпоследнюю сигарету, я закурил, направившись в комнату. Пойду спать, время уже позднее."
                "Если мой путь – сигма, то так тому и быть."
                "В конце-концов, что я ждал от этих \"вимен\"?"
                "Понятно что, вот только, учитывая мои базовые характеристики, то самое могло перепасть мне чисто случайно, при большой удачи."
                "Которая, к слову, не была за мной замечена."
                "Я почесал глухо болящую грудь, и затянулся до першения в горле. Подавившись дымом и закашлявшись, я отошел чуть в сторону, чтобы никому не мешать."
                "Продышавшись, выбросил недокуренную сигарету. Все. Заебло. Пора бы уже бросать эту хуйню. Мне скоро выпускаться, а я еще даже не знаю кем стать."
                "Пора бы уже нормально браться за свою жизнь. Думаю, даже хорошо, что меня прокинули."
                "Такое очищает мысли и открывает глаза."
                "Главное, чтобы это не было обычным приливом ночной мотивации и при новом знакомстве я не побежал песиком на случку. Тьфу. От себя тошно."

                if day4_with_skin :
                    "В этот раз комната не пустовала."

                    scene sanatorium skin dormitory room
                    with Fade(0.4, 0.5, 0.4, color="#000")

                    "Мыкало, которого я не видел с момента заселения, отжимался на полу. Судя по промокшей футболке и блестящей лысине, занимался он уже давно и усердно."
                    "Моего прихода он даже не заметил – вот так он был сосредоточен."
                    "Хмыкнув, я скинул с себя верхнюю одежду и пошел в душ. Давненько я не мылся, мне кажется от меня уже пованивать стало."
                    "Ополоснувшись и почистив зубы, я выше из ванной, увидев, что Мыкало продолжает отжимания."
                    sanya "Хуя ты машина! На друга моего похож."
                    "Тут его ритм прервался, он вздрогнул и посмотрел на меня."
                    skin "О, извини, не заметил тебя!"
                    "Он сделал еще пару отжиманий и легко поднялся с пола."
                    skin "Ровно сто раз! Сейчас еще десяточку пробегу, можно и на боковую"
                    sanya "Чего десяточку?"
                    skin "Километров конечно!"
                    "Он Сайтама, что ли?"
                    skin "Давай со мной? Прочищает мозги и чакры, спишь как убитый!"
                    "Еще бы. После десяти-то километров."

                    menu :
                        "Согласиться." :
                            $ day5_run_with_skin = True
                        "Отказаться" :
                            $ day5_run_with_skin = False

                    if day5_run_with_skin :
                        "Впрочем, чего б на ночь и не побегать? Раз уж принял решения меняться, то пока рано назад давать. После пробежки уже можно, в принципе."
                        sanya "Ну, давай. Только я в своем темпе побегу. И не так много как ты."
                        skin "Без проблем, брат. Главное, ведь сам процесс, правильно?"
                        "Я ничего не ответил, натягивая спортивки и кроссовки. Уверен, после первой же сотни метров задохнусь и пойду спать."
                        extend "А завтра по-новой курить и таскаться за девушками. Плавали, знаем."
                        "Выйдя на прохладный воздух, я с удовольствием его вдохнул. Иногда, все-таки, приятно вот так выйти подышать. Жизнь не такой дерьмовой кажется."
                        skin "Ну, погнали"
                        "Он с места дал такого стрекача, будто не марафон бежит, а стометровку."
                        "Я покачал головой. Есть же люди, интересно, через сколько он перестанет выпендриваться и побежит как нормальный человек?"
                        "Взяв неторопливый темп, больше похожий на обычную прогулку, я побежал по парку, размышляя о хорошем и стараясь поддерживать заданный ритм."
                        "Два шага вдох, два шага выдох."
                        "Мимо меня ошпаренным козлом пролетел Мыкало, скрывшись во тьме. Что ж... его физическая подготовка вызывает уважение."
                        "Я уже подустал, хотя пробежал всего ничего."
                        "Если размышлять трезво – все, чем я занимаюсь сейчас полнейший бред. Обычное прожигание времени. Ни саморазвития, ничего."
                        "Я гроблю здоровье выпивкой и сигаретами. Я убиваю дни в интернете и бесполезных встречах."
                        "Они ничего мне не приносят. Это все быстрые удовольствия, которые не несут ничего хорошего. Моя жизнь абсолютно бессмысленная, просто проходит мимо."
                        "Я словно остался тем беззаботным ребенком, которого ничего не волновало, который просто просыпался, чтобы весело провести время."
                        "Но ведь это неправильно – вечно быть этим ребенком. Жизнь она более сложная и глубокая, она не ограничивается..."
                        "Да ничем она не ограничивается! Передо мной открыты все двери, у меня в моем возрасте тысяча возможностей для роста."
                        "Надо только прилагать усилия, и не мало. Наверное, именно это меня и останавливает. Я просто слишком ленив, слишком мягок для того."
                        "Чтобы начать менять себя. Дерево не строгают бумагой, как и металл не куют деревом. Нужно быть тверже. Нужно смочь победить себя – и в этом моя главная проблема."
                        "Я не могу победить себя. Я не могу сломать ту скорлупу, в которой сижу. В ней тепло и комфортно."
                        "Мягко и уютно. И эта мягкость – она разжижает меня. Делает податливым и безвольным. Я не хочу меняться. Вернее я хочу меняться." 
                        "У меня есть желание изменить мою жизнь к лучшему, у каждого оно есть, я думаю."
                        "Я даже могу начать менять её к лучшему. Удалить ютуб, вставать чуть раньше."
                        "Я могу начать ковырять свою скорлупу. Но вот делать это систематически, на протяжении многих и многих часов, дней, лет..."
                        "Я не могу. Начать просто – закончить еще проще. Поддерживать процесс – не в моих силах. Не в моих силах проспаться каждый день."
                        "Не в моих силах продолжать ковырять скорлупу, пока пальцы не перестанут кровоточить. Это больно. Это сложно. Лучше посижу, подожду, пока мне не принесут мне это на блюдечке."
                        "Но не принесут. Я могу сидеть хоть до старости, хоть до своей смерти ждать и нежиться в зоне комфорта, делая лишь попытки, чтобы просто успокоить свою совесть."
                        "Как дозы для наркомана."
                        "Как никотин для курильщика. Просто видимость. Просто иллюзия – я же остаюсь тем же."
                        "Тем же слабохарактерным уебком в скорлупе, из которой не выбраться."
                        "Я могу сколько размышлять по ночам о том, как я буду крут и успешен в будущем. Я могу сколько угодно мечтать о том, как буду выполнять свои цели."
                        "Я могу сколько угодно их ставить и говорить об этом всем, но это не изменит сути."
                        "Моей сути трусливого и ленивого маленького мальчика. Безвольного. Лицемерного даже к себе."
                        "Это ужасно. Хочу ли я так жить? Очевидно нет. Могу ли я что-то изменить в себе?"
                        "Это намного более сложный вопрос. Я могу попытаться. Как пытался сотни раз до этого. Мои слабости – это самый крепкий камень."
                        "Мои попытки – это жалкие капли воды. Но вода все же может победить камень, хоть для этого и требует много времени."
                        "Порой целая жизнь. Нужна ли мне жизнь, полная попыток изменить себя?"
                        skin "Ну, как ты, брат?"
                        "Этот спортсмен мирового класса затормозил рядом со мной, сходу взяв мой черепаший темп."
                        "Кажется, он даже не запыхался. Такие люди вызывают черную зависть, тем, что находят в себе мотивацию к действию."
                        "И чем они отличается от меня? Почему он может каждый день работать над собой, а я – нет? Может это воспитание?"
                        skin "О чем задумался, брат?"
                        sanya "Скажи, где ты находишь мотивацию к действию?"
                        skin "Что? О чем ты?"
                        sanya "Как ты ебашишь каждый день? Ради чего?"
                        "Он хмыкнул, перейдя на обычный шаг. Я тоже перестал бежать, так как сбил дыхание. Да и ноги подустали."
                        skin "Это хороший вопрос, брат. Но я не могу на него ответить. Просто однажды решил для себя, что буду каждый день делать упражнения. И начал делать"
                        sanya "И все? И не хотелось бросить?"
                        skin "Конечно хотелось. И сейчас хочется. Но когда я вижу в зеркале своё тело."
                        skin "Чувствую, что я могу пробежать километр в спринте и подтянуться хоть сотню раз, знаю, что с каждым днем мой предел становится выше и выше..."
                        skin "В общем это заставляет меня вставать с кровати. Это как зависимость, можно сказать."
                        skin "Но правильная зависимость. Вместо чего-то вредного тут – собственные достижения. Чувство продуктивной деятельности. Понимаешь?"
                        sanya "Понимаю. Но..."
                        skin "Есть разные люди брат. Те, для кого цель – собственный комфорт. Они готовы жопу рвать ради него."
                        skin "Готовы ебашить каждый день до кровавых соплей, лишь бы защитить его или приобрести."
                        skin "Есть те, кто хочет ощущать постоянный дискомфорт, расти над собой, ставить цели и достигать их – в этом они находят собственное счастье."
                        skin "Скажи, чем эти люди отличаются?"
                        sanya "Ну... Если так подумать, то ничем."
                        skin "Именно. В целях они разные, но действия одни и те же. И что это значит?"
                        sanya "Я хуй знает..."
                        skin "Комфорт – это иллюзия. Его не существует, потому что его условия и рамки постоянно меняются. Его не достичь как не старайся. Потому что комфорт – это идеал."
                        sanya "По-моему, это какой-то бред. Я сейчас чувствую себя в комфорте, в принципе. Мне норм, я не страдаю."
                        skin "Нет, брат. Если бы ты не страдал, ты бы не ходил с кислым лицом дни напролет. Ты просто не задумываешь над этим, вот и все."
                        sanya "Как это вообще относиться к мотивации?"
                        skin "Что бы ты не делал, все твои действия в любом случае будут направлены на то, чтобы жить лучше, комфортнее и безопаснее."
                        skin "Мотивация любого человека – он сам. Даже если это касается его близких, друзей или других людей."
                        skin "Нас так запрограммировала природа. Даже самые благородные мотивы овеяны эгоизмом."
                        sanya "Ты заебал, когда ты превратился в ебаного Угвея. Еще че философского может спизданешь."
                        skin "В твоем вопросе – я не помощник. Никто не помощник. Если ты ищешь мотивации – ищи её в своей голове, а не голове другого человека. Это чисто стадный инстинкт, когда ты пытаешься подражать другому."
                        skin "Но, брат, пойми, это работает не всегда и это слишком ненадежно. Если ты пойдешь таким путем, тебе нужна будет постоянная поддержка со стороны."
                        skin "Такое тоже имеет место быть, не спорю. Но это ебаные костыли, от которых ты не факт что избавишься. Вот чего ты хочешь от жизни?"
                        sanya "Я не знаю"
                        skin "В твоем возрасте это абсолютно нормально. Особенно в наш век. Раньше все было проще: Дожил до совершеннолетия? Молодец! Женись, расти сына – вот весь смысл жизни. Тебе такое интересно?"
                        sanya "Не очень..."
                        skin "А я из простых. Поэтому и занимаюсь спортом, чтобы сын был здоров. И ищу такую же девушку. Просто я нашел свою цель..."
                        sanya "Ну ебать! Мог бы так сразу и сказать, к чему была эта лекция?"    
                        skin "К тому, чтобы ты понял: иногда для того, чтобы измениться нужна совсем маленькая и простая цель."
                        skin "А иногда и спасение целого мира не сможет заставить человека сделать шаг наружу. Это все равно что подбирать пароль к сейфу"
                        sanya "Я могу подбирать его целую жизнь, и так и не найти. Так и зачем такую жизнь?"
                        skin "Значит, сам подбор пароля – смысл жизни"
                        sanya "Ой, ебать ты вообще сам себя слышишь?"
                        skin "Слышу, брат. И тебе советую. Искать это нормально. Если ты перестанешь это делать – это уже тревожный звонок. Цель поисков в любом случае окупит сам поиск."
                        sanya "Даже если искал всю жизнь?"
                        "На это Мыкало лишь загадочно улыбнулся и свернул в другую сторону, растворившись во тьме."
                        "Какой же он все-таки странный. Но... Может быть он и прав. В конце-концов, вряд ли много людей моего возраста нашло свой смысл просыпаться по утрам."
                        "Некоторые до самой смерти плывут по течению. Просто постараюсь не опускать руки. Искать себя это и правда нормально."
                        "С такими мыслями я пошел спать. Думаю, этот день прошел неплохо."

                        jump _day6

                else :
                    ""

                if not day5_run_with_skin :
                    sanya "Не, извини. День был сложный, хочу выспаться"
                    "Понятливо кивнув, он отстал. Я же плюхнулся в кровать, стараясь не думать ни о чем, лишь бы побыстрее уснуть. День, определенное, выдался очень дерьмовый..."

        else :
            "Не хочется, чтобы между нами были какие-то недомолвки. Так что лучше нормально все обговорить, чтоб точно расставить все точки над i."
            "Решив подобным образом, я сам себе кивнул и пошел в комнату."
            yuli "Рада, что ты правильно расставил приоритеты."
            "Что за хуйня?"
            "На моей кровати развалилась Юля собственной персоной."
            sanya "Что? Ты как сюда попала?"
            yuli "Через дверь"
            "Она невинно улыбнулась, легко поднявшись с кровати."
            yuli "Ты выбрал абсолютно правильный вариант развития отношений, Саша. Это самое лучше решение в твоей жизни. Твоему одиночеству пришел конец"
            "Последние слова она произнесла мне буквально в ухо, обдав их горячим дыханием. По коже пробежали мурашки, и я тут же почувствовал её руки на своих плечах."
            yuli "Я очень рада, Саша. Ты большой молодец!"
            "Она потянула меня к кровати, и я как зачарованный послушался. Усадив меня на постель, она присела мне на колени."
            "Её лицо было в паре сантиметров от моего. Её глаза смотрели нежно и очень добро. Руки мягко гладили мои плечи."
            yuli "Думаю, ты заслужил награду, мой милый Саша."
            "Произнеся это, она чуть толкнула меня в грудь."
            "Что происходит?"
            "Неожиданное чувство падения, когда щекочет в животе, потом резкая остановка, встряхнувшая органы."
            yuli "Это будет твоей наградой..."
            "Меня настигло чувство невероятной эйфории. Хотелось смеяться, плакать, кричать от злости и верещать от восторга."
            "И все это одновременно. Этот убойный коктейль из эмоций был подобен удару пыльным мешком по голове – неожиданно."
            "Сбивающе с толку. Перед глазами завертелись цветные круши и неясные образы женского тела."
            "Как бы я не старался, я не мог их рассмотреть. Лишь тени, абрисы и едва заметные намеки."
            "Все это длилось недолго. Меньше минуты."
            yuli "А теперь – спи. Ты отлично постарался"
            "Волна эйфории ушла так же, как и появилась – резко."
            "Оставив после себя лишь приятную истому, благодаря которой я очень быстро уснул, даже не задумываясь над тем, что сейчас произошло."
            jump _day6

    elif day5_loneliness_in_cafe :

        "Чувство некой усталости подсказало мне, что моя социальная батарейка на нуле."
        "Особого желания с кем-то общаться не было, поэтому я решил сесть один."
        "Хорошо, что девочки сидели ко мне спиной и не могли меня видеть. "
        extend "Объяснятся с ними не хотелось."
        "Быстренько выхлебав идеальной консистенции суп, я принялся терзать сочные сырники, щедро политые ароматной сгущенкой."

        play sound "audio/chair_crack.mp3" noloop fadein 0.2 fadeout 0.2

        noname "Привет..."
        "Я вздрогнул от неожиданности, чуть не подавившись кофе."
        "На стул передо мной мягко приземлилась Юля, на её милом личике блуждала приветливая улыбка."

        show yuli horny
        with dissolve

        sanya "Привет..."
        "Последнее, что мне сейчас хотелось, это общаться с Юлей. " 
        extend "Но раз она пришла, то ничего не поделать."
        
        yuli "Извини, что вчера не пришла! "
        extend "Ты долго ждал?"
        
        show yuli shy
        with dissolve

        "Она состроила такую извиняющуюся рожицу, что у меня пробежали мурашки по спине."
        sanya "Ну, так... "
        extend "Я нашел, чем себя занять..."
        
        show yuli sad
        with dissolve

        yuli "Вот как..."
        "Кажется, этот ответ её расстроил."
        extend "Повисла неловкая тишина."

        show yuli horny2
        with dissolve

        yuli "А давай встретимся сегодня!"
        "Неожиданно выкрикнула она, чуть ли не на всю столовую."
        yuli "Я сегодня точно приду! "
        extend "Честно-честно! "
        extend "Просто в прошлый раз возникли некоторые... "
        extend "трудности, вот!"
        sanya "Какие трудности?"
        "Странно она ведет себя как-то."

        show yuli shy
        with dissolve

        "Она смутилась и щечки мило порозовели."
        yuli "Я отравилась... "
        extend "Весь день из номера не вылезала..."
        sanya "Почему не позвонила? "
        extend "У тебя же есть мой номер."
        yuli "Забыла."
        "Она смутилась ещё больше."
        "Хм, странно все это. "
        extend "Но выглядит она, по крайней мере, раскаявшейся."
        "Стоит ли мне встретиться с ней?"
        
        menu:
            "Согласиться.":
                $ str_for_notification = "{size=-12}Юля запомнит это{/size}"
                    
                show screen notification_popup_big
                with dissolve

                pause 2.0

                hide screen notification_popup_big
                with dissolve

                "Ладно, уж. "
                extend "В конце концов, почему бы не дать такой милой девушке второй шанс?"
                sanya "Давай. "
                extend "Жду тебя после процедур там же, где вчера. "
                extend "Без опозданий!"

                show yuli happy
                with dissolve

                yuli "Конечно!"
                "Юля словно расцвела, услышав эти слова."

                play sound "audio/chair_crack.mp3" noloop fadein 0.2 fadeout 0.2
                pause 0.6
                play sound "audio/footsteps.mp3" noloop fadein 0.2 fadeout 0.2
                
                hide yuli happy
                with dissolve

                "Подскочив как ужаленная, она, не прощаясь, куда-то ускакала. "
                extend "Я же, хмыкнув ей в ответ, продолжил завтрак."
                "И чего со мной не поела?"
                #TODO: не закончено!
                jump _day6

            "Отказаться.":

                $ str_for_notification = "{size=-12}Юля запомнит это{/size}"
                    
                show screen notification_popup_big
                with dissolve

                pause 2.0

                hide screen notification_popup_big
                with dissolve

                "Идти с ней вновь, да и в принципе с кем-то гулять не было никакого желания. "
                extend "После хорошего дня хотелось побыть одному."
                sanya "Юль, извини, но у меня на вечер сегодня другие планы."

                show yuli horny
                with dissolve

                "На Юлином лице застыла улыбка. "
                extend "Смотрелось это жутко. "
                extend "Словно живой человек резко превратился в куклу."
                yuli "Хорошо. "
                extend "Я тебя поняла."
                "С этими словами она встала."
                yuli "Рада была пообщаться."

                play sound "audio/footsteps.mp3" noloop fadein 0.2 fadeout 0.2    
                hide yuli
                with dissolve
            
                "Произнеся эти слова странным тоном, в котором отсутствовали любые эмоции, она деревянной походкой удалилась."
                "Да уж... "
                extend "Впервые отказал девушке, если честно. Странное чувство."
                "Без аппетита доев свой завтрак, я пошёл на утренние процедуры."
                #TODO: не закончено!
                
                jump _day6


label _day6 :
    window hide
    stop music fadeout 2.0
    with None
    scene black 
    stop sound fadeout 2.0
    play music "audio/lobby_music.mp3" fadein 5.0 fadeout 2.5 volume 1.1
    play sound "audio/typewriter-sound.mp3" volume 0.5 loop
    centered "{size=+30}{font=fonts/sfpro_semibold.ttf}{cps=4.8}Конец первой главы.  {nw}{/cps}{/font}{/size}"
    stop sound
    #TODO: Егор, ctrl+f и поищи по "TODO" и закончи полностью пятый день сперва

    with Fade(4.0, 2.0, 5.0)
    jump _end

label _end :
    scene black
    with Fade (2.0, 0.5, 1.0)
    
    pause 4.0

    centered "{size=+24}Над проектом работали:\n{color=#3B7}Asind\nDarlingInSteam\nDanilka108\nXpomin\nTheNorth\nArtsBer\nJuravl\nrero{/color}{/size}"
    centered "{size=+24}Сценарий:\n Главный сценарист: {color=#3B7}ArtsBer{/color}\nГеймджем сценарий первого и второго дня: {color=#3B7}Xpomin{/color}{/size}"
    centered "{size=+24}Игровая режиссура:\n {color=#3B7}Asind, DarlingInSteam, TheNorth{/color}{/size}"
    centered "{size=+24}Дизайн:\nОтветственный за визуал: {color=#3B7}Asind{/color}\nРабота с артами: {color=#3B7}Asind, DarlingInSteam{/color}\nОтветственные за саунд-дизайн: {color=#3B7}Juravl, TheNorth, Asind, DarlingInSteam{/color}{/size}"
    centered "{size=+24}Мини-игры:\n\"Автобус\" и \"Перепей соперника\": {color=#3B7}Danilka108{/color}\n\"Найди предмет\": {color=#3B7}Asind{/color}{/size}"
    centered "{size=+24}Музыка:\n Главная тема и музыка концовок: {color=#3B7}rero{/color}\nМузыка настроений: {color=#3B7}Juravl{/color}{/size}"

    centered "Авторы использованного контента:"
    centered "Andrey Usikov - Rostov Font\nChristian Robertson - Roboto Font\nSan Francisco Pro Font - © 2015-2017 Apple Inc. All rights reserved.\nCMU Sans Serif Font - under SIL Open Font License\n Perun. Copyright © Stefan Peev, Context Ltd, 2016"
    centered "Strauss Festival Orchestra Vienna\nLudovico Einaudi - Nefeli\nSymphony No. 4 in A Major, Op. 90, MWV N16, \"Italian\": IV. Saltarello. Presto. Симфонический орекстр Бирмингема.\nSchumann: Kinderszenen, Op. 15 - 7. Traumerei. Владимир Самойлович Горовиц\n9 духовно-музыкальных сочинений: III. Херувимская песнь; Исполнитель: Государственный камерный хор Министерства культуры СССР; Композитор: Пётр Ильич Чайковский"
    centered "Awakening Dew - Keys of Moon\Downpour - Keys of Moon\nForest Walk - Alexander Nakarada\nHall of the Mountain King - Kevin MacLeod • Edvard Grieg\nCherry Metal - Arthur Vyncke\nSpace Floating - FSM Team feat. < e s c p >\nOtixx - Nostalgia\nharris cole & aso - safe now (slowed & reverb)"

    centered "{size=+24}В разделе \"Об игре\" можно найти ссылку на репозиторий GitHub.{/size}"
    centered "{size=+24}Спасибо за прохождение первой главы новеллы. Мы благодарны за Ваше внимание.{/size}"
    centered "{size=+24}Новости по выходу новой главы можно отслеживать в нашей группе ВК. Ссылка в разделе \"Об игре\"{/size}"