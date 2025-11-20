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

# 🧰 Installation & benötigte Libraries

Dieses Projekt nutzt die Python-Bibliothek **RPi.GPIO**, um GPIO-Pins des Raspberry Pi anzusteuern.  
Damit wird sowohl der Feuchtigkeitssensor ausgelesen als auch eine LED gesteuert.

> **Hinweis:**  
> Die Bibliothek funktioniert **nur auf einem echten Raspberry Pi**.  
> Unter Windows und macOS kann das Script bearbeitet, aber **nicht ausgeführt** werden.

---

## 💻 Installation auf dem Raspberry Pi

### Terminal öffnen
- Raspberry-Menü → **Accessories → Terminal**  
oder  
- **Ctrl + Alt + T**

### Libraries installieren
```bash
sudo apt update
sudo apt install python-rpi-gpio
```

## 🪟 Windows Nutzer

Unter Windows können keine Raspberry-Pi-GPIO-Pins angesprochen werden.  
Das Script kann **nicht ausgeführt**, aber normal **bearbeitet** werden.

### CMD öffnen
- Startmenü → **cmd** eingeben → Enter

### PowerShell öffnen
- Startmenü → **PowerShell** eingeben → Enter

---

## 🍎 macOS Nutzer

Auch macOS kann keine Raspberry-Pi-GPIOs ansteuern.  
Das Script kann hier nur **bearbeitet oder verwaltet** werden.

### Terminal öffnen
- **CMD + Leertaste** → „Terminal“ eingeben → Enter  
oder  
- Finder → **Programme → Dienstprogramme → Terminal**

---

## ▶️ Script starten (nur Raspberry Pi)

```bash
python feuchtigkeitssensor.py
```

### Verdrahtung
Siehe https://github.com/Nathanyiel/Raspi-Feuchtigkeitssensor/blob/main/Feuchtigkeitssensor_Schaltplan.drawio.png

---
