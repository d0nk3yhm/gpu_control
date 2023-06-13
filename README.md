# NVIDIA GPU Controller - (Python Wrapper)

This is a Python wrapper for controlling GPU temperature and fan speed. It provides convenient access to the following functions:

- `get_temperature()`: Retrieves the current GPU temperature.
- `set_fan_speed(speed)`: Sets the GPU fan speed to the specified value.
- `get_fan_speed()`: Retrieves the current GPU fan speed.

## Prerequisites

- Python: Make sure you have Python installed on your system. ( build with python 3.10 win_amd64)
- GPU Control Library: Ensure that the underlying GPU control library is correctly installed and accessible.
    - nvml from NVIDIA is included in this package.


## Usage

Once the GPU Control Wrapper module is installed, you can use it in your Python code as follows:

```python
import gpu_control

# Get the GPU temperature
temperature = gpu_control.get_temperature()
print("GPU temperature:", temperature)

# Set the GPU fan speed
speed = 80  # Example value
result = gpu_control.set_fan_speed(speed)
if result == 0:
    print("Fan speed set successfully.")
else:
    print("Failed to set fan speed.")

# Get the GPU fan speed
fan_speed = gpu_control.get_fan_speed()
print("GPU fan speed:", fan_speed)
```

Ensure that the module is properly imported, and you can then call the provided functions to control your GPU temperature and fan speed.

## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT).
