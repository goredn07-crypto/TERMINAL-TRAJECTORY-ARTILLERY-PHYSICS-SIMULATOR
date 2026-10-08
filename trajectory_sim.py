import math

# --- 1. CONSTANTS ---
GRAVITY = 9.81  # Acceleration due to gravity in m/s^2
GRID_WIDTH = 60  # Number of columns in terminal plot
GRID_HEIGHT = 15  # Number of rows in terminal plot

# --- 2. USER INPUTS ---
print("=" * 60)
print("     TERMINAL TRAJECTORY & ARTILLERY PHYSICS SIMULATOR")
print("=" * 60)

velocity = float(input("Enter launch velocity (m/s) [e.g., 25-60]: "))
angle_deg = float(input("Enter launch angle (degrees) [e.g., 15-80]: "))
target_distance = float(input("Enter target distance (meters) [e.g., 50-250]: "))
target_tolerance = 3.0  # Hit window: +/- 3 meters

# --- 3. MATHEMATICAL CALCULATIONS ---
# Convert angle to radians for Python's math library
angle_rad = math.radians(angle_deg)

# Split velocity into horizontal and vertical components
vx = velocity * math.cos(angle_rad)
vy = velocity * math.sin(angle_rad)

# Total flight time: t = (2 * vy) / g
total_time = (2.0 * vy) / GRAVITY

# Maximum height: H = (vy^2) / (2 * g)
max_height = (vy**2) / (2.0 * GRAVITY)

# Total horizontal range: R = vx * total_time
total_range = vx * total_time

# Print calculated analytical metrics
print("\n" + "-" * 40)
print("FLIGHT METRICS")
print("-" * 40)
print(f"Horizontal Velocity (Vx) : {vx:.2f} m/s")
print(f"Vertical Velocity (Vy)   : {vy:.2f} m/s")
print(f"Total Flight Time        : {total_time:.2f} seconds")
print(f"Maximum Altitude         : {max_height:.2f} meters")
print(f"Total Range Covered      : {total_range:.2f} meters")

# --- 4. HIT / MISS DECISION LOGIC ---
distance_error = total_range - target_distance

print("\n" + "-" * 40)
print("TARGET ENGAGEMENT RESULT")
print("-" * 40)

if abs(distance_error) <= target_tolerance:
    print(
        f"🎯 DIRECT HIT! The projectile landed within {abs(distance_error):.2f}m of the target."
    )
elif distance_error < 0:
    print(
        f"❌ UNDER-SHOT! Fell short by {abs(distance_error):.2f}m. Increase velocity or optimize angle."
    )
else:
    print(
        f"❌ OVER-SHOT! Overflew by {distance_error:.2f}m. Decrease velocity or adjust angle."
    )

# --- 5. TERMINAL ASCII TRAJECTORY PLOTTER ---
print("\n" + "=" * 60)
print("TRAJECTORY VISUALIZATION (Altitude vs. Distance)")
print("=" * 60)

# Determine coordinate scale factors
max_x = max(total_range, target_distance) * 1.05
max_y = max_height * 1.15

# Loop row-by-row from top of the grid to bottom
y_idx = GRID_HEIGHT
while y_idx >= 0:
    current_y = (y_idx / GRID_HEIGHT) * max_y
    line = ""

    x_idx = 0
    while x_idx <= GRID_WIDTH:
        current_x = (x_idx / GRID_WIDTH) * max_x

        # Calculate theoretical height at this specific distance x:
        # y(x) = x * tan(theta) - (g * x^2) / (2 * vx^2)
        if current_x <= total_range and vx > 0:
            calc_y = (current_x * math.tan(angle_rad)) - (
                (GRAVITY * (current_x**2)) / (2.0 * (vx**2))
            )
        else:
            calc_y = -1.0

        # Vertical tolerance band for plotting characters
        y_band = max_y / (GRID_HEIGHT * 1.2)

        # Draw target marker on ground
        if (
            y_idx == 0
            and abs(current_x - target_distance) <= (max_x / GRID_WIDTH) / 2
        ):
            line += "T"
        # Draw projectile trajectory curve
        elif abs(calc_y - current_y) <= y_band and current_x <= total_range:
            line += "*"
        # Draw axes
        elif x_idx == 0:
            line += "|"
        elif y_idx == 0:
            line += "_"
        else:
            line += " "

        x_idx += 1

    # Print current row with an altitude label on every 3rd line
    if y_idx % 3 == 0:
        print(f"{current_y:6.1f}m {line}")
    else:
        print(f"       {line}")

    y_idx -= 1

# Bottom scale label
print(f"       0m" + " " * (GRID_WIDTH - 10) + f"{max_x:.1f}m (Distance)")
print("Legend: [*] Trajectory Arc   [T] Target Location   [|/_] Axes\n")