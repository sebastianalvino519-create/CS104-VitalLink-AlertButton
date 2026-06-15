import time
import requests
import RPi.GPIO as GPIO

# --- CONFIGURACIÓN DE TELEGRAM ---
TOKEN = "8861759862:AAEKJrn_VhFccRKfUdkhhJGl2Thi9tCc4tU"
CHAT_ID = "8881369051"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# --- CONFIGURACIÓN DE LOS PINES ---
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False
print("Monitoreando eventos... Presiona el botón de alerta.")

# --- BUCLE PRINCIPAL ---
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")
            
            # Código nuevo que envía la alerta a tu celular
            payload = {
                "chat_id": CHAT_ID,
                "text": "Someone pressed the alert button!"
            }
            try:
                requests.post(URL, json=payload)
                print("¡Alerta enviada a Telegram!")
            except Exception as e:
                print(f"Error al enviar Telegram: {e}")
                
            button_pressed = True
            
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
            
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nPrograma finalizado por el usuario.")
    GPIO.cleanup()
