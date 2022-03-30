import os
import time
from colorama import init, Fore

class bcolors:
    WHITE = '\033[2;37m' #WHITE
    PURPLE = '\033[0;35m' #PURPLE
    GREEN = '\033[0;92m' #GREEN
    CYAN = '\033[0;36m' #CYAN
    YELLOW = '\033[0;93m' #YELLOW
    RED = '\033[0;91m' #RED
    BLUE = '\033[0;34m' #BLUE
    RESET = '\033[0;0m' #RESET COLOR


def my_funcion(data):
    os.system(data)
    os.system('clear')
    print('\n')
    print('###########################')
    print('##'+bcolors.YELLOW+'     FIN de PROCESO    '+bcolors.GREEN+'##')
    print('###########################')
    print('\n\n')
    print('Espere ...')
    print('')
    time.sleep(2)
    init()


def downvideo():
    os.system('clear')
    print('')
    print(bcolors.YELLOW+'DESCARGAR VIDEO COMPLETO'+bcolors.GREEN)
    print('========================')
    print('')
    url = input(bcolors.CYAN+"Ingrese URL del Video de Youtube ( "+bcolors.PURPLE+"0 para Volver al Menú "+bcolors.CYAN+")"+bcolors.GREEN+" \n \n -> ")
    if len(url) < 3:
        init()
    else:
        video = "youtube-dl --format mp4 " + url
    my_funcion(video)


def downaudio():
    os.system('clear')
    print('')
    print(bcolors.YELLOW+'DESCARGAR AUDIO de un VIDEO'+bcolors.RESET)
    print('===========================')
    print('')
    url = input(bcolors.CYAN+"Ingrese URL del Video de Youtube ( "+bcolors.PURPLE+"0 para Volver al Menú "+bcolors.CYAN+")"+bcolors.GREEN+" \n \n -> ")
    if len(url) < 3:
        init()
    else:
        video = "youtube-dl -x --audio-format mp3 " + url 
    my_funcion(video)


def init():
    os.system('clear')
    print(Fore.LIGHTGREEN_EX+'\n') ## Usando Colorama 
    print('############################################')
    print('##                                        ##')
    print('##'+bcolors.PURPLE+'               BIENVENIDO               '+bcolors.GREEN+'##')
    print('##                                        ##')
    print('##'+bcolors.YELLOW+'  DESCARGAS VIDEOS y AUDIOS DE YOUTUBE  '+bcolors.GREEN+'##')
    print('##                                        ##')
    print('############################################')
    print(bcolors.WHITE+'                               by Mastrosoft')
    print(bcolors.GREEN+'')
    print('')
    print('*'+bcolors.RED+' Eligar Metodo :')
    print(bcolors.YELLOW+'==================')
    print(bcolors.GREEN+'')
    print('')
    print(' 1 -'+bcolors.CYAN+' Descargar Video Completo')
    print(bcolors.GREEN+'')
    print(' 2 -'+bcolors.CYAN+' Descargar solo el Audio')
    print(bcolors.GREEN+'')
    print(' 0 -'+bcolors.CYAN+' SALIR')
    print(bcolors.GREEN+'')
    print('')
    op = input(bcolors.YELLOW+'Opción ....: '+bcolors.GREEN)
    if op.isdigit():
        op = int(op)
        if op == 1:
            downvideo()
        if op == 2:
            downaudio()
        if op == 0:
            salir()
    else:
        salir()


def salir():
    os.system('clear')
    print('\n')
    print('##################################')
    print('##'+bcolors.YELLOW+'     SALIENDO del PROGRAMA    '+bcolors.GREEN+'##')
    print('##################################')
    print('\n')
    print (bcolors.RED+"Programa Cerrado", end=" "+bcolors.GREEN)
    for i in range(15):
        if i < 14:
            print(".", end="")
            x = 0
            while x < 3000:
                x+=1
    time.sleep(1)
    print("\n")
    exit()


#### Initial Program
init()


