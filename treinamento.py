import cv2
import os
import numpy as np
import json
import globals
import time

# --------------------------------------------------------------------------------------------------------
# Este script realiza o treinamento das imagens anteriormente capturadas pela webcam
# --------------------------------------------------------------------------------------------------------

# Método responsável por percorrer o banco de imagens de treinamento, e retorna os respetivos IDs de cada pessoa e as
# respetivas imagens. Exemplo: { pessoa_1: [img1, im2, img3] }
def getImagemComid():

    # Classificadores (3 algoritmos diferentes)
    eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50, threshold=0)
    fisherface = cv2.face.FisherFaceRecognizer_create()
    lbph = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 50)  # Exemplo de parametros: 2, 2, 7, 7, 50

    caminhos = [os.path.join('photos', f) for f in os.listdir('photos')]
    faces = []  # guardar as faces de cada pessoa "xpto"
    ids = []  # guardar os IDs de cada pessoa "xpto"

    # Ler as imagens
    for caminhoImagem in caminhos:
        # imread() faz a leitura de uma imagem no doretório
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)

        # Get ids de todas as imagens
        # TODO :: introduzir o nome da pessoa no script de captura, e extrair aqui o nome para adicionar em um novo array.
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])  # erro ao fazer cast para int
        ids.append(id)  # add ID na lista de IDs
        faces.append(imagemFace)  # add face na lista de faces

        # Get image and convert to gray scale
        # Testing: existe todas as imagens da pasta de imagens
        # cv2.imshow('Face', imagemFace)
        # cv2.waitKey(10)
#     return np.array(ids), faces  # converte a lista de ids para o tipo np.array (tipo de dado requerido para fazer o treinamento)
#
# ids, faces = getImagemComid()


    ids, faces = np.array(ids), faces  # converte a lista de ids para o tipo np.array (tipo de dado requerido para fazer o treinamento)

    print('Iniciando o treinando das imagens...')

    folder_classifications = 'classifications'
    if not os.path.exists(folder_classifications):
        os.mkdir(folder_classifications)

    # O método train() faz o treinamento (lê todas as imagens e realiza o aprendizado), vai executar todos
    # os processos do algoritmo Eigenface
    eigenface.train(faces, ids)  # Aprendizagem supervisionada, onde se pada as imagens e o ID respetivo
    eigenface.write(folder_classifications + '/classificadorEigein.yml')  # grava o treinamento em ficheiro

    # Verify how many people exists :: if >= 1 exit the program
    with open('nomes.json', 'r') as nomes:
        data = json.load(nomes)
        if len(data['pessoas']) <= 2:
            print(f'{globals.colors["FAIL"]}Para realizar o treino é necessário adicionar pelo menos 2 pessoas!{globals.colors["ENDC"]}')
            time.sleep(3)
            return None

    fisherface.train(faces, ids)
    fisherface.write(folder_classifications + '/classificadorFisher.yml')

    lbph.train(faces, ids)
    lbph.write(folder_classifications + '/classificadorLBPH.yml')

    print('Treinamento realizado!')
