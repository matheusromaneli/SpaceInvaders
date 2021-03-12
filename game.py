from PPlay.window import *

def main(d):
    window= Window(500, 500)
    window.set_title("Space Invaders")
    teclado = window.get_keyboard()

    while True:

        if teclado.key_pressed("esc"):
            return 0

        window.draw_text(f"A dificuldade é: {d}", 0, window.height/2, size=45, color=(255,255,255))
        
        window.update()
