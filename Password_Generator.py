# Passwort Generator in Python
# Made by github.com/chatopex
# Version 1.0.1 I Python 3.9

import string
import secrets

print("Password Gen 1.0.1 by github.com/chatopex")
print("                        ")

def passwort_generator(anzahl_passwoerter, laenge, sonderzeichen):
    passwoerter = []
    zeichen = ""
    if sonderzeichen:
        zeichen = string.ascii_letters + string.digits + string.punctuation
    else:
        zeichen = string.ascii_letters + string.digits
    for _ in range(anzahl_passwoerter):
        passwort = ''.join(secrets.choice(zeichen) for _ in range(laenge))
        passwoerter.append(passwort)
    return passwoerter

# Benutzereingaben abfragen
anzahl_passwoerter = int(input("Wie viele Passwörter möchten Sie generieren: "))
laenge = int(input("Wie lang sollen die Passwörter sein: "))
sonderzeichen = input("Möchten Sie Sonderzeichen in den Passwörtern verwenden? (ja/nein) ")
sonderzeichen = sonderzeichen.lower()

# Passwörter generieren und ausgeben
passwoerter_liste = passwort_generator(anzahl_passwoerter, laenge, sonderzeichen == "ja")
for pw in passwoerter_liste:
    print(pw)
