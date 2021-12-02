import pandas as pd

inst = pd.read_csv(
    "../input.txt", 
    names=["type","value"],
    header=None,
    delimiter=" ",
)

# ======== PART ONE ========
# Horizontal and vertical movements are independent

# -------- Horizontal --------
inst_h = inst.loc[inst.loc[:,"type"] == "forward"]
print(f"Forward instructions:\t{len(inst_h)}")

final_h = inst_h.loc[:,"value"].sum()
print(f"Final horizontal position:\t{final_h}")

# -------- Vertical --------

inst_v = inst.loc[inst.loc[:,"type"].isin(["up","down"])].copy()

print(f"Vertical instructions:\t{len(inst_h)}")

inst_v.loc[:,"sign"] = inst_v.loc[:,"type"].apply(
    lambda x: -1.0 if x == "up" else 1.0
)

inst_v.loc[:,"signed_value"] = inst_v.loc[:,"sign"] * inst_v.loc[:,"value"]

final_v = inst_v.loc[:,"signed_value"].sum()
print(f"Final vertical position / depth:\t{int(final_v)}")

print(f"Multiplied final depths and horizontal position:\t{int(final_v*final_h)}")#

# ======== PART TWO ========
print(f"======== Part Two starts ========")

depth = 0
pos = 0
aim = 0
for _, r in inst.iterrows():
    val = r.loc["value"]
    inst_type = r.loc["type"]

    if inst_type == "forward":
        depth += aim * val
        pos += val
    elif inst_type == "up":
        aim -= val
    elif inst_type == "down":
        aim += val
    else:
        raise ValueError(f"Instruction type {inst_type} not supported")

print(f"Final depth:\t:{depth}")
print(f"Final pos:\t:{pos}")
print(f"Final aim:\t:{aim}")
print(f"Multiplied final depths and horizontal position:\t{int(pos * depth)}")

