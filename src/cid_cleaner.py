import pandas as pd

cid = pd.read_csv('./src/data/parameters/csv/CID-10-SUBCATEGORIAS.csv')

print(cid.columns)

cid = cid.drop(columns=['CLASSIF', 'RESTRSEXO', 'CAUSAOBITO', 'DESCRABREV', 'REFER', 'EXCLUIDOS', 'Unnamed: 8', 'Unnamed: 9'])

print(cid.columns)

cid.to_csv('./src/data/parameters/csv/CID10-TABLE.csv', index=False)