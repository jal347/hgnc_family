import csv
from biothings_client import get_client
from collections import defaultdict

GENE_CLIENT = get_client('gene')

def query_hgnc(hgnc_ids: list):
    """Use biothings_client.py to query hgnc ids and get back '_id' in mygene.info

    :param: hgnc_ids: list of HGNC ids
    """
    res = GENE_CLIENT.querymany(hgnc_ids, scopes='HGNC', fields='_id', returnall=True)
    new_res = defaultdict(list)
    for item in res['out']:
        if not "notfound" in item:
            new_res[item['query']].append(item['_id'])
    return [new_res, res['missing']]


# dictionary to used to make gene_id with family_id
# key family_id
family = {}
# contains the json object
# key hgnc_id
hgnc = {}

# populates the family dictionary
with open('family.csv', encoding='utf-8') as hgnc_family:
    family_reader = csv.DictReader(hgnc_family, delimiter=",")
    for row in family_reader:
        # replace null values
        row = {k: ('' if v == 'NULL' else v) for k, v in row.items()}
        family[row['id']] = {
            "id": row['id'],
            "abbr": row['abbreviation'],
            "name": row['name'],
            "comments": row['external_note'],
            "pubmed": list(map(int, row['pubmed_ids'].split(","))) if row['pubmed_ids'] else [],
            "typical_gene": row['typical_gene']
        }



with open('gene_has_family.csv', encoding='utf-8') as hgnc_id:
    hgnc_reader = csv.DictReader(hgnc_id, delimiter=",")
    for row in hgnc_reader:
        gene_id = row['hgnc_id']
        family_id = row['family_id']
        # if id exists then add another entry into hgnc_genegroup else make a new json rec
        if gene_id in hgnc.keys():
            hgnc[gene_id]["hgnc_genegroup"].append(family[family_id])
        else:
            hgnc[gene_id] = {
                "_id": gene_id,
                "hgnc_genegroup": [family[family_id]]
            }


query = query_hgnc(hgnc.keys())
for key in query[1]:
    hgnc.pop(key, None)
for key, value in query[0].items():
    hgnc[key]["_id"] = value[0]

print(len(hgnc.keys()))
print(query[1])


