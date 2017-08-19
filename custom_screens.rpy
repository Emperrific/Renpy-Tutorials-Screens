style centered_style:
    xalign 0.5
    yalign 0.5
    spacing 5

style combo_text:
    size 50

style combo_hbox is centered_style

init python:
    def incTotal():
        global total
        total+=1

screen hbox_screen(buttons=["Test"], text_size=30):
    hbox:
        style "centered_style"
        spacing 10
        xmaximum 300
        box_wrap True
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size


screen vbox_screen(buttons=["Test"], text_size=30):
    vbox:
        xalign 0.1
        yalign 0.1
        spacing 5
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size


screen grid_screen(buttons=["Test1", "Test2"], text_size=30):
    grid 2 len(buttons)/2+1:
        spacing 5
        xalign 0.8
        yalign 0.1
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size
        for i in range(0, (len(buttons)/2 + 1) * 2 - len(buttons)):
            null

screen combo_screen:
    style_prefix "combo"
    hbox:
        vbox:
            yalign 0.5
            text "One"
            text "Two"
            text "Three"
        vbox:
            text "Four"
            text "Five"
            text "Six" 
            text "Seven"
        vbox:
            text "Total: [total]"
        imagebutton auto "button_%s.png":
            action [Function(incTotal), SelectedIf(total % 2 == 1)]
