define sanya = Character('Саня', color="#f5fcc4")
define sanya_with_surname = Character("[player_name]", color="#f5fcc4")

    # функция ввода имени

    # $ player_name = "Саня "
    # $ player_name_buf = renpy.input("Можешь напомнить?", length=12)
    # $ player_name_buf = player_name_buf.strip()

    # if player_name_buf == "" :
    #     $ player_name = "Саня Юрченко"
    # else :
    #     $ player_name += player_name_buf

    # "Спасибо, что напомнил мне свою фамилию, [player_name]!"

label start:
    jump first_day

label first_day:
    scene black scen

    play sound "audio/alarm-sound.mp3"
    "*Звук будильника*"
    stop sound

    scene sanya room with fade

    play sound "audio/deep-moan.mp3"
    "*Вздох*"
    stop sound

    sanya "Ну что, день первый пошёл..."
    sanya "Как же меня это всё заебало: эти бесконечные лабораторные работы, сдачи курсачей..."
    sanya "A экзамены так вообще смех какой-то: ты забиваешь на учёбу болт весь семестр, а потом в поте лица пыхтишь без сна над какой-нибудь электротехникой, которая тебе нахрен не сдалась!"
    sanya "Всё бы ничего, но я, конечно, далеко не такого ожидал, когда поступал в универ."
    sanya "Эх, как же хочу вернуться в школьные года, когда ты вечно ищешь способы поднять бабок на алкашку." 
    sanya "Затем идёшь в \"проверенный ларёчек\" и покупаешь литр водки на литр колы в обычные дни, или же литр водки на литр апельсинового сока по праздникам."
    sanya "Сейчас это звучит ужасно, но в этом явно есть своя романтика подростковых лет..."
    sanya "А теперь я уже совсем старый стал, – 20 лет ёпте! Сменил вот недавно паспорт, теперь даже над фоткой в нём не поржать."
    sanya "Господи, как ссать-то охота..."

    scene sanya toilet with fade
        
    play sound "audio/toilet-sound.mp3" volume 0.5
    "*Звук смыва унитаза*"
    stop sound

    scene black scen with fade

    play music "audio/street-music.mp3" 
    $ renpy.pause (5.0)
    scene bus station with fade

    sanya "А я вот иду и думаю: \"а не слишком ли я много пить стал в последнее время?\""
    sanya "Уже будто и не помню себя трезвым..."
    sanya "Даже матушку свою довёл."
    sanya "Вчера с мужиками пришли пиво попить, последний день лета проводить, скажем так, а она меня поджидает у туалета и говорит:"
    sanya "\"Хоть бы раз домой вернулся с девчонкой какой-нибудь красивенькой, а не как обычно с парнями в зассаных майках\", — \"Мама, ну мы же панки\"..."
    sanya "А вот и мой автобус подъезжает."    

    stop music 

    play sound "audio/bus.mp3" 
    "*Звук подъезжающего автобуса*"
    stop sound

    scene bus with fade

    "И че дальше?"