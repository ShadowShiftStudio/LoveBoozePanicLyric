define sanya = Character("[player_name] ", color="#aad2ff")
define pasha = Character('Пашка Запивон ', color="#ffc9aa")
define yuli = Character('Юля ', color="#ffaaff")
define nadya = Character('Надя ', color="#ffaab1")
define storyteller = Character('Рассказчик ', color="#b3aaff")
define olga_dmitrievna = Character('Ольга Дмитревна ', color="#aaffd7")
define grusha = Character('Агриппина Владимировна ', color="#12d69b")
define pavel = Character('Павел Геннадьевич ', color="#ffb4aa")
define skin = Character('Мыкало ', color="#e1ffaa")
define noname = Character('Незнакомец ', color="#4d4d4d")
define emili = Character('Эмилия', color="#e28cd7")

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

define day1_pasha_kfc = False
define day1_sanya_wants_camp = False
define day1_pasha_lose_in_drinking = False
define day1_yuli_agreed_after_kfc = False
define day2_sanya_went_to_smoke = False
define day2_sanya_vote_for_ussr = False
define day2_nadya_bought_sigaretts = False
define day2_nadya_het_one_sigarett = False
define day2_choosen_instead_yuli = False
define day2_nadya_have_a_dialog = False
define day3_go_with_nadya = False
define day3_go_with_yuli = False
define day4_smoke_after_words_olga = False
define day4_move = False
define day4_take_pill = False
define day4_drink = False
define day4_yuli_meal = False
define day4_nadya_meal = False
define day4_smoke_old_siggarete = False
define day4_siggaret_or_room = False
define day4_suicide = False
define day4_go_with_emili = False
define day4_fight = False
define choice_yulia = False
define choice_nadya = False
define choise_lonly = False
define mood_counter = 0

define hi_score = 0

define player_name = "Саня"
define str_for_notification = ""

screen notification_popup():
    add "notification.png" xalign 1.0 yalign 0.055 xzoom 0.6
    text "[str_for_notification]" xalign 0.99 yalign 0.06 color "#ffffff" 

screen notification_popup_big():
    add "notification.png" xalign 1.0 yalign 0.055 
    text "[str_for_notification]" xalign 0.99 yalign 0.06 color "#ffffff" 

screen toska():
    add "night color.png":
        at transform:
            xalign 0.5 yalign 0.5
            alpha 0.0
            linear 4.0 alpha 1.0
            block:
                linear 1.0 zoom 1.2 alpha 0.9
                linear 0.6 zoom 1.0 alpha 1.0
                repeat

label splashscreen:
    play sound "audio/intro_sound.mp3" 
    image back = "#272727"

    scene back
    with dissolve

    show logo studio logo at center with Dissolve(1.6)

    pause 2.0

    scene back 
    with Dissolve(1.5)

    show logo disclaimer with dissolve
    
    pause 100.0

    image sanya_gui = "gui/sanya.png"
    
    hide logo disclaimer
    with dissolve

    pause 0.1

    scene sanya_gui
    with dissolve
    stop sound
    return

label start:
    jump first_day

label first_day:
    image night = "night color.png"
    scene black scen
    
    play music "audio/alarm-sound.mp3"
    "*Звук будильника*"
    stop music
    play sound "audio/alarm-sound-end.mp3"
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
    "Эх, как же хочу вернуться в школьные года, когда ты вечно ищешь способы поднять бабок на алкашку." 
    "Затем идёшь в \"проверенный ларёчек\" и покупаешь литр водки на литр колы в обычные дни, или же литр водки на литр апельсинового сока по праздникам."
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

    scene black scen 
    with fade

    $ mplay("audio/street-music.mp3")
    pause (2.0)
    scene bus station 
    with fade

    "А я вот иду и думаю: \"а не слишком ли я много пить стал в последнее время?\""
    "Уже будто и не помню себя трезвым..."
    "Из бесконечного потока мыслей меня смог вытащить только гудок подъезжающего ЛИАЗа."
    "А вот и мой автобус подъезжает."    
    sanya "Ладно, пора и честь знать."

    $ mstop() 
    pause(2.0)

    play sound "audio/bus.mp3" volume 0.15
    "*Звук подъезжающего автобуса*"
    stop sound

    play sound "audio/sound-in-bus.mp3" volume 0.2

    scene bus 
    with fade
    "Даже матушку свою довёл."
    "Вчера с мужиками пришли пиво попить, последний день лета проводить, скажем так, а она меня поджидает у туалета и говорит:"
    "\"Хоть бы раз домой вернулся с девчонкой какой-нибудь красивенькой, а не как обычно с парнями в зассаных майках\", — \"Мама, ну мы же панки\"..."
    "Впрочем, ладно. У меня есть немного времени, чтобы поспать. Надо было ночью не заниматься хернёй..."
    #$ _hi_score(hi_score)
    call screen bus
    # TODO: ЗАКОНЧИТЬ РЕКОРД
    "[_return]"
    #call play_bus 
    

    scene black scen 
    with fade
    "Какой странный сон мне приснился..."
    "Бесконечно едешь прямо... Как далеко можно так уехать?"
    play sound "audio/bus.mp3" volume 0.15
    $ renpy.pause (7.5)
    stop sound fadeout 1.5
    play music "audio/street-sound.mp3" volume 0.1
    scene bus station near nstu 
    with fade

    show pasha neutral:
        alpha 0.0 xalign 0.5 yalign 1.0
        # Take 1.0 seconds to move things back to the left.
        linear 1.0 xalign 0.6 alpha 1.0

    "Только вышел из автобуса, как тут мне на встречу идёт крупный парень, он явно меня узнал, а вот я его не очень..."
    "Ба-а, так это же Пашка Запивон так за лето подкачался!"
    pasha "Дарова, Саня, как сам, как жизнь? Целое лето тебя не видел же!"
    sanya "Паша, а я тебя и не узнал сперва, Накачался за лето я вижу!"
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

    scene lecture scen 
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
    "Справа от меня сидит миловидная особа в весьма открытой одежде. Похоже, не одному мне душно с этой лекции."

    show yuli greeting at right 
    with dissolve 

    "Ой, похоже, она заметила, что я пялюсь на неё..."
    "Девушка справа" "Приветики, куда смотришь?"
    sanya "До этого играл с лектором в гляделки, но боюсь, что он играет не по правилам, так что начал искать себе соперника на равных. Вот, наткнулся на тебя..."
    "Бог ты мой, насколько же это была плохая и несуразная шут..."

    show yuli horny at right 
    with dissolve

    "О боже, она посмеялась. ей понравилась моя дурацкая шутка!"
    "Я на высоте!! Надо давить дальше!"
    sanya "А меня Саша зовут!"
    yuli "А меня Юля, очень приятно познакомиться! Ах-хах"

    show yuli happy at right 
    with dissolve

    sanya "Юля, ты перевелась откуда-то? Я почему-то тебя раньше никогда не видел!"

    show yuli happy at center 
    with move

    yuli "(шёпотом) А потому что на лекции надо чаще ходить, я тебя тоже за целый год ни разу не видела!"
    "Тут она права, я вообще на эту лекцию по схемотехнике попал лишь потому что где-то надо было дождаться Пашу, у него-то, видите ли, пра-а-актика, надо прийти-и-и!"

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

    "Ну что же поделать, раз такая красивая мадам будоражит мои нейроны прямо сейчас! Повезло ещё, что я в этот самый момент не решил сказать слово \"ХУЙ!\""
    
    show yuli sad at center 
    with move

    sanya "(уже шёпотом) Согласен... Особенно сильно раздражает, когда по этим бесполезным предметам, как, например, этот, нужно потом ещё и полноценный экзамен сдавать, билеты к нему учить и чего похуже."
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
    "В эту минуту я осмотрел всю аудиторию. Вокруг меня были одни девушки... О нет, кажется, я перепутал кабинеты... И теперь вместо бесполезной схемотехники я сижу... Я сижу в компании приятных дам! Что за день!"

    show yuli sad at center  
    with dissolve

    yuli "Ты что, перепутал лекторные? Бедняжка..."
    "Какие ещё лекторные, правильно же лектории! Тебе бы точно не помешало послушать про лингвистические уче..."
    "Ох... Она назвала меня бедняжкой... Мне кажется, что я таю..."
    "Её взгляд такой сочувствующий, видно, что она не пытается мне сочувствовать, а именно это и делает!"
    "Сейчас она мне кажется милой до безобразия."
    extend " Такая естественная и простая."
    "Одевается вызывающе, но при этом такая стеснительная..."

    show yuli disappointed at left
    with dissolve

    "Ой, сколько времени я уже молча просто пялюсь на неё? Надо срочно что-то сказать!!"
    sanya "У тебя лямки майки слезли, но я вижу, (шёпотом) как выступает ещё и вторая линия обороны!"

    show yuli shy at center 
    with dissolve

    yuli "(шёпотом) Что ты такое говоришь, дурачок?"
    sanya "(шёпотом) До этого мне казалось, что я сижу на самом бесполезном для меня предмете, но теперь я понимаю, насколько же я ошибался."
    yuli "Я тоже совсем не понимаю, что я тут забыла-то?"
    "Разговор, кажется, заходит в тупик. Нельзя же вечно обсуждать скукоту лекции, иначе это свойство перейдёт и на сам диалог!"
    sanya "Юля, а ты чем любишь заниматься обычно?"

    show yuli horny at center 
    with move

    yuli "Не знаю, чем я люблю заниматься обычно, но после этой пары я свободна на все четыре стороны!"

    sanya "Ого, какой темперамент!"
    "Я за эти 10 минут на лекции по лингвистике уже такие слова, как темперамент начал использовать? А что, весьма продуктивно!"
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

    show yuli horny at center 
    with move

    "*Юля легко проводит рукой по моему подбородку, поворачивая голову в сторону преподавателя*"

    "Преподаватель" "Молодой человек, ну наконец-то! Попрошу Вас немедленно покинуть лекционный зал! "
    "Я было оторопел от такой наглости со стороны преподавателя, что начал даже собирать свои вещи, как тут меня взяла за руку Юля и обратилась ко мне"
    yuli "Саша, я тоже уже устала от этой душной лекции, хочешь, мы сейчас же вместе куда-нибудь сходим вместо неё? Время с тобой мне ведь явно понравится больше..."
    "Согласиться погулять с Юлей, значит кинуть Пашу с пивом, а ведь я уже договорился с ним, будет некрасиво так поступить."
    "С другой стороны, сколько я уже пил с Пашей, а с девочкой погулять не приходилось уже очень давно..."

    menu :
        "Согласиться" :
            
            $ str_for_notification = "Юля запомнила это"
                
            show screen notification_popup 
            with dissolve
            
            sanya "Юля, да я же с радостью! Собирайся, мы уходим!"
            "Тут я заметил, что Юле и собираться не из чего, просто встала и пошла за мной!"
            $ day1_pasha_kfc = False

        "Отказаться" :

            $ str_for_notification = "Юля запомнила это"
                
            show screen notification_popup 
            with dissolve

            sanya "Юля, давай погуляем завтра, я сегодня никак не могу – с другом уже договорился встретиться! Мы с ним тысячу лет не виделись!"
            sanya "Ты знаешь, что сделай, напиши мне свой ник в телеграме, я тебе сегодня вечером ещё напишу обязательно!"
            $ day1_pasha_kfc = True

    hide screen notification_popup
    with dissolve


    if day1_pasha_kfc :

        hide yuli happy
        scene nstu enter 
        with fade

        "Наконец-то лекция закончилась..."
        extend " Как обычно она была душной, зато на ней я познакомился с прекрасной Юлей"

        show pasha neutral 
        with dissolve

        "У входа я сразу встретил Пашку, который уже ждал меня."
        pasha "Ну чё, [sanya], погнали в кефас?"

        hide pasha neutral 
        with dissolve
        scene black scen 
        with fade

        $ renpy.pause(1.0)

        "Вспомнив про намеченные планы, я согласился, и в скором времени мы уже были на месте."

        play music "audio/kfc-sound.mp3" volume 0.5

        scene kfc inside 
        with fade

        "Зайдя внутрь, мне в нос сразу же ударил сладкий запах курочки, мы с Пашей переглянулись и быстро пошли заказывать."
        "Людей было не так много, хотя, казалось бы, вечер – час-пик!"

        show pasha neutral 
        with dissolve

        pasha "Слушай, ты уже записался на дополнительную физру? У нас в зале ещё есть свободные места."
        sanya "Я даже не думал об этом, всё, что я выбирал до этого, было полной хернёй, - занятия скучные, а преподы - мудаки"
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

        if _return == "pasha":
            $ day1_pasha_lose_in_drinking = False
        elif _return == "sanya":
            $ day1_pasha_lose_in_drinking = True
            
        play music "audio/street-sound.mp3" volume 0.5

        scene black scen 
        with fade

        $ renpy.pause(2.0)

        scene kfc outside 
        with fade

        show pasha neutral 
        with dissolve

        "Знатно накидавшись, мы вышли из кефаса и решили перекурить."

        show pasha giggles
        with dissolve

        pasha "После вкусного обеда по закону Архимеда, чтобы жиром не заплыть, нужно срочно покурить!"
        sanya "А ты не подкинешь сигаретки?"

        show pasha smiles 
        with dissolve

        pasha "Конечно, братка, держи."
        "После пары затягов у меня сдавило горло и сразу захотелось блевать."
        sanya "Ебаный винстон синий, блядь!!"

        "Мы с Пашком так много выпили, а я ещё даже и не думал рассказать ему о моём знакомстве с Юлькой."
        "Да просто все мысли были о том, как же я"
        if day1_pasha_lose_in_drinking :
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
        sanya "Её Юля зовут, очень красивое имя даже! Мы с ней совсем недолго проболтали, а потом меня препод по беспределу выгонять начал. Видите ли, я шумлю тут!"
        sanya "Ну она мне и предложила прогуляться вместо пары, но я-то знаю, что тёлок много, а друзей не выбирают! Сразу вспомнил, что на сегодня я занят. Ну и я вежливо ей..."

        show pasha angry 
        with dissolve

        pasha "ТАК, не понял, то-есть ты познакомился с симпо́тной девочкой, она позвала тебя сразу же гулять, а ты, такой дурной, решил вместо этого пойти пить пиво со мной?"
        sanya "Паш, мы же с тобой раньше договорились..."

        show pasha sad
        with dissolve

        pasha "Да ты совсем дурак? Тебе золото с неба упало, а ты что-то про договорились мне тут талдычишь!"
        sanya "Ну я взял её номер, сказал завтра ещё погуляем..."
        pasha "А ну! Пиши ей прямо щас, говори что передумал, что ты мужик и хочешь видеть её!"
        sanya "Паша, ну я ж ..."
        extend " ну я ж того ... в зюзю!"

        show pasha angry
        with dissolve

        pasha "Пи-ши я те-бе ска-зал!"
        "Последняя трезвая частичка меня просто кричит, что это всё не к добру..."
        "Я достал телефон, нашёл её контакт и написал ей следующее, считай, любовное послание:"
        
        image message_yuli_background = "message yuli background.png"
        image message_yuli_messages = "message yuli messages.png"
        stop music

        window hide

        $ sms_show(_("Юлолия"), True)
        with dissolve

        sms_c "Сегодня"

        sms_r "поивет юлтчка!!!"

        sms_r "{image=emoji rofl}"

        sms_r "п мы можкм с тобой скйчас прямо встетитсья?б"

        sms_r "{image=emoji sweat}"

        sms_r "посто я очень ну хряу тебя видеть!"

        sms_r "мяу)"
        $ sms_hide()

        with dissolve

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

        with dissolve
        show pasha angry
        with dissolve

        pasha "Ну и чего ты ждёшь? Беги к ней обниматься-целоваться!"

        menu :
            "Согласиться" :
                show screen notification_popup 
                with dissolve
                $ mood_counter += 1;
                pasha "Саня, Саня, не теряй такие возможности! Я тоже уже как раз до хаты собираюсь. Давай, расскажешь завтра, как оно там!"
                $ day1_yuli_agreed_after_kfc = True
            "Отказаться" :
                show screen notification_popup 
                with dissolve
                $ mood_counter -= 1;
                sanya "Паша, да... Мне уже в любом случае пора бы домой идти. Если случайно встретимся, то встретимся, если нет, то не суждено значит."
                $ day1_yuli_agreed_after_kfc = False

        hide screen notification_popup
        with dissolve

        if day1_yuli_agreed_after_kfc :

            scene black scen
            with fade
            play music "audio/love_music.mp3" fadein 4.5 volume 0.4 fadeout 5.5
            scene bridge
            with fade

            
            show yuli greeting
            with dissolve

            storyteller "Саня нервно пробирался к набережной, надеясь, что не споткнется о собственные ноги. Он был еще немного пьян от выпитого с Пашей. Однако он был рад встрече с Юлей."

            storyteller "Когда он увидел ее, она стояла у перил и смотрела на воду. Саня подошел к ней, и она повернулась, чтобы поприветствовать его улыбкой."

            yuli "Привет, Саша! Очень рада наконец-то с тобой познакомиться"

            sanya "Привет, Юля. Я тоже рад тебя видеть"

            "Вау, она выглядит еще красивее, чем я помнил"
            show yuli wet disappointed 
            with dissolve
            yuli "На улице идет сильный дождь, но я подумала, что мы все равно можем прогуляться по мосту"

            sanya "Конечно, звучит неплохо"

            yuli "Итак, что ты думаешь о сегодняшней лекции?"

            sanya "Если честно, я не особо обращал внимание. Я был слишком занят разговором с тобой"

            show yuli wet neutral 
            with dissolve
            yuli "Ха-ха, ну надеюсь, я не сильно тебя отвлекала"

            "С ней так легко разговаривать. Такое чувство, что мы давно знакомы"

            storyteller "Пока они шли по мосту, Саня и Юля болтали о своих интересах и увлечениях. Они обнаружили, что у них много общего, и вскоре дождь прекратился, и солнце выглянуло из-за туч."

            yuli "Ну что, Саша, не хочешь перекусить где-нибудь?"

            sanya "Да, звучит здорово. Тут неподалеку есть очень милое кафе"
            scene black scen
            with Fade(2.0, 0.0, 1.0)
            
            "Я не могу поверить, как хорошо все идет. Она потрясающая. Кажется, она мне действительно нравится"
            image foreground_cafe = "foreground cafe.png"

            scene background cafe
            show yuli happy:
                xalign 0.7
                yalign 0.5
                zoom 0.77
            show foreground_cafe
            show black
            hide black  with Fade(2.0, 0.0, 2.0)
            
           
            
            play sound "audio/kfc-sound.mp3" volume 0.1
            

            storyteller "Пока они сидели в уютном кафе, наслаждаясь едой и компанией друг друга, Саня чувствовал себя на вершине мира. Он не мог поверить, как ему повезло, что он встретил такую девушку, как Юля."
            show yuli horny2 with dissolve:
                xalign 0.7
                yalign 0.5
                zoom 0.77
            yuli "Саша, я сегодня отлично провела время. Спасибо, что вышел ко мне под дождь"

            sanya "Нет, это тебе спасибо, Юля. Я тоже прекрасно провел время. Мы обязательно должны повторить это как-нибудь"
            show yuli horny with dissolve:
                xalign 0.7
                yalign 0.5
                zoom 0.77
            yuli "С удовольствием"

            "Не могу дождаться, когда увижу её вновь. Это начало чего-то особенного"
            hide yuli happy with dissolve
            hide foreground_cafe
            scene black scen
            with fade
            stop sound

        else :
            play music "audio/slow_sad_classical_music.mp3"  fadein 4.5 volume 0.4 fadeout 5.5
            scene black scen
            with fade
            "Я действительно не хотел встречи с Юлей, поэтому решил пробираться через закрытый мост."
            "Юля ждала меня совсем в другом месте. Скажу ей, что просто передумал встречаться, или побоялся, что слишком пьян..."
            "Прогуливаясь по ночным улочкам, я дошёл до моста. Передо мной воцарилась та самая, уже классическая надпись:"

            scene bridge
            with fade

            "Мост временно закрыт для пеших прогулок, приносим свои извинения"
            "Это временное закрытие длиться уже буквально год! Дыра справа от надписи как бы намекает, что мост закрыт только на словах."
            "Пробравшись через дырку на карачках, по ту сторону я увидел Юлю. Она меня сразу заметила и приветливо улыбнулась мне."

            show yuli greeting
            with dissolve

            yuli "О, ты пришёл! Так быстро!"
            sanya "Да, Юля, привет..."

            "Я же не хотел её видеть, как так получилось? Специально же пошёл через закрытый мост..."

            sanya "Набережная большая, Юля, а ты... такая маленькая на её фоне"

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

            "Мы стояли молча, смотрели на темную воду и отражающиеся на ее поверхности огни."

            sanya "Юля, извини, если я что-то не так сказал. Я не хотел тебя напугать или еще что-то."

            yuli "Все нормально, Саша. Я просто немного нервничаю. Я не привыкла к таким вещам."

            sanya "К чему?"

            yuli "Ну, знаешь, знакомиться с кем-то новым. Идти куда-то ночью. Это не то, что я часто делаю."

            sanya "Понятно. Ну, мы можем не оставаться здесь, если ты не хочешь."

            yuli "Нет, все в порядке. Я рада, что вырвалась из своей зоны комфорта. Приятно, что мне есть с кем поговорить."

            "Мы поговорили еще немного, о школе, о наших интересах, о наших семьях. Это было приятно, но было заметно, что Юля не интересуется мной в романтическом плане."

            scene black scen
            with fade

            "В конце концов, мы попрощались, и я пошел домой один. Это была грустная прогулка, но, по крайней мере, у меня появился новый друг."

    else :

        "Мы молча встали и вышли из лекторной."

        play music "audio/strauss-festival.mp3" fadein 4.5 volume 0.1 fadeout 1.5

        hide yuli happy

        scene nstu enter 
        with fade

        "На улице в этот самый момент как раз показался красивый закат, поэтому мы решили прогуляться в сторону набережной."

        scene black scen
        with fade

        "Мы говорили обо всём на свете: об учёбе, о семье, о людях, что нас окружают."
        "С ней я забыл свои многочисленные проблемы."

        scene rain yuli
        with fade

        show yuli neutral
        with dissolve
        
        "Она подошла к забору и молча смотрела на правый берег."
        yuli "Саша, здесь так красиво..."
        
        stop music

        play music "audio/stop_breaths.mp3" fadein 1.5 volume 0.5
        "Я перестаю дышать..."
        stop music fadeout 2.0

        play music "audio/strauss-festival.mp3" fadein 4.5 volume 0.1 fadeout 1.5

        sanya "Мне тоже очень нравится."

        show yuli horny
        with dissolve

        yuli "Обнимемся?"
        storyteller "Саня на мгновение замешкался, испытывая чувство вины за то, что он так плохо поступил по отношению к Паше."
        storyteller "Но, в то же время, он не мог устоять перед соблазном провести больше времени с Юлей."
        storyteller "Он наклонился и крепко обнял ее."
        sanya "Конечно, давай обнимемся."
        
        hide yuli horny

        scene bridge
        with fade

        storyteller "Пока они шли по мосту, Саня не мог отделаться от ощущения кома в горле. Он понимал, что неправильно обошёлся с товарищем."
        storyteller "Но компания Юли была так приятна, что он отогнал эту мысль на задворки сознания."
        storyteller "Когда они дошли до середины моста, Саня увидел, что к ним приближается Паша. Он ощутил приступ вины и тревоги, когда понял, что его друг ждал его всё это время."
        
        show pasha angry at center
        with dissolve

        show yuli disappointed at right
        with dissolve

        pasha "Эй, мужик, что происходит? Я ждал тебя в кефасе больше часа!"
        sanya "А, привет, Паша. Извини, я что-то закрутился..."

        show yuli shy at right
        with dissolve

        "Юля смутилась и начала возиться с телефоном."

        hide pasha angry 
        with dissolve 

        yuli "Эм, мне, наверное, пора. Только что звонила мама, ей нужно, чтобы я скорее возвращалась домой."

        hide yuli shy 
        with dissolve

        stop music fadeout 3.0

        show pasha angry 
        with dissolve

        storyteller "Саня был разочарован тем, что их свидание оборвалось, но в то же время он почувствовал облегчение от того, что ему не придется встречаться с неодобрительным взглядом Паши."
        sanya "Хорошо, хорошо. Я был рад встретиться с тобой, Юля."

        hide pasha angry

        scene black scen
        with fade

        storyteller "Когда они шли обратно к университету, Саня не мог отделаться от чувства вины за то, что только что произошло."
        storyteller "Он понимал, что подвел друга и совершил ошибку, решив пойти на свидание с Юлей вместо того, чтобы встретиться с Пашей."

        scene nstu night 
        with fade

        show pasha sad at center
        with dissolve

        play music "audio/einaudi_nefeli.mp3" fadein 2.0 fadeout 2.0 volume 0.2
        pasha "Знаешь, Саня, я думал, что мы друзья. Но, похоже, ты не ценишь нашу дружбу так, как я."
        sanya "Да нет же, Паша, всё не так. Извини, я просто увлёкся делами..."
        pasha "Да какая разница. Я не хочу больше об этом говорить. Просто не делай так больше."

        hide pasha angry
        with dissolve

        pause (2.0)

        storyteller "С этими словами Паша ушел, оставив Саню стоять одного на улице. Саня понимал, что совершил ошибку, но он также знал, что не может вернуть то, что уже произошло."
        storyteller "Он поклялся как-нибудь загладить свою вину перед Пашей и больше никогда не предавать доверие друга."
        "После всех мыслей, я не нашел ничего лучше, чем поехать домой."

        scene black scen 
        with fade

        pause 2.0
    if not day1_pasha_kfc:
        play sound "audio/sound-in-bus.mp3" volume 0.1

        scene bus night
        show night

        "Как обычно, по пути домой я глубоко погрузился в себя. Мои мысли перескакивали со скучных лекций и лаб на Пашку, на новую подругу Юлю и обратно."
        
        stop sound
        play sound "audio/bus.mp3" volume 0.1

        $ renpy.pause(7.0)

        stop sound
        play music "audio/home-sad.mp3" volume 0.2

        scene sanya cry
        with fade

        # звук открытия двери и ходьбы
        "Открыв дверь домой, я первым делом пошёл к окну."
        sanya "За столько лет я так и не смог бросить"
        "Достав последнюю сигаретку из пачки ванильного чапмана, я пару раз затянулся."
        sanya "Фух, сразу полегчало. На днях надо будет купить ещё пару пачек в кб"
        "Странный день вышел сегодня. Кажется, какое решение я бы не принял, всё пошло бы всё равно через жопу..."
        
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
        "Но даже с Юлей я не мог избавиться от чувства пустоты, которое преследовало меня уже долгое время. Может быть, дело было во мне, может быть, это я изменился. А может, это мир вокруг меня потерял свои краски."
        "Я тупо уставился в потолок, мои мысли бесцельно блуждали. В чем был смысл всего этого? Почему я вообще здесь оказался?"
        "Я знал, что должен вырваться из этого состояния, но это было легче сказать, чем сделать. Груз моей собственной печали, казалось, раздавил меня, задушил."
        "Так я и лежал, погруженный в свои мысли, пока, наконец, усталость не взяла верх и я не погрузился в беспокойный сон, надеясь, что завтра наступит какое-то облегчение."
    else:
        "Когда я лежал в постели той ночью, я не мог не думать о Юле. Она была умной, красивой и доброй. Но я знал, что между нами никогда ничего не будет."
        "Я уснул с тяжелым сердцем, зная, что никогда не найду любовь."

    stop music fadeout 3.0

    show black with Fade(3.0, 0.0, 2.0)

    jump second_day

label second_day :

    pause 3.0
    hide white
    with fade

    "И опять же... Я проснулся с ощущением тяжкого груза на сердце."
    "Господи, какой же срач. Как вообще отыскать здесь то, что мне нужно?"
    play music "audio/space-floating.mp3" fadein 2.5 loop fadeout 3.0 volume 0.1
    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("sanya room", 8,
        ("backpack", 1613, 630, _("Рюкзак РЕДАН")),
        ("light", 111, 800, _("Зажигалка")),
        ("marlboro1", 630, 660, _("Пачка сигарет (пустая)")),
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
        hover=brightness(.1),
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve

    centered "{size=+24}Найдите все предметы за 8 секунд.\nНажмите ЛКМ, чтобы начать."
    window hide
    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)
    play music "audio/einaudi_nefeli.mp3" fadein 1.0 fadeout 2.0 volume 0.2
    # результаты
    if hf_return == 0:
        centered "{size=+24}Предметы собраны успешно.\n Но все пачки пусты.."
    else:
        if hf_return == 1:
            centered "{size=+24}GAME OVER\nНе нашёлся 1 предмет."
        else:
            centered "{size=+24}GAME OVER\nНе нашлось [hf_return] предмета(-ов)"

    $ hf_hide()
    with dissolve

    "Вот дерьмо..."
    "Единственное, что мне нужно прямо сейчас, - это чапа."
    extend " Только сигарета поможет мне забыться."
    
    
    scene sanya cry
    with fade

    "Подойдя к окну, я достал уже изрядно потрепанную пачку сигарет, но единственное, что я в ней нашел, - это затхлый запах табака."
    "Пиздец... День только начался, а я уже лишился самого важного."
    "Придется сходить в кб за сигами. Ведь говорил же себе вчера купить пару пачек, но все равно забыл."

    scene black scen
    with fade

    play music "audio/street-sound.mp3" fadein 2.0 fadeout 2.0 volume 0.2

    pause 4.0

    scene red white
    with fade

    "Наконец-то купил сиги. Жизнь продолжается."
    "Итак, раз уж я решил ехать в санаторий, то лучше бы не затягивать со всем этим бюрократическим адом и собрать все документы за раз."
    "-Примечание: перед тем, как Вы отправитесь в наш великолепный санаторий, вам нужно принести следующие документы: "
    "Копию паспорта, свидетельство о рождении, книжку со всеми проставленными прививками...-"    
    sanya "Ебись оно все в рот!"
    "Выписка из ЕГРН, 2-НДФЛ, 3-НДФЛ... бла-бла-бла... Справка о целостности заднего прохода..."
    extend " Так, стоп, а это им для чего?"
    "Выбора у меня всё равно нет. Нужно развеяться, сменить обстановку. Иначе я могу просто не выдержать..."
    "Придется ехать в универ."

    scene bus station
    with fade

    "Снова эта убитая и дряхлая остановка. Быть может, ещё в совке она выглядела нормально, но сейчас..."
    extend " Это просто пиздец."

    scene black scen 
    with fade
 
    play sound "audio/bus.mp3" fadein 0.5 fadeout 1.5 volume 0.1

    pause 7.0

    stop sound

    scene bus 
    with fade

    play music "audio/sound-in-bus.mp3" fadein 1.5 fadeout 2.5 volume 0.1

    "Этот автобус вообще меняется? Хотя да... С каждым годом он всё хуже и хуже"
    "Проезжая мимо старых домов и разбитых дорог, я поймал себя на мысли, что мой город либо статичен в своём развитии, либо я уже перестал видеть краски жизни..."
    "После этих мыслей я начал погружаться в сон"

    call play_bus from _call_play_bus
    

    stop music
    
    scene black scen
    with fade

    "Ох, блядь! Чуть не проспал свою же остановку."

    play sound "audio/bus.mp3" fadein 0.5 fadeout 1.5 volume 0.1

    pause 7.0

    stop sound

    scene bus station near nstu
    with fade
    show pasha neutral
    with dissolve

    play sound "audio/street-sound.mp3" loop volume 0.2
    "Первое, что я увидел, когда вышел из автобуса, - это огромную фигуру Паши. Да его и сложно не заметить..."
    sanya "Паша! Привет. Я хотел тебе кое-что сказать..."

    if day1_pasha_kfc :
        "Паша быстро меня заметил и подошел ко мне"

        show pasha smiles
        with dissolve

        pasha "Санек, привет. Как поспал? Хотя... Можешь не отвечать. Как всегда херово, я знаю."
        sanya "Да, бошка трещала не по-детски."
        sanya  "Мне вчера письмо пришло с приглашением в санаторий. Я тут подумал и решил, что стоило бы съездить, подлечиться..."
        pasha  "О, Саня, тебе это сейчас больше всего, можно сказать, не хватает."
        pasha "Я конечно, с тобой туда ни ногой, ты меня знаешь, я и так здоров как бык. Но за тебя пальчики мы с ребятами скрестим!"
        
    else :

        sanya "Извини меня за вчерашнее... Я совсем замотался. Вылетело из головы."
        pasha "Не парься. Я ещё вчера сказал, что больше это обсуждать не хочу. Просто забей. Но я надеюсь ты понимаешь, что так лучше больше не делать!"

        show pasha smiles
        with dissolve

        pasha "А ещё, ты мне за это теперь пива торчишь!"
        extend " И минимум три литра бада!"

        pasha "Ладно, ты сам как вообще?"
        sanya "Как и всегда. Абсолютно хуево."
        sanya "Кстати, тебе вчера не приходило письмо с приглашением в санаторий?"

        show pasha neutral
        with dissolve

        pasha "Может и приходило. Ты же знаешь, что я весь спам от универа даже не читаю. Тем более про санатории, которые каждый год предлагают."
        sanya "Бесплатно же. Чего бы не скататься. Так ещё можно родакам сказать, что универ не оплачивает поездку. Денег получить."
        pasha "Бесплатный сыр только в мышеловке, запомни!"

        show pasha giggles
        with dissolve

        pasha "Они тебе, может, там вообще зонд в жопу запихнут, пока ты спать будешь!"
        "А-а-а, так вот для чего им справка о целостности ануса нужна..."
        sanya "Не хочешь со мной съездить? Бухла купим, будем по вечерам пить."
        "Если и ломать целостность ануса, то хотя бы не одному!"

        show pasha sad
        with dissolve

        pasha "Извини, но желания ехать в этот старый санаторий у меня нет."
        pasha "Но ты, как вернёшься, расскажи, как там оно проходит."
        pasha "Если там правда могут поставить на ноги, то в следующем году уже вместе можем и поехать!"

        show pasha smiles
        with dissolve

        pasha "Ладно, Санёк, был рад повидаться! Мне на пары пора"

        hide pasha smiles
        with dissolve

    
    if not day1_yuli_agreed_after_kfc and day1_pasha_kfc :

        pasha "Кстати, а как там с девочкой твоей дела обстоят?"
        image night = "night color.png"
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
        sanya "Паша, помнишь, когда я написал Юле и пошел к ней?"

        show pasha neutral
        with dissolve

        pasha "Да, не думай, что я от бухла сразу память теряю!"
        sanya "Ладно-ладно. Так вот, мы с ней встретились и поболтали. Этот разговор я точно запомню надолго..."
        sanya "Я подошел к набережной. Мы решили прогуляться."
        sanya "Мы очень славно гуляли, я даже подумывал уже взять её за ручку"
        sanya "Через некоторое время ей набрала мама и позвала домой"
        sanya "Я проводил её до лифта и обнял, мы попрощались, и она сказала, что этот день ей представлялся очередным скучным деньком, который я скрасил своим появлением!"
        sanya "У меня чуть сердце не взорвалось от таких речей..."

        show pasha smiles 
        with dissolve

        pasha "Ах ты ж красавец то! а! Всё правильно сделал. Идеальнее некуда."
        pasha "Видишь же? Не зря я тебя заставил ей написать. Радуйся, что у тебя такой друг есть."
        pasha "Напомню ещё раз: \"Когда будешь летать, не забывай с кем ползал!\""

        show pasha neutral
        with dissolve

        pasha "Так, ладно, мне уже пара идти на пару. А ты, как я понял, только за документами в универ приехал?"
        sanya "Ну, да"
        pasha "Удачи тебе тогда, Саня! И в санатории приятно отдохнуть. Я тебе ещё вечером напишу, мемов в телеграм накидаю!"
        pasha "Увидимся через неделю, значит? На этом же месте?"
        sanya "Верно, верно, на этом же месте, ровно через неделю!"

        hide pasha neutral 
        with dissolve
    
        "Всё-таки хорошо, что я смог увидеть Пашу. Теперь как-то даже веселее. Пора идти в универ..."

    scene black scen 
    with fade

    "Распрощавшись с Пашкой, я направился прямиком в деканат. Желания возиться с документами у меня не было совсем."
    sanya "Ненавижу, блядь, бюрократию..."
    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene nstu que
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
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("nstu que", 8,
        ("a1", 413, 730, _("1-НДФЛ")),
        ("a2", 918, 930, _("2-НДФЛ")),
        ("a3", 630, 660, _("3-НДФЛ")),
        ("a4", 413, 850, _("Справка об усыновлении")),
        ("a5", 555, 900, _("Справка о целостности ануса")),
        ("a6", 990, 661, _("Скан паспорта")),
        ("a7", 733, 844, _("Скан свидетельства о рождении")),
        ("a8", 900, 730, _("Направление на анализы кала")),
        ("a9", 885, 644, _("Справка об отсутствии судимостей")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
        # включаем смену курсора при наведении
        mouse=True,
        # включаем инвентарь с убиранием из него найденных предметов
        inventory=True,
        # включаем подсказки
        hint=False,
        # включаем подсветку предмета при наведении
        hover=brightness(.17),
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve

    centered "{size=+24}Найдите расскиданные справки за 20 секунд.\nНажмите ЛКМ, чтобы начать."

    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)

    # результаты
    if hf_return == 0:
        centered "{size=+24}Все справки собраны!"
        $ hf_hide()
        with dissolve
        "Фух, теперь можно со спокойной душой заходить в кабинет..."
    else:
        if hf_return == 1:
            centered "{size=+24}GAME OVER\nНе нашлась одна справка..."
        else:
            centered "{size=+24}GAME OVER\nНе нашлось [hf_return] справки(-ок)"
        "Ай, да и чёрт с ним, может и так примут, кто вообще эти документы смотреть-то будет?"
        "Идиотская бумажная волокита!"
    scene black with fade
    stop music fadeout 3.0

    stop sound fadeout 0.5
    "Уже вечерело, времени ушло куда больше, чем я ожидал. У выхода из корпуса я заметил несколько одногруппников, по разговору было понятно, что они направляются в курилку."
    "Может тоже сходить?"

    menu :

        "Пойти в курилку" :
            $ str_for_notification = "У этого действия будут последствия"

            show screen notification_popup_big
            with dissolve

            $ day2_sanya_went_to_smoke = True
        "Забить и покурить дома" :
            $ str_for_notification = "У этого действия будут последствия"

            show screen notification_popup_big
            with dissolve

            $ day2_sanya_went_to_smoke = False

    hide screen notification_popup_big
    with dissolve

    if day2_sanya_went_to_smoke :
        scene black scen 
        with fade

        "Поприветствовав одногруппников, я с ними направился в сторону курилки."

        play music "audio/street-sound.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene kyrilka
        with fade

        "Одногруппник" "Как же бесит препод по схемотехнике, мы с ним только первый день, а он уже показал себя полным мудаком."
        "Одногруппник" "Да уж, он точно будет валить на сессии. Кстати, Саня, тебя вроде не было на лекции."
        sanya "Да я проебался немного, пришёл не на свою лекцию."
        "Потянувшись за пачкой сигарет, неожиданно для себя я её не обнаружил."
        "Порывшись получше в рюкзаке я пришел только к одному выводу: я ..."
        extend " должен стрельнуть сигу."
        sanya "Слушайте, а у вас сигаретки не будет? Видимо свои я где-то посеял."
        "Стоявший справа от меня парень с неодобрительным взглядом протянул мне сижку шоколадного чапмана. Сделав пару затягов, мне приятно ударило по горлу, а никотин немного меня расслабил."
        "Парни в основном обсуждали прошедшую лекцию и подходящую лабораторную по электротехнике."
        "По их словам препод требовательный, но справедливый. На практиках он часто смеется со студентов, которые ничего не понимают, но тем не менее старается понятно донести материал."
        "Одногруппник" "Бля, недавно видел статью про СССР, как же  тогда хреново было, не то что сейчас. Вы как вообще к нему относитесь?"
        "Мне так нравится СССР, на самом деле... Но что-то мне подсказывает, что эти ребята явно негативно настроены..."
        "Все посмотрели на меня. Они ждут моего мнения по этому поводу? Надо что-то сказать..."

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
            sanya "Честно говоря, мне кажется что в СССР было лучше, чем сейчас. Жизнь была проще, люди добродушнее..."
            "Сказав это, я заметил на себе неодобрительные взгляды одногруппников."
            "Одногруппник" "Пхахаха, ты что, в атомик харт переиграл, доходяга? Давай-ка мы национализируем твои денюжки, пионер."
            "Они накинулись на меня толпой, противостоять им я никак не мог."
            "Кое-как отбрыкавшись, я направился в сторону универа."
            "Состояние у меня было хуже некуда, хотелось просто уйти как можно дальше от этого мира."
            "Не ожидал я от них такого, да и что плохого в СССР? Чего только стоит советское мороженое."
            "После этих унижений, я уже не хотел курить. Я выкинул сигарету. Хотел плакать. Хотел заорать на всю улицу, но сдержался."

            scene black scen
            with fade

            "У выхода из корпуса я заметил Юлю, смотрящую в мою сторону. Она подбежала ко мне, явно заметив моё паршивое настроение."

            scene nstu enter
            with fade
            show yuli afraid
            with dissolve

            play music "audio/keys-of-moon-a-little-fantasy.mp3" fadein 3.5 fadeout 2.5 volume 0.1

            yuli "Саша, что с тобой случилось? Выглядишь ужасно подавленным."
            sanya "Да так, ничего серьезного, день с самого утра не задался, не стоит так беспокоится."
            show yuli happy
            with dissolve
            yuli "Ну, раз ты так говоришь... Главное помни, что ты всегда можешь ко мне обратиться."

            

            yuli "Пойдем, я провожу тебя до дома, может тебе полегчает в моей компании."
            sanya "Пойдем, конечно."

            hide yuli happy
            scene black scen
            with fade

            "Как же приятно идти по улице в компании такой красивой и весёлой девушки..."
            yuli "Сань, может у тебя всё-таки что-то случилось?"
            sanya "Нет, всё в порядке, Юля. Ты лучше расскажи, как у тебя дела."
            "Поболтав немного, я решил предложить зайти за сигаретами. Свои новенькие я уже успешно проебал."

            scene red white
            with fade

            show yuli empathy
            with dissolve

            yuli "Я подожду тебя снаружи. Не люблю такие магазины..."
            sanya "Хорошо! Скоро буду."

            hide yuli empathy
            scene magazine inside
            with fade
            
            sanya "Можно, пожалуйста, пачку чапы ванильной."
            "Немного погодя, я добавил:"
            sanya "И два советских пломбира в вафельном стаканчике!"
            "Кассир" "Да, с вас..."

            scene red white
            with Fade(2.0, 0.0, 1.0)
            show yuli empathy
            with dissolve

            sanya "Ну всё, пойдем дальше. Мне что-то захотелось мороженого, я и тебе взял!"
            show yuli horny
            with dissolve
            yuli "Советское! Обожаю!"

            
            scene black scen
            with Fade(2.0, 0.0, 2.0)

            "Через пять минут мы уже были около моего дома."

            scene sanya home
            with fade
            show yuli shy
            with dissolve

            yuli "Ого! Я и не знала, что мы так близко живем!"
            yuli "Почему я тебя до этого ни разу не видела?"
            "Пока мы шли, я думал позвать её с собой в санаторий."
            "Конечно, знакомы мы не так долго, но с ней мне легко и приятно. Почему нет?.."
            "Жаль, правда, что Паша не захотел."
            sanya "Слушай, а ты не хочешь съездить со мной в санаторий на недельку?"
            "Чёрт, я же перебил её. Надеюсь не обидется."

            show yuli horny
            with dissolve

            yuli "Ура, мы поедем в санаторий, мы отлично проведем время вместе."
            "Она же, блядь, даже не успела подумать. Да и пофиг."
            sanya "Не хочешь ко мне зайти, можем посмотреть кино или чем-то ещё интересным заняться?"
            #"Учитывая, как она думает над своими действиями, мне может что-нибудь да перепасть."
            "Юля не успела ответить, у неё зазвонил телефон."

            show yuli horny2
            with dissolve

            yuli "Прости, Саш. Мама уже зовёт домой, сегодня не получится, поздновато."
            "Мы обнялись на прощание."
            sanya "Тогда завтра в 8:00 встретимся у университета."
            yuli "Конечно, буду ждать с нетерпением!"
            "Да... Снова не повезло."

            stop music fadeout 3.0

            hide yuli horny2
            show black scen
            with Fade(2.0, 0.0, 1.0)

        else:
            sanya "Согласен, сейчас жизнь куда лучше, ни то что в совке, посмотреть только на то, куда он нас привел, в кошмарную перестройку."

            "Одногруппник" "Да, ты прав, в то время был полный пиздец."
            "Одногруппник" "Слышали, недавно версию разработчиков атомик харт выпустили. Кто-нибудь уже играл?"
            "Одногруппник" "Да, там совок прямо таки восхваляется."

            "Докурив, мы попрощались друг с другом и разошлись. Я направился в сторону универа."

            "Может и зря я так отозвался о СССР... "
            "Говорят, там советское мороженное и квас в бочках были вкусными!"

            scene black scen
            with fade

            "У выхода из корпуса я заметил Юлю, смотрящую в мою сторону. Она подбежала ко мне явно заметив моё паршивое настроение."

            scene nstu enter
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
            scene black scen
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
            show black scen
            with fade

        $ day2_sanya_vote_for_ussr = True

    else :
        
        scene nstu enter
        with fade

        "Выйдя из корпуса я потянулся за пачкой сигарет, но тут же обнаружил, что её там нет."
        "Осмотрев все карманы рюкзака, сигарет я так и не нашёл. Видимо, где-то посеял. Придется заглянуть в кб на обратном пути."
        "А ведь только утром покупал. Может спиздил кто?"
        "Ладно, в этот раз пойду пешком до дома. Сэкономлю хотя бы на проезде."

        scene black scen
        with fade

        "Пройдя пару кварталов, я заметил вход в парк, который находится недалеко от моего дома. Чем не отличное место, чтобы привести мысли в порядок?"

        scene park
        with fade

        "Красивый парк. Но сначала стоит сбегать за сигами всё-таки."

        scene black scen
        with fade

        pause 3.0

        scene magazine inside
        with fade

        show nadya angry
        with dissolve

        "Благо уже вечер и в магазинах нет большой очереди. Передо мной стояла девушка, которая о чем-то спорила с кассиром. Я решил прислушаться к их разговору."

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
        scene red white
        with fade
        show nadya flirting
        with dissolve

        nadya "Слушай, не мог бы ты купить мне чапу ванильную? Я забыла паспорт, а кассир ни в какую не продаёт. Меня, если что, Надя зовут."

        menu :

            "Купить сиги." :
                $ str_for_notification = "Надя запомнила это"
                $ mood_counter += 1;
                show screen notification_popup
                with dissolve

                $ day2_nadya_bought_sigaretts = True

            "Ты же малолетка. Домой иди." :
                $ mood_counter -= 1;
                $ str_for_notification = "Надя запомнила это"

                show screen notification_popup
                with dissolve

                $ day2_nadya_bought_sigaretts = False

        hide screen notification_popup
        with dissolve

        if day2_nadya_bought_sigaretts :
            hide nadya flirting 
            with dissolve

            sanya "Ладно. Сейчас куплю тебе чапу."

            scene magazine inside
            with fade

            sanya "Добрый вечер, пару пачек ванильного чапман."
            "Кассир оценивающим взглядом оглядел меня с ног до головы."
            "Кассир" "Паспорт, пожалуйста."
            "Недолго думая, я показал его, на что он утвердительно кивнул и начал рыться за прилавком."
            "Оплатив покупку, я подошел  к девушке и протянул ей пачку."

            show nadya happy
            with dissolve

            nadya "Большое спасибо, ты меня правда спас. Кстати говоря, мне кажется мы уже где-то виделись."
            "Я попытался вспомнить где же я её видел, но ничего в голову так и не пришло."

            show nadya smiles
            with dissolve

            nadya "А-а, вспомнила, ты был вчера на лекции по лингвистики, тебя ещё препод выгнал."
            sanya "Да, было такое, не знаю чего он так взъелся на меня."
            nadya "Ха-ха, меньше кричать на всю аудиторию надо."
            sanya "Ты права, моя вина."
            nadya "Я хотела по парку прогуляться, составишь мне компанию?"
            sanya "Пойдем, мне всё равно нечем заняться."

            scene black scen
            with fade

            pause 3.0

            scene park
            with fade

        else :

            hide nadya flirting 
            with dissolve

            "Поразмыслив над просьбой девушки, я решил не покупать ей сигареты, выглядит она совсем молодо, может быть ей и 18-ти лет то нет."

            scene magazine inside
            with fade

            sanya "Добрый вечер, ванильный чапмен, пожалуйста."
            "Кассир оценивающим взглядом оглядел меня с ног до головы."
            "Кассир" "Паспорт гани."
            "Недолго думая, я показал его, на что он утвердительно кивнул и начал рыться за прилавком."
            "Оплатив покупку, я вышел на улицу. Девушки я там так и не увидел."
            sanya "Интересно куда она так неожиданно ушла."
            "Оставив размышления, я направился в сторону парка, где присел на ближайшую лавочку."

            scene park
            with fade

            "Достав сигаретку, я уже было потянулся в карман за зажигалкой, как какой-то незнакомец дал мне прикурить."
            "Разглядев появившийся передо мной силуэт, я заметил ту же девушку, которую видел в магазине."

            show nadya flirting
            with dissolve

            nadya "Парень, я тебя спасла, но в благородство играть не буду, дашь мне сижку и мы в расчёте."

            menu :

                "Стрельнуть сижку, оторвать её от своей души." :
                    $ str_for_notification = "Надя запомнила это"
                    $ mood_counter += 1;
                    show screen notification_popup_big
                    with dissolve
                    $ day2_nadya_het_one_sigarett = True

                "Обойдешься без сиги." :
                    $ str_for_notification = "Надя запомнила это"
                    $ mood_counter -= 1;
                    show screen notification_popup_big
                    with dissolve
                    $ day2_nadya_het_one_sigarett = False

            hide screen notification_popup
            with dissolve

            if day2_nadya_het_one_sigarett :

                "Недолго думая я достал ещё одну сигаретку и протянул милой даме."
                
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

        if day2_nadya_bought_sigaretts or day2_nadya_het_one_sigarett :
            
            $ day2_nadya_have_a_dialog = True
            show nadya handson 
            with dissolve

            nadya "Ну вот и отлично, как ты? Выглядишь уставшим."
            sanya "Да не волнуйся, просто замотался сегодня, лучше о себе расскажи."
            nadya "Честно и рассказывать то нечего, учусь в ... на гуманитарном факультете."
            sanya "Видимо, на лингвистической специальности?"
            nadya "Да, так и есть. Ты, я так понимаю, тоже? Мы вроде раньше не встречались, перевелся что-ли?"
            sanya "Нет, просто не на свою лекцию попал."

            show nadya laughs
            with dissolve

            nadya "Ну ты даешь, как так получилось-то?"
            sanya "Случайно как-то, я вообще друга ждал и решил заглянуть на лекцию."
            sanya "Слушай, а чем ты увлекаешься?"

            show nadya giggles
            with dissolve

            nadya "В свободное время читаю, люблю вышивать, время от времени я не прочь поиграть во что-нибудь."
            nadya "Ещё я часто гуляю и хожу по театрам."
            sanya "Ничего себе, я никогда не был в театрах, а поиграть и я люблю."

            show nadya flirting
            with dissolve

            nadya "Может тогда сходим как-нибудь?"

            "Я был бы не против составить ей компанию, но как тогда быть с Юлей?"

            menu :

                "Согласиться..." :
                    $ day2_choosen_instead_yuli = True
                    $ mood_counter += 1;
                    $ str_for_notification = "Надя запомнила это"

                    show screen notification_popup_big
                    with dissolve

                    sanya "Конечно, я буду только рад составить тебе компанию."

                    show nadya smiles
                    with dissolve

                    nadya "Отлично, тогда решим на днях, когда пойдем."

                    "Мы продолжили разговаривать на различные темы, пока у Нади не зазвонил телефон."

                    nadya "Прости, мне уже пора, добавишь меня в телеграме?"
                    sanya "Да, конечно."
                    nadya "Класс, мой номер: ..."
                    nadya "Ладно, мне пора идти. Ещё увидимся."

                    show nadya flirting
                    with dissolve

                    "Неожиданно она крепко стиснула меня в своих объятиях."

                    hide nadya flirting
                    with dissolve

                    "На такой приятной ноте прервалось наше знакомство. Уже было достаточно поздно, поэтому недолго думая я решил отправиться прямиком к своему дому."

                "Нейтральный ответ" :
                    $ day2_choosen_instead_yuli = False
                    $ mood_counter -= 1;
                    $ str_for_notification = "Надя запомнила это"

                    show screen notification_popup_big
                    with dissolve

                    sanya "Прости, последнее время я очень занят, может когда-нибудь в другой раз."

                    show nadya light sad
                    with dissolve

                    nadya "Ладно уж, может в следующий раз."

                    "Мы продолжили разговаривать на различные темы, пока у Нади не зазвонил телефон."
                    nadya "Прости, мне уже пора, добавишь меня в телеграме?"
                    sanya "Да, конечно."
                    nadya "Класс, мой номер: ..."
                    nadya "Ладно, мне пора идти. Ещё увидимся."

                    hide nadya light sad
                    with dissolve

                    "Уже было достаточно поздно, поэтому недолго думая я решил отправиться прямиком к своему дому."
            
            hide screen notification_popup
            with dissolve
    
    scene black scen
    with fade

    if not day2_nadya_het_one_sigarett and not day2_nadya_bought_sigaretts and not day2_sanya_went_to_smoke:
        "Зайдя в квартиру, я сразу достал сигарету и пошёл к окну."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry
        with fade

        "Настроение было, мягко говоря, ужасным."
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
        yuli "В следующий раз найди меня. Пойдем домой вместе, как раз узнаешь где я живу и вообще, мы можем почаще видеться."
        sanya "Спасибо, я очень рад это слышать. С этого дня мы будем ходить домой вместе."
        yuli "Слушай, мне недавно приходило уведомление из универа, ты не хочешь съездить со мной в санаторий?"
        sanya "Тебе тоже, я как раз туда собираюсь, завтра уже отъезд."
        yuli "Ура, я знала что ты мне не откажешь."
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

        scene sanya cry
        with fade

        "Настроение было, мягко говоря, ужасным."
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
        "Зайдя в комнату, я сразу пошёл на балкон. Достав сигаретку из пачки вишневого чапмана, я сразу вспомнил о Наде."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry
        with fade

        "Наше знакомство в парке было очень неожиданным, но очень приятным."
        if day2_choosen_instead_yuli :
            "Надя мне сразу понравилась, она очень умная и необычная. В добавок курит чапу, так же, как и я. Интересно она ответит, если я ей позвоню?"

            stop music
            play music "audio/cell-phone-ring-simple.mp3" fadein 1.5 fadeout 2.0 volume 0.1

            scene sanya notification
            with fade

            "Спустя пару протяжных гудков в трубке послышался знакомый голос."

            stop music
            play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

            nadya "Привет, Саш, чего ты звонишь так поздно?"

            sanya "Надь привет, а ты не хотела бы съездить со мной в санаторий университета? Там целая неделя бесплатная."
            sanya "Думаю нам было бы весело вместе."

            nadya "Конечно, я только рада буду составить тебе компанию."
            sanya "Я очень рад это слышать, может тогда завтра встретимся в 8:00 у универа?"
            nadya "Да, в 8:00 будет как раз. Ладно, Саш, я пойду, а то мне уже спать пора."
            nadya "Спокойной ночи!"
            sanya "Спасибо, ещё раз, тебе тоже спокойной!"
            
            "Мои мысли были только о Наде."
            "Надеюсь мы будем жить в соседних комнатах. Гулять вместе."
            "А по ночам проводить оздоровительные процедуры по улучшению кровообращения в области таза. (что за ебанавт это писал?! исправить!)"

        else :
            "Надя мне сразу понравилась, она очень умная и необычная. В добавок курит чапу, так же как и я. Интересно она ответит, если я ей позвоню?"

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
            sanya "Спасибо, ещё раз, тебе тоже спокойной!"

        "С этими словами я положил трубку и достал ещё одну сигарету."

        scene sanya cry
        with dissolve


        "Я достал наушники и включил недавно добавленную в плейлист музыку."
        "Ей оказалась \"Несогласие - Жду любви\"."
        "Ещё минут пятнадцать я сидел на балконе, курил и наслаждался музыкой."
        "В скором времени меня начало клонить в сон и я решил перебраться на кровать."

        scene sanya bed with dissolve :
            linear 35 zoom 1.1
            linear 35 zoom 1.0
            repeat

        "Спать на ней будет явно удобнее чем на балконе."
        
    elif day1_pasha_kfc and not day1_yuli_agreed_after_kfc and day2_sanya_vote_for_ussr:
        "Зайдя в квартиру, я сразу пошёл к окну."

        pause 1.5

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.5 volume 0.1

        scene sanya cry
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

        scene sanya cry
        with fade

        "Настроение было, мягко говоря, ужасным."
        "Вспомнив, что я почти весь день не курил, я потянулся за сигаретой. И правда, сегодня вся голова была забита Юлей. Целый день я думал только ней."
        "Я облокотился на балкон и закурил."
        "Честно говоря, я так рад встрече с Юлей, она смогла разукрасить мою жизнь... Предать ей смысл. "
        "За прошедшие пару дней она разделяла со мной как радости, так и неудачи."
        "Лучше неё нет никого на свете."
        "Я хочу быть с ней постоянно."
        "Поскорее бы настало завтра, я так хочу её увидеть."
        "Для меня она единственный лучик счастья в этом бренном мире."
        sanya "Может позвонить ей?"
        sanya "Хотя уже поздно... Она, наверное, спит."

        "Затушив сигарету, я сразу лёг в кровать, надеясь, что завтра наступит как можно скорее."

        scene sanya bed with Dissolve(3.0):
            linear 35 zoom 1.1
            linear 35 zoom 1.0
            repeat
    stop music fadeout 7.0
    scene black scen 
    with Fade(3.0, 0.0, 3.0)

    jump third_day

label third_day :
    
    scene sanya bed with Fade(0.0, 1.0, 4.0) :
        linear 35 zoom 1.1
        linear 35 zoom 1.0
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
        "Юля" if not day1_pasha_kfc or day2_sanya_vote_for_ussr :
            $ mood_counter += 1;
            $ str_for_notification = "У этого действия будут последствия"

            show screen notification_popup_big
            with dissolve

            $ choice_yulia = True

            "Первым в голове возник образ Юли. Вчерашняя прогулка оставила приятное послевкусие."
            "Я и не ожидал что мы всего за пару дней так сблизимся, мы удачно совпали характерами, временами мне кажется, что мы с ней очень похожи."
            "Интересно, смогу ли я ещё встретиться с ней?"

        "Надя" if day2_nadya_have_a_dialog :
            $ mood_counter += 1;
            $ str_for_notification = "У этого действия будут последствия"

            show screen notification_popup_big
            with dissolve

            $ choice_nadya = True

            "Первым в голове возник образ Нади. Наше знакомство оказалось для меня неожиданностью. Мы встречались только один раз, но она всем видом показывала что я ей симпатичен."

        "Один" :
            $ mood_counter -= 1;
            $ str_for_notification = "У этого действия будут последствия"

            show screen notification_popup_big
            with dissolve

            $ choise_lonly = True

            "А ведь и ехать не с кем... Поеду тогда один."

    hide screen notification_popup_big
    with dissolve

    scene bus station
    with fade

    "Заебала эта остановка. Когда её уже снесут к хуям собачьим?"
    "А вот и моя развалюшка..."

    play sound "audio/bus.mp3" fadein 1.5 fadeout 1.5 volume 0.1

    scene black scen 
    with fade

    pause 6.0
    stop sound

    play music "audio/sound-in-bus.mp3" fadein 1.5 fadeout 2.0 volume 0.1

    scene bus
    with fade

    "Посплю пока. Главное не проспать остановку..."

    call play_bus from _call_play_bus_1
    

    "Снова тот же сон..."

    
    scene black scen 
    with fade

    stop music
    play sound "audio/bus.mp3" fadein 1.5 fadeout 1.5 volume 0.1

    pause 6.0
    stop sound

    scene bus station near nstu
    with fade

    "Кажется, по времени всё нормально. Можно уже не торопиться."

    scene black scen
    with fade

    "На часах было без пяти восемь, а в конце улицы уже виднелся ждавший меня автобус."
    "Подойдя ближе я был приятно удивлен, передо мной открылся вид не на старенький и потрепанный ЛИАЗ, а на красивый Икарус, он выглядел так будто только сошёл с конвейера."

    scene neew bus
    with fade

    if choise_lonly :
        if day2_nadya_have_a_dialog and (not day1_pasha_kfc or day2_sanya_vote_for_ussr or day1_yuli_agreed_after_kfc):

            show nadya angry at right
            with dissolve

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
            call play_bus from _call_play_bus_2

            "Проснувшись, автобус уже тронулся и я не застал Юлю на своём месте."
            "Я поднялся и прошёся по рядам... Нашёл Надю и обратился к ней"
            sanya "А ты не видела Юлю? Она же с нами садилась? Неужели из-за меня решила не ехать вовсе..."
            $ mood_counter -= 1;
            "Надя что-то буркнула в ответ, явно не желая  даже разговаривать со мной сейчас."
            "Я молча сел рядом. Будь что будет"



        if day2_nadya_have_a_dialog :

            show nadya angry
            with dissolve

            nadya "Привет! Я не понимаю, а почему ты сел один-то?!"
            sanya "Прости... Я не очень хотел садиться к кому-то. Не было настроения."
            nadya "Мы же с тобой договаривались! Разве это правильный поступок?"

            hide nadya angry
            with dissolve

            "Надя молча села рядом. Говорить дальше она ничего не хотела. Я же побоялся сделать всё ещё хуже"

            jump _sanatorium

        elif not day1_pasha_kfc or day2_sanya_vote_for_ussr or day1_yuli_agreed_after_kfc :

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

            jump _alone


    elif choice_nadya :

        sanya "Привет, в этот раз запаслась чапой? А то мне кажется я взял маловато!"

        show nadya smiles
        with dissolve

        nadya "Ха-ха-ха, конечно взяла, если будем жить рядом, можем вместе ходить курить"
        "Она такая необычная - можно говорить, что правда думаешь, и не стеняться, хотя бы в плане сигарет"
        sanya "Кстати, а зачем тебе ехать в санаторий?"

        show nadya giggles
        with dissolve

        nadya "А ты как думаешь? Не с отитом же!"
        "Зато, зная какие справки она собирала, можно не сомневаться в здоровье её ануса..."
        sanya "Не знаю... может что-то с легкими?"
        "Курит-то она много..."
        nadya "Шерлок Холмс нервно курит, конечно, с твоей дедукцией! А ты зачем едешь-то?"
        sanya "Да как-то отвлечься надо и здоровье поправить. Тяжело так после лета сразу на учебу, тем более когда все лето занимался хуйней"

        menu :
            "Да ладно...? Слушай, а ... какой тебя любимый цвет?" :
                nadya "Слушай, ты тоже не выспался? Давай поспим пока едем? Не могу соображать ничего, что ты говорил? Сплю уже"

            "Ну не надо делать вид, что ты идеальная и вся такая правильная - меня сейчас стошнит" :
                "Надя обиделась и мне пришлось отсесть. Не думаю, что мы серьезно поссорились."
                jump _sanatorium
        

        jump _sanatorium

    elif choice_yulia :

        $ is_bad_ask = False

        play music "audio/sound-in-bus.mp3" fadein 4.0 fadeout 5.0 volume 0.10
        "Сяду-ка я к Юле - проверенный вариант, так скажем."
        sanya "Юль, привет..."

        show yuli happy
        with dissolve

        if day1_pasha_kfc == True :
            yuli "Приветик! Хоть здесь ты побудешь без своего Пашки-алкаши"
            show yuli sad
            with dissolve

        else :

            sanya "Жалко конечно, что Паша не поехал, мне будет его не хватать"
            yuli "Да ладно тебе, нужен тебе этот качок-харчок!"
            sanya "Паша мне очень помогал в жизни, иногда как прихватит - так только его шутка в себя приведет."

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
                    stop music fadeout 0.3
                    play music "audio/sigma.mp3" volume 0.3
                    pause 4.0

                "Эммм.... ну если только.... мне искусственное дыхание нужно будет......."  :
                    stop music fadeout 0.3
                    play music "audio/fail.mp3" volume 0.1

                    centered "{size=+24}Участие принимали:\nAsind,\nDarlingInSteam,\nDanilka108,\nXpomin,\nTheNorth"

                    pause 4.0
        stop music fadeout 0.5 
        play music "audio/sound-in-bus.mp3" fadein 3.0 fadeout 5.0 volume 0.10

        show yuli shy
        with dissolve

        yuli "На самом деле, я рада, что ты тоже едешь в санаторий!"
        yuli "Кстати, а у тебя какие-то проблемы со здоровьем или ты просто так?"
        sanya "Да у меня последнее время что-то ночи становятся все длиннее, а дни все тусклее. Надо отвлечься как-то, природа, думается мне, - самое то!"

        if day1_sanya_wants_camp == True:
            "Главное не говорить, что меня мамка сюда отправила, а то не видать мне ничего с юлькой."

        sanya "А ты почему едешь? Учебу прогулять хочешь?"
        
        if day1_sanya_wants_camp == False :
            yuli "Да меня мама отправила, говорит, что отвлечься пора бы, а то я все лето проварилась в делах"
        else :
            yuli "Да пришло уведомление, я долго не думала, решила - надо ехать"

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
        alpha 0.0
        linear 4.0 alpha 1.0
        block:
            linear 1.0 zoom 1.2 alpha 0.9
            linear 0.6 zoom 1.0 alpha 1.0
            repeat
    "Смотря на пустой автобус, я понял лишь одно - я никому не нужен."
    "Впрочем, оно и не удивительно, последние дни я всё делал не так, как нужно было бы."
    "Пустота автобуса, предначертанная жизнью, будто говорила мне, что я неудачник, что я никому не был нужен и не буду."

    play music "audio/sound-in-bus.mp3" fadein 1.5 fadeout 2.0 volume 0.1 

    "Всё, что мне оставалось, - это молча смотреть в окно и наблюдать на проезжающие леса, дома,"
    #call play_bus
    play sound "audio/diskoteka_avaria.mp3"
    extend " ИКАРУС????"
    window hide

    play music "audio/seven-summer.mp3" fadein 1.5 fadeout 1.5 volume 0.2

    centered "{size=+24}Автобус попал в аварию.\nПогибло два человека.\nЕдинственный Пассажир и водитель."
    $ renpy.pause(1, hard=True)
    stop sound
    jump _end

label _sanatorium :

    scene black scen
    with dissolve

    pause 2.0

    "Мы наконец-то подъезжаем к \"Синереченску\" - санаторию, в котором мне придется провести целых две недели. Надеюсь, это будет стоить того."

    scene sanatorium forest neer san
    with dissolve

    "Красивая природа дала понять, что санаторий находится в глуши. Всё вокруг отдовало зелёными оттенками и говорило тебе о первозданности."
    "Высокие и пушистые деревья рядом с обочиной заставляли каждую часть тела расслабиться, почувствовать себя свободным."
    "Река, которая проходило под небольшим мостом текла в неизвестную мне даль, но я чувствовал потрясающий интерес к ней."
    "Наблюдая за этой природой, я не заметил, как мы начали заезжать на территорию санатория."

    play sound "audio/bus.mp3" noloop fadein 1.5 fadeout 1.0 volume 0.1
    pause 2.0

    olga_dmitrievna "Так, выгружаемся!"
    
    stop music fadeout 1.5

    scene sanatorium sanatorium
    with dissolve

    play sound "audio/forest-sound.mp3" loop fadein 1.5 fadeout 3.0 volume 0.1

    "Конструктивный стиль, полный острых углов и кубических форм."
    "Никаких архитектурных излишеств, но много зелени, клумб, серо-белые цвета бетонных строений."
    "Вся эта свистопляска буйной цветастой зелени, бесцветных стен, да и общая атмосфера легкой запущенности - все это веяло легкой меланхолией, словно весь этот санаторий - отражений моей жизни."
    "Человек из толпы" "Будто в прошлое попал!"
    "Не могу не согласиться, вид старенького санатория оставлял приятные, душевные чувства где-то в глубине меня."
    "Мне сразу вспомнились рассказы моего, уже почившего, дедули, о том, как он был сначала октябренком, а потом и пионером."
    "От него я наслышался о небывалой красоте и атмосферности тех самых, советских лагерей и санаториев."
    "Я мог часами слушать его рассказы о том, как он ходил в походы, играл в лапту, выступал на концертах, рисовал плакаты и мастерил всякие вещи в клубе электронщиков."
    "С тех пор, я мечтал посетить какой-нибудь пост-советский лагерь и окунуться в прошлое, но годы шли, а мечта всё отдалялась от меня."
    "Я продолжил смотреть в окно автобуса, подскакивающего на редких ухабах давно не ремонтированной дороги, с нетерпением, дожидаясь нашего приезда."
    "Встав, я в числе первых вышел на воздух. Он мне показался необычайно свежим, видимо годы жизни в городе дали о себе знать."
    "Водитель уже открыл багажное отделение и, с неохотой,  доставал наши сумки, ставя их прямо на пыльный бетон."
    "Достав пачку чапмана и вынув сигарету, я сунул сладковатый фильтр в рот, планируя как следует затянуться после долгой дороги."
    
    show olga olga happy
    with dissolve

    olga_dmitrievna "Так, молодые люди, одно из правил санатория гласит, что курить можно только в строго отведенных местах, чтобы не мешать другим отдыхающим!"
    olga_dmitrievna "А лучше и вовсе не курить. Вы, как-никак, на лечение приехали!"
    
    menu :
        "Жестко раскурить чапу" :
            $ day4_smoke_after_words_olga = True

            "Поездка была настолько долгая, что отказать в сигаретке себе я никак не мог, даже не смотря на запрет со стороны вожатой."
            
            play sound "audio/cigarette.mp3" noloop fadein 0.5 fadeout 0.5
            pause 3.0

            "Проигнорировав её, я с удовольствием втянул ароматный дым любимого чапмана."
            "Никотин приятно ударил в голову, лёгкие разжались и я, с удовольствием, продолжил смаковать сигаретку."

            show olga olga angry
            with dissolve

            $ str_for_notification = "У этого действия будут последствия"
                
            show screen notification_popup_big
            with dissolve

            pause 2.0

            hide screen notification_popup_big
            with dissolve

            "Ольга Дмитриевна неодобрительно глянула на меня."
            sanya "Мне пиздец..."   

            "От этого взгляда мурашки пошли по спине. Надеюсь она не заставит таскать мешки с сахаром по всему санаторию."
            olga_dmitrievna "А сейчас давайте я вам проведу небольшую экскурсию, пока мы идем до ваших комнат."

            hide olga angry 
            with dissolve

        "Сдержаться" :
            $ day4_smoke_after_words_olga = False

            "Ольга Дмитриевна неодобрительно посмотрела на тех, кто ее проигнорировал и с вежливой улыбкой произнесла."
            olga_dmitrievna "А сейчас давайте я вам проведу небольшую экскурсию, пока мы идем до ваших комнат."

            hide olga happy
            with dissolve

    scene black
    with dissolve

    stop music fadeout 0.4
    play sound "audio/footsteps.mp3" fadein 0.5 fadeout 0.5 volume 0.8
    pause 2.0
    
    "Ольга Дмитриевна бодро шла вперед, громко информируя нас о том, какой этот санаторий хороший и как качественно мы тут отдохнем. "

    scene sanatorium sanatorium park
    with dissolve

    play sound "audio/forest-sound.mp3" loop fadein 1.0 fadein 2.0 volume 0.1

    "Я плелся без особого энтузиазма, лениво поглядывая по сторонам, но вот семьи, молодые и не очень, с детьми и адекватные, весело шагали в ногу, следуя за энергичной сопровождающей."
    "Среди всей когорты приехавших на лечение, было мало молодых, что тоже отнюдь не добавляло мне настроения. Провести пол месяца со старыми пердунами и молодыми парочками мне точно не улыбалось."
    "Старость, думал я, подступает незаметно. Как и всякая другая болезнь." 
    "Вот ты здоров, силен, молод и можешь выдуть чикушку за раз, а на утро выпить крепкого чаю и быть в строю."
    "А потом раз - и вот ты уже хрустишь коленками и боишься лишний раз наклониться, потому что темнеет в глазах." 
    "Так и с простудой: ходишь весь здоровый, чувствуешь себя прекрасно."
    "А на утро просыпаешься с больным горлом и температурой."
    "Вот и я, как и эти старые пердуны, незаметно для себя постарел-заболел. В их естественной среде обитания комфортно себя чувствую, буду те же процедуры что и они проходить."
    "Ну, рядом хотя бы есть парочка жгучих красоток, которые вполне могут скрасить мои оздоровительные процедуры. А может и дополнить их... Хе-хе.  "

    if day3_go_with_yuli :
        "Я незаметно оглянулся в поисках Юли, в мыслях уже готовый пригласить ее на совместное принятие грязевой ванны."
    if day3_go_with_nadya :
        "Я незаметно оглянулся в поисках Нади, в мыслях уже готовый пригласить ее на совместное принятие грязевой ванны."
    
    if day3_go_with_yuli :
        "Как бы я не крутил головой, никак не мог найти ее. Юли нигде видно не было. Может, она пошла к себе в комнату, минуя экскурсию? А может ей стало плохо?"
        "Гадать бессмысленно, в любом случае мы встретимся - санаторий небольшой. Может и вовсе процедуры проходить вместе будем, хе-хе..."
        "Но все равно неприятно, с ней бы в любом случае экскурсия была бы веселее."
        "Разочарованно вздохнув, я ускорил шаг, догоняя наш отряд молодых и не очень. Поправив рюкзак, с еще более дерьмовым настроением, поплелся в самом конце."

    if day3_go_with_nadya :
        $ mood_counter -= 1
        "Найдя искомую в компании какого-то парня, я приветливо махнул ей. Надя помахала в ответ, и продолжила щебетать с этим пацанчиком, что в довесок со своей сумкой, тянул и ее вещи. Что-то не помню его в автобусе."
        "Где-то под сердцем неприятно затянуло, а изнутри начала подниматься тихая волна жгучей злобы. Но я тут же одернул себя, немного удивившись порыву."
        "Мы с ней даже толком не знакомы, что это я тут начал. К тому же, не факт, что это ее парень."
        "Может знакомый или родственник? Да и вообще какое мне дело!"
        "Потряся головой, словно отгоняя наваждение, я поправил рюкзак и с еще более дерьмовым настроением, поплелся в самом конце."

    "Фоном неслась складная, явно много раз произнесенная речь Ольги Дмитриевны."
    "Там мелькали объяснения режима, правил и процедур, но я особо не слушал, обращая внимание больше на окружение."
    "В конце концов, мне тут жить еще пару недель."
    "Территория санатория была поистине огромной, но зданий на нем было мало. Да и сами здания были довольно компактными, явно не рассчитанными на большое количество людей."
    
    show olga happy at center
    with dissolve

    olga_dmitrievna "Вот тут у нас медпункт, если кому-то станет плохо"

    scene sanatorium medical post
    with dissolve

    "Выхватил я из общего потока речи конкретику, и,  ради интереса, взглянул в указанном направлении."
    "Медпунктом оказалось бетонное побеленное здание, формой напоминающее коробку из под спичек."

    show grusha happy
    with dissolve
    
    "На крыльце, в удобном с виду кресле, сидела полноватая женщина в белом халате, курящая трубку."
    sanya "Значит ей, сука, можно, а нам, простым людям, нельзя?"
    "Но в ответ моим мыслям раздался полный возмущения голос Ольги Дмитриевны"
    olga_dmitrievna "Агриппина Владимировна! Сколько раз я вас просила не курить около медпункта?!"

    show grusha sad
    with dissolve

    "Названная меланхолично посмотрела на пышущую праведным гневом женщину и спокойно продолжила попыхивать задорно дымящейся трубке."
    "Ольга Дмитриевна еще постояла, негодующим взглядом обжигая стойкую старушку, и в конце-концов сдалась, продолжив экскурсию."
    
    hide grusha
    with dissolve
    "Ха! А мне нравится эта бабка, надо будет с ней скорешиться."

    scene sanatorium park
    with fade

    "Я стал больше прислушиваться к болтовне Ольги Дмитриевны, но усталость и голод брали свое."
    "Идти стало тяжеловато, и, видимо, не только мне."
    "Послышалось недовольное ворчание и Ольга Дмитриевна, поняв общее настроение стала закругляться."
    
    show olga happy
    with dissolve
    
    olga_dmitrievna "Что ж, я думаю пора проводить вас по комнатам!"
    "Недовольное ворчание сменилось одобрительным гоготом. В том числе и моим. "
   
    hide olga
    with dissolve

    "Комнаты располагались в отдельном здании, самом большом из всех, пускай и не слишком большим в общем."
    "Четыре этажа, с обширными балконами, и, надеюсь, с такими же обширными комнатами."
    "Выглядел он конечно побито, словно за ним почти не ухаживали, но тем не менее весьма добротно. Хорошо бы внутри было получше."
    "Ну, лучше, чем можно было ожидать..."
    
    scene black
    with dissolve
    
    stop music fadeout 1.0
    play sound "audio/footsteps.mp3" noloop fadein 0.3 fadeout 0.3 volume 0.8
    pause 4.0

    play sound "audio/door_open.mp3" noloop fadein 0.1 fadeout 0.1 volume 1.0
    pause 2.0

    scene sanatorium dormitory room
    with Fade(0.3, 0.4, 0.3, color="#000")

    "Все было достаточно светлым, но каким-то устаревшим что ли..."
    extend "Или просто очень дешевым."

    "Но при этом таким родным и знакомым, что захотелось вдохнуть полной грудью и сказать: "
    play music "audio/prepare-to-fight.mp3" fadein 2.5 fadeout 3.0 volume 0.15
    extend "Что это за чучело-хуючело?"
    
    show pavel pavel neutral:
        ypos 0.1
        linear 0.9 xalign 0.9
    with Dissolve(1.0)
 
    show olga olga happy:
        ypos 0.1
        linear 0.1 xalign 0.1
    with Dissolve(0.5)

    
    "Вслед за мной в комнату зашел мужик. Конкретный такой мужик, будто бы только что вышедший из жесткого запоя. Пахло от него соответствующе."
    
    olga_dmitrievna "Это Пал Генадьич."
    "Терпеливо пояснила Ольга Дмитриевна."
    olga_dmitrievna "Он очень хороший мужчина, и теперь он ваш сосед по комнате."

    menu:
        "Переселиться":
            $ day4_move = True;
                    
        "Остаться":
            $ day4_move = False;
    
    if day4_move == True:
        $ str_for_notification = "У этого действия будут последствия"
            
        show screen notification_popup_big
        with dissolve

        pause 2.0

        hide screen notification_popup_big
        with dissolve

        "Смотря на это вонючее нечто, что уже по хозяйски развалилось на кровати, раскидав носки с тапочками в разные стороны, я понял одно."
        sanya "Я не собираюсь с ним жить."
            
        show olga olga angry
        with dissolve

        olga_dmitrievna "Ну как же это! Павел Генадьевич очень хороший молодой человек! Культурный, аккуратный, чистоплотный..."
        "В этот момент этот культурный молодой человек, успевший зайти проведать туалет, как следует высморкался в раковину." 
        "От звука его хобота, казалось, затряслись стены во всех зданиях санатория."
        "Красноречиво глянув на Ольгу Дмитриевну, я получил полный непонимания взгляд."
        sanya "Я не собираюсь с ним жить!"
        olga_dmitrievna "Ну, как же это! Ну..."
        sanya "Я требую другую комнату!"

        if day4_smoke_after_words_olga :
            $ day4_fight = True
            olga_dmitrievna "К сожалению, у нас сейчас нет свободных комнат"
            "Она беспомощно развела руками, с вежливой улыбкой глядя на меня. Однако судя по злорадным огонькам в глазах, это было неправдой. "
            sanya "Вы что, хотите, чтобы я жил... вот с этим?!"
            "Я махнул рукой в сторону алкаша, уже раздевшегося до трусов."
            "Тот, поняв, что  речь идет о нем, поднял на меня свое пропитое лицо." 
            "Пару секунд, на его лице отражался мучительный умственный процесс. Потом морда мужика побагровела."

            hide olga olga angry
            with dissolve

            show pavel neutral:
                linear 0.9 xalign 0.4
            with dissolve

            stop music fadeout 0.5
            play music "audio/fight.mp3" fadein 3.0 fadeout 2.0 volume 0.2

            pavel "Ты это мне, щенок?!"
            "Он вскочил, причем очень резво, что было неожиданно для его грузной комплекции."
            "Меня его порыв никак не впечатлил. Уж с кем я точно справлюсь, так это с пропитым алкашом. "
            sanya "Тебе, морда пропитая."
            "Руки чуть задрожали, а дыхание предательски ускорилось, по спине пробежал холодный пот. Не от страха, нет - от прилива адреналина."
            "Я корпусом повернулся к приблизившегося вплотную алкашу, едва сдерживаясь, чтобы не поморщиться от запаха перегара. "
            "Я, конечно, тоже не трезвенник, бывало и на улице засыпал. Но чтобы вот так... "
            "Алкаш возвышался надо мной, как Голиаф над Давидом, но так же как и Давид, я не дрогнул перед великаном."
            pavel "Ты меня что, алкашом назвал?"
            "Глаза его опасно сузились, но меня таким точно не напугаешь. Видывали и пострашнее."
            
            with vpunch
            "Неожиданно челюсть взорвалась болью, а сознание поплыло в неведомые дали."
            "Я даже не успел заметить, как этот ублюдок меня ударил!"

            with hpunch
            "На ногах устоять я смог, хоть ноги и подкосились, однако болью взорвался живот."
            
            play sound "audio/Fall.mp3" fadein 0.1 fadeout 0.2
            scene black scen
            with Fade(0.5, 0.5, 0.5, color="#000")
            
            "Вот тут у нас проблемы, Ватсон! Бухнувшись на колени, я судорожно пытался вздохнуть, царапая пальцами плитку." 
            stop music fadeout 3.0
            "Но мучился я не долго - висок взорвался болью и я потерял сознание."
            "Очнулся я от резкого запаха, чуть ли не вскочив с  кушетки.  Но чьи-то стальные руки крепко прижали меня к жесткой поверхности, не давай двинуться лишний сантиметр. "

            scene medicina
            with fade
            
            show grusha happy
            with dissolve

            with hpunch

            grusha "Ишь, какой резкий драчун! Да стой ты!" 
            "Вырываться я перестал только тогда, когда понял, что нахожусь в медицинском кабинете, а передо мной медсестра, а не тот бугай. "
            "Посветив мне фонариком в глаза и поводим им же перед носом, Агриппина Владимировна (а это была именно она, я ее хорошо запомнил) осталась довольна осмотром. "
            "Засунув руку в карман халата, она сунула мне под нос таблетку. "
            grusha "На! Выпьешь после обеда, чтобы голова быстрее прошла"
            sanya "Спасибо..."
            grusha "Пожалуйста. Идти можешь?"
            sanya "Могу..."
            
            show grusha angry
            with dissolve

            with hpunch
            
            grusha "Ну так иди нахуй отсюда!"
            "Не став больше нужного занимать эту колоритную женщину, я пружиной подскочил с кушетки, охнув от боли резкой вспышки боли в голове. "
            "Баба Груша на это только хмыкнула, доставая из второго кармана огромную трубку. Глазами она указала на выход."
            "Поняв все без лишних слов, я ретировался из кабинета."
            
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
            sanya "Ну, хотя бы на обед не опоздал... Может даже с девчонками встречусь"
            "Подбодрив себя подобным образом я поплелся в сторону столовой. "

            scene sanatorium canteen
            with fade

        else:
            $ day4_fight = False
            "Явно через силу, но Ольга Дмитриевна все же произнесла:"
            olga_dmitrievna "Ну, у нас есть одна свободная комната... Можем заселить вас туда. Но только в качестве исключения"
            sanya "Было бы неплохо"
            "Покивал я важно."
            "Надеюсь, там будет девочка..."
            olga_dmitrievna "Прошу за мной"

            scene sanatorium walkway
            with fade

            show olga olga angry at center:
                ypos 0.6
            with dissolve

            "Шли мы недалеко, комната была буквально через пару дверей. "
            olga_dmitrievna "Вот ваша комната, располагайтесь. А я пойду проверю остальных заселяющихся"
            
            hide olga angry
            with dissolve

            "Полный предвкушения, я открыл дверь. "
            
            scene sanatorium skin dormitory room
            with fade

            "Меня встретил бардак и разбросанные везде носки с футболками, а на кровати, в позе йога, сидел бритый паренек, явно скинхедской наружности."
            extend " Облом..."
            "Услышав шум, он открыл глаза."
            skin "Тихо, блять, ты мешаешь моему слиянию с бесконечно вечным!"
            "Знатненькой прихуев с такого приветствия, я пробурчал извинения и виновато прошел к свободной кровати, поставив сумку. "
            "Заебись, из огня да в полымя, охуенно переселился. "
            "Раскладывая свои вещи, я украдкой посматривал на скинхеда. "
            "Выглядел он, конечно, колоритно. Кожаная жилетка на голое тело, джинсы, толстенная серьга в ухе и абсолютно лысый череп. "
            "Находится в комнате с этим чудаком было не очень комфортно, решение переселиться от вонючего, но обычного алкаша уже не выглядело хорошим. "
            skin "Да бля, че ты на меня зыришь?"
            "От неожиданности я вновь оторопел, не зная, что ответить. Он же с закрытыми глазами был, как он увидел?"
            skin "Ладно, бля, похуй" 
            "Он резко вскочил с кровати и замер в странной позе, постояв так пару секунд он потянулся, хрустнув костями, и неожиданно протянул руку:"
            skin "Меня Мыкало звать!"
            sanya "Саня..."
            skin "Здрав будь, Саня!"
            sanya "Здрав..." 
            "Вот это имечко конечно.."
            skin "Располагайся, че замер-то, помочь чем что ли?"
            "Я осознал, что я неприлично долго разглядываю своего необычного соседа, так что одернув руку (резче, чем хотелось бы) и буркнул:"
            sanya "Все нормально, я сам как-нибудь."
            "Развернувшись, я продолжил разбирать свои вещи, стараясь сделать это как можно быстрее, чтобы смыться из комнаты на обед."
            skin "Странный ты какой-то..."
            "На себя посмотри, древняя реликвия... Вслух я это, конечно, не сказал. "
            skin "О, я тебя вспомнил, ты с кислой мордой шел позади всех на экскурсии"
            sanya "Ну, было дело..."
            skin "А все потому, что у тебя энергетика загрязнена!" 
            sanya "Чего?"
            skin "Прочиститься тебе надо, вот что! Где-то у меня тут была одна штука..."
            "Он чуть ли не с головой зарылся в свою сумку, увлеченно там что-то разыскивая."
            sanya "Слабительное что ли?"
            skin "Во!"
            "Он воздел в руку в потолок, в ней было зажато что-то, что было подозрительно похоже на самокрутку..."
            skin "По древним рецептам наших славных предков! Сушеные листья клена, береза, акации и куча разных полезных трав! Вмиг встанешь на ноги!"
            "Это он мне древнерусский косячок предлагает?"

            menu :
                
                "Жетско затянуться" :
                    $ day4_smoke_old_siggarete = True
                    $ day4_take_pill = True
                    $ str_for_notification = "У этого действия будут последствия"
            
                    show screen notification_popup_big
                    with dissolve

                    pause 2.0

                    hide screen notification_popup_big
                    with dissolve

                    "Я с сомнением посмотрел на протянутую руку, потом на честную морду панка."
                    "Тот, заметив мои душевные метания, доверительно произнес: "
                    skin "Сам собирал и набивал, точно по рецепту!"
                    sanya "И где ты эти рецепты откопал?"
                    "Не то, чтобы мне было интересно, но иногда забавно слушать вот таких вот... индивидов. Мыкало, услышав вопрос по теме, радостно начал объяснять."
                    skin "Я когда у бабушки на чердаке убирался, одну книгу нашел, можно сказать, манускрипт!"
                    extend "Русскими рунами писано было, Родом клянусь! И бумага такая, будто из кожи сделана, ну ты понимаешь о чем я..."
                    sanya "Ну как сказать..."
                    skin "Короче, я на один форум зашел, там мне все и объяснили. Сказали, это древний травник, возможно, созданный еще при рюриковичах, представь!"
                    sanya "А ты, оказывается, не один такой..."
                    skin "Вот, я его изучил поподробнее, там некоторые слова понятны были, и понял, что медицина в сравнении с этим - чепуха полная! Вот ты знал, что все проблемы со здоровьем от нестабильной связи с землей идут?"
                    sanya "Ну хоть не с Нибиру..."
                    skin "Я тоже сначала смеялся, а потом попробовал - и прозрел!"
                    "Он вновь протянул мне скрутку, причем с таким одухотворенным лицом, что я просто не смог отказать. Вот так в секты и попадают."
                    sanya "Ну, ладно, давай свое чудодейственное средство"
                    "Он с готовностью сунул мне в руку скрутку, кажется, в сушеном лопухе, и достал зажигалку."
                    sanya "У меня своя"
                    "Я достал из кармана жигу, и чиркнув кремнем подпалил краешек травяной папиросы."
                    "По комнате распространился запах горелой травы, но не то, чтобы он неприятно пах. Ободренный этим фактом, я затянулся. "
                    sanya "Кха-кха-кха-кха!" 
                    "Легкие обожгло огнем, а в голове зашумело. Кашель был настолько сильный, что меня чуть не вырвало. Дышать я не мог, так что очень скоро начал задыхаться. "
                    skin "Ой, я тебе, кажется, не ту дал! Щас, подожди... Где же она..."
                    "Он под мой нестерпимый кашель вновь принялся копаться в своей сумке, и в скором времени извлек оттуда новую скрутку. "
                    skin "Держи! Это то, что надо!"
                    sanya "И... Иди... Помоги...."
                    "Я даже не смог послать его нахуй, из-за того, что очень сильно задыхался."
                    "Сознание плыло, а я все еще не мог вздохнуть. Липкий страх пополз по спине и с каждой секундой без воздуха он становился сильнее."
                    sanya "Вра... Врача..."
                    "Паника захлестнула меня, и к кашлю прибавилась еще и одышка. Настоящее комбо и фаталити для дыхательных путей."
                    "В глазах темнело, от кашля меня вырвало, что отнюдь не способствовало поступлению кислорода. "
                    "Да чтоб еще раз я что-то пробовал из рук незнакомцев! "
                    "С такими мыслями я и ушел в отруб."

                    
                    "Ох-х-х, как же мне хуево..."
                    "Перед глазами все вертелось и кружилось, а во рту будто бы насрали кошки. Причем несколько раз."
                    "Легкие болели так, будто бы его прострелили. Нахуй я согласился?.. Щас бы сидел в столовой, пил чаек с девчонками и в ус не дул."
                    grusha "О, ты очнулся!"
                    "Я попытался рассмотреть источник голоса, но адский калейдоскоп перед глазами мешал это сделать. "
                    grusha "Рот открой"
                    "Но не успел я послушаться, как губ что-то коснулось и я почувствовал, что мне впрыснули что-то прямо в горло. "
                    "Закашлявшись от жуткой горечи, попавшей не в то горло, я блеванул в заботливо подставленный кем-то тазик. "
                    "Как следует прочистив желудок, я с облегчением откинулся на кушетке. "
                    grusha "Полегчало?"
                    "Я снова не успел ответить - в рот опять что-то впрыснули, но не такие неприятное и не так резко, так что с трудом, но я смог проглотить препарат."
                    sanya "Вы кто? Где я?"
                    grusha "Я Агриппина Владимировна, твой ангел хранитель на случай, если опять будешь принимать сомнительные вещества. А находишься ты в раю, где ставят на ноги таких как ты"
                    sanya "А-а-а"
                    grusha "Бэ-э, дурында, еще раз тут появишься - я палец о палец не ударю. Такой молодой, а уже... эх!"
                    "Бурчание продолжалось, но уже так невнятно, что разобрать было сложно. "
                    "С каждой минутой мне становилось все лучше и лучше. По крайней мере, вертолетики кончились, да и легкие не так сильно болели. "
                    "Наконец, я смог нормально осмотреться. "
                    "Обычный процедурный кабинет. В дальнем углу звенела колбами низенькая женщина, видимо, это и есть Агриппина Владимировна. "
                    "Обернувшись, она просканировала меня своим орлиным взглядом и что-то решив для себя сунула руку в карман. "
                    grusha "На! Выпьешь после обеда чтобы до конца все токсины вывести"
                    sanya "Спасибо..."
                    grusha "Пожалуйста, идти можешь?"
                    sanya "Могу..."
                    grusha "Ну так иди нахуй отсюда!" 
                    "Бодро вскочив, я вылетел пробкой из процедурного кабинета. Никогда так быстро в себя не приходил, хотя считай при смерти был. Баба Груша реально волшебница! "
                    "В животе заурчало, но аппетита как такового не было, поскольку чувство насранности во рту не пропало. Хотелось чем-то прополоскать рот, желательно пивком..."

                "Я ещё не обедал, закон Архимеда не позволяет" :
                    $ day4_smoke_old_siggarete = False
                    $ day4_take_pill = False
                    $ str_for_notification = "У этого действия будут последствия"
            
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
        "Я решил не спорить с Ольгой Дмитриевной и направился прямо к свободной кровати." 
        "На второй куском жира развалился \"очень хороший мужчина\", с пузом до колен и тройным подбородком. "
        olga_dmitrievna "Вот и хорошо, вот и прекрасно! Надеюсь, вы подружитесь!"

        hide olga happy
        with dissolve
        
        show pavel neutral:
            linear 0.5 xalign 0.5
        with dissolve

        "С этими словами неунывающая Ольга Дмитриевна ушла, оставив меня наедине с Павлом Геннадьевичем, что в ответ ей произнес что-то нечленораздельное."
        "Ладно, возможно я слишком категоричен. В конце-концов не просто же так он до такой жизни дошел?"
        "За этим всем явно что-то стоит. К тому же половину лета я почти в таком же состоянии пробыл, что я тут лицемерю."

        stop music fadeout 1.5

        hide pavel neutral
        with dissolve

        "Может скорешимся с ним, кто знает? Но сначала надо разобрать вещи."
        "У меня их было немного, поэтому я быстро управился, рассовав все по тумбочкам и единственному шкафу в комнате."
            
        "Павел Геннадьевич даром времени не терял и от его кровати на всю комнату раздался богатырский храп."
        "Кажется, даже окна задрожали."

        play sound "audio/door_open.mp3" noloop fadein 0.3 fadeout 0.3 
        scene sanatorium balcony
        with Fade(0.3, 0.2, 0.3, color="#000")
        play music "audio/forest_walk.mp3" fadein 2.0 fadeout 3.0 volume 0.2

        "Выйдя на балкон, оказавшийся скорее лоджией, я невольно залюбовался открывшейся передо мной картиной."
        "Тут стоял столик с пепельницей, пара стульев и открывался просто дивный вид!"

        "Симбиоз природы и человек в лучшем его проявлении."
        "Никогда не был особым ценителем ландшафтного дизайна, но тут действительно что-то было."

        "Множество клумб и цветов, которые складывались в незамысловатые узоры. Много беседок, изумрудные поляны и много деревьев."
        "Я глубоко вздохнул свежий воздух, пахший холодной рекой и мокрыми камнями, и у меня даже немного закружилась голова."

        "Даже курить не хотелось! Вот настолько плодотворно воздействовала на меня местная природа."

        play sound "audio/chair_crack.mp3" noloop fadein 0.2 fadeout 0.2        
        "Плюнув на все, я плюхнулся в кресло и любуясь видом все таки достал свой вишневый чапман."

        play sound "audio/cigarette.mp3" noloop fadein 0.3 fadeout 0.3
        pause 4.0

        "Красота! Ляпота!"
        "Кажется, я понимаю, что чувствовал Иван Васильевич, когда смотрел на Москву."
        "Все-таки, есть в созерцании бесконечно вечного что-то великое, вдохновляющее, настраивающее на определенный умственный лад..."

        play sound "audio/snore_big.mp3" noloop fadein 0.2 fadeout 0.2

        "~Хр-р-р~"
        sanya "Да блядство!"
        
        "Вышло это неожиданно громко даже для меня."

        play sound "audio/pavel_cough.mp3" noloop fadein 0.1 fadeout 0.1

        "За стеной послышался громкий кашель, такой сильный, что я даже испугался."
        "Заглянув в окно, обнаружил, что Павел Геннадьевич сидит на кровати и пытается вздохнуть"
        "Голова его покраснела как помидор, а изо рта вырывался жуткий хрип."

        "Ой..." 
        extend "Как бы не вышло чего."

        "Но, слава богу, все обошлось."
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
        show pavel smokes
        with dissolve
        
        "Мы оба наслаждались видом, тишиной и возможностью просто спокойно посидеть."
        "Никуда не нужно идти. Нет вечно давящей ответственности, горящих дедлайнов, беспокойства и стресса."
        "Тут по настоящему можно ощутить течение времени. Понять его силу, почувствовать мощь."

        pavel "Модные у тебя сигареты."
        "Павел Геннадьевич докурил свою и забычковал оранжевый фильтр."
        
        sanya "Да обычный вроде. Чапман вишневый."
        pavel "С кнопкой, что ли?"

        "В его взгляде появилась насмешка."

        sanya "Нет, просто фильтр такой." 
        pavel "Дашь попробовать? А я тебе свои."

        "Он протянул пачку красного Мальборо."
        "Мы обменялись сигаретами и закурили."
        
        play sound "audio/cigarette.mp3" fadein 0.3 fadeout 0.3
        pause 4.0
        
        "После Чапмана, Мальборо показалось более крепкой, однако я к нему быстро привык."
        "Но голова немного закружилась, так что я старался делать более редкие тяжки."

        sanya "Хороший табак, впечатляет."
        pavel "Меня другой не берет."

        "Он сделал очередную тяжку, втянув сигарету чуть ли не в половину. Мощный мужик, зря я на него бузил."
        pavel "Неплохие сигареты."
        "Одобрительно проговорил он, выдыхая дым."
        pavel "А есть без лишних запахов? Не люблю я все эти вишни-хуишни, мне б нормального крепкого табачку."
        sanya "Ну да, вроде есть классический чапман, но я его никогда не пробовал."
        pavel "Это хорошо, надо бы попробовать."
        "Он кинул сигарету в пепельницу. За пару тяг он дошел до самого фильтра, и уже доставал следующую из своей пачки."
        "Я же понял, что многовато в себя никотина принял, так что тоже положить докуренную до половины сигарету."

        pavel "Я люблю чистый запах табака, без всяких примесей. Только так раскрывается его уникальный вкус."
        pavel "А если всякие вишни, арбузы, а добавлять, то в чем смысл? Иди салата наверни, если фрукты так нравятся."

        sanya "Ну не всем нравится чистый запах табака, некоторые пытаются его смягчить."
        pavel "Да-а-а, и так во всем! Все что-то пытаются смягчить, замаскировать, замылить. Зачем?!"
        pavel "Почему бы не наслаждаться тем, что есть? Не зря же оно нам дано, правильно?"

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
                $ day4_drink = True
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
                $ str_for_notification = "Это действие имеет последствия..."
                show screen notification_popup_big
                with dissolve

                pause 2.0

                hide screen notification_popup_big
                with dissolve

                sanya "Извините, Пал Геннадьич, но меня там кое-кто ждем в столовой, давайте в следующий раз?"
                "Взгляд мужчины погрустнел, но он все равно протянул мне руку."
                pavel "Ничего, Саня, все нормально. Мы же тут две недели будем, еще успеется!"

                hide pavel neutral
                "С этими словами он встал, хрустнув коленями, и прошел в комнату."
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

            scene black scen
            with fade

            "Голова адски кружилась, меня штормило даже лежа."
            "Сквозь пелену и мельтешащие круги надо мной появилось обеспокоенное лицо Павла Геннадьича, а голос его доносился как из под земли."
            pavel "Санька, Санька! Ты голову расшиб!"
            "Он говорил что-то еще но я уже не слышал. Сознание постепенно затухало."
            "Ох-х-х, как же мне хуево..."
            "Перед глазами все вертелось и кружилось, а во рту будто бы насрали кошки. Причем несколько раз."
            "Живот болел так, будто бы его прострелили, а пищевод саднил, будто я хлестал кислоту, а не коньяк."
            "Нахуй я согласился?.. Щас бы сидел в столовой, пил чаек с девчонками и в ус не дул."
            
            scene medicina
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
            "Я снова не успел ответить - в рот опять что-то впрыснули, но не такие неприятное и не так резко, так что с трудом, но я смог проглотить препарат."
            sanya "Вы кто? Где я?"
            grusha "Я Агриппина Владимировна, твой ангел хранитель на случай, если опять перепьешь. А находишься ты в раю, где ставят на ноги таких как ты."
            sanya "А-а-а-а."
            grusha "Б, дурында, еще раз тут появишься - рассолом буду отпаивать. Такой молодой, а уже... эх!"
            "Бурчание продолжалось, но уже так невнятно, что разобрать было сложно."
            "С каждой минутой мне становилось все лучше и лучше."
            "По крайней мере, вертолетики кончились, да и живот не так сильно болел."
            "Наконец, я смог нормально осмотреться."
            "Обычный процедурный кабинет. В дальнем углу звенела колбами низенькая женщина, видимо, это и есть Агриппина Владимировна."

            "Обернувшись, она просканировала меня своим орлиным взглядом и что-то решив для себя сунула руку в карман."
            grusha "На! Выпьешь после обеда чтобы до конца все токсины вывести."
            sanya "Спасибо..."
            grusha "Пожалуйста, идти можешь?"
            sanya "Могу..."

            show grusha angry
            with dissolve
            
            grusha "Ну так иди нахуй отсюда!"
            "Бодро вскочив, я вылетел пробкой из процедурного кабинета."

            scene sanatorium medical post
            with fade

            "Никогда так быстро в себя после попойки не приходил, да еще и такой жесткой. Баба Груша реально волшебница!"

            "В животе заурчало, но аппетита как такового не было, поскольку чувство насранности во рту не пропало."
            "Хотелось чем-то прополоскать рот, желательно пивком..."

    scene sanatorium canteen
    with dissolve
    stop music fadeout 0.5
    play music "audio/kfc-sound.mp3" fadein 1.0 fadeout 2.0 volume 0.2

    "Зайдя в столовую, я сразу почувствовал приятный запах котлеток."
    "Тут было немноголюдно, так что свободных столов было навалом. Видимо, некоторые решили пропустить в этот раз обед и отдохнуть с дороги."
    "Впрочем, я их понимал."
    "Сегодня подавали самое классическое блюдо из всех возможных: котлетку с пюрешкой, от которых поднимался пар."
    "Кружка ароматного кофейного напитка или какао на выбор, пара кусочков хлеба с маслом и салат цезарь, с ощутимыми кусочками жареной курицы."
    "Как бы слюной не истечь пока несу..."
    sanya "Балдёж!..."
    "Поместив пищу на поднос, я осмотрелся выбирая, куда сесть. Места было много, но в одиночестве сидеть не хотелось."
    "В дальнем углу приметил Юлю, сидящую в одиночестве, а также Надю, которая сидела в противоположной стороне у окна, и тоже, к счастью, одна."
    "К кому бы мне подсесть?"
    
    menu:
        "Подсяду к Юле":
            $ day4_yuli_meal = True
            $ str_for_notification = "Это действие имеет последствия..."

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
            
            yuli "Прости, я немного отвлеклась и потеряла группу. Пришлось самой все осматривать."
            sanya "А-а-а, ну, ничего, я тогда давай позже тебе все покажу? После процедур можем погулять."

            show yuli happy
            with dissolve

            yuli "Да конечно,  я только рада буду."
            "На этой ноте наша небольшая беседа подошла к концу и мы оба принялись за еду."
            "Ну что сказать, еда тут знатная! Давненько я не ел такой вкусной котлетки, а пюрешка вообще во рту таяла!"
            "Идеально соленая, без комочков с приятным молочным послевкусием."
            "Масло, уже успевшее подтаять легко размазалось по ароматному, еще теплому хлебу, наверное, его пекут прямо здесь."
            "А салатик идеально сочетал в себе свои ингредиенты и этот баланс создавал прекрасную гармонию вкуса."
            
            play sound "audio/deep-moan.mp3" fadein 0.2 fadeout 0.2
            "Откинувшись на спинку стула, я с удовольствием выдохнул, чувствуя приятную сытость."
            pause 1.0

            "Сверху шлифанул плотным какао, не слишком сладким и не водянистым, прямо как я люблю!"
            
            sanya "Блаженство, не ожидал что еда здесь будет настолько вкусная."
            pause 2.0

            yuli "И не говори."
            "Мы оба развалились на стульях и потягивали наши напитки, наслаждаясь обществом друг друга."
            sanya "Как говорит один мой друг: после сытного обеда, по законам Архимеда..."
            
            show yuli happy
            with dissolve

            yuli "Чтобы жиром не заплыть - надо срочно покурить!"
            "Закончила за меня Юля и звонко рассмеялась. Я невольно залюбовался ее искренней улыбкой, что так мягко сияла на нежно девичьем личике."
            sanya "Точняк! Ты не против составить мне компанию?"
            yuli "Не против, пойдем проветримся."
            "Она протянула мне руку и я с радостью взял ее."
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

            play music "audio/forest-sound.mp3" fadein 0.3 fadeout 0.3 volume 0.3

            "Ей служила отдаленная беседка на живописном берегу реки. На столе стояли пепельницы, однако в них не было ни одного окурка."
            "Видимо, это место пользуется особой популярностью."
            play sound "audio/cigarette.mp3" fadein 0.2 fadeout 0.2
            "Достав сигаретку, я закурил."
            pause 3.0

            show yuli empathy
            with dissolve
            
            yuli "Как тебе тут?"
            sanya "Ну, пока сложно сказать... В целом, нравиться. Чистый воздух, вкусная еда."
            sanya "Скоро всякие процедуры начнутся. Поживем-увидим, как говорится."
            
            yuli "Тут очень спокойно и тихо. После шумного и грязного города - истинное наслаждение."
            sanya "И не говори..."
            "Так, в тишине, в которой так нуждались, мы и пробыли пару минут, пока я докуривал."
            
            show yuli shy
            with dissolve

            yuli "Ладно, мне уже пора. Скоро процедуры. Может тогда вечером у меня встретимся?"
            sanya "Конечно, я только за."
            yuli "Тогда, до вечера?"

            show yuli horny
            with dissolve

            yuli "До вечера..."
            "На прощание мы крепко обнялись, замерев так на несколько минут."
            "Никто не хотел отстраняться первым, но нам пришлось."
            "Режим есть режим, так что попрощавшись, мы разбрелись в разные стороны."

        "Подсяду к Наде":
            $ day4_nadya_meal = True
            $ str_for_notification = "Это действие имеет последствия..."

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

            nadya "Да конечно, я только рада буду."
            "На этой ноте наша небольшая беседа подошла к концу и мы оба принялись за еду."
            
            "Ну что сказать, еда тут знатная! Давненько я не ел такой вкусной котлетки, а пюрешка вообще во рту таяла!"
            "Идеально соленая, без комочков с приятным молочным послевкусием."
            "Масло, уже успевшее подтаять легко размазалось по ароматному, еще теплому хлебу, наверное, его пекут прямо здесь."
            "А салатик идеально сочетал в себе свои ингредиенты и этот баланс создавал прекрасную гармонию вкуса."
            
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
            
            nadya "Чтобы жиром не заплыть - надо срочно покурить!"
            "Закончила за меня Юля и звонко рассмеялась. Я невольно залюбовался ее искренней улыбкой, что так мягко сияла на нежно девичьем личике."
            sanya "Точняк! Ты не против составить мне компанию?"
            
            show nadya smiles
            with dissolve

            nadya "Не против, пойдем проветримся."
            "Она протянула мне руку и я с радостью взял ее."
            
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

            "Ей служила отдаленная беседка на живописном берегу реки. На столе стояли пепельницы, однако в них не было ни одного окурка."
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
            sanya "Скоро всякие процедуры начнутся Поживем-увидим, как говорится."
            nadya "Тут очень спокойно и тихо. После шумного и грязного города - истинное наслаждение."
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
        "По пути на процедуры, вспомнил про таблетку. Забежав в столовую, кинул ее в рот и запил водой из под крана."
        
        "Ну вот! Другое дело, теперь можно и в грязевую ванную залезть, и зонд в жопу засунуть."
        "Шутка! "
        extend "Надеюсь..."
        
        scene black 
        with Fade(0.2, 0.3, 0.2, color="#000")
   
        if day4_yuli_meal:
            "Процедуры оказались... "
            extend "довольно приятными."
            "Горячая сауна, грязевая ванна, массажик, пускай делала его и не сексапильная девочка, а огромная женщина, руки которой были толщиной с мою голову."
            "А также прочие приколдесы, после которых ты чувствуешь себя человеком."
            
            scene sanatorium evening park
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Расслабленный, отдохнувший и довольный я шел по парку в сторону курилки, намереваясь шлифануть все ароматной сигареткой чапмана, и провести время в компании прекрасной девушки."
            "Эх, жить хорошо и жизнь хороша!"

            scene sanatorium alcove
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Зайдя в пустующую курилку, я присел на лавочку и, любуясь открывающимися видами, открыл стремительно пустующую пачку."
            sanya "Жить - пиздато!"
            "Однако шел час, второй. Пачка пустела, а Юля все не приходила."
            
            "Не вытерпев, я пошел искать ее."
            
            scene sanatorium evening park
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Прошелся по парку, заглядывая во всякие укромные места. Пошел к корпусу, надеясь встретить ее по пути. Но ни в парке, ни в корпусе не было и следа моего романтического интереса. "
            "Отчаявшись, я даже спросил парочку встречных, не видели ли они девушку, похожую на нее. Большинство просто пожимало плечами."

            scene sanatorium night
            with Fade(0.2, 0.3, 0.2, color="#000")

            "Расстроившись, я вышел из корпуса на свежий воздух. Достал из пачки последнюю сигарету, и поднес ко рту."
            noname "Эй! Здесь нельзя курить!"
            "Обернувшись, я увидел какую-то тетку в белом халате. Раздраженно выдохнув, убрал сигарету обратно."
            
            menu :
                "Сижка излечит меня" :
                    $ day4_siggaret_or_room = True
                "Пойду посплю..." :
                    $ day4_siggaret_or_room = False
            
            if day4_siggaret_or_room:

                scene black
                with Fade(0.2, 0.3, 0.2, color="#000")

                "Хотелось побыть одному, в комнате сто процентов был Павел Геннадьевич, так что выбор пал на курилку. Там обычно никого не было, да и созерцание красивых видов успокаивает."
                "Так что кинув прощальный взгляд на злую тетку, не разрешающую курить где попало, я медленно побрел в свое сакральное место."

                scene sanatorium evening park
                with Fade(0.2, 0.3, 0.2, color="#000")

                "Топая по красивому парку, я размышлял о тленности жизни и бессмысленности существования. Исчезновение Юли больно ударило по настроению и самооценке, что сказывалось и на \"светлости моего лика\"."
                "Думаю, такой хмурой рожи у меня давненько не было. Наверное, если я посмотрюсь в зеркало - оно треснет нахуй."
                noname "Извини, у тебя что-то случилось?"
                "Тоненький голосок, раздавшийся сзади, застал меня врасплох. Неловко дернувшись, я обернулся."
                "Огромными глазищами снизу вверх на меня смотрела симпатичная девушка с розовыми волосами. Причем волосы были столь искусно покрашены, что казалось, будто это их настоящий цвет."
                sanya "Что-что, извини?"
                noname "У тебя что-то случилось? Выглядишь грустным"
                "Она спросила это настолько искренне, что я растерялся. Никогда не думал, что люди могут обращаться так к незнакомцу."

                menu :
                    "Ебать мусорка, пойду мимо." :

                        $ day4_go_with_emili = False

                        "Мне льстило, что о моем психическом здоровье кто-то поинтересовался, но слишком уж много девушек за последнее время сделали мне от ворот поворот, не хочется обжигаться снова. "
                        "Оставив розоволосую позади, я поспешил в курилку."

                        if day4_drink:

                            play sound "audio/cigarette.mp3" fadein 2.0 fadeout 2.0 

                            "Кажется, эта беседка становится мне роднее дома. Сев на скамейку, я закурил."
                            "Первая глубокая тяжка немного прочистила сознание, освободив места для разных мыслей. Далеко не самых приятных."

                            play music "audio/Love.mp3" fadein 2.0 fadeout 2.0 volume 0.1

                            pavel "О, какие люди, я думал ты в медблоке отлеживаешься." 
                            "Я хмыкнул."
                            sanya "Баба Груша настоящая волшебница."
                            pavel "Это врач местный?"
                            sanya "Да, не слишком приветливая, зато лечит хорошо."
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
                            
                            show pavel smile
                            with dissolve
                            
                            pavel "Нет. Мы начинаем их придумывать из воздуха, потому что нам становиться скучно."
                            pavel "У взрослых, на самом деле, не так много развлечений."
                            sanya "И смысл тогда в такой жизни?"
                            pavel "Огромный. Ты стремишься жить без проблем, постоянно их наживая. Ты решаешь их, создавая новые, решаешь уже их и так далее."
                            pavel "Это замкнутый круг, уроборос во плоти. Вечный дискомфорт и вечное развитие. Разве не в этом смысл жизни?" 
                            pavel "Проходить испытания для создания лучшей версии себя?"
                            sanya "Не все нравятся трудности. Иногда людям хочется обычного комфорта."
                            pavel "Возможно. Однако обычно такие люди долго не живут. Естественный отбор в действии."
                            sanya "Я думаю, это работает немного не так..."
                            pavel "Считай как знаешь. В любом случае помни, что жизнь это сплошные испытания и их преодоления." 
                            pavel "И миг, когда ты проходишь определенный порог - твоя лучшая награда."
                            sanya "Сомнительное удовольствие"
                            pavel "Вот и узнаешь."
                            "Павел Геннадьевич затушил сигарету и поднялся."
                            pavel "Не вешай нос, студент. В мире миллионы свободных девушек, открытых к предложениям." 
                            pavel "В мире миллион возможностей. Конечно, иногда непросто осознать это или даже отпустить человека, но всегда держи это в голове. Бывай, я пойду прогуляюсь."
                            "Мужчина сунул руки в карманы и вышел из беседки."
                            "Посидев еще немного, я выбросил окурок и пошел в сторону корпуса."
                            "Жизнь - миллион возможностей. Надо просто осознать это."
                            "Эти мысли вертелись у меня все время, пока я шел в корпус. С этой мыслью я ложился в кровать. Эта мысль была последней перед сном."
                            "Она стала моей мантрой. Она стала той ниточкой, что держала мое настроение в \"зеленой зоне\"."
                            "Нужно просто осознать..."

                            stop music
                            jump _day5

                        else:
                            scene sanatorium alcove
                            with Fade(0.2, 0.3, 0.2, color="#000")
                            
                            "Кажется, эта беседка становится мне роднее дома. Сев на скамейку, я закурил. Первая глубокая тяжка немного прочистила сознание, освободив места для разных мыслей. Далеко не самых приятных."

                            play sound "audio/cigarette.mp3" fadein 2.0 fadeout 2.0 

                            show pasha smile:
                                xpos 1.0
                                linear 0.7 xalign 0.5
                            with dissolve

                            play music "audio/Love.mp3" fadein 2.0 fadeout 2.0 volume 0.1

                            pavel "О, какие люди"
                            "Я хмыкнул."
                            sanya "Баба Груша настоящая волшебница"
                            pavel "Это врач местный?"
                            sanya "Да, не слишком приветливая, зато лечит хорошо"
                            "Павел Геннадьевич сел рядом, достав свою пачку красного Мальборо. "
                            pavel "Выглядишь мрачно"
                            sanya "Со всеми бывает"
                            pavel "Не поспоришь"
                            "Помолчали. Каждый думал о своем, смотря на природу. "
                            pavel "Когда я был в твоем возрасте, после каждой более-менее серьезной проблемы мне казалось, что жизнь окончена. Однако стоило немного подумать, приложить усилия, как решение находилось."
                            pavel "И так всю жизнь. Кажется, что жизнь сложна. Ну, отчасти так и есть, каждый день приходится решать кучу маленьких и больших проблем, однако это входит в привычку и не доставляет особых неудобств. "
                            sanya "А что, без проблем жить совсем нельзя?"
                            pavel "Нет. Мы начинаем их придумывать из воздуха, потому что нам становиться скучно. У взрослых, на самом деле, не так много развлечений"
                            sanya "И смысл тогда в такой жизни?"
                            pavel "Огромный. Ты стремишься жить без проблем, постоянно их наживая. Ты решаешь их, создавая новые, решаешь уже их и так далее. Это замкнутый круг, уроборос во плоти. Вечный дискомфорт и вечное развитие."
                            pavel "Разве не в этом смысл жизни? Проходить испытания для создания лучшей версии себя?"
                            sanya "Не все нравятся трудности. Иногда людям хочется обычного комфорта"
                            pavel "Возможно. Однако обычно такие люди долго не живут. Естественный отбор в действии"
                            sanya "Я думаю, это работает немного не так..."
                            pavel "Считай как знаешь. В любом случае помни, что жизнь это сплошные испытания и их преодоления. И миг, когда ты проходишь определенный порог - твоя лучшая награда"
                            sanya "Сомнительное удовольствие"
                            pavel "Вот и узнаешь"
                            "Павел Геннадьевич затушил сигарету и поднялся."
                            pavel "Не вешай нос, студент. В мире миллионы свободных девушек, открытых к предложениям. В мире миллион возможностей."
                            pavel "Конечно, иногда непросто осознать это или даже отпустить человека, но всегда держи это в голове. Бывай, я пойду прогуляюсь"
                            "Мужчина сунул руки в карманы и вышел из беседки. Посидев еще немного, я выбросил окурок и пошел в сторону корпуса."
                            "Жизнь - миллион возможностей. Надо просто осознать это. "
                            "Эти мысли вертелись у меня все время, пока я шел в корпус. С этой мыслью я ложился в кровать. Эта мысль была последней перед сном."
                            "Она стала моей мантрой. Она стала той ниточкой, что держала мое настроение в \"зеленой зоне\"."
                            "Нужно просто осознать..."

                            stop music
                            jump _day5

                        if day4_move:   
                            
                            scene sanatorium balcony night
                            with Fade(0.2, 0.3, 0.2, color="#000")
                            
                            play music "audio/Love.mp3" fadein 1.5 fadeout 2.5 volume 0.15
                            
                            "Смеркалось. Был поздний вечер и солнце уже почти закатилось за горизонт. Сквозь темнеющее небо пробивались первые, самые яркие звезды. А может быть лишь их предсмертный свет, созданный взрывом."
                            "Звезды действительно достойны восхищения. Даже после смерти, многие годы их свет виден нам. Возможно, некоторые из них умерли тысячелетия назад, а мы все еще их видим, думаем о них."
                            "В сравнении с ними смерть человека - пустота. Ничего.  Меньше чем миг, меньше чем ноль."
                            "Даже вся эта бравада, про память и пока нас помнят - мы живы полнейший бред."
                            "О звездах не помнят. Звезды видят и они кажутся живыми. Человек жив, пока его видит и его видят. А воспоминания о нем... Они такие же эфемерные."
                            "Субъективные. Это ведь даже не слепок, не фото. Это частичка, которую к тому же можно трактовать совершенно по-разному."
                            "Можно ли это назвать жизнью после смерти? Нет. Очевидно, что нет."
                            "От сигареты осталась половина."
                            "Звезд на небе стало больше."
                            "Я подошел к окну."
                            "Темно."
                            "Глядя в небесную бесконечность, я думал над тем, что мне делать дальше. Какая вообще у меня жизненная цель?"
                            "Отучиться, получить работу? А дальше? В чем смысл этого? Зачем мне это нужно?"
                            "Каждый день по восемь часов пахать, чтобы в конце месяца получить зарплату. Потом слить ее быстрые удовольствия и все по новой."
                            "У меня нет хобби, нет собственной семьи, да и появится она вообще у меня?"
                            "Та девушка, с которой я действительно захочу прожить жизнь. А не вариант попроще, как у сотен других."
                            "Какое же дерьмо... Двадцать лет жизни... Кажется, так мало, только начал жить, но по факту..."
                            "Кажется, я уже заруинил свои характеристики персонажа и мне придётся жить на костылях всю мою жизнь."
                            "Сигарета дотлела. Дотлели и мои мысли. Полностью опустошенный и разбитый я выкинул бычок."
                            "Навалилась ужасная усталость, но пересиливая себя я побрел в корпус."
                            "Жить - пиздато. Пизже некуда."
                            
                            stop music fadeout 3.0
                            jump _day5

                    "Может... Поболтать?" :

                        $ day4_go_with_emili = True
                        
                        sanya "Да так..." 
                        "Я смутился и отвел взгляд от огромных голубых глазищ, которые, казалось, отражали само небо. "
                        noname "Если ты хочешь, я могу тебя выслушать!" 
                        sanya "Э-э-э..."
                        noname "Но я, конечно, не заставляю!"
                        sanya "Спасибо..."
                        noname "Меня Эмилия зовут!"
                        sanya "Саша..."
                        emili "Приятно познакомиться! Так что у тебя случилось?"
                        "Я, конечно, не выложил Эмилии все как есть. Обтекаемыми фразами, не вдаваясь в подробности рассказал о насущных проблемах."
                        "И, удивительно, но мне стало немного легче. Впервые, за долгое время я почувствовал, что кому-то не плевать на меня."
                        "Тем страннее, что этот кто-то первая встречная девушка. "
                        "Эмилия тоже немного рассказала о себе. Рассказ, к слову, вышел как бы не грустнее моего."
                        "Строгие родители, отсутствие свободного выбора, распланированная жизнь и дни по жесткому режиму."
                        "Поездка в санаторий стала небольшой отдушиной для девушки, где можно немного отдохнуть от постоянной учебы и тирании родителей. "
                        "Будучи стеснительной, но до ужаса сердобольной она не смогла пройти мимо хмурого меня."
                        "Однако сама растерявшись от своей смелости, решила действовать весьма напористо. Что, в общем-то, не было плохо. "
                        "Она оказалось классной и веселой девушкой, так что настроение начало подниматься из глубин моего внутреннего мира. "
                        "Придя в курилку и зависнув там, мы обсуждали совершенно разные темы, порой, даже с неожиданным жаром для тех, кто был незнаком до этого. "
                        sanya "Ты правда никогда раньше не пила алкоголь?"
                        "Моему удивлению не было предела. "
                        sanya "Тебе же уже двадцать!"
                        emili "Мне мама запрещает..." 
                        "Смущается она, конечно, убийственно мило. "
                        sanya "Но ведь тебе двадцать! Ты же можешь просто уйти из дома и делать все, что захочешь"
                        "Эмилия на это лишь грустно улыбнулась, медленно покачав головой. "
                        "Поняв, что это не лучшая тема для разговора, я поспешил ее сменить. "
                        sanya "А в шаурму ты ела?" 
                        "Еба-а-а-а-а, а а еще тупее вопрос не мог задать? "
                        "Девушка смутилась, став расправлять складки платья на коленях."
                        emili "Нет, но мне подружка сказала, что она очень вкусная"
                        sanya "Ты серьезно не ела шаурму?"
                        "Моему удивлению не было предела. "
                        "Эмилия покачала головой."
                        emili "У меня диета. Я кушаю только дома..."
                        sanya "Капец, подруга, твоя жизнь проходит зря! Как только выйдем отсюда, я тебе покажу насколько прекрасна юность и шаурма!" 
                        emili "Ловлю на слове!" 
                        "Эмилия звонко рассмеялась. Потом чуть грустно произнесла:"
                        emili "Надеюсь, мы сможем видеться, когда я вернусь на учебу..." 
                        sanya "Пф! Конечно! Как говориться, кто школу... то есть универ не гулял, тот жизни не видал! В конце, концов, впереди новогодние каникулы, да и выходные есть"
                        emili "Ну да"
                        "Эмилия вновь улыбнулась, но глаза ее остались грустными."
                        "Не желая больше расстраивать новую знакомую, я перевел разговор на более приятные темы. Но зарубку себе в памяти сделал - во что бы то не стало найти Эмилию после санатория и угостить ее шаурмой!"
                        "Сгущались сумерки, солнце заходило за горизонт, но мы продолжали болтать. "
                        "Лишь когда Эмили начала зевать и клевать носом, мы поняли, что пора закругляться. "
                        "Дойдя до корпуса, мы тепло попрощались, направившись в разные стороны. Настроение возвратилось в норму, курить совсем-совсем не хотелось."
                        "Вдохнув пьянящий ночной воздух, я улыбнулся сам себе и новой встрече. "
                        "Жизнь - продолжается! "

                        jump _day5

            else :
                
                "Идти никуда не хотелось. Настроение упало в ноль, так что я поплелся в свою комнату."

                scene sanatorium walkway
                with Fade(0.4, 0.3, 0.7, color="#000")

                scene sanatorium dormitory room
                with Fade(0.4, 0.3, 0.7, color="#000")

                "Павла Геннадьевича не было, что немного меня порадовало. Видеть никого не хотелось. Пройдя на балкон, я упал в кресло и достал последнюю сигарету чапы."

                scene sanatorium balcony night
                with Fade(0.3, 0.4, 0.3, color="#000")

                play music "audio/Love.mp3" fadein 1.5 fadeout 2.5 volume 0.15

                "Смеркалось. Был поздний вечер и солнце уже почти закатилось за горизонт. Сквозь темнеющее небо пробивались первые, самые яркие звезды. А может быть лишь их предсмертный свет, созданный взрывом. "
                "Звезды действительно достойны восхищения. Даже после смерти, многие годы их свет виден нам. Возможно, некоторые из них умерли тысячелетия назад, а мы все еще их видим, думаем о них. "
                "В сравнении с ними смерть человека - пустота. Ничего. Меньше чем миг, меньше чем ноль."
                "Даже вся эта бравада, про память и пока нас помнят - мы живы полнейший бред."
                "О звездах не помнят. Звезды видят и они кажутся живыми. Человек жив, пока он видит и его видят. А воспоминания о нем..."
                "Они такие же эфемерные. Субъективные. Это ведь даже не слепок, не фото."
                "Это частичка, которую к тому же можно трактовать совершенно по-разному."
                "Можно ли это назвать жизнью после смерти? Нет. Очевидно, что нет."
                "От сигареты осталась половина."
                "Звезд на небе стало больше."
                "Я подошел к краю балкона."
                "Темно."
                "Глядя в небесную бесконечность, я думал над тем, что мне делать дальше. Какая вообще у меня жизненная цель?"
                "Отучиться, получить работу? А дальше? В чем смысл этого? Зачем мне это нужно?"
                "Каждый день по восемь часов пахать, чтобы в конце месяца получить зарплату. Потом слить ее быстрые удовольствия и все по новой."
                "У меня нет хобби, нет собственной семьи, да и появится она вообще у меня?"
                "Та девушка, с которой я действительно захочу прожить жизнь. А не вариант попроще, как у сотен других."
                "Какое же дерьмо... Двадцать лет жизни... Кажется, так мало, только начал жить, но по факту... Кажется, я уже заруинил свои характеристики персонажа и мне придётся жить на костылях всю мою жизнь. "
                "Или не придется?"
                "Сигарета почти догорела, бычок жег пальцы, но я не обратил на это внимание."
                "Облокотился на бортик балкона."
                "Я ничего не хочу. Ни искать смысл жизни, ни что-то еще."
                "Я просто хочу, чтобы все это закончилось. Может даже сейчас."
                
                stop music fadeout 3.0
                "Просто перенести усилие чуть вперед и мое бессмысленное существование наконец закончиться."

                play music "audio/heart.mp3" fadein 1.0 fadeout 2.0 volume 0.2
                show screen toska
                
                menu :
                    "Шаг вперед." :
                        $ day4_suicide = True
                    "Пойти спать" :
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
                    
                    scene sanatorium dormitory room
                    with Fade(0.2, 0.3, 0.2, color="#000")
                    
                    sanya "Какой же я долбоеб."
                    "Как ни странно, но это придало мне сил. С мрачными мыслями и плохим настроением, я все же смог уснуть."

                    jump _day5
                else :
                    "Темнота внизу зачаровывала. И в этой темноте появилось лицо родителей и Пашки."
                    sanya "Блять!.."

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
            "Процедуры оказались..."
            extend "довольно приятными."
            play music "audio/love_music.mp3" fadein 2.0 fadeout 2.0 volume 0.3
            
            scene sanatorium evening park
            with Fade(0.4, 0.5, 0.4, color="#000")

            "Горячая сауна, грязевая ванна, массажик, пускай делала его и не сексапильная девочка, а огромная женщина, руки которой были толщиной с мою голову."
            "А также прочие приколдесы, после которых ты чувствуешь себя человеком."
            
            play sound "audio/footsteps_asphalt.mp3" noloop fadein 0.2 fadeout 0.2
            "Расслабленный, отдохнувший и довольный я шел по парку в сторону курилки, намереваясь шлифануть все ароматной сигареткой чапмана, и провести время в компании прекрасной девушки."
                        
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
            nadya "Настроение хорошее просто"
            "Мы обнялись, когда она зашла в беседку, и плюхнулись на лавочку."
            "Надя тут же достала свою пачку ванильного Чапмана."
            sanya "Кто бы говорил."
            "Я кивнул на сигареты в ее руках, на что она лишь неловко пожала плечами."

            show nadya empathy
            with dissolve

            nadya "Ну, рассказывай, как твой день прошел"
            sanya "Да че рассказывать, обычный день..."
            "Удивительно, но вот этого неловкого чувства, будто разговариваю с красивой девушкой, не было."
            "Было так же комфортно, как, например, на посиделках с пацанами или с тем же Пашкой."
            "Когда мы выходили на улицу, чтобы перекурить и перетереть. Свободное общение, простые темы." 
            "Все что нужно, чтобы скинуть лишнее эмоциональное напряжение и расслабиться."
            sanya "Ты думала, чем будешь заниматься после университета?"
            nadya "Не-а. Я, если честно, и поступила-то сюда, потому что тут балл невысокий был, а я читать люблю." 
            nadya "Но, как это обычно бывает, ожидания не совпали с реальностью. Эта лингвистика, как оказывается, мало похожа на литературу"
            "Она рассмеялась."
            nadya "Думаю поработаю в кофейне, родители, если что, помогут. А там, может быть, пройду курсы сценаристики или там режиссера какого-нибудь. Посмотрим, в общем, впереди еще куча времени, чтобы понять, чем заняться по жизни"
            sanya "Ты удивительно легко относишься к этому"

            show nadya neutral
            with dissolve

            nadya "В смысле?"
            sanya "Все девушки, с которыми я общался конкретно так заморачиваются насчет своего будущего."
            sanya "Типа вот я отучусь, потом туда, через год сюда, замуж дети или там карьера, путешествия, слава и прочее"
            "Она пожала плечами"
            
            show nadya smiles
            with dissolve

            nadya "Я просто пока не знаю, чего хочу от жизни." 
            nadya "Я не очень люблю путешествовать. Это, конечно, интересно, но лично для меня тяжело." 
            nadya "Работать и делать карьеру хочется в том, деле, которое интересно, иначе какой смысл?" 
            nadya "Работать на нелюбимой работе - это какой-то особенный вид мазохизма, по-моему." 
            nadya "Мы еще молоды, нам свойственно искать свой путь, нынешние реалии это позволяют"
            "Я молча кивнул. Действительно, в наших реалиях мы еще можем подумать о том, чем заняться в жизни. У наших родителей, такой возможности не было."
            nadya "А ты чем планируешь заниматься?"
            sanya "Может пойду работать по профессии, может в армию, может еще куда-нибудь. Пока не знаю"

            show nadya giggles
            with dissolve

            nadya "В общем, как и у всех сверстников наших."
            nadya "Не знаю, плохо это или хорошо, что мы в двадцать все еще не можем определиться с жизненным путем." 
            nadya "Меня мама родила в девятнадцать, папа уже тогда работал." 
            nadya "И вот, я на год старше своей тогдашней мамы, но ни отношений, ни планов на жизнь у меня нет"
            "Я вспомнил парня, который нес сумки Нади, и осторожно спросил:"
            sanya "Кстати, на экскурсии, я видел, что твою сумку нес какой-то парень..."
            nadya "Это парень моей подруги, они сюда вдвоем приехали. Он наши сумки нес."
            sanya "А"

            show nadya flirting
            with dissolve
            
            nadya "А что это ты спросил? Ревнуешь?"
            sanya "Ну разве что чуть-чуть"
            "Смущенно пробормотал я, желая увидеть реакцию девушки."
            "Надя же сначала чуть покраснела, а потом, видя мою красную мину, звонко рассмеялась." 
            "Закончив, она утерла выступившие в уголках глаз слезы и наклонилась чуть ближе к моему лицу."
            
            show nadya flirting
            with dissolve

            nadya "Пока ты ближе всех подобрался к роли моего парня"
            "Она произнесла это таким чарующим голосом, что у меня по спине пробежали мурашки, а в штанах началось бодрое шевеление."
            "Однако, не растерявшись, я наклонился в ответ."
            sanya "Это радует"
            "Мы смотрели друг на друга пару секунд. Пара секунд в сантиметре друг от друга. Очень волнительные пару секунд."
            "Одновременно отпрянув друг от друга, мы смущенно посмотрели в стороны."

            show nadya smyshyaetsya
            with dissolve

            nadya "Холодает..."
            sanya "Есть немного... Может, в корпус?"
            nadya "Пойдем."
            "Пока мы шли до корпуса, то не проронили ни единого слова. Атмосфера неловкости, царящая между нами, как-то не настраивала на беседу."
            "Однако эта неловкость была какой-то романтичной..."

            show nadya smiles
            with dissolve
            
            nadya "Спасибо, что погулял со мной"
            sanya "Тебе спасибо, было весело"
            "Мы постояли, смотря в стороны. Вдруг Надя взяла меня за футболку и притянула к себе, чмокнув в щеку. И тут же, не оборачиваясь и не смотря на меня прошмыгнула в свою комнату."
            "От неожиданности я впал в ступор. Отмерев, я потер щеку, которую поцеловала Надя."
            sanya "День закончился определенно удачно..."
            "По-дурацки улыбаясь, я пошел в комнату."
            "Жить - пиздато!"

            jump _day5
    else:
        "Процедуры оказались... "
        extend "довольно приятными."
        "Горячая сауна, грязевая ванна, массажик, пускай делала его и не сексапильная девочка, а огромная женщина, руки которой были толщиной с мою голову."
        "А также прочие приколдесы, после которых ты чувствуешь себя человеком."
        "Расслабленный, отдохнувший и довольный я шел по парку в сторону курилки, намереваясь шлифануть все ароматной сигареткой чапмана, и провести время в компании прекрасной девушки."
        "Эх, жить хорошо и жизнь хороша!"

        scene sanatorium alcove
        with Fade(0.2, 0.3, 0.2, color="#000")

        "Зайдя в пустующую курилку, я присел на лавочку и, любуясь открывающимися видами, открыл стремительно пустующую пачку."
        sanya "Жить - пиздато!"

        noname "Скучал?"

        play music "audio/love_music.mp3" fadein 4.0 fadeout 2.0 volume 0.3
        show yuli greeting
        with dissolve

        "Я обернулся на голос, улицезрев одетую в легкий сарафан Юлю, которая легко мне улыбалась."
        "У меня защемило сердце от ее красоты, и я, повинуясь наитию, выпалил..."
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
        "П - продуманность!"
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
        
        # TODO (возможно поменять)
        play music "audio/heart.mp3" fadein 3.0 fadeout 2.0 volume 0.1
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

        show screen toska
        with dissolve

        show yuli empty
        with dissolve

        yuli "Саша?"
        "По телу пробежали мурашки от того, насколько она была... не Юлей."        
        yuli "Саша?"
        "Она произнесла это не открывая рта и не моргая, смотря как будто бы сквозь меня."
        "Отсутствующий, скорее даже мертвый взгляд."
        
        show yuli empty glitch
        with dissolve 
        
        yuli "Саша?"
        yuli "СашаСашаСашаСашаСашаСашаСашаСаша СашаСашаСашаСашаСашаСашаСашаСаша СашаСашаСашаСашаСашаСашаСаша"
        sanya "кх-къх"

        "Крик застрял в горле."
        "Воздух сгустился и перестал быть прозрачным. Черные щупальца потянулись ко мне их тумана, в который он превратился."
        "Дыхание становилось быстрее и быстрее с каждой секундой. Сердце, казалось, сломает грудную клетку."
        "Туман подползал ближе. Лицо Юли становилось ближе."
        
        hide screen toska
        with dissolve
        scene black
        with Fade(0.2, 0.3, 0.2, color="#000")
        
        show yuli empty glitch at center:
            zoom 1.4
            ypos 1.3
        with dissolve 

        "Паническая атака накрыла с головой и я забыл как дышать. Чувства отключились и я словно попал в сонный паралич."
        "Перед глазами - мертвое лицо Юли."
        "Кислородное голодание - я теряю сознание."
        stop music fadeout 3.0

        jump _day5

label _day5 :

    if day4_suicide :
        "Утро красит нежным светом... стены санатория. На новом месте спалось неплохо. Хотя ночь выдалась... Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."
        
        if day4_move and (day4_smoke_old_siggarete or not day4_smoke_old_siggarete) :

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
        
        "Потянувшись, я вышел на балкон."

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 2.5

        scene sanatorium balcony
        with dissolve

        "Прохладный свежий воздух взбодрил. Пускай сейчас начало сентября, но погода держалась все еще летняя. Хотя ночами и утром было довольно прохладно. Листья пока только начали желтеть и в основном везде было зелено. Красота! "
        "Вдохнув полной грудью пьянящий лесной воздух, я посмотрел вниз. "
        sanya "В темноте земля казалась дальше..." 
        "Зайдя внутрь, пошел выполнять утренние процедуры. До завтрака еще пара часов, так что торопиться некуда."

        stop music
    
    if day4_nadya_meal :
        "Утро красит нежным светом... стены санатория. На новом месте спалось неплохо. Хотя ночь выдалась... Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."

        if day4_move and (day4_smoke_old_siggarete or not day4_smoke_old_siggarete) :

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
        
        "Потянувшись, я вышел на балкон."

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 2.5

        scene sanatorium balcony
        with dissolve

        "Прохладный свежий воздух взбодрил. Пускай сейчас начало сентября, но погода держалась все еще летняя."
        "Хотя ночами и утром было довольно прохладно. Листья пока только начали желтеть и в основном везде было зелено. Красота!"

        stop music
    
    if day4_go_with_emili :
        "Утро красит нежным светом... стены санатория. На новом месте спалось неплохо. Хотя ночь выдалась... Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."

        if day4_move and (day4_smoke_old_siggarete or not day4_smoke_old_siggarete) :

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

        "Потянувшись, я вышел на балкон."

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 2.5

        scene sanatorium balcony
        with dissolve

        "Прохладный свежий воздух взбодрил. Пускай сейчас начало сентября, но погода держалась все еще летняя."
        "Хотя ночами и утром было довольно прохладно. Листья пока только начали желтеть и в основном везде было зелено. Красота!"

        stop music
    
    if not day4_go_with_emili and (day4_drink or not day4_drink) :
        "Утро красит нежным светом... стены санатория. На новом месте спалось неплохо. Хотя ночь выдалась... Не самой приятной."
        "Проснувшись на рассвете от лучика солнца на своем лице, я зажмурился и открыл глаза."

        if day4_move and (day4_smoke_old_siggarete or not day4_smoke_old_siggarete) :

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

        play music "audio/home-sad.mp3" fadein 1.5 fadeout 2.0 volume 2.5

        scene sanatorium balcony
        with dissolve

        "Прохладный свежий воздух взбодрил. Пускай сейчас начало сентября, но погода держалась все еще летняя."
        "Хотя ночами и утром было довольно прохладно. Листья пока только начали желтеть и в основном везде было зелено. Красота!"

        stop music

    
label _end :
    scene black scen
    with fade
    
    pause 5.0

    centered "{size=+24}Участие принимали:\nAsind,\nDarlingInSteam,\nDanilka108,\nXpomin,\nTheNorth,\nArtsBer,\nJuravl"
    centered "{size=+24}Asind:\nМини-игры, арты, музыка, диалоги первого дня."
    centered "{size=+24}DarlingInSteam:\nИмплементация сценария в код, арты, музыка, диалоги второго дня."
    centered "{size=+24}Danilka108:\nМини-игры, работа с нейросетью, покушал."
    centered "{size=+24}TheNorth:\nСценарий, диалоги второго и третьего дня.\nКод, сценарий, звуки четвертого дня.\nБог, блять"
    centered "{size=+24}Xpomin:\nСобрал шкаф, собрал компьютер, сценарий, диалоги второго и третьего дня."
    centered "{size=+24}ArtsBer:\nУстал, писал сценарий, устал писать сценарий."
    centered "{size=+24}Juravl:\nФоновые звуки, саунды."
    centered "{size=+24}В разделе \"Об игре\" можно найти ссылку на репозиторий GitHub."
    centered "{size=+24}Спасибо за прохождение данной новеллы. Мы благодарны за Ваше внимание."