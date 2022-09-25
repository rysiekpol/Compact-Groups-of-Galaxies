import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

galaxies = pd.read_csv("galaxies_morphology.tsv", sep="\t")
isolated = pd.read_csv("isolated_galaxies.tsv", sep="\t")
legend_names = ["isolated galaxies", "groups galaxies"]
#Analyzing data with histogram
plt.hist([isolated.squeeze(), galaxies["n"]], stacked=True, label=legend_names, edgecolor="black", bins=24, color = ['#ff7f7f', '#7f7fff'])
plt.ylabel("Count")
plt.xlabel("n")
plt.legend()
plt.show()
#Analazying dataset with kolmogorov-smirnov test
galaxies_fraction = galaxies[galaxies.n > 2]["n"].count()/galaxies["n"].count()
isolated_fraction = isolated[isolated.n > 2]["n"].count()/isolated["n"].count()
kolmogorov_test = stats.kstest(galaxies["n"], isolated.squeeze(), alternative="two-sided")
print(galaxies_fraction, isolated_fraction, kolmogorov_test.pvalue)
