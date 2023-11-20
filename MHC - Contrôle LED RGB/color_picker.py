#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time

# Configuration des broches GPIO
led_red = 17
led_green = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setwarnings(False)

# Définir la fréquence PWM
PWM_FREQ = 1000

# Configuration PWM avec une plage de 0 à 100
red_pwm = GPIO.PWM(led_red, PWM_FREQ)
green_pwm = GPIO.PWM(led_green, PWM_FREQ)

# Démarrer les PWM avec un rapport cyclique initial de 0
red_pwm.start(0)
green_pwm.start(0)

# Récupérer les arguments passés au script
r = int(sys.argv[1]) / 2.55
g = int(sys.argv[2]) / 2.55
b = int(sys.argv[3]) / 2.55

# Fonction pour définir la couleur en utilisant les valeurs R, G, B
def set_color(r, g, b):
    red_pwm.ChangeDutyCycle(r)
    green_pwm.ChangeDutyCycle(g)

# Exécution en fonction des valeurs R, G, B
set_color(r, g, b)

# Vous pouvez ajouter d'autres actions ici en fonction de vos besoins

# Arrêter les PWM et nettoyer les broches GPIO
#red_pwm.stop()
#green_pwm.stop()
#GPIO.cleanup()*
time.sleep(2)