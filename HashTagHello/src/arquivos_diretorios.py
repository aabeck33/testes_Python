'''
    Recursos da biblioteca OS
'''

'''
import os

caminho = r'C:\Users\beck_\OneDrive\Documents\eclipse-workspace\other'
novo_caminho = r'C:\Users\beck_\OneDrive\Documents\eclipse-workspace\<outro_caminho>'
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)
for arquivo in lista_arquivos:
    os.rename(f'{caminho}/{arquivo}','{novo_caminho}/{arquivo}')
'''

'''
### Listar diretórios e arquivos:
import os

root = os.path.join('..\..', 'HashTagHello')

for directory, subdir_list, file_list in os.walk(root):
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)
    print()
'''
'''
### Renomear os arquivos de um disretório:
import datetime
import os

root = os.path.join('..', 'food')

for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        source_name = os.path.join(directory, name)
        timestamp = os.path.getmtime(source_name)
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')
        target_name = os.path.join(directory, f'{modified_date}_{name}')
        print(f'Renaming: {source_name} to: {target_name}')
        os.rename(source_name, target_name)
'''
print('Ola!')