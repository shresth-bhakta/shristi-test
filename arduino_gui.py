import tkinter as tk
from serial_backend import ArduinoSerial

# Connect to Arduino (Change 'COM3' to your port, e.g., '/dev/ttyUSB0' on Linux)
arduino = ArduinoSerial(port='COM3')

def send_to_arduino():
    command = entry.get()
    if command:
        output = arduino.send_command(command)
        output_label.config(text=f"Arduino: {output}")

# GUI Setup
root = tk.Tk()
root.title("Arduino Serial Monitor")

tk.Label(root, text="Enter Arduino Command:").pack()
entry = tk.Entry(root, width=30)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_to_arduino)
send_button.pack()

output_label = tk.Label(root, text="Arduino Output: ")
output_label.pack()

root.mainloop()
