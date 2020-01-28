import json

# Lê o ficheiro JSON com os IDs e nomes das pessoas e o contador de IDs
def read_names_file():
    with open('nomes.json', 'r') as nomes:
        data = json.load(nomes)
        return data

# print('Nomes:', data['pessoas'])

# Retorna o nome do ID procurado
def get_nome(id_procurado):
    data = read_names_file()
    for id in data['pessoas']:
        if id == str(id_procurado):
            # print('Nome da pessoa:', data['pessoas'][id])  # pessoas[id] é o nome da pessoa
            return data['pessoas'][id]
    # print('Este nome não consta na BD.')
    return 'Desconhecido'

# Cores para o print
colors = {
    "OKBLUE": '\033[94m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
}

# Estrutura inicial para guardar os nomes em formato JSON
names_file_initial = {
    "pessoas": {
        "0": "Desconhecido"
    },
    "idAtual": 0
}

names_file_initial_path = 'nomes.json'

# --------------------------------------------------------------------------------------------------------
# Help links
# --------------------------------------------------------------------------------------------------------

# Working With JSON Data in Python
# https://realpython.com/python-json/

# How to print colored text in terminal in Python?
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

# CV2: “[ WARN:0] terminating async callback” when attempting to take a picture
# https://stackoverflow.com/questions/53888878/cv2-warn0-terminating-async-callback-when-attempting-to-take-a-picture

# How to clear the interpreter console?
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console

# Quick and easy file dialog in Python?
# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python

# Python tkinter askopenfilename not responding
# https://stackoverflow.com/questions/51662441/python-tkinter-askopenfilename-not-responding

# AttributeError: module 'cv2.cv2' has no attribute 'createLBPHFaceRecognizer'
# https://stackoverflow.com/questions/44633378/attributeerror-module-cv2-cv2-has-no-attribute-createlbphfacerecognizer