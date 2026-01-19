from pathlib import Path
from datetime import datetime
import shutil

pasta_organizada = Path("arquivos_organizados")

pasta_organizador = Path('organizador')
if not pasta_organizador.exists():
    pasta_organizador.mkdir()
    print(f'Pasta {pasta_organizador} criada com sucesso! Mova os arquivos aqui para organizar.')
    
arquivo_log = Path('registro.log')

arquivos_qtd = 0
extensoes_encontradas = []

for arquivo in Path('organizador').iterdir():
    arquivos_qtd += 1
    extensao = arquivo.suffix[1:]
    if extensao not in extensoes_encontradas:
        extensoes_encontradas.append(extensao)
    sub_pasta = pasta_organizada/extensao
    if not sub_pasta.exists():
        sub_pasta.mkdir(exist_ok=True, parents=True)

    shutil.move(arquivo, sub_pasta/arquivo.name)
    with open(arquivo_log, 'a', encoding='utf-8') as log:
        agora = datetime.now()
        log.write(agora.strftime(f'[INFO] %d/%m/%Y %H:%M:%S Movido o arquivo {arquivo.name} para a pasta {sub_pasta}\n'))
    
print(f'{arquivos_qtd} arquivos organizados com sucesso!\n')
print('Extensões encontradas:')
for extensao in extensoes_encontradas:
    print(extensao, end=' ')
