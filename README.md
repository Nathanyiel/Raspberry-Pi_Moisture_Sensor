# Raspi-Feuchtigkeitssensor # 🌱 Plant Moisture Monitor

Ein Raspberry Pi Projekt zur **Überwachung der Bodenfeuchtigkeit** von Pflanzen mit einem kapazitiven Sensor + MCP3008 ADC.  
Das Script misst regelmäßig die Feuchtigkeit und gibt eine **Warnung (LED, Buzzer, Konsole)** aus, wenn der Wert unter einen definierten Schwellwert fällt.  

> Ziel: Nie wieder vergessen, die Pflanze zu gießen! 💧

---

## ✨ Features
- 📊 **Messung der Bodenfeuchtigkeit** über MCP3008 (SPI)
- 🌡️ **Kalibrierung** für "trocken" & "nass" → genaue %-Werte
- 🚨 **Warnung bei Trockenheit** (Konsole, LED, Buzzer)
- 🕐 **Konfigurierbares Intervall, Schwellwert & Hysterese**
- 📝 Option für **Logging & Erweiterungen** (z. B. Telegram Notifications)

---

## 🔧 Hardware Setup

### Benötigte Komponenten
- Raspberry Pi (mit aktiviertem SPI)
- MCP3008 ADC
- Kapazitiver Bodenfeuchtigkeitssensor
- (optional) LED + Widerstand, Buzzer

### Verdrahtung
| Komponente | Pin am Pi (BCM) |
|------------|----------------|
| MCP3008 VDD/VREF | 3.3V |
| MCP3008 AGND/DGND | GND |
| MCP3008 CLK | GPIO11 (SCLK) |
| MCP3008 DOUT | GPIO9 (MISO) |
| MCP3008 DIN | GPIO10 (MOSI) |
| MCP3008 CS | GPIO8 (CE0) |
| Sensor AO | MCP3008 CH0 |
| LED | GPIO23 |
| Buzzer | GPIO18 |

---
