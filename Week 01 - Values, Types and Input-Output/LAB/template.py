# RECORD CHECK  -  IT System Infrastructure Monitor
# Name  : Klein Warren Giovani MOUBEYI
# Lane  : IT
# Date  : 2026-10-02

# ==================================================================== INPUT
# 1. Ask the user for three values (System name, processed units, target units).

system_label = input("Enter system name: ")
units_processed = float(input("Enter processed units count: "))
target_units = float(input("Enter target units count: "))


# ================================================================== PROCESS
# 2. Perform automated calculations for infrastructure metrics.

difference = target_units - units_processed
percent = (units_processed / target_units) * 100

# Extra calculated metric for Excellent tier:
# Calculates the missing unit percentage to evaluate overall system gap.
missing_ratio = (difference / target_units) * 100


# =================================================================== OUTPUT
# 3. Print formatted validation report.

print()
print("=" * 38)
print(f"  SYSTEM CHECK   -  {system_label}")
print("=" * 38)

print(f"Processed Units : {units_processed:>12.2f}")
print(f"Target Units    : {target_units:>12.2f}")
print(f"Gap to Target   : {difference:>+12.2f}")
print(f"Completion Rate : {percent:>12.2f} %")
print(f"System Loss     : {missing_ratio:>12.2f} %")

print("=" * 38)