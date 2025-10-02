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
- (📝 Option für **Logging & Erweiterungen** (z. B. Telegram Notifications))

---

## 🔧 Hardware Setup

### Benötigte Komponenten
- Raspberry Pi (mit aktiviertem SPI)
- 4 mal 330 Ω Widerstände
- 1 mal 1kΩ Widerstand
- 1 mal LED
- Kabel

### Verdrahtung
Siehe https://github.com/Nathanyiel/Raspi-Feuchtigkeitssensor/blob/main/Feuchtigkeitssensor_Schaltplan.drawio.png

---
