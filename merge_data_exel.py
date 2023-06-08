import pandas as pd

source_file = pd.read_excel('source.xlsx', sheet_name='Sheet1')
source_file.columns.str.match("Unnamed")
source_file = source_file.loc[:, ~source_file.columns.str.match("Unnamed")]

dst_file = pd.read_excel('dst.xlsx', sheet_name='Sheet1')
dst_file.columns.str.match("Unnamed")
dst_file = dst_file.loc[:, ~dst_file.columns.str.match("Unnamed")]

for index, row in source_file.iterrows():
    if row['No Telp.'] not in dst_file.values:
        print("data is new")
        data = pd.DataFrame(row).transpose()
        dst_file = pd.concat([dst_file, data])

    else:
        print("already exist")

dst_file.to_excel("dst.xlsx")