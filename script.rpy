## 여러 스타일 정의
style big:
    size 100
    xalign 0.5
    yalign 0.5
style game_start_menu:
    yalign 0.7

## 특수 스크린
screen game_start_menu:
    tag menu
    textbutton _("시작") xalign 0.1 yalign 0.7 action Start()
    textbutton _("게임 불러오기") xalign 0.3 yalign 0.7 action ShowMenu("load")
    textbutton _("환경 설정") xalign 0.5 yalign 0.7 action ShowMenu("preferences")
    textbutton _("도움말") xalign 0.7 yalign 0.7 action Help()
    textbutton _("나가기") xalign 0.9 yalign 0.7 action Quit(confirm=False)
    textbutton "되돌아가기" xalign 0.5 yalign 0.98 action Show("main_menu")
screen main_menu():
    tag menu
    window:
        style "mm_root"
        text "ATL Learn" style "big"
    textbutton "게임 메뉴" xalign 0.5 yalign 0.98 action Show("game_start_menu")
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    hbox:
        frame:
            style "game_menu_navigation_frame"
        frame:
            style "game_menu_content_frame"
            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    vbox:
                        transclude
            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    transclude
            else:
                transclude
    use navigation
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
screen quick_menu():
    pass
screen navigation():
    vbox xalign 0.02 yalign 0.5:
        if main_menu:
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Help") action Help()
            textbutton _("Quit") action Quit()
            textbutton _("Return") action Return()
        else:
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Save Game") action ShowMenu("save")
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Main Menu") action MainMenu()
            textbutton _("Help") action Help()
            textbutton _("Return") action Return()
screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        style_group "prefs"
        vbox:
            null height 120
            hbox :
                vbox:
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                null width 100
                vbox:
                    label _("Transitions")
                    textbutton _("All") action Preference("transitions", "all")
                    textbutton _("None") action Preference("transitions", "none")
            null height 30
            hbox:
                vbox:
                    label _("Skip")
                    textbutton _("Seen Messages") action Preference("skip", "seen")
                    textbutton _("All Messages") action Preference("skip", "all")
                null width 50
                vbox:
                    label _("After Choices")
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")
                null width 50
                vbox:
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
            null height 30
            vbox:
                vbox:
                    label _("Music Volume")
                    bar value Preference("music volume")
                null height 20
                vbox:
                    label _("Sound Volume")
                    bar value Preference("sound volume")
                null height 20
                vbox:
                    label _("Voice Volume")
                    bar value Preference("voice volume")
                null height 20
screen save():
    tag menu
    use navigation
    hbox xalign 0.5 yalign 0.98:
        textbutton _("<") action FilePagePrevious()
        textbutton _("A") action FilePage("auto")
        for i in range(1, 9):
            textbutton str(i) action FilePage(i)
        textbutton _(">") action FilePageNext()
    grid 2 2:
        transpose True
        xalign 0.5
        yalign 0.5
        for i in range(1, 5):
            button:
                action FileAction(i)
                has hbox 
                add FileScreenshot(i)
                text ( " %2d. " % i
                        + FileTime(i, empty=_("Empty Slot."))
                        + "\n"
                        + FileSaveName(i)) style "large_button_text"
screen say(who, what):
    window yalign 0.9 id "window":
        has vbox xalign 0.3 yalign 0.16
        if who:
            text who size 20 id "who"
        text what id "what"

## 여러 스크린 정의
screen hello_world:
    text "Hello, World" style "big"
screen buttons():
    hbox:
        textbutton "저장" action ShowMenu("save")
        textbutton "옵션" action ShowMenu("preferences")
        textbutton "스킵" action Skip()
        textbutton "자동진행" action Preference("auto-forward", "toggle")
screen main():
    textbutton "메인 메뉴로 돌아가기" xalign 0.5  action MainMenu(False)

## 씬 시작
label start:
    scene black
    show screen hello_world
    show screen buttons()
    show screen main()
    $ count = 0
    while(1):
        "example" "touch count : [count]"
        $ count = count + 1
    return
