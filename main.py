import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()


largura = 640
altura = 480

x_cobra = int(largura/2) 
y_cobra = int(altura/2)

velocidade = 5
x_controle = velocidade
y_controle = 0

x_obstaculo = randint(60, 580)
y_obstaculo = randint(60, 430)

x_obstaculo_2 = randint(60, 580)
y_obstaculo_2 = randint(60, 430)

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 20, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SNAKE CRAZY')
fps = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, x_obstaculo,  y_obstaculo, x_obstaculo_2, y_obstaculo_2, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2) 
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    x_obstaculo = randint(60, 580)
    y_obstaculo = randint(60, 430)
    x_obstaculo_2 = randint(60, 580)
    y_obstaculo_2 = randint(60, 430)
    morreu = False
    
    

while True:
    fps.tick(40)
    tela.fill((0,0,40))
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,255,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        
    cobra = pygame.draw.rect(tela, (0,0,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    obstaculo = pygame.draw.rect(tela, (225,165,0), (x_obstaculo,y_obstaculo,65,65))
    obstaculo_2 = pygame.draw.rect(tela, (225,165,0), (x_obstaculo_2,y_obstaculo_2,65,65))
  
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        x_obstaculo = randint(60,580)
        y_obstaculo = randint(60,430)
        x_obstaculo_2 = randint(60,580)
        y_obstaculo_2 = randint(60,430)
        pontos += 10
        comprimento_inicial = comprimento_inicial + 15
       
        
    if cobra.colliderect(obstaculo):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
    if cobra.colliderect(obstaculo_2):
        x_maca = randint(60, 580)
        y_maca = randint(60, 430)
    if obstaculo.colliderect(obstaculo_2):
        obstaculo = randint(60, 580)
        obstaculo = randint(60, 430)

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

      
  
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('times', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((0,0,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    
    if x_cobra > largura:
        fonte2 = pygame.font.SysFont('times', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((0,0,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
          
    if x_cobra < 0:
        fonte2 = pygame.font.SysFont('times', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((0,0,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
          
    if y_cobra < 0:
        fonte2 = pygame.font.SysFont('times', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((0,0,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
          
    if y_cobra > altura:
        fonte2 = pygame.font.SysFont('times', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((0,0,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if cobra.colliderect(obstaculo):
        fonte2 = pygame.font.SysFont('times', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((0,0,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()      

    if cobra.colliderect(obstaculo_2):
        fonte2 = pygame.font.SysFont('times', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()
        

        morreu = True
        while morreu:
            tela.fill((0,0,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()      

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450,40))

    
    pygame.display.update()