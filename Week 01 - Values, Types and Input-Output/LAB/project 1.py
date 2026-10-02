# ====================================================================
# RECORD CHECK - my version
# ====================================================================

# Name : Klein Warren Giovani MOUBEYI
# Lane : IT
# Date : 02/10/2026


# ==================================================================== INPUT
# 1. Ask the user for your three values.

# getting inputs for IT lane
hostname = input("Enter hostname: ")
gb_used = float(input("Enter GB used: "))
gb_total = float(input("Enter GB total: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.

# calculate free space and usage percentage
difference = gb_total - gb_used
percent = (gb_used / gb_total) * 100

# my extra line for excellent grade (free space percentage)
free_percent = (difference / gb_total) * 100


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("-" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("-" * 34)

# formatted values with right alignment and 2 decimal places
print(f"GB Used     : {gb_used:>10.2f}")
print(f"GB Total    : {gb_total:>10.2f}")
print(f"GB Free     : {difference:>+10.2f}")
print(f"Usage Rate  : {percent:>10.2f}%")
print(f"Free Rate   : {free_percent:>10.2f}%")

print("-" * 34)