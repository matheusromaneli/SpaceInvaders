from PPlay.window import *
import menu
import game
import dificuldade

state = 0
dificulty = 1
while True:
    score = 0
    state = menu.menu()
    if state == 0:
        win,score = game.main(dificulty,score)
        game.over(win,score*dificulty)
    elif state == 1:
        dificulty = dificuldade.main(dificulty)
    elif state == 2:
        state = 0
    elif state == 3:
        break
