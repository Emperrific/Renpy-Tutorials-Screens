style centered_style:
    xalign 0.5
    yalign 0.5


screen hbox_screen(buttons=["Test"], text_size=30):
    add "CoderGirl-WhiteBackground.jpg"
    hbox:
        style "centered_style"
        xmaximum 300
        box_wrap True
        spacing 5
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size


screen vbox_screen(buttons=["Test"], text_size=30):
    vbox:
        spacing 5
        xalign 0.1
        yalign 0.1
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
    hbox:
        style "centered_style"
        vbox:
            yalign 0.5
            label "One" text_size 50
            label "Two" text_size 50
            label "Three" text_size 50
        vbox:
            label "Four" text_size 50
            label "Five" text_size 50
            label "Six" text_size 50
            label "Seven" text_size 50