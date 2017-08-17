# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]

    scene bg room
    show screen hbox_screen(numbers, 50)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    hide screen hbox_screen
    show screen vbox_screen(numbers, 50)

    e "You've created a new Ren'Py game."

    hide screen vbox_screen
    show screen grid_screen(numbers, 50)

    e "Once you add a story, pictures, and music, you can release it to the world!"

    hide screen grid_screen
    show screen combo_screen

    "The end."
    # This ends the game.

    return
