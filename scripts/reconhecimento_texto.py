import pytesseract
from PIL import Image
import os

# Configurar o caminho do Tesseract (se necessário)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def reconhecer_texto(caminho_imagem):
    """
    Reconhece o texto em uma imagem usando Tesseract OCR.
    """
    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem, lang='por')  # 'por' para português
    return texto

def processar_imagens(pasta_entrada, pasta_saida):
    """
    Processa todas as imagens na pasta de entrada e salva os textos reconhecidos na pasta de saída.
    """
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.endswith(('.jpg', '.png', '.jpeg')):
            caminho_imagem = os.path.join(pasta_entrada, nome_arquivo)
            texto = reconhecer_texto(caminho_imagem)

            nome_saida = f"resultado{os.path.splitext(nome_arquivo)[0][-1]}.txt"
            caminho_saida = os.path.join(pasta_saida, nome_saida)

            with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write(texto)

            print(f"Texto reconhecido de {nome_arquivo} salvo em {nome_saida}")

if __name__ == '__main__':
    pasta_entrada = r'inputs'
    pasta_saida = r'outputs'
    processar_imagens(pasta_entrada, pasta_saida)