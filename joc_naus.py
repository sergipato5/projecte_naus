import time
from pygame.locals import *
import pygame

guanyador = 0
AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons2.png'
WHITE = (255,255,255)
GREEN = (0,255,0)
MAGENTA = (255,0,255)

# Pantalles:
# Pantalla 1 = Menú
# Pantalla 2 = Joc
# Pantalla 3 = GAME OVER
# Pantalla 4 = Credits
pantalla_actual = 1

#Vides jugador 1

vides_image1 = pygame.image.load('assets/vida_aliat.png')
vides_image2 = pygame.image.load('assets/vida_enemic.png')
pygame.init()
pygame.mixer.music.load('assets/musica_fondo.mp3')






# Jugador 1:
player_image = pygame.image.load('assets/pixil-frame-0.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 4
vides_jugador1 = 3

# Jugador 2:
player_image2 = pygame.image.load('assets/nau-enemic-pixilart (2).png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 4
vides_jugador2 = 3

# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(GREEN) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 20
temps_entre_bales = 500 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def mostrar_menu():
    imprimir_pantalla_fons('assets/menú2.png')
    font1 = pygame.font.SysFont(None,100)
    font2 = pygame.font.SysFont(None,80)
    font3 = pygame.font.SysFont(None, 20)
    img1 = font1.render("Monkey Space!", True, MAGENTA)
    img2 = font2.render("1. Jugar", True, GREEN)
    img3 = font2.render("2. Credits", True, GREEN)
    img4 = font2.render("3. Sortir", True, GREEN)
    img5 = font3.render("Moviments: Jugar amb W,A,D i amb les fletxetes", True, GREEN)
    pantalla.blit(img1,(225,40))
    pantalla.blit(img2, (225, 150))
    pantalla.blit(img3, (225, 260))
    pantalla.blit(img4, (225, 370))
    pantalla.blit(img5, (245, 470))

    def mostrar_credits():
        pass

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if pantalla_actual == 4:
            vides_jugador2 = 3
            vides_jugador1 = 3

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1
        if pantalla_actual == 2:
            pygame.mixer.music.load('assets/credits_so.mp3')
            pygame.mixer.music.play(loops=-1)  # Música de fondo durante toda la partida
            if event.type == KEYDOWN:
                pygame.mixer.music.stop()
                if event.key == K_SPACE:
                    pantalla_actual = 1

        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                if event.key == K_1:
                    pantalla_actual = 3
                    pygame.mixer.music.load('assets/musica_fondo.mp3')
                    pygame.mixer.music.play(loops=-1)  # Música de fondo durante toda la partida
                if event.key == K_2:
                    pantalla_actual = 2
                if event.key == K_3:
                    pygame.quit()
        #Controlar les naus
        pygame.mixer.init()
        so_dispar1 = pygame.mixer.Sound('assets/dispar_laser.mp3')
        so_dispar1.set_volume(100)  # Ajusta el volumen si es necesario

        so_dispar2 = pygame.mixer.Sound('assets/laser_dispar2.mp3')
        so_dispar2.set_volume(100)  # Ajusta el volumen si es necesario

        if pantalla_actual ==3:
            if event.type == KEYDOWN:
            #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    so_dispar1.play()
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    so_dispar2.play()
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time

    if pantalla_actual == 1:
        mostrar_menu()
    elif pantalla_actual == 2:
        imprimir_pantalla_fons('assets/CREDITS.png')


    if pantalla_actual == 4:
        imprimir_pantalla_fons('assets/GAME_OVER.png')
        font = pygame.font.SysFont(None,100)
        text = "Player " + str(guanyador) + " Wins!"
        img = font.render(text, True, GREEN)
        pantalla.blit(img,(175,350))



    if pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                bales_jugador1.remove(bala)
                vides_jugador2 = vides_jugador2 - 1
                # eliminem la bala
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)
                vides_jugador1 = vides_jugador1 - 1
                # eliminem la bala
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        # Dibuixar vides jugador 1:
        if vides_jugador2 >= 3:
            pantalla.blit(vides_image2,(25,40))
        if vides_jugador2 >= 2:
            pantalla.blit(vides_image2,(75,40))
        if vides_jugador2 >= 1:
            pantalla.blit(vides_image2,(125,40))

        # Dibuixar vides jugador 2:
        if vides_jugador1 >= 3:
            pantalla.blit(vides_image1,(650,560))
        if vides_jugador1 >= 2:
            pantalla.blit(vides_image1,(700,560))
        if vides_jugador1 >= 1:
            pantalla.blit(vides_image1,(750,560))

        if vides_jugador1 <= 0 or vides_jugador2 <=0:
            pantalla_actual = 4
            guanyador = 1
            if vides_jugador1 <= 0:
                guanyador = 2
            pygame.mixer.music.load('assets/fiasco.mp3')
            so_dispar2.set_volume(400)
            pygame.mixer.music.play()


    pygame.display.update()
    clock.tick(fps)