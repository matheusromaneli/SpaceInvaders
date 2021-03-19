from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
def set_vetor(v,j, pos = True):
    if pos:
        y = 30
        for i in v:
            i.set_position(j.width/2 - i.width/2, y)
            y += i.height + 20
    else:
        for i in v:
            i.set_position(0,-i.height)

def draw_buttons(b):
    for i in b:
        i.draw()

def menu():
    window = Window(600,700)
    window.set_title("Menu")
    mouse = window.get_mouse()
    pressed = True
    buttons = [Sprite("Assets/Jogar.jpg" , 1),Sprite("Assets/Dificuldade.png" , 1),Sprite("Assets/Ranking.jpg" , 1),Sprite("Assets/Sair.jpg" , 1)]
    set_vetor(buttons,window)
    fundo = Sprite("Assets/fundo.jpg",1)
    while True:

        if mouse.is_button_pressed(1):
            if not(pressed):
                if mouse.is_over_object(buttons[0]):
                    return 0

                if mouse.is_over_object(buttons[1]):
                    return 1

                if mouse.is_over_object(buttons[2]):
                    return 2

                if mouse.is_over_object(buttons[3]):
                    return 3
            pressed = True
        else:
            pressed = False
            
        fundo.draw()
        draw_buttons(buttons)
        window.update()
