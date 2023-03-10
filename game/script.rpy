define sanya = Character('Саня', color="#f5fcc4")
define sanya_surname = Character("[player_name]", color="#f5fcc4")

# комментарии к звуку можно убрать, как сами решите

label start:
    jump first_day


label first_day:

    scene black scen

    play sound "audio/alarm-sound.mp3"
    "\"Звук будильника\""
    stop sound

    scene sanya room with fade

    play sound "audio/deep-moan.mp3"
    sanya "Первый день семестра... Какой же заеб меня ждет впереди."
    stop sound

    sanya "Всё бы ничего, но я, конечно, далеко не такого ожидал, когда поступал в универ."
    sanya "Хотелось бы вернуться в то время, когда я пил не просыхая, заучивал билеты перед экзаменами..."
    sanya "Конечно не без дерьма с этими блок-схемами, но была канеш атмосфера та еще."
    sanya "Пора идти поссать."

    scene sanya toilet with fade
        
    play sound "audio/zvuk-unitaza.mp3" volume 0.5
    "\"Звук смывания унитаза\""
    stop sound

    return 





    # $ player_name = "Саня "
    # $ player_name_buf = renpy.input("Можешь напомнить?", length=12)
    # $ player_name_buf = player_name_buf.strip()

    # if player_name_buf == "" :
    #     $ player_name = "Саня Юрченко"
    # else :
    #     $ player_name += player_name_buf

    # "Спасибо, что напомнил мне свою фамилию, [player_name]!"