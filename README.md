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

This code, besides the code open sourced by NVIDIA is provided under the [MIT License](https://opensource.org/licenses/MIT).

## NVIDIA (files) License
- nvml.dll
- nvml.lib

 * Copyright 1993-2020 NVIDIA Corporation.  All rights reserved.
 *
 * NOTICE TO USER:
 *
 * This source code is subject to NVIDIA ownership rights under U.S. and
 * international Copyright laws.  Users and possessors of this source code
 * are hereby granted a nonexclusive, royalty-free license to use this code
 * in individual and commercial software.
 *
 * NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOURCE
 * CODE FOR ANY PURPOSE.  IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR
 * IMPLIED WARRANTY OF ANY KIND.  NVIDIA DISCLAIMS ALL WARRANTIES WITH
 * REGARD TO THIS SOURCE CODE, INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
 * IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL,
 * OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
 * OF USE, DATA OR PROFITS,  WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
 * OR OTHER TORTIOUS ACTION,  ARISING OUT OF OR IN CONNECTION WITH THE USE
 * OR PERFORMANCE OF THIS SOURCE CODE.
 *
 * U.S. Government End Users.   This source code is a "commercial item" as
 * that term is defined at  48 C.F.R. 2.101 (OCT 1995), consisting  of
 * "commercial computer  software"  and "commercial computer software
 * documentation" as such terms are  used in 48 C.F.R. 12.212 (SEPT 1995)
 * and is provided to the U.S. Government only as a commercial end item.
 * Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through
 * 227.7202-4 (JUNE 1995), all U.S. Government End Users acquire the
 * source code with only those rights set forth herein.
 *
 * Any use of this source code in individual and commercial software must
 * include, in the user documentation and internal comments to the code,
 * the above Disclaimer and U.S. Government End Users Notice.
 */

/*
NVML API Reference

The NVIDIA Management Library (NVML) is a C-based programmatic interface for monitoring and
managing various states within NVIDIA Tesla &tm; GPUs. It is intended to be a platform for building
3rd party applications, and is also the underlying library for the NVIDIA-supported nvidia-smi
tool. NVML is thread-safe so it is safe to make simultaneous NVML calls from multiple threads.

API Documentation

Supported platforms:
- Windows:     Windows Server 2008 R2 64bit, Windows Server 2012 R2 64bit, Windows 7 64bit, Windows 8 64bit, Windows 10 64bit
- Linux:       32-bit and 64-bit
- Hypervisors: Windows Server 2008R2/2012 Hyper-V 64bit, Citrix XenServer 6.2 SP1+, VMware ESX 5.1/5.5

Supported products:
- Full Support
    - All Tesla products, starting with the Fermi architecture
    - All Quadro products, starting with the Fermi architecture
    - All GRID products, starting with the Kepler architecture
    - Selected GeForce Titan products
- Limited Support
    - All Geforce products, starting with the Fermi architecture

The NVML library can be found at \%ProgramW6432\%\\"NVIDIA Corporation"\\NVSMI\\ on Windows. It is
not be added to the system path by default. To dynamically link to NVML, add this path to the PATH
environmental variable. To dynamically load NVML, call LoadLibrary with this path.

On Linux the NVML library will be found on the standard library path. For 64 bit Linux, both the 32 bit
and 64 bit NVML libraries will be installed.

Online documentation for this library is available at http://docs.nvidia.com/deploy/nvml-api/index.html

