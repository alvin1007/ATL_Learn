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
