import cv2
import numpy as np
import os
import json
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
# Este script capturas imagens a partir de uma web cam
# --------------------------------------------------------------------------------------------------------
def init_capture():
    classificador = cv2.CascadeClassifier("classifiers/haarcascade-frontalface-default.xml")  # haarcascade-frontalface-default => XML file to do the face training detection
    classificadorOlho = cv2.CascadeClassifier("classifiers/haarcascade-eye.xml")
    camera = cv2.VideoCapture(0)  # 0 is the number of the first cam (of computer)
    amostra = 1  # number of photos taken when press a certain key
    numeroAmostras = 25

    # Input para receber o nome da pessoa
    nome = input(f'{globals.colors["WARNING"]}Digite seu nome: {globals.colors["ENDC"]}')

    largura, altura = 220, 220  # size of samples
    print('Capturando as faces (25 amostras) ...')

    # Gera novo ID para pessoa atual
    id = 0
    if os.path.exists(globals.names_file_initial_path):  # Se este file existe é porque ja foi capturado imagem ao menos uma vez
        with open('nomes.json', 'r') as nomes:
            data = json.load(nomes)
            id = data['idAtual']
            id += 1
            data['idAtual'] += 1
            data['pessoas'][id] = nome
    else:
        with open('nomes.json', 'w') as initial_structure:

            # Build the initial structure
            data = globals.names_file_initial

            # Adding the first person
            id = data['idAtual']
            id += 1
            data['idAtual'] += 1
            data['pessoas'][id] = nome
            json.dump(data, initial_structure, indent=4)

    # Create folder "photos" if note exists
    if not os.path.exists('photos'):
        os.mkdir('photos')

    while True:
        conectado, imagem = camera.read()  # reading the webcam

        # var para detetar imagem em escala de cinza => melhor perforcance do algoritmo
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        # print('Avg imagemCinza:', np.average(imagemCinza))

        # facesDetectadas => saves all faces found by the algorithm (this var have a matrix with positions x and y (start point of a face) and the face width and height
        # classificator was trained with the haarcascade-frontalface-default.xml file
        # params:
        # imagemCinza :: image where I want to detect faces
        # scaleFactor :: indicate the image scale
        # minSize :: min to do the face detection
        facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

        # Cicle to draw the rectangle (or square) envolving the face
        # l :: width, a :: height
        for (x, y, l, a) in facesDetectadas:
            # params :: (image to aplay rectangle, start point, end point, rectangle's color, border to draw
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

            # find eyes inside rectangle ---------------------------------------------------------
            regiao = imagem[y:y + a, x:x + l]  # face
            regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)  # converting to gray scale
            olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
            # Draw rectangles envolving eyes
            for (ox, oy, ol, oa) in olhosDetectados:
                cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)
            # ------------------------------------------------------------------------------------

                # Saving one sample (image of the moment) when press key "q"
                if cv2.waitKey(1) & 0xFF == ord('q'):

                    # Capture image only if luminosity is good!
                    if np.average(imagemCinza) > 110:  # 0 - 255 (less luninosity - more luminosity)

                        # Resizing the image
                        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))

                        # Save the sample
                        # cv2.imshow("Imagem", imagem)
                        cv2.imwrite("photos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
                        print("[foto " + str(amostra) + " capturada com sucesso]")
                        amostra += 1

        # Show them webcam image
        cv2.imshow("Face", imagem)
        cv2.waitKey(1)  # "wainting for a key" (uncomment if running with problems)

        # Stop capturing from webcam when taken 25 samples
        if (amostra >= numeroAmostras + 1):
            break

    # Guarda nova pessoa em nomes.JSON
    with open('nomes.json', 'w') as nomes_to_save:
        json.dump(data, nomes_to_save, indent=4)

    print("Amostras da face capturadas com sucesso.")
    camera.release()  # flush memory
    cv2.destroyAllWindows()