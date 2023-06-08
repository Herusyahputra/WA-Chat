import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path


def clean_data(data_source_html):
    # Open the HTML file and read its contents
    with open(data_source_html) as f:
        contents = f.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(contents, 'html.parser')

    # Find the table element(s) in the HTML content
    tables = soup.find_all('table')

    # Convert the table(s) into a DataFrame
    dfs = []
    for table in tables:
        df = pd.read_html(str(table))[0]
        dfs.append(df)

    result_data_clean = pd.concat(dfs)
    result_data_clean = result_data_clean[result_data_clean["Pantarlih"] == "Belum Diverifikasi"]
    result_data_clean = result_data_clean[result_data_clean["No Telp."] != "(tolong di update)"]

    for col in result_data_clean["No Telp."]:
        result_data_clean["No Telp."] = result_data_clean["No Telp."].apply(lambda x: x[1:] if x.startswith("0") else x)

    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("1")]
    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("2")]
    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("3")]
    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("4")]
    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("5")]
    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("6")]
    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("7")]
    result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("8")]

    result_data_clean["No Telp."] = result_data_clean["No Telp."].str.replace('-', '')
    result_data_clean["No Telp."] = result_data_clean["No Telp."].str.replace(' ', '')

    result_data_clean = result_data_clean[result_data_clean.iloc[:, 4].str.len() == 8]
    result_data_clean = result_data_clean[~result_data_clean['No Telp.'].str.startswith('2')]
    result_data_clean.columns.str.match("Unnamed")
    result_data_clean = result_data_clean.loc[:, ~result_data_clean.columns.str.match("Unnamed")]

    return result_data_clean


data_source = "zhongzheng.html"
data_clean = clean_data(data_source)
extensions = "".join(Path(data_source).suffixes)
new_ext = ".xlsx"
new_filename = str(Path(data_source)).replace(extensions, new_ext)

# save into exel
data_clean.to_excel(new_filename)
