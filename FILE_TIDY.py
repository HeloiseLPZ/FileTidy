from os import listdir
from os.path import isfile, join
import os
import shutil

file_path = r'C:\Users\lophel\Downloads'

# récupérer tous les fichiers
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

# créer une liste et un dictionnaire vide
file_list = []
filetype_dict = {}

# Créer une loop
for file in files:

    # découper le nom de l'extention
    filetype = file.split('.')[1]

    # Vérifier si le fichier existe dans la liste
    if filetype not in file_list:

        #Ajouter le type de fichier dans la liste si ce n'est pas le cas
        file_list.append(filetype)

        # Nommer le nouveau fichier
        new_folder_name = file_path+'/' + filetype + '_fichier'

        # Ajouter le nouveau nom de fichier dans le dictionnaire
        filetype_dict[str(filetype)] = str(new_folder_name)

        # Vérifier si le fichier existe dans la liste
        if os.path.isdir(new_folder_name) == True:


            # Sortir de la loop s'il existe
            continue
        else:

            # Créer le nouveau fichier s'il n'existe pas
            os.mkdir(new_folder_name)

i = 1

# Créer la loop pour tous les fichiers
for file in files:

    # Récupérer le chemin source de tous les fichiers
    src_path = file_path+'/'+file

    # découper le nom de l'extention
    filetype = file.split('.')[1]

    # Vérifier si le fichier existe dans le dictionnaire
    if filetype in filetype_dict.keys():

        # Ajouter dans le dictionnaire s'il n'existe pas
        dest_path = filetype_dict[str(filetype)]

        # Changer la destination du fichier
        shutil.move(src_path, dest_path)

    # Print from where to where a file is being moved
    #print(i, '. ', src_path + '>>>' + dest_path)

    # Incrémenter la variable de 1
    i = i+1
