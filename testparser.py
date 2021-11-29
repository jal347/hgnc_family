import pandas as pd
import csv
# read both data files
data1 = pd.read_csv('family.csv')
data2 = pd.read_csv('gene_has_family.csv')



# rename the column so we can do an inner join
data1.rename(
    columns=({'id':'family_id'}),
    inplace=True
)

# number of family ids
print(len(data1['family_id']))

# all the hgnc ids
print(len(data2["hgnc_id"]))

# all of the unique hgnc ids
print(len(data2["hgnc_id"].unique()))

# all of the 1-1 hgnc ids to family ids
print(len(data2[~data2.hgnc_id.duplicated(keep=False)]))

# all of the 1-n hgnc ids to family ids
dupes = data2[data2.hgnc_id.duplicated(keep=False)].sort_values("hgnc_id")
print(dupes)
print(len(dupes["hgnc_id"]))

# groups the duplicate 1-n hgnc ids to family ids
dupes = dupes.groupby(["hgnc_id"]).size().reset_index(name="mapping")
print(dupes)

# the max 1-n hgnc ids to family ids (7)
print(dupes["mapping"].max())
mapping = dupes.groupby(["mapping"]).size().reset_index(name="count")
print(mapping)
#pd.set_option('display.max_columns', None)
#print(data1.loc[data1["family_id"] == 1085])



# print the columns to make sure name matches
# print(data1.columns)
# print(data2.columns)

# inner join between the two files
# data = pd.merge(data1, data2, on='family_id', how='inner')
# print(data.columns)
#
# print("print shapes:")
# print(data.shape)
# print(data1.shape)
# print(data2.shape)
#
# print(data.head)

#data.to_csv("merge.csv", index=False)

test = ''

int_list = list(map(int, test.split(","))) if test else []
print(int_list)
