import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from astropy.cosmology import FlatLambdaCDM
from astropy import units as u
from astropy.coordinates import SkyCoord
import itertools

galaxies = pd.read_csv("galaxies_morphology.tsv", sep="\t")
isolated = pd.read_csv("isolated_galaxies.tsv", sep="\t")
df = pd.read_csv("groups.tsv", sep="\t")
cords = pd.read_csv("galaxies_coordinates.tsv", sep="\t")

df.dropna(inplace=True)
df.set_index("Group", inplace=True)
cords.set_index("Group", inplace=True)

cosmo = FlatLambdaCDM(H0=67.74, Om0=0.3089)
df["da"] = [cosmo.angular_diameter_distance(x).to(u.kpc) for x in df["z"]]

list_of_medians = []
iterator_group = df.index.tolist()
for name in iterator_group:
    group = cords.loc[name]
    group.set_index("Name", inplace=True)
    tuple_of_group = [(group["RA"][x], group["DEC"][x]) for x in range(len(group))]
    list_of_separations = []
    for galaxy1, galaxy2 in itertools.combinations(tuple_of_group, 2):
        p1 = SkyCoord(ra=galaxy1[0] * u.degree, dec=galaxy1[1] * u.degree, frame="fk5")
        p2 = SkyCoord(ra=galaxy2[0] * u.degree, dec=galaxy2[1] * u.degree, frame="fk5")
        list_of_separations.append((p1.separation(p2).to(u.radian)*df.loc[name]["da"]).value)
    series_of_separation = pd.Series(list_of_separations)
    list_of_medians.append(series_of_separation.median())

df["median"] = list_of_medians

shapiro_test_median = stats.shapiro(df["median"]).pvalue
shapiro_test_mu = stats.shapiro(df.mean_mu).pvalue
pearson_test_median_mu = stats.pearsonr(df.mean_mu, df["median"]).pvalue
print(df.loc["HCG 2"]["median"], shapiro_test_median, shapiro_test_mu, pearson_test_median_mu)