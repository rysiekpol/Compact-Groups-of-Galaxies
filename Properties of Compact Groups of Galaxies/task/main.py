import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("groups.tsv", delimiter="\t")

df.dropna(inplace=True)

mean_ISL = df.groupby("features").agg("mean", numeric_only=True)['mean_mu']

#Analysis of variance
sample_0 = df[df.features == 0]["mean_mu"]
sample_1 = df[df.features == 1]["mean_mu"]
shapiro_test0 = stats.shapiro(sample_0).pvalue
shapiro_test1 = stats.shapiro(sample_1).pvalue
fligner_test = stats.fligner(sample_0, sample_1).pvalue
ANOVA_test = stats.f_oneway(sample_0, sample_1).pvalue

print(shapiro_test1, shapiro_test0, fligner_test, ANOVA_test)

#print(mean_ISL[1], mean_ISL[0])
