#!/usr/bin/env python
# -*- coding: utf-8 -*-


def majuscule(mot: str) -> str:
    """
    Returns the uppercase version of the string
    This function does the same thing as str.upper
    """
    result = ""
    for c in mot:
        if c.islower():
            # Uppercase code + 32 = lowercase letter
            c = chr(ord(c) - 32)
        result += c
    return result


if __name__ == "__main__":
    mots = [
        "riz",
        "cours",
        "voiture",
        "oiseau",
        "bonjour",
        "églantier",
        "arbre",
        "_-_!@#$%?&*()ÉE_-_",
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
