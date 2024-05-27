# Proiect Rețele de Calculatoare

Acest proiect este o aplicație simplă client-server care permite clientului să controleze anumite aplicații de pe partea de server. Clientul poate trimite comenzi serverului pentru a efectua acțiuni asupra aplicațiilor suportate (aplicația nativă de muzică Apple Music și aplicația Terminal).

## Cum să începi

Pentru a începe cu acest proiect, va trebui să aveți Python instalat pe mașina locală și modulul AppleScript. Clonați acest repository și navigați la directorul proiectului.

## Structura Proiectului

Proiectul are următoarea structură:

```
.
├── cerinta.txt
├── client.py
├── server.py
```

- `cerinta.txt`: Acest fișier conține cerințele proiectului.
- `client.py`: Acesta este scriptul de partea clientului care trimite comenzi către server.
- `server.py`: Acesta este scriptul de partea serverului care ascultă comenzile de la client și efectuează acțiuni asupra aplicațiilor suportate.

## Utilizare

1. Rulați scriptul server:

```sh
python server.py
```

2. Într-un terminal separat, rulați scriptul client:

```sh
python client.py
```

3. Clientul va afișa o listă de aplicații disponibile și comenzi. Introduceți o comandă pentru a efectua o acțiune asupra unei aplicații. Introduceți "exit" pentru a închide clientul.

## Cerințe Proiect

Cerințele proiectului sunt detaliate în fișierul `cerinta.txt`. Vă rugăm să consultați acest fișier pentru mai multe informații.

## Contribuții

Acest proiect a fost realizat de:
  - Popa Isabela Maria
  - Plăstoi Răzvan
  - Vorniceanu Vlad-Ioan
