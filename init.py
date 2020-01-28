import os
import captura
import treinamento
import reconhecedor
import reconhecer_uma_imagem
import globals

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Teoria Algoritmica da Informação (2019/2020)
# Tabalho 3 - Parte Bônus (Reconhecimento Facial)
# Professor: Armando Pinho
# Alunos: Borys Chystov, Dante Marinho e Francisco Santos
#
# Developed with Python 3.7.4
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# --------------------------------------------------------------------------------------------------------
# Menu for Facial Recognition program
# --------------------------------------------------------------------------------------------------------

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
option = "-1"

def about():
    clear()
    print(f'\n{globals.colors["OKBLUE"]}~ ~ ~ (About) Ideia geral do programa para reconhecimento facial ~ ~ ~')
    print(f'\n{globals.colors["ENDC"]}1º passo: Deve fazer a captura de imagens pela webcam, de pelo menos duas pessoas' \
            '\n2ª passo: Iniciar o processo de treinamento das imagens'\
            '\n3º passo: Fazer o reconhecimento facial pela webcam através de um dos três classificadores disponíveis.')
    input(f'{globals.colors["FAIL"]}\n< Tecle ENTER pasa voltar>')

while option is not "0":
    clear()
    print(f'\n{globals.colors["OKBLUE"]}~ ~ ~ Reconhecimento Facial ~ ~ ~')
    print(f'{globals.colors["ENDC"]}1 - Capturar imagens pela webcam')
    print('2 - Iniciar treinamento das imagens')
    print('3 - Reconhecimento facial pela webcam (Classificador Eigenfaces)')
    print('4 - Reconhecimento facial pela webcam (Classificador Fisherface)')
    print('5 - Reconhecimento facial pela webcam (Classificador LBPH)')
    print('6 - Reconhecimento facial a partir de ficheiro de imagem (Classificador LBPH)')
    print('7 - (i) About')
    print(f'{globals.colors["FAIL"]}0 - SAIR')
    option = input(f'{globals.colors["WARNING"]}\nOpção: ')
    print(f'{globals.colors["ENDC"]}')

    if option == '1':
        # Capturar imagens pela web cam
        captura.init_capture()
    elif option == '2':
        " Iniciar treinamento das imagens"
        treinamento.getImagemComid()
    elif option == '3':
        # Reconhecimento facial pela webcam (Classificador Eigenfaces)
        reconhecedor.reconhecer_faces('Eigenfaces')
    elif option == '4':
        # Reconhecimento facial pela webcam (Classificador Fisherface)
        reconhecedor.reconhecer_faces('Fisherfaces')
    elif option == '5':
        # Reconhecimento facial pela webcam (Classificador LBPH)
        reconhecedor.reconhecer_faces('LBPH')
    elif option == '6':
        reconhecer_uma_imagem.detect_face_from_image()
    elif option == '7':
        about()