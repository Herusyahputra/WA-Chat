import pandas as pd
from bs4 import BeautifulSoup
import pywhatkit
from pynput.keyboard import Controller, Key

keyboard = Controller()


def send_message(number, message):
    pywhatkit.sendwhatmsg_instantly(number, message, tab_close=True)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


# Open the HTML file and read its contents
with open('CHANGSHENG ST.html') as f:
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
# result_data_clean = pd.read_excel('zhongseng.xlsx', sheet_name='Sheet1')
result_data_clean = result_data_clean[result_data_clean["Pantarlih"] == "Belum Diverifikasi"]
result_data_clean = result_data_clean[result_data_clean["No Telp."] != "(tolong di update)"]

# for col in result_data_clean["No Telp."]:
#     result_data_clean["No Telp."] = result_data_clean["No Telp."].apply(lambda x: x[1:] if x.startswith("0") else x)
#
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("1")]
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("2")]
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("3")]
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("4")]
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("5")]
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("6")]
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("7")]
# result_data_clean = result_data_clean[~result_data_clean.iloc[:, 8].str.startswith("8")]
#
# result_data_clean["No Telp."] = result_data_clean["No Telp."].str.replace('-', '')
# result_data_clean["No Telp."] = result_data_clean["No Telp."].str.replace(' ', '')
#
# result_data_clean = result_data_clean[result_data_clean.iloc[:, 4].str.len() == 8]
# result_data_clean = result_data_clean[~result_data_clean['No Telp.'].str.startswith('2')]
# result_data_clean.columns.str.match("Unnamed")
# result_data_clean = result_data_clean.loc[:, ~result_data_clean.columns.str.match("Unnamed")]

database_already_send = pd.read_excel('database_already_send.xlsx', sheet_name='Sheet1')
database_already_send.columns.str.match("Unnamed")
database_already_send = database_already_send.loc[:, ~database_already_send.columns.str.match("Unnamed")]

for index, row in result_data_clean.iterrows():
    # if row['No Telp.'] not in database_already_send.values:
    data = pd.DataFrame(row).transpose()
    message = f'Salam! Semoga Anda selalu dalam keadaan sehat dan bahagia. \n' \
              f'Kami dari Petugas pemutakhiran data pemilih Luar Negeri (PANTARLIH-LN) ' \
              f'bersama KDEI Taiwan dalam rangka Pemilihan umum (PEMILU) Presiden Indonesia 2024 sedang melakukan pencocokan ' \
              f'data untuk memastikan anda terdaftar sebagai pemilih tetap (DPT), ' \
              f'apakah benar anda ber: \n\n' \
              f'Nama Lengkap: {row["Nama Lengkap"]}\n' \
              f'No Passport: {row["Nomor Paspor"]}\n' \
              f'Tempat/tanggal lahir: {row["Tempat & Tanggal Lahir"]}\n' \
              f'Alamat di Taiwan: {row["Alamat"]}\n\n' \
              f'Jika informasi sudah benar, mohon dipilih metode pencoblosan apakah anda berkenan *mendatangi Tempat Pemungutan Suara (TPS)* ' \
              f'atau surat suara akan dikirim ke alamat tersebut melalui *POS*. Karena informasi ini penting untuk' \
              f' menyukseskan pemilu, harap segera konfirmasi dengan membalas pesan ini. Terima kasih. \n\n' \
              f'PANTARLIH-LN Taiwan'\

              # \

              # f'Anda dapat membalas pesan ini dengan memilih metode pemilihan Datang ke Tempat Pemungutan suara atau Dikirim ke alamat melalui POS (Pilih salah 1), Beritahu kami jika terdapat kekeliruan atau ' \
              # f'perubahan data seperti alamat menyesuaikan tempat tinggal saat  ini. \n\n\n'

    # number = f'+886{row["No Telp."]}'
    # send_message(number, message)
    # print(number)
    # print(message)
        # database_already_send = pd.concat([database_already_send, data])

print(result_data_clean)
# print(database_already_send)
result_data_clean.to_excel("CHANGSHENG.xlsx")
