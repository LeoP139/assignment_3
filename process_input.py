import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

output = []

output.append(f"x: {x}")
output.append(f"y: {y}")
output.append(f"z: {z}")

x += y
output.append(f"x += y: {x}")

x -= z
output.append(f"x -= z: {x}")

x *= y
output.append(f"x *= y: {x}")

if z != 0:
    x %= z
    output.append(f"x %= z: {x}")
    x /= z
    output.append(f"x /= z: {x}")
    final = x + y + z
    output.append(f"Final result (x + y + z): {final}")
else:
    output.append("Error: z = 0 (division/modulo not allowed)")

print("\n".join(output))
