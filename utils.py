import os

# Caminho relativo das pastas de entrada e saída de imagens
INPUT_DIR = os.path.join('Data', 'Input')
OUTPUT_DIR = os.path.join('Data', 'Output')


def in_file(filename):
    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)
