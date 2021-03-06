from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import menu
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

def main(dificulty):

    window = Window(600,700)
    window.set_title("Menu")
    mouse = window.get_mouse()

    dificulty_buttons = [Sprite("Assets/Fácil.jpg" , 1),Sprite("Assets/Médio.jpg" , 1),Sprite("Assets/Difícil.jpg" , 1), Sprite("Assets/Voltar.jpg" , 1)]
    set_vetor(dificulty_buttons,window)
    fundo = Sprite("Assets/fundo.jpg",1)
    pressed = True
    while True:
        if mouse.is_button_pressed(1):
            if not(pressed):
                if mouse.is_over_object(dificulty_buttons[0]):
                    return 1
                if mouse.is_over_object(dificulty_buttons[1]):
                    return 2
                if mouse.is_over_object(dificulty_buttons[2]):
                    return 3
                if mouse.is_over_object(dificulty_buttons[3]):
                    return dificulty
            pressed = True
        else:
            pressed = False
        fundo.draw()
        draw_buttons(dificulty_buttons)
        window.update()

