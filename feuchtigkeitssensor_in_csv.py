import RPi.GPIO as GPIO
import time
import csv
import os
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO_OUT = 4    # Versorgt Divider kurz
GPIO_IN  = 17   # Liest Messknoten
GPIO_LED = 27   # LED-Anzeige

# Setup
GPIO.setup(GPIO_OUT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GPIO_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GPIO_LED, GPIO.OUT, initial=GPIO.LOW)

# CSV-Datei vorbereiten
csv_file = "soil_log.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, mode="a", newline="") as f:
    writer = csv.writer(f)
    # Header schreiben, falls Datei neu ist
    if not file_exists:
        writer.writerow(["Timestamp", "Value", "Status"])

def measure_once(pulse_ms=10):
    GPIO.output(GPIO_OUT, GPIO.HIGH)
    time.sleep(pulse_ms/1000.0)      # z.B. 10 ms
    val = GPIO.input(GPIO_IN)        # 0 = LOW (feucht), 1 = HIGH (trocken)
    GPIO.output(GPIO_OUT, GPIO.LOW)
    return val

try:
    while True:
        v = measure_once(10)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if v == 0:
            GPIO.output(GPIO_LED, GPIO.HIGH)
            status = "Feucht"
            print(f"{timestamp} -> Feucht")
        else:
            GPIO.output(GPIO_LED, GPIO.LOW)
            status = "Trocken"
            print(f"{timestamp} -> Trocken")

        # Ergebnis in CSV schreiben
        with open(csv_file, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, v, status])

        time.sleep(2.0)   # Messintervall (anpassbar)

finally:
    GPIO.cleanup()
