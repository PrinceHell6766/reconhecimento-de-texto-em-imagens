import cv2
import pytesseract
import os

# Configurar o caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def reconhecer_texto(caminho_imagem):
    """
    Reconhece o texto em uma imagem usando Tesseract OCR.
    """
    # Ler a imagem
    imagem = cv2.imread(caminho_imagem)

    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar OCR na imagem
    texto = pytesseract.image_to_string(imagem_cinza, lang='por')  # 'por' para português

    return texto

def processar_imagens(pasta_entrada, pasta_saida):
    """
    Processa todas as imagens na pasta de entrada e salva os textos reconhecidos na pasta de saída.
    """
    # Verificar se a pasta de saída existe, caso contrário, criar
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Processar cada imagem na pasta de entrada
    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.endswith(('.jpg', '.png', '.jpeg')):
            # Caminho completo da imagem
            caminho_imagem = os.path.join(pasta_entrada, nome_arquivo)

            # Reconhecer o texto na imagem
            texto = reconhecer_texto(caminho_imagem)

            # Gerar o nome do arquivo de saída
            nome_saida = f"resultado{os.path.splitext(nome_arquivo)[0][-1]}.txt"  # resultado1.txt, resultado2.txt, etc.
            caminho_saida = os.path.join(pasta_saida, nome_saida)

            # Salvar o texto reconhecido em um arquivo
            with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write(texto)

            print(f"Texto reconhecido de {nome_arquivo} salvo em {nome_saida}")

if __name__ == '__main__':
    # Definir os caminhos das pastas de entrada e saída
    pasta_entrada = r'C:\Users\rodri\Documents\reconhecimento_texto\inputs'
    pasta_saida = r'C:\Users\rodri\Documents\reconhecimento_texto\outputs'

    # Processar as imagens
    processar_imagens(pasta_entrada, pasta_saida)