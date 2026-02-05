# %%
import glob
import os
import pandas as pd

path = r"prac1\p1\*.txt"

for fname in sorted(glob.glob(path)):
    df = pd.read_csv(
        fname,
        usecols=[0, 1],
        sep=r"\s+",
        skiprows=4,
        header=None,
        names=["l", "V"],
    )

    meanV = df["V"].mean()

    # filename like: 0p05.txt  ->  R = 0.05
    base = os.path.basename(fname)
    R = base.replace(".txt", "").replace("p", ".")

    print(f"R = {R}  ->  Average voltage = {meanV:.6f} V")
