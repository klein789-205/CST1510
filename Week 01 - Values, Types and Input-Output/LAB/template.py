# RECORD CHECK  -  AI Data Pipeline Monitor
# Name  : Klein Warren Giovani MOUBEYI
# Lane  : AI / Data Science
# Date  : 2026-10-02

# ==================================================================== INPUT
# 1. Ask the user for three values (Dataset name, processed rows, target rows).

dataset_label = input("Enter dataset name: ")
rows_processed = float(input("Enter processed rows count: "))
target_rows = float(input("Enter target rows count: "))


# ================================================================== PROCESS
# 2. Perform automated calculations for pipeline health metrics.

difference = target_rows - rows_processed
percent = (rows_processed / target_rows) * 100

# Extra calculated metric for Excellent tier:
# Calculates the missing data percentage to evaluate overall pipeline loss.
missing_ratio = (difference / target_rows) * 100


# =================================================================== OUTPUT
# 3. Print formatted validation report.

print()
print("=" * 38)
print(f"  DATASET CHECK  -  {dataset_label}")
print("=" * 38)

print(f"Processed Rows  : {rows_processed:>12.2f}")
print(f"Target Rows     : {target_rows:>12.2f}")
print(f"Gap to Target   : {difference:>+12.2f}")
print(f"Completion Rate : {percent:>12.2f} %")
print(f"Data Loss Ratio : {missing_ratio:>12.2f} %")

print("=" * 38)