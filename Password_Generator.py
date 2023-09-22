# Passwort Gen in Python
# Made by github.com/chatopex
# Version 1.0.0 I Python 3.9

import string
import secrets

print("Hier sind 10 Passwörter:")
print("                        ")

def passwort_generator(anzahl_passwoerter, laenge):
    passwoerter = []
    zeichen = string.ascii_letters + string.digits + string.punctuation  # ASCII Buchstaben, Ziffern und Sonderzeichen
    for _ in range(anzahl_passwoerter):
        passwort = ''.join(secrets.choice(zeichen) for _ in range(laenge))
        passwoerter.append(passwort)
    return passwoerter

# 10 Passwörter der Länge 20 generieren
passwoerter_liste = passwort_generator(10, 20)

# Passwörter ausgeben
for pw in passwoerter_liste:
    print(pw)
