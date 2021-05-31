import pygame
import psutil

BRANCO = (255,255,255)
PRETO = (0,0,0)
LARANJA = (246,130,0)
VERMELHO = (250,0,0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

pygame.init()
largura_tela, altura_tela = 1024, 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
tela.fill(BRANCO)
terminou = False

def mostra_texto(texto, pos, cor):
    font = pygame.font.Font(None, 24)
    text = font.render(f"{texto}", 1, cor)
    textpos = text.get_rect(center=pos,)
    tela.blit(text, textpos)

def desenha_abas():
    aba0 = pygame.Rect(0, 0, 255, 50)
    pygame.draw.rect(tela, PRETO, aba0)
    mostra_texto("ABA ZERO",(128,25), BRANCO)

    aba1 = pygame.Rect(256, 0, 255, 50)
    pygame.draw.rect(tela, PRETO, aba1)
    mostra_texto("ABA UM",(384,25), BRANCO)

    aba2 = pygame.Rect(512, 0, 255, 50)
    pygame.draw.rect(tela, PRETO, aba2)
    mostra_texto("ABA DOIS",(640,25), BRANCO)

    aba3 = pygame.Rect(768, 0, 256, 50)
    pygame.draw.rect(tela, PRETO, aba3)
    mostra_texto("ABA TRÊS",(896,25), BRANCO)
    return [aba0, aba1, aba2, aba3]

def mostra_uso_memoria():
    mem = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    pygame.draw.rect(tela, AZUL, (20, 250, larg, 70))
    larg = larg*mem.percent/100
    pygame.draw.rect(tela, VERMELHO, (20, 250, larg, 70))
    total = round(mem.total/(1024*1024*1024),2)
    font = pygame.font.Font(None, 24)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, PRETO)
    textpos = (20, 230)
    tela.blit(text, textpos)

def format_memory(info):
    return round(info/(1024*1024*1024), 2)

def memoria():
    disco = psutil.disk_usage('.')
    text = f"Total:   {format_memory(disco.total)} GB"
    mostra_texto(text,(90, 120),PRETO)
    text = f"Em uso:  {format_memory(disco.used)} GB"
    mostra_texto(text, (100, 140), PRETO)
    text = f"Livre:   {format_memory(disco.free)} GB"
    mostra_texto(text, (92, 160), PRETO)
    text = f"Percentual de Disco Usado: {disco.percent}%"
    mostra_texto(text, (160, 180), PRETO)

def mostra_conteudo(i):
    if i==1:
        memoria()
        mostra_uso_memoria()
terminou = False
i=0
texto='Aba zero'
while not terminou:
    abas = desenha_abas()
    mostra_texto("Projeto de Bloco", (512, 70), PRETO)
    mostra_texto(texto,(512,94),PRETO)
    mostra_conteudo(i)
for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for index, aba in enumerate(abas):
                    if aba.collidepoint(pos):
                        if index==0:
                            i=0
                            texto=f"Clicou na aba {index}"
                        elif index==1:
                            i=1
                        elif index==2:
                            i=2
                            texto=f"Clicou na aba {index}"
                        else:
                            i=3
                            texto=f"Clicou na aba {index}"
pygame.display.update()
tela.fill(BRANCO)
pygame.display.quit()
pygame.quit()