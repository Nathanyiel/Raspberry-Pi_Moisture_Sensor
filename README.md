# Raspi-Feuchtigkeitssensor # 🌱 Plant Moisture Monitor

Ein Raspberry Pi Projekt zur **Überwachung der Bodenfeuchtigkeit** von Pflanzen mit einfachen Mitteln.  
Das Script prüft regenmäßig die Feuchtigkeit der Erde und gibt eine Rückgabe über eine LED und die Console.  

> Ziel: Nie wieder vergessen, die Pflanze zu gießen! 💧

---

## ✨ Features
- 📊 **Messung der Bodenfeuchtigkeit** mit einfachen Mitteln
- 🌡️ **Rückgabe** von Boolen (nass/trocken) 
- 🚨 **Warnung bei Trockenheit** (Konsole, LED)
- 🕐 **Konfigurierbares Intervall** zur Minderung der Korrosion

---

## 🔧 Hardware Setup

### Benötigte Komponenten
- Raspberry Pi (mit aktiviertem SPI)
- 4 mal 330 Ω Widerstände
- 2 mal 1kΩ Widerstand
- 1 mal LED
- Kabel

🧰 Installation & benötigte Libraries

Für die Ansteuerung der GPIO-Pins verwendet das Projekt die Python-Bibliothek RPi.GPIO.
Sie ist notwendig, um die Feuchtigkeit auszulesen und die LED anzusteuern.

Hinweis: Die Bibliothek funktioniert nur auf einem echten Raspberry Pi.
Unter Windows oder macOS kann das Script bearbeitet, aber nicht ausgeführt werden.

💻 Installation auf dem Raspberry Pi

Terminal öffnen

Raspberry-Menü → Accessories → Terminal
oder

Ctrl + Alt + T drücken

Library installieren

sudo apt update
sudo apt install python3-rpi-gpio


Damit ist die Umgebung vollständig eingerichtet.

🪟 Windows Nutzer

Unter Windows können die GPIOs nicht genutzt werden.
Das Script kann dort nicht ausgeführt, aber problemlos bearbeitet werden.

CMD öffnen:
Startmenü → „cmd“ eingeben → Enter

PowerShell öffnen:
Startmenü → „PowerShell“ eingeben → Enter

🍎 macOS Nutzer

Auch macOS kann kein Raspberry-Pi-GPIO ansteuern.
Das Script lässt sich aber bearbeiten oder für GitHub verwalten.

Terminal öffnen:
CMD + Leertaste → „Terminal“ eingeben → Enter
oder Finder → Programme → Dienstprogramme → Terminal

▶️ Script starten (nur Raspberry Pi)
python3 feuchtigkeitssensor.py

### Verdrahtung
Siehe https://github.com/Nathanyiel/Raspi-Feuchtigkeitssensor/blob/main/Feuchtigkeitssensor_Schaltplan.drawio.png

---
