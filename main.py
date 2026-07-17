from pathlib import Path
import shutil 

caminho = input('Digite o caminho da pasta(ex: C:/Users/nome/Downloads): ')
diretorio = Path(caminho)
if not diretorio.exists():
    print("Essa pasta não existe.")
    print("Reinicie o programa e tente novamente.")
    exit()

dicionario_pastas = {
    # Imagens
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".gif": "Imagens",
    ".bmp": "Imagens",
    ".webp": "Imagens",

    # Documentos
    ".pdf": "Documentos",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".md": "Documentos",
    ".rtf": "Documentos",

    # Planilhas
    ".xls": "Planilhas",
    ".xlsx": "Planilhas",
    ".csv": "Planilhas",

    # Apresentações
    ".ppt": "Apresentacoes",
    ".pptx": "Apresentacoes",

    # Áudio
    ".mp3": "Musicas",
    ".wav": "Musicas",
    ".flac": "Musicas",

    # Vídeos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    # Compactados
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",

}

for arquivo in diretorio.iterdir():
    if arquivo.is_file():
        categoria = dicionario_pastas.get(arquivo.suffix.lower(), 'Outros')
        pasta_destino = diretorio / categoria
        destino = pasta_destino / arquivo.name
        pasta_destino.mkdir(exist_ok=True, parents=True)
        print(f"Movendo {arquivo.name} para {categoria}")
        shutil.move(arquivo, destino)