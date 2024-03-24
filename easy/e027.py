import cmath
import re

# Read input
z = input()

# Find real and imaginary part of complex number
z_pattern = r"^([-+]?\d+)([-+]\d+)j$"

matches = re.match(z_pattern, z)

z_real = int(matches.group(1))
z_img = int(matches.group(2))

# Construct the complex numbers
complex_num = complex(z_real, z_img)

# Fetch modulus (r) and phase (phi) of complex numbers
r = abs(complex_num)
phi = cmath.phase(complex_num)

# Print r & phi values
print(r)
print(phi)
