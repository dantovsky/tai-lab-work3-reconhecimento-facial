import cv2
import globals
import os

# --------------------------------------------------------------------------------------------------------
# Reconhecimento facial utilizando um dos três classificador: Eigenfaces, Fisherfaces ou o LBPH
# --------------------------------------------------------------------------------------------------------

def reconhecer_faces(classificador):
    detectorFace = cv2.CascadeClassifier('classifiers/haarcascade-frontalface-default.xml')

    if classificador == 'Eigenfaces':
        reconhecedor = cv2.face.EigenFaceRecognizer_create()
        reconhecedor.read('classifications/classificadorEigein.yml')

    if classificador == 'Fisherfaces':
        reconhecedor = cv2.face.FisherFaceRecognizer_create()
        reconhecedor.read('classifications/classificadorFisher.yml')

    if classificador == 'LBPH':
        reconhecedor = cv2.face.LBPHFaceRecognizer_create()
        reconhecedor.read('classifications/classificadorLBPH.yml')

    print('Realizando o reconhecimento facial através do classificador {}.'.format(classificador))

    larrgura, altura = 220, 220
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    if os.name == 'nt':
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        print('O sistema eh o ', os.name)
    else:
        camera = cv2.VideoCapture(0)
        print('O sistema eh o ', os.name)

    while True:
        conectado, imagem = camera.read()
        imagemCinza = None
        if conectado:
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))  # Colocar minSize baixo se tiver capturado a face de uma imagem pequena (150 seria um valor normal para capturas de um rosto normal)

        # Message to user (how to exit the program)
        cv2.putText(imagem, 'Press "q" to exit.', (larrgura, altura + (altura + 30)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

        for (x, y, l, a) in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (larrgura, altura))  # var to get the converted image to size 220x220

            # Draw the rectangle around the face
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

            # Code to do the square draw in recognized face person
            id, confianca = reconhecedor.predict(imagemFace)
            nome = globals.get_nome(id)

            cv2.putText(imagem, nome, (x, y + (a + 30)), font, 2, (0, 0, 255))  # Params: imagem, posicionamento do texto, fonte a usar, tamanho da fonte, cor da fonte
            cv2.putText(imagem, str(confianca), (x, y + (a + 50)), font, 1, (0, 0, 255))  # Params: imagem, posicionamento do texto, fonte a usar, tamanho da fonte, cor da fonte

        if conectado == True:
            cv2.imshow('Face Recognition', imagem)
        if cv2.waitKey(1) == ord('q'):  # Break the cicle when click "q" key
            break

    camera.release()
    cv2.destroyAllWindows()