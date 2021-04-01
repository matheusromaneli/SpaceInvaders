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

def main(dificulty):
    dif = {1:"Facil", 2:"Medio", 3:"Dificil"}
    window= Window(600, 700)
    window.set_title("Space Invaders")

    teclado = window.get_keyboard()

    fundos = [Sprite("Assets/Fundo.png", 1), Sprite("Assets/Fundo.png", 1)]
    fundos[0].y = 0
    fundos[1].y = -fundos[0].height 

    nave = Sprite("Assets/Nave.png", 1)
    nave.set_position(window.width/2 - nave.width/2, window.height-nave.height)

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

        #Movimentaçoes
        if teclado.key_pressed("esc"):
            return 0

        if teclado.key_pressed("right") and nave.x+nave.width < window.width:
            nave.move_x(velNave * window.delta_time())

        if teclado.key_pressed("left") and nave.x > 0:
            nave.move_x(-velNave * window.delta_time())

        if teclado.key_pressed("space") and cooldownTiro <= 0:
            tiro = Sprite("Assets/Tiro.png", 1)
            tiro.set_position( nave.x + nave.width/2 - tiro.width/2, nave.y-tiro.height)
            tiros.append(tiro)
            cooldownTiro = 80 * dificulty

        for i in fundos:
            i.move_y(1)

            #posiciona o fundo novamente
            if i.y > window.height:
                i.y = window.height - 2 * i.height

        #tempo de recarga
        cooldownTiro += velTiro * window.delta_time()

        #draws
        # for i in fundos:
        #     i.draw()
        window.set_background_color ((0,0,0))
        for tiro in tiros:
            tiro.move_y(velTiro* window.delta_time())
            if tiro.y + tiro.height < 0:
                del tiros[tiros.index(tiro)]
            tiro.draw()
        #Mudar Direcao
        for monstro in horda:
            if(monstro[-1].x + monstro[-1].width > window.width):
                velMonstro *= -1
                move(horda,-1)
            if (monstro[0].x < 0):
                velMonstro *= -1
                move(horda)

        #Movimentaçao monstro
        for monstros in horda:
            for i in monstros:
                i.move_x(velMonstro * dificulty/3)
                i.draw()

        nave.draw()
        dificulty_text= f"Dificuldade: {dif[dificulty]}"
        window.draw_text(dificulty_text, window.width - len(dificulty_text)*8, 5, size = 20, color = (255,255,255))
        window.draw_text(f"FPS: {atual}",0,5, size = 20, color = (255,255,255))
        window.update()
