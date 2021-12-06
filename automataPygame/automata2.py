import sys
import pygame
from pygame import event
import numpy as np
from pygame import draw
import time
from numpy import random
from pygame import mixer

# inicializacion de la pantalla


def automata_celular(rule, instrumento1,  nota1, nota2, color1, color2):
    pygame.init()

    # ancho y alto de la pantalla
    width, height = 700, 700

    # creacion de la pantallla
    screen = pygame.display.set_mode((height, width))

    # Colores
    bg = 25, 25, 25
    white = 255, 255, 255
    black = 000, 000, 000
    screen.fill(bg)

    # especificacion de cuadros en ejes
    ncX, ncY = 200, 200

    # ancho
    cuW = width / ncX
    # alto cuadros
    cuH = height / ncY

    # Esatado de la celda. Vivas = 1, Muertas = 0
    gameState = np.zeros((ncX, ncY))
    gameState[int(ncX/2), 0] = 1
    rulesarray = [0, 0, 0, 1, 1, 1, 1, 1]
    x = random.rand(0, 1)

    #nombreinstrumento = input("A")
    # 128 64 32 16 8  4  2  1
    # Reglas random , ademas se muestra que regla es

    rules2 = [0, 1]
    pauseExect = False
    rulesrandom = [random.choice(rules2), random.choice(rules2), random.choice(rules2), random.choice(
        rules2), random.choice(rules2), random.choice(rules2), random.choice(rules2), random.choice(rules2)]
    a = int("".join(map(str, rulesrandom)), 2)
    # print(a)

    # crear otro funcion que creee la reglas a partir de un numero entero a un binario

    # funcion para reproducir los sonidos

    nota0 = mixer.Sound(f'./Notas_Musicales/{instrumento1}/{nota1}.wav')
    nota1 = mixer.Sound(f'./Notas_Musicales/{instrumento1}/{nota2}.wav')

    for y in range(0, ncY):
        for x in range(0, ncX):
            # se crea el poligono de para cada celda
            poly = [(x * cuW, y * cuH),
                    ((x+1) * cuW, y * cuH),
                    ((x+1) * cuW, (y+1) * cuH),
                    (x * cuW, (y+1) * cuH)]
            # se dibujan los cuadrados para x y para y
            pygame.draw.polygon(screen, black, poly, 1)

    y = 0

    while True:

        newGameState = np.copy(gameState)

        # registro del teclado o mouse
        ev = pygame.event.get()

        for e in ev:
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                pauseExect = not pauseExect

        for x in range(0, ncX):
            # se crea el poligono de para cada celda
            ruleIdx = 4 * gameState[(x-1) % ncX, y] + 2 * \
                gameState[(x) % ncX, y] + 1 * gameState[(x+1) % ncX, y]

            newGameState[x, (y+1) % ncY] = manual_rule(rule)[int(ruleIdx)]

            poly = [(x * cuW, y * cuH),
                    ((x+1) * cuW, y * cuH),
                    ((x+1) * cuW, (y+1) * cuH),
                    (x * cuW, (y+1) * cuH)]

            # se dibujan los cuadrados para x y para y
            if newGameState[x, y] == 1:
                pygame.draw.polygon(screen, color1, poly, 0)
                nota0.play()
            elif newGameState[x, y] == 0:
                pygame.draw.polygon(screen, color2, poly, 0)
                nota1.play()

        time.sleep(0.1)

        if not pauseExect:
            y = (y+1) % ncY

        # actualizamos el juego
        gameState = np.copy(newGameState)
        pygame.display.flip()


def manual_rule(x):
    if x <= 255 or x >= 0:
        rules = list(np.binary_repr(x, width=8))
        rules.reverse()
    return rules


def ejecutar_pygame(numero, instrumento1, nota1, nota2, color1, color2):
    automata_celular(numero, instrumento1, nota1, nota2, color1, color2)
