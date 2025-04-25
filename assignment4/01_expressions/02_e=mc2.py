# Speed of light in meters per second
C: int = 299792458  

# Get mass input from user in kilograms
mass_in_kg: float = float(input("Enter kilos of mass: "))

# Calculate energy using E = m * c^2
energy_in_joules: float = mass_in_kg * (C ** 2)

# Display the calculation details
print("\ne = m * c^2...")
print(f"m = {mass_in_kg} kg")
print(f"c = {C} m/s")
print(f"\n{energy_in_joules} joules of energy!")
