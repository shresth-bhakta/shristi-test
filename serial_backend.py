import serial
import time

class ArduinoSerial:
    def __init__(self, port, baudrate=9600):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Allow time for Arduino to reset

    def send_command(self, command):
        self.ser.write((command + '\n').encode())  # Send command
        time.sleep(0.5)  # Give time for Arduino to respond
        return self.ser.readline().decode().strip()  # Read response

    def close(self):
        self.ser.close()
