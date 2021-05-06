"""
     _____ _   _  _____     _____ ________  ___ _____  ______  ___ ______
    |  _  | \ | ||  ___|   |_   _|_   _|  \/  ||  ___| | ___ \/ _ \|  _  \
    | | | |  \| || |__ ______| |   | | | .  . || |__   | |_/ / /_\ \ | | |
    | | | | . ` ||  __|______| |   | | | |\/| ||  __|  |  __/|  _  | | | |
    \ \_/ / |\  || |___      | |  _| |_| |  | || |___  | |   | | | | |/ /
     \___/\_| \_/\____/      \_/  \___/\_|  |_/\____/  \_|   \_| |_/___/

    by Shrafdine OURO-AGORO
    Date: 05/05/2021
"""

import sys
import os
import string
import random


OAS_characters_SAO = string.ascii_letters + string.digits + string.punctuation


def helper():
    """
        Fonction d'aide qui s'affichera à la moindre erreur hahaha !!!
    """
    print("\t===========================================")
    print("\t              ONE-TIME PAD                 ")
    print("\t===========================================")

    print("Bienvenue dans l'aide du programme ONE-TIME PAD.\n")
    print("Description:")
    print(
        "\t Ce programme permet de chiffrer un fichier texte à l'aide de l’algorithme de chiffrement [ One-Time-Pad ].")
    print(
        "\t Il renvoie un fichier de sortie dans le repertoire courant. Il genere et enregistre dans un troisieme   \n"
        "\t fichier (dans le rpertoire courant) les PAD (les cles) associes à chaque nom de fichier 'texte' chiffre \n"
        "\t sous forme : 'noms_fichier_chiffre : pad'")
    print("Utilisations:")
    print(
        "\t #python main.py <chemin_vers_le_fichier>: chiffre le fichier texte et attribue un nom par défaut au fichier"
        "\n\t\t de sortie.")
    print(
        "\t #python main.py <chemin_vers_le_fichier> <nom_du_fichier_de_sortie>: chiffre le fichier texte et permet à\n"
        "\t\t l'utilisateur de nommer le fichier de sortie.")
    print("\t #python main.py <chemin_vers_le_fichier> -decrypt <PAD>: dechiffre  un un fichier chiffre et affiche le\n"
          "\t\t résultat dans la console.")


def load_from_file(filename):
    """
    Cette fonction permet de charger le contenu d'un fichier dans une liste.
    :param filename:nom du fichier à charger
    :return: contents: liste des caractères du fichier
    """
    # Verifie si le fichier existe
    try:
        open(filename, "r")
    except:
        sys.exit("Fichier Introuvable!!!\n")
    # Verifie si le fichier est vide
    if os.path.getsize(filename) == 0:
        sys.exit("Le fichier " + filename + " est vide!!!\n")
    # Ouverture du fichier et chargement de la liste
    with open(filename, "r") as file:
        contents = file.read()
    return list(contents)


def load_from_text(filename, cyphertext):
    """
    Cette fonction permet de créer un fichier de sortie. Si ce fichier
    existe déjà, il l'écrase.
    :param filename: nom du fichier chiffré
    :param cyphertext: texte chiffré
    :return:
    """
    with open(filename, "w") as file:
        for letter in cyphertext:
            file.write(letter)
    print("Vous trouverez le texte chiffré dans le fichier " + filename + ".")


def generate_file(log_filename, filename, key):
    """
    Cette fonction permet de créer le fichier des log. Si celui-ci
    existe déjà, il ajoute à la ligne
    :param log_filename: nom du fichier log
    :param filename: nom du fichier chiffré
    :param key: pad
    :return:
    """
    with open(log_filename, "a") as file:
        file.write(filename + " : ")
        for letter in key:
            file.write(letter)
        file.write("\n")
    print("Vous trouverez le PAD correspondant au fichier " + filename + " dans le fichier " + log_filename +
          "\nReferer vous à l'aide en cas d'incompréhension.")


def generate_key(length):
    """
    Cette fonction permet de générer le pad aléatoirement en fonction de la taille du texte
    :param length: taille du texte
    :return: key: le pad
    """
    key = []
    for i in range(length):
        key.append(random.choice(OAS_characters_SAO))  # Choix d'un caractère aléatoirement
    return key


def encode(contents, key):
    """
    Cette fonction permet de chiffrer le texte.
    :param contents: le texte à chiffrer
    :param key: le pad
    :return: cyphertext: le texte chiffré.
    """
    cyphertext = []
    # Opération
    for i in range(len(contents)):
        cyphertext.append(chr(ord(contents[i]) ^ ord(key[i])))
    return cyphertext


def decrypt(cyphertext, key):
    """
    Cette fonction permet de déchiffrer un texte.
    Si la taille du pad ne correspond pas à celle du texte, elle renvoie
    message d'erreur.
    :param cyphertext: texte à déchiffrer
    :param key: pad correspondant
    :return: contents: le texte initiale
    """
    contents = []
    # Verifie si le texte et le pad ont la même taille
    if len(cyphertext) != len(key):
        sys.exit("Le PAD et le text sont incompatibles (pas de même tail"
                 "le).\nVerifier le fichier ou le PAD et reessayer!!\n")
    # Opération
    for i in range(len(cyphertext)):
        contents.append(chr(ord(cyphertext[i]) ^ ord(key[i])))
    return contents


def generate_default_name(name):
    """
    Cette fonction génère un nom par défaut pour le fichier de sortie
    :param name: nom du fichier à chiffré
    :return: le nom par défaut
    """
    default_name = "".join(name.split(".")[:-1])
    return default_name + "_chiffre.txt"


if __name__ == "__main__":
    OAS_logFileName_SAO = "padLog.txt"

    # Vérification du nombre d'argument
    if len(sys.argv) < 2:
        print("Pas assez d'arguments en paramètres")
        helper()
        exit()

    # Chiffrement
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":     # Affichage de l'aide Aide
            helper()
            exit()
        else:                       # Nom du fichier de sortie par défaut
            OAS_defaultName_SAO = generate_default_name(sys.argv[1])
            OAS_contents_SAO = load_from_file(sys.argv[1])
            OAS_pad_SAO = generate_key(len(OAS_contents_SAO))
            OAS_cyphertext_SAO = encode(OAS_contents_SAO, OAS_pad_SAO)
            print("Texte chiffré: ", end="")
            print("".join(OAS_cyphertext_SAO))
            load_from_text(OAS_defaultName_SAO, OAS_cyphertext_SAO)
            generate_file(OAS_logFileName_SAO, OAS_defaultName_SAO, OAS_pad_SAO)
    else:                           # Nom du fichier de sortie spécifié
        if len(sys.argv) == 3:
            OAS_contents_SAO = load_from_file(sys.argv[1])
            OAS_pad_SAO = generate_key(len(OAS_contents_SAO))
            OAS_cyphertext_SAO = encode(OAS_contents_SAO, OAS_pad_SAO)
            print("".join(OAS_cyphertext_SAO))
            load_from_text(sys.argv[2], OAS_cyphertext_SAO)
            generate_file(OAS_logFileName_SAO, sys.argv[2], OAS_pad_SAO)

    # Dechiffrement
        if len(sys.argv) == 4:
            if sys.argv[2] == "-decrypt":
                OAS_cyphertext_SAO = load_from_file(sys.argv[1])
                print("".join(decrypt(OAS_cyphertext_SAO, list(sys.argv[3]))))
            else:
                print(sys.argv[2] + ": Argument non reconnu")
                helper()
