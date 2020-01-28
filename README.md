#  TAI - Lab Work 3 (Parte Bônus) - Reconhecimento Facial

## Este trabalho foi desenvolvido com Python e OpenCV, e forma parte do Lab Work nº 3 da disciplina de TAI.

Teoria Algoritmica da Informação (2019/2020)

Tabalho 3 - Parte Bônus (Reconhecimento Facial)

Professor: Armando Pinho

Alunos: Borys Chystov, Dante Marinho e Francisco Santos

Developed with Python 3.7.4

## Requerimentos do sistema
- Python3
- NumPy
    Deve ir até o seguinte caminho:
    C:\Users\Dantiii\AppData\Local\Programs\Python\Python37-32\Scripts>
    Rodar o comando:
    pip install numpy (rodei a partir do CMD ao brir, pois no caminho acima deu-me erro)
- PIL
	Usado apenas na parte final do curso, na parte de avaliação dos algoritmos
	Serve para fazer o carregamento de iamgens no Python
	pip install pillow
- OpenCV (!) Ver tópico sobre resolução de problemas caso tenha problemas ao executar o programa
    (procurar por "Unofficial Windows Binaries for Python Extension Packages")
    https://www.lfd.uci.edu/~gohlke/pythonlibs/
    Precisa fazer download da versão que tem descrito "contrib"
    opencv_python-4.1.2+contrib-cp37-cp37m-win_amd64 (ou a verão 32 bits)
    
    Desinstalar outra versão do pencv-python:
    pip unistall opencv_python

## Instruções de execução do programa

- 1 - Rodar o script init.py :: este irá fornecer um menu.
    
    ```python3 init.py```

- 2 - Escolher a opção (1) para capturar imagens pela webcam, será pedido para inserir o noma da pessoa, e em seguida capture 25 fotos (teclar "q" para uma captura).
    
    (!) É necessário adicionar pelo menos duas pessoas ao banco de imagens (caso contrário poderá ocasionar um erro ao executar o ficheiro de treinamento)
- 2 - Rodar a opção (2) para iniciar o treinamento para que sejam classificadas as imagens da pasta de imagem.
- 3 - Rodar uma das opções de reconhecimento facial pela webcam ou a opção de reconhecimento a partir de uma imagem.

Após a primeira execução do programa, será criado autometicamente um ficheiro "nomes.json" com a seguinte estrutura em formato JSON:

```
{
    "pessoas": {
        "0": "Desconhecido"
    },
    "idAtual": 0
}
```

## Resolução de problemas (ambiente Windows)

Tanto paro o pacote do OpenCV quanto para o PIL (Pillow) houve problemas, que mesmo com a instalação feita segundo as
instruções dos tutores do curso, ainda assim os pacotes não foram reconhecidos ao rodar o programa. O problema foi
solucionado instalando os tais pacotes através do instalador de pacotes da IDE Pycharm. Segue os passos que foi seguido,
tanto as instruções do curso quando a que foi feita posteriormente.

- OpenCV (procurar por "Unofficial Windows Binaries for Python Extension Packages")
    https://www.lfd.uci.edu/~gohlke/pythonlibs/
    Precisa fazer download da versão que tem descrito "contrib"
    Instalei o pacote (tenho o Python 64 bits):
    opencv_python-4.1.2+contrib-cp37-cp37m-win_amd64

    Desinstalar outra versão do pencv-python:
    pip unistall opencv_python

    Foi indicado colocar o ficheiro acima no caminho:
    C:\Users\Dantiii\AppData\Local\Programs\Python\Python37-32\Scripts>
    E fazer:
    pip install opencv_python-4.1.2+contrib-cp37-cp37m-win_amd64

    (!) Deu-me erro, então coloquei o ficheiro dentro de C:\Users\Dantiii e rodei o comando de instalação, e funcionou

    (!) Tive erros para rodar um programa de teste. Foi recomendado desinstalar o opencv e instalar pelo Pycharm:

    Erro 1:
    File "cam.py", line 1, in <module>
        import cv2
    ImportError: No module named cv2

    Erro 2:
    ImportError: numpy.core.multiarray failed to import

    Caso esteja, recomendo instalar o OpenCV diretamente pelo Pycharm. 
    Para isso, vá em: File > Settings > Project: "Nome do Projeto" e abra Project Interpreter. 
    No lado superior direito clique em "+".
    Pesquise na lupa por "opencv-contrib-python" e clique em "Install".

    Outra coisa que da pra tentar é configurar o "path" nas variáveis de ambiente do Windows 
    (painel de controle, sistema, configurações avançadas), edita a variável path e coloca o 
    caminho de instalação do OpenCV. Dê uma olhada nesse vídeo
    https://www.youtube.com/watch?v=8tjMiImv-Kk

## Possíveis erros ao rodar o programa

### Erro 1
```
Traceback (most recent call last):
  File "init.py", line 50, in <module>
    import treinamento
  File "/home/dantiii/Desktop/TAI_Lab3/reconhecimento-facial-python-opencv/treinamento.py", line 10, in <module>
    eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50, threshold=0)
AttributeError: module 'cv2.cv2' has no attribute 'face'
```

Poderá tentar umas destas soluções, mas apenas consegui resolver ao instalar o pacote do OpenCV-contrib a partir do instalador de pacotes do Pycharm:

https://stackoverflow.com/questions/44633378/attributeerror-module-cv2-cv2-has-no-attribute-createlbphfacerecognizer

### Erro 2

```
"SyntaxError: Non-ASCII character '\xc3' in ... 
```

Precisa iniciar o programa com o Python3:

```
python3 init.py
```

## Programa de teste (testar se o opencv está corretamente instalado)

Criar um script com o seguinte conteúdo (deverá aparecer um número de versão e em seguida
uma listagem grande as funcionalidade do objeto "face"):

~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import cv2

print(cv2.__version__)
help(cv2.face)
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

## Considerações finais e referências

Este trabalho é o resultado de um curso realizado na Udemy. Todo o código produzido durante o curso poder ser encontrado neste repositório:

https://github.com/dantovsky/reconhecimento-facial-python-opencv

Foi também criado uma branch para implementar e arrumar o código voltado ao projeto da disciplina de TAI, e pode ser encontrado na branch #tai-lab-work3":

https://github.com/dantovsky/reconhecimento-facial-python-opencv/tree/tai-lab-work3

Para evitar a informação desnecessária e não misturar haver confusão entre os branchs, resovel-se criar este novo repositório apenas para o trabalho de TAI:

https://github.com/dantovsky/tai-lab-work3-reconhecimento-facial (este repositório)