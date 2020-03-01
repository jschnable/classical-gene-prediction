import matplotlib.pyplot as plt
import pandas as pd
import seaborn

fh = open("PAVScores/pav_scores_independent.csv")
fh.readline()
list_of_genes = set([])
for x in fh:
    y = x.strip().split(',')
    list_of_genes.add(y[0])

#print(list_of_genes)
#1/0
classical_genes = set([])
fh = open("MaizeGeneSets/phenotype_103_genes.csv")
#fh = open("MaizeGeneSets/GWAS_819_genes.csv")
#fh = open("MaizeGeneSets/GPWAS_1718_genes.csv")
for x in fh:
    if x.strip() in list_of_genes:
        classical_genes.add(x.strip())

fh = open("MaizeGeneSets/GWAS_819_genes.csv")
farm_genes = set([])
for x in fh:
    if x.strip() in list_of_genes:
        farm_genes.add(x.strip())

fh = open("MaizeGeneSets/GPWAS_1718_genes.csv")
gpwas_genes = set([])
for x in fh:
    if x.strip() in list_of_genes:
        gpwas_genes.add(x.strip())

all_pheno_genes = classical_genes.union(farm_genes.union(gpwas_genes))
no_pheno_genes = list_of_genes.difference(all_pheno_genes)

df = pd.read_csv("PAVScores/pav_scores_independent.csv",index_col=0)

farm_df = df.loc[farm_genes]
classical_df = df.loc[classical_genes]
gpwas_df = df.loc[gpwas_genes]
nopheno_df = df.loc[no_pheno_genes]

df_dict = {
"FarmCPU":farm_df,
"LoF Mutant":classical_df,
"GPWAS":gpwas_df,
"All Others":nopheno_df
}

plot_order = ["All Others","FarmCPU","GPWAS","LoF Mutant"]

d2p = {}
for x in ["PAVMax","PAVMean","PAVMin","PAVFreq"]:
    d2p[x] = []
    for y in plot_order:
        d2p[x].append(list(df_dict[y][x]))

fig = plt.figure()
ax1 = fig.add_subplot('221')
ax2 = fig.add_subplot('222')
ax3 = fig.add_subplot('223')
ax4 = fig.add_subplot('224')

for ax,datatype in zip([ax1,ax2,ax3,ax4],["PAVMax","PAVMean","PAVMin","PAVFreq"]):
    ax.violinplot(d2p[datatype], [1,2,3,4], points=100, widths=0.9, showmeans=True,inner=None,
                      bw_method='silverman')
    ax.set_xticks([1,2,3,4])
    ax.set_xticklabels(plot_order)
    ax.set_title(datatype)
plt.show()
