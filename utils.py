"""
Credits: Developed by ethical-ux
"""

import os
import re
import shutil
from datetime import datetime

#list files
def lfiles(directory, extension=None):
    """Liste tous les fichiers dans un répertoire avec une extension spécifique."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if extension and not filename.endswith(extension):
                continue
            files.append(os.path.join(root, filename))
    return files

#copy files
def cfiles(src_dir, dest_dir, extension=None):
    """Copie des fichiers d'un répertoire source vers un répertoire de destination."""
    files = lfiles(src_dir, extension)
    for file in files:
        dest = os.path.join(dest_dir, os.path.basename(file))
        shutil.copy(file, dest)

#search in files
def sfiles(directory, pattern):
    """Recherche un motif regex dans tous les fichiers d'un répertoire."""
    matches = []
    for file in lfiles(directory):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            found = re.findall(pattern, content)
            if found:
                matches.append((file, found))
    return matches

#rename files
def rfiles(directory, old_text, new_text):
    """Renomme les fichiers dans un répertoire en remplaçant un texte par un autre."""
    for file in lfiles(directory):
        new_name = file.replace(old_text, new_text)
        os.rename(file, new_name)
#backup directory
def bdirectory(directory):
    """Crée une sauvegarde d'un répertoire avec un horodatage."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_dir = f"{directory}_backup_{timestamp}"
    shutil.copytree(directory, backup_dir)
    return backup_dir

"""
Credits: Developed by ethical-ux
"""