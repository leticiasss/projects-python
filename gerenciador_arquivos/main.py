import os
import glob
import shutil

extensions = {
  "jpg": "images",
  "png": "images",
  "svg": "images",
  "exe": "programs",
  "msi": "programs",
  "pdf": "documents",
  "docx": "documents",
  "txt": "documents",
  "xlsx": "documents",
  "rar": "arquive",
  "zip": "arquive",
  "gz": "arquive",
  "tar": "arquive",
  "json": "json",
  "css": "web",
  "js": "web",
  "html": "web",
  "apk": "apk"
}

path = r"/home/leticia/Downloads" # pasta de downloads do Linux (alterar quando rodar em outro distro)

for extension, folder_name in extensions.items():
  files = glob.glob(os.path.join(path, f'*.{extension}'))  # retorna uma lista de path e suas extensões
  print(f'[*] Encontrados {len(files)} arquivo(s) com extensão "{extension}"')

  if not os.path.isdir(os.path.join(path, folder_name)) and files:
    print(f'[+] Making {folder_name} folder!')
    os.mkdir(os.path.join(path, folder_name))   # Cria uma pasta com o folder_name, caso ela não exista

  for file in files:
    basename = os.path.basename(file)
    dst = os.path.join(path, folder_name, basename)  

    print(f'[*] Moving {file} for {dst}')
    shutil.move(file, dst)