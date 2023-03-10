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
    sanya "Эх, как же хочу вернуться в школьные года, когда ты вечно ищешь способы поднять бабок на алкашку, а затем идёшь в \"проверенный ларёчек\" и покупаешь литр водки на литр колы в обычные дни, или же литр водки на литр апельсинового сока по праздникам."
    sanya "Сейчас это звучит ужасно, но в этом явно есть своя романтика подростковых лет.."
    sanya "А теперь я уже совсем старый стал, – 20 лет ёпте! Сменил вот недавно паспорт, теперь даже над фоткой в нём не поржать."
    sanya "Господи, как ссать-то охота..."

    scene sanya toilet with fade
        
    play sound "audio/toilet-sound.mp3" volume 0.5
    "*Звук смыва унитаза*"
    stop sound

    