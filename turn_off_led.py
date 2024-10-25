import RPi.GPIO as GPIO

# Correct pin numbers for the LED channels
red_pin = 17  # GPIO pin for red channel of the LED
green_pin = 22  # GPIO pin for green channel
blue_pin = 27  # GPIO pin for blue channel

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Turn off the RGB LED by setting all channels to LOW
GPIO.output(red_pin, GPIO.LOW)
GPIO.output(green_pin, GPIO.LOW)
GPIO.output(blue_pin, GPIO.LOW)

# Clean up GPIO settings
GPIO.cleanup()
