import os
import shutil
# from pathlib import Path

def check_archive_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Fout: De map '{folder_path}' bestaat niet.")
        return False
    return True

def get_files_in_folder(folder_path):
    files = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            files.append(file)
    return files

def archive_files(archive, files):
    for file in files:
        extension = os.path.splitext(file)[1].lower()
        file_name = os.path.basename(file)
        file = os.path.join(archive, file)
        print(f"Bestand: {file_name}, Extensie: {extension}")
        if extension in [".docx", ".pdf", ".txt"]:
            doelbestand = os.path.join(f"archief/documenten/", file_name)
            shutil.copy(file, doelbestand)
        elif extension in [".jpg", ".jpeg", ".png", ".gif"]:
            doelbestand = os.path.join(f"archief/afbeeldingen/", file_name)
            shutil.copy(file, doelbestand)
        else:
            doelbestand = os.path.join(f"archief/overig/", file_name)
            shutil.copy(file, doelbestand)      
      