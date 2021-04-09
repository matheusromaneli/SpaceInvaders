from PPlay.window import *
from PPlay.sprite import *

def move(array,signal = 1):
    for i in array:
        for j in i:
            j.x += signal * 10
            j.y += 10

def spawn_monster(array, size,pos):
    for i in range(size):
        if pos%2:
            array.append(Sprite("Assets/Monstro.png"))
        else:
            array.append(Sprite("Assets/Monstro_branco.png"))
        array[i].set_position((array[0].width * 3/2) * i , (array[0].height*3/2) *(1+pos))

def spawn_horda(array, linha, coluna):
    for i in range(coluna):
        monstros = []
        spawn_monster(monstros,linha,i)
        array.append(monstros)

def main(dificulty,score):
    dif = {1:"Facil", 2:"Medio", 3:"Dificil"}
    window= Window(600, 700)
    window.set_title("Space Invaders")
    window.update()
    teclado = window.get_keyboard()

    nave = Sprite("Assets/Nave.png", 1)
    nave.set_position(window.width/2 - nave.width/2, window.height-nave.height)
    lifes = 3
    velNave = 500 / dificulty
    tiros = []
    velTiro = -500 
    velMonstro = 2
    cooldownTiro = 0
    horda = []
    spawn = True
    cont=0
    fps=0
    atual=0
    while True:
        #FPS
        cont += window.delta_time()
        fps += 1
        if cont>1:
            atual= fps
            cont=0
            fps=0

        if spawn:
            spawn_horda(horda,5,5)
            spawn = False
            start = window.time_elapsed()

        #Movimentaçoes
        if teclado.key_pressed("esc"):
            return -1,-1

        if teclado.key_pressed("right") and nave.x+nave.width < window.width:
            nave.move_x(velNave * window.delta_time())

        if teclado.key_pressed("left") and nave.x > 0:
            nave.move_x(-velNave * window.delta_time())

        #Tiro
        if teclado.key_pressed("space") and cooldownTiro <= 0:
            tiro = Sprite("Assets/Tiro.png", 1)
            tiro.set_position( nave.x + nave.width/2 - tiro.width/2, nave.y-tiro.height)
            tiros.append(tiro)
            cooldownTiro = 80 * dificulty

        #tempo de recarga
        cooldownTiro += velTiro * window.delta_time()

        #draws
        
        window.set_background_color ((0,0,0))
        #Tiros
        for tiro in tiros:
            tiro.move_y(velTiro* window.delta_time())
            if tiro.y + tiro.height < 0:
                del tiros[tiros.index(tiro)]
            tiro.draw()
        #Monstros
        quantidade = 0
        for monstros in horda:
            if monstros:
                if(monstros[-1].x + monstros[-1].width > window.width):
                    velMonstro *= -1
                    move(horda,-1)
                if (monstros[0].x < 0):
                    velMonstro *= -1
                    move(horda)
                for monstro in monstros:
                    monstro.move_x(velMonstro * dificulty/3)
                    monstro.draw()
                    if monstro.collided(nave):
                        ##perde
                        return False, int(score/(1 + (end-start)/1000))
                    for tiro in tiros:
                        if monstro.collided(tiro):
                            score += int(1000/(1+horda.index(monstros)))
                            del monstros[monstros.index(monstro)]
                            del tiros[tiros.index(tiro)]
                            break
                    quantidade += 1

        if quantidade == 0:
            ##ganha
            end = window.time_elapsed()
            return True, int(score/(1 + (end-start)/1000))
        nave.draw()
        dificulty_text= f"Dificuldade: {dif[dificulty]}"
        window.draw_text(dificulty_text, window.width - len(dificulty_text)*8, 5, size = 20, color = (255,255,255))
        window.draw_text(f"FPS: {atual}",0,5, size = 20, color = (255,255,255))
        window.update()

def over(win,score):
    if win == 0:
        color = (188,0,0)
        text = "YOU LOSE"
        
    elif win == 1:
        color = (0,0,188)
        text = "YOU WIN"
    else:
        return 
    score_text = f"Score: {score}"

    window= Window(600, 700)
    window.set_title("Space Invaders")
    teclado = window.get_keyboard()
    while True:
        if teclado.key_pressed("esc"):
            return
        window.set_background_color ((0,0,0))
        window.draw_text(text,window.width/2- len(text) * 25 , window.height/2 - 200, size = 100, color = color)
        window.draw_text(score_text,window.width/2 - (len(score_text)-1) * 10, window.height/2, size = 40, color = (255,255,255))
        window.update()
