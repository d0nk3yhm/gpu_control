import gpu_control

print("# Fan speed:", gpu_control.get_fan_speed())
print("# Temperature:", gpu_control.get_temperature())
result = gpu_control.set_fan_speed(90)
