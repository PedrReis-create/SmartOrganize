from pathlib import Path
import shutil 

# Para indentificar em qual pasta vai cada arquivo
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

# Função Organizar 
def organizar(diretorio, simulação):
    contadores = {}
    arquivos_movidos = 0
    
    for arquivo in diretorio.iterdir():
        if arquivo.is_file():        
            # Descobrir a categoria
            categoria = dicionario_pastas.get(arquivo.suffix.lower(), 'Outros')
            
            # Criar a pasta
            pasta_destino = diretorio / categoria
            
            # Definir destino
            destino = pasta_destino / arquivo.name
            
            # Gerar novo nome se necessário
            contador_nome = 1
            
            while destino.exists():
                novo_nome = f'{arquivo.stem} ({contador_nome}){arquivo.suffix}'
                destino = pasta_destino / novo_nome
                contador_nome += 1
                
            # Mover arquivo
            if not simulação:
                
                # Verificar se destino já existe
                pasta_destino.mkdir(exist_ok=True, parents=True)
                
                print(f"Movendo {arquivo.name} para {destino}")
                shutil.move(arquivo, destino)
                
                
            
            else:
                print(f'Would move {arquivo.name} -> {destino}')
            
            # Incrementa o contador
            arquivos_movidos += 1
            
            if categoria in contadores:
                    contadores[categoria] += 1
            else:
                    contadores[categoria] = 1
                
            
    # Relatório final
            
    print('='*10)
    print('Organization completed successfully!')
    for chave, valor in contadores.items():
        print(f'{chave}: {valor}')
    print(f'Total moved: {arquivos_movidos}')
    print('='*10)
            

print('=' * 10)
print('SmartOrganize')
print('=' * 10)


# MENU
caminho = input('Digite o caminho da pasta(ex: C:/Users/nome/Desktop/Nome_pasta): ')
diretorio = Path(caminho)

print('1 - Organize files \n2 - Simulation')
option = input('Escolha uma opção: ')

if not diretorio.exists():
    print("Essa pasta não existe.")
    print("Reinicie o programa e tente novamente.")
    exit()

if option == '1':
    organizar(diretorio, False)

elif option == '2':
    # Simulação
    organizar(diretorio, True)
    
else:
    print('Opção inválida')
    exit()
        
        
# Comentário para melhor compreensão das váriaveis dentro de organizar()

# diretorio
# │
# └── C:/Users/User/Downloads
#       │
#       ├── categoria
#       │      │
#       │      └── "Documentos"
#       │
#       ├── pasta_destino
#       │      │
#       │      └── C:/Users/User/Downloads/Documentos
#       │
#       └── destino
#              │
#              └── C:/Users/User/Downloads/Documentos/curriculo.pdf