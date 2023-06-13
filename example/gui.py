import tkinter as tk
import threading
import time
import gpu_control

# Function to update the temperature and fan speed labels
def update_labels(root):
    while True:
        temperature = gpu_control.get_temperature()
        fan_speed = gpu_control.get_fan_speed()
        temperature_label.config(text="Temperature: {} °C".format(temperature))
        fan_speed_label.config(text="Fan Speed: {}%".format(fan_speed))

        # If fan speed override is off, adjust the fan speed according to the temperature
        if fan_speed_override_var.get() == 0:
            # Ensure optimal_temperature and max_temperature entries are valid before adjusting fan speed
            if optimal_temperature_entry.get().isdigit() and max_temperature_entry.get().isdigit():
                optimal_temperature = int(optimal_temperature_entry.get())
                max_temperature = int(max_temperature_entry.get())

                # Calculate the new fan speed
                if temperature > optimal_temperature and temperature < max_temperature and fan_speed < 90:
                    new_fan_speed = fan_speed + 10  # increase by 10%
                elif temperature >= max_temperature:
                    new_fan_speed = 100
                elif temperature < optimal_temperature and fan_speed > 10:
                    new_fan_speed = fan_speed - 10  # decrease by 10%
                else:
                    new_fan_speed = fan_speed  # keep the fan speed unchanged
                
                # Apply the new fan speed
                gpu_control.set_fan_speed(new_fan_speed)
        
        time.sleep(1)  # Wait for 1 second


# Function to set the fan speed based on user input and temperature values
def set_fan_speed():
    if fan_speed_override_var.get() == 1:
        fan_speed = fan_speed_entry.get()
        if fan_speed.isdigit():
            fan_speed = int(fan_speed)
            if 0 <= fan_speed <= 100:
                gpu_control.set_fan_speed(fan_speed)
                error_label.config(text="")  # Clear any previous error message
            else:
                # Invalid fan speed value, display an error message
                error_label.config(text="Invalid fan speed value. Enter a value between 0 and 100.")
        else:
            # Invalid input, display an error message
            error_label.config(text="Invalid fan speed input. Enter a numeric value.")
    else:
        # Fan control set to automatic, calculate and set fan speed
        temperature = gpu_control.get_temperature()
        optimal_temperature = int(optimal_temperature_entry.get())
        max_temperature = int(max_temperature_entry.get())
        if optimal_temperature <= temperature <= max_temperature:
            fan_speed = int((temperature - optimal_temperature) * 100 / (max_temperature - optimal_temperature))
        elif temperature < optimal_temperature:
            fan_speed = 0
        else:
            fan_speed = 100
        gpu_control.set_fan_speed(fan_speed)
        error_label.config(text="")  # Clear any previous error message

# Create the main window
root = tk.Tk()
root.title("GPU Control")
root.geometry("400x450")

# Create labels for temperature and fan speed
temperature_label = tk.Label(root, text="Temperature: -", font=("Arial", 16))
temperature_label.pack(pady=10)
fan_speed_label = tk.Label(root, text="Fan Speed: -", font=("Arial", 16))
fan_speed_label.pack(pady=10)

# Create checkbox for fan speed override
fan_speed_override_var = tk.IntVar()
fan_speed_override_checkbox = tk.Checkbutton(root, text="Override Fan Speed", variable=fan_speed_override_var)
fan_speed_override_checkbox.pack()

# Create entry field for fan speed override
fan_speed_entry_label = tk.Label(root, text="Fan Speed:")
fan_speed_entry_label.pack()
fan_speed_entry = tk.Entry(root, state=tk.DISABLED)
fan_speed_entry.pack()

# Create button to set the fan speed
set_fan_speed_button = tk.Button(root, text="Set Fan Speed", command=set_fan_speed)
set_fan_speed_button.pack(pady=10)

# Create label for error messages
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

# Update the state of the fan speed entry based on the checkbox state
def checkbox_state_changed():
    if fan_speed_override_var.get() == 1:
        fan_speed_entry.config(state=tk.NORMAL)
        set_fan_speed_button.config(state=tk.NORMAL)
    else:
        fan_speed_entry.config(state=tk.DISABLED)
        set_fan_speed_button.config(state=tk.DISABLED)

fan_speed_override_var.trace("w", lambda *args: checkbox_state_changed())  # Call checkbox_state_changed() when checkbox state changes

# Create labels and entries for optimal and max temperature
optimal_temperature_label = tk.Label(root, text="Optimal Temperature:")
optimal_temperature_label.pack()
optimal_temperature_entry = tk.Entry(root)
optimal_temperature_entry.pack()
max_temperature_label = tk.Label(root, text="Max Temperature:")
max_temperature_label.pack()
max_temperature_entry = tk.Entry(root)
max_temperature_entry.pack()

# Function to apply the optimal and max temperature values
def apply_temperature_values():
    optimal_temperature = optimal_temperature_entry.get()
    max_temperature = max_temperature_entry.get()
    if optimal_temperature.isdigit() and max_temperature.isdigit():
        optimal_temperature = int(optimal_temperature)
        max_temperature = int(max_temperature)
        # Apply the temperature values here as needed
    else:
        # Invalid input, display an error message
        error_label.config(text="Invalid temperature input. Enter numeric values.")

# Create apply button for temperature values
apply_button = tk.Button(root, text="Apply", command=apply_temperature_values)
apply_button.pack(pady=10)

# Start the thread to update labels
update_thread = threading.Thread(target=update_labels, args=(root,))
update_thread.start()

# Start the GUI main loop
root.mainloop()
