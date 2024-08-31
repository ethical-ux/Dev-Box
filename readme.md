# Boîte à Outils pour Développeurs

**Credits: Developed by ethical-ux**

Ce projet fournit une série d'outils utilitaires en Python pour aider dans les tâches courantes liées à la gestion de fichiers et à la manipulation de texte. Vous pouvez utiliser ces outils via la ligne de commande pour simplifier vos processus de développement.

## Fonctionnalités

1. **Lister les fichiers**
   - Lister tous les fichiers dans un répertoire spécifique.
   - Optionnellement, filtrer les fichiers par extension.

2. **Copier des fichiers**
   - Copier des fichiers d'un répertoire source vers un répertoire de destination.
   - Optionnellement, filtrer les fichiers par extension.

3. **Rechercher dans les fichiers**
   - Rechercher un motif spécifique (utilisant des expressions régulières) dans tous les fichiers d'un répertoire.

4. **Renommer des fichiers**
   - Renommer les fichiers dans un répertoire en remplaçant un texte spécifique par un autre.

5. **Sauvegarde d'un répertoire**
   - Créer une sauvegarde d'un répertoire avec un horodatage pour éviter les conflits.

## Installation

1. Clonez le dépôt :

   ```
   git clone https://github.com/ethical-ux/Dev-Box.git
   ```

2. Accédez au répertoire du projet :

   ```
   cd Dev-Box
   ```

## Utilisation

Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez ensuite utiliser les outils via la ligne de commande comme suit :

### Lister les fichiers

```
python main.py --list <directory>
```

### Copier des fichiers

```
python main.py --copy <src_dir> <dest_dir>
```

### Rechercher dans les fichiers

```
python main.py --search <directory> "<regex_pattern>"
```

### Renommer des fichiers

```
python main.py --rename <directory> "<old_text>" "<new_text>"
```

### Sauvegarde d'un répertoire

```
python main.py --backup <directory>
```

## Exemples

- **Lister tous les fichiers dans `data/`** :

  ```
  python main.py --list data/
  ```

- **Copier tous les fichiers `.txt` de `source/` vers `destination/`** :

  ```
  python main.py --copy source/ destination/ --extension .txt
  ```

- **Rechercher l'expression "error" dans tous les fichiers du répertoire `logs/`** :

  ```
  python main.py --search logs/ "error"
  ```

- **Renommer les fichiers remplaçant `oldname` par `newname` dans `documents/`** :

  ```
  python main.py --rename documents/ "oldname" "newname"
  ```

- **Créer une sauvegarde du répertoire `project/`** :

  ```
  python main.py --backup project/
  ```

## Auteurs

**Credits: Developed by ethical-ux**

## Licence

Ce projet est sous la licence MIT.