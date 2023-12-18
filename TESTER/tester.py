import serial
import tkinter as tk
from threading import Thread

# Function to read data from Arduino
def read_serial_data():
    while True:
        try:
            line = ser.readline().decode().strip()
            if line:
                update_gui(line)
        except UnicodeDecodeError:
            pass

# Function to update the GUI with received data
def update_gui(data):
    data_list = data.split(',')
    digital_data = data_list[1:54]
    analog_data = data_list[55:]

    digital_labels = [f'D{i+2}' for i in range(52)]
    analog_labels = [f'A{i}' for i in range(16)]

    for label, value in zip(digital_labels, digital_data):
        digital_labels_values[label].config(text=f'{label}: {value}')

    for label, value in zip(analog_labels, analog_data):
        analog_labels_values[label].config(text=f'{label}: {value}')

# Serial connection settings
ser = serial.Serial('COM4', 9600)  # Replace 'COMx' with your Arduino's port

# GUI setup
root = tk.Tk()
root.title("Arduino Data Display")

# Digital Labels
digital_labels_values = {}
for i in range(52):
    label = tk.Label(root, text=f'D{i+2}:')
    label.grid(row=i, column=0, padx=5, pady=2, sticky=tk.E)
    value_label = tk.Label(root, text='--')
    value_label.grid(row=i, column=1, padx=5, pady=2, sticky=tk.W)
    digital_labels_values[f'D{i+2}'] = value_label

# Analog Labels
analog_labels_values = {}
for i in range(16):
    label = tk.Label(root, text=f'A{i}:')
    label.grid(row=i, column=2, padx=5, pady=2, sticky=tk.E)
    value_label = tk.Label(root, text='--')
    value_label.grid(row=i, column=3, padx=5, pady=2, sticky=tk.W)
    analog_labels_values[f'A{i}'] = value_label

# Start a separate thread to read serial data
thread = Thread(target=read_serial_data, daemon=True)
thread.start()

root.mainloop()
