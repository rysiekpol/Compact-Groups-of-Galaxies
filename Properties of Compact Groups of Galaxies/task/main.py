import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("groups.tsv", delimiter="\t")

df.dropna(inplace=True)

mean_ISL = df.groupby("features").agg("mean")['mean_mu']

print(mean_ISL[1], mean_ISL[0])
