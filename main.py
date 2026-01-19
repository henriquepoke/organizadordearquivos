from pathlib import Path
import shutil
from datetime import datetime

agora = datetime.now()

organizador = Path('organizador')
registro = Path('registro.log')

arquivosMovidos = dict()
logList = list()

for arquivo in organizador.iterdir():
    match arquivo.suffix:
        case '.png':
            pngDir = Path('pastas/png')
            if pngDir.exists():
                print('.png,', end=' ')
                shutil.move(arquivo, pngDir)
                arquivosMovidos = {
                    'arquivo': arquivo.name,
                    'horário': agora.strftime('%H horas e %m minutos do dia %d do mes %m do ano %Y')
                }
                logList.append(arquivosMovidos)
            else:
                pngDir.mkdir()
        case '.jpg':
            JpgDir = Path('pastas/jpg')
            if JpgDir.exists():
                print('.jpg,', end= ' ')
                shutil.move(arquivo, JpgDir)
                arquivosMovidos = {
                    'arquivo': arquivo.name,
                    'horário': agora.strftime('%H horas e %m minutos do dia %d do mes %m do ano %Y')
                }
                logList.append(arquivosMovidos)
            else:
                JpgDir.mkdir()
        case '.pdf':
            pdfDir = Path('pastas/pdf')
            if pdfDir.exists():
                print('.pdf,', end= ' ')
                shutil.move(arquivo, pdfDir)
                arquivosMovidos = {
                    'arquivo': arquivo.name,
                    'horário': agora.strftime('%H horas e %m minutos do dia %d do mes %m do ano %Y')
                }
                logList.append(arquivosMovidos)
            else:
                pdfDir.mkdir()
        case '.docx':
            docxDir = Path('pastas/docx')
            if docxDir.exists():
                print('.docx,', end= ' ')
                shutil.move(arquivo, docxDir)
                arquivosMovidos = {
                    'arquivo': arquivo.name,
                    'horário': agora.strftime('%H horas e %m minutos do dia %d do mes %m do ano %Y')
                }
                logList.append(arquivosMovidos)
            else:
                docxDir.mkdir()
        case '.xlsx':
            xlsxDir = Path('pastas/xlsx')
            if xlsxDir.exists():
                print('.xlsx,', end= ' ')
                shutil.move(arquivo, xlsxDir)
                arquivosMovidos = {
                    'arquivo': arquivo.name,
                    'horário': agora.strftime('%H horas e %m minutos do dia %d do mes %m do ano %Y')
                }
                logList.append(arquivosMovidos)
            else:
                xlsxDir.mkdir()
        case '.txt':
            txtDir = Path('pastas/txt')
            if txtDir.exists():
                print('e .txt', end= ' ')
                shutil.move(arquivo, txtDir)
                arquivosMovidos = {
                    'arquivo': arquivo.name,
                    'horário': agora.strftime('%d/%m/%Y %H:%M')
                }
                logList.append(arquivosMovidos)
            else:
                txtDir.mkdir()
print('existem...')
print(logList)

with open('registro.log', 'a', encoding='utf-8') as arquivo:
    for log in logList:
        linha = f"[INFO] {log['arquivo']} movido | Horário: {log['horário']}\n"
        arquivo.write(linha)