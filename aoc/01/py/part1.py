import pandas as pd

depths = pd.read_csv("../input.txt", header=None).iloc[:, 0]
print(f"Number of measurements: {len(depths)}")

diffs = depths.diff().dropna()
increases = (diffs > 0).sum()

print(f"Number of increases: {increases}")

# ======== Part Two ========

window = 3
rolling_depths = depths.rolling(window).sum().dropna()

rolling_depths_diff = rolling_depths.diff().dropna()

rolling_increases = (rolling_depths_diff > 0).sum()

print(f"Number of rolling increases {rolling_increases}")
