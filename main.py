from PPlay.window import *
import menu
import game
import dificuldade

window= Window(500, 500)
teclado = window.get_keyboard()
state = 0
dificulty = 1
while True:
    state = menu.menu()
    if state == 0:
        state = game.main(dificulty)
    elif state == 1:
        dificulty = dificuldade.main()
    elif state == 2:
        state = 0
    elif state == 3:
        window.close()
