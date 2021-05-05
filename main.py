import sys
import string
import random

OAS_characters_OAS = string.ascii_letters + string.digits + string.punctuation


def load_from_file(filename):
    try:
        open(filename, "r")
    except:
        sys.exit("Fichier Introuvable")
    with open(filename, "r") as file:
        contents = file.read()
    return list(contents)


def create_from_text(filename, cyphertext):
    with open(filename, "w") as file:
        file.write(cyphertext)


def generate_key(length):
    key = []
    for i in range(length):
        key.append(random.choice(OAS_characters_OAS))
    return key


def encode(filename):
    contents = load_from_file(filename)
    key = generate_key(len(contents))
    cyphertext = []
    for i in range(len(contents)):
        cyphertext.append(chr(ord(contents[i]) ^ ord(key[i])))
    return cyphertext


if __name__ == "__main__":
    encode("tzz")
