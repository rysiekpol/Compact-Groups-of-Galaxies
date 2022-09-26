import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

galaxies = pd.read_csv("galaxies_morphology.tsv", sep="\t")
isolated = pd.read_csv("isolated_galaxies.tsv", sep="\t")
df = pd.read_csv("groups.tsv", sep="\t")

df.dropna(inplace=True)
df.set_index("Group", inplace=True)

mean_galaxies = galaxies.groupby("Group").agg(mean_n = ("n", "mean"), mean_T = ("T", "mean"))
merged_galaxies = mean_galaxies.merge(df, left_index=True, right_index=True)

shapiro_test_mu = stats.shapiro(merged_galaxies.mean_mu).pvalue
shapiro_test_n = stats.shapiro(merged_galaxies.mean_n).pvalue
shapiro_test_T = stats.shapiro(merged_galaxies.mean_T).pvalue
pearson_test_mu_n = stats.pearsonr(merged_galaxies.mean_mu, merged_galaxies.mean_n).pvalue
pearson_test_mu_T = stats.pearsonr(merged_galaxies.mean_mu, merged_galaxies.mean_T).pvalue

print(shapiro_test_mu, shapiro_test_n, shapiro_test_T, pearson_test_mu_n, pearson_test_mu_T)

fig, axes = plt.subplots(1, 2)
ax1, ax2 = axes
fig.tight_layout(pad=2)
ax1.scatter(merged_galaxies.mean_n, merged_galaxies.mean_mu)
ax2.scatter(merged_galaxies.mean_T, merged_galaxies.mean_mu)

plt.show()