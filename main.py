"""
Credits: Developed by ethical-ux
"""

import sys
import argparse
from utils import lfiles, cfiles, sfiles, rfiles, bdirectory

def main():
    parser = argparse.ArgumentParser(description="Boîte à outils pour développeurs.")
    parser.add_argument('--list', help="Lister tous les fichiers dans un répertoire", type=str)
    parser.add_argument('--copy', nargs=2, help="Copier des fichiers d'un répertoire à un autre", type=str)
    parser.add_argument('--search', nargs=2, help="Rechercher un motif regex dans les fichiers d'un répertoire", type=str)
    parser.add_argument('--rename', nargs=3, help="Renommer des fichiers en remplaçant un texte par un autre", type=str)
    parser.add_argument('--backup', help="Créer une sauvegarde d'un répertoire", type=str)

    args = parser.parse_args()

    if args.list:
        files = lfiles(args.list)
        for file in files:
            print(file)

    if args.copy:
        src_dir, dest_dir = args.copy
        cfiles(src_dir, dest_dir)

    if args.search:
        directory, pattern = args.search
        matches = sfiles(directory, pattern)
        for file, found in matches:
            print(f"Dans {file}, trouvé : {found}")

    if args.rename:
        directory, old_text, new_text = args.rename
        rfiles(directory, old_text, new_text)

    if args.backup:
        backup_dir = bdirectory(args.backup)
        print(f"Sauvegarde créée : {backup_dir}")

if __name__ == "__main__":
    main()

"""
Credits: Developed by ethical-ux
"""