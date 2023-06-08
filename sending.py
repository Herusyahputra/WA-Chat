import pandas as pd
import phonenumbers
import pywhatkit

from pynput.keyboard import Controller, Key

keyboard = Controller()


def is_valid_whatsapp_number(phone_number, text_message):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            return False
        if not phonenumbers.is_possible_number(parsed_number):
            return False
        return pywhatkit.sendwhatmsg_instantly(phone_number, text_message, tab_close=True) is None
        # return pywhatkit.sendwhats_image(phone_number, img_path='D:/doc/Whatsapp_bot/test.png', caption="Bukti pendaftaran pemilu 2024") is None

    except:
        return False


# input data here
result_data_clean = pd.read_excel('24032023/data_send_new_taipei_all_2.xlsx', sheet_name='Sheet1')
result_data_clean.columns.str.match("Unnamed")
result_data_clean = result_data_clean.loc[:, ~result_data_clean.columns.str.match("Unnamed")]

database_already_send = pd.read_excel('database_already_send.xlsx', sheet_name='Sheet1')
database_already_send.columns.str.match("Unnamed")
database_already_send = database_already_send.loc[:, ~database_already_send.columns.str.match("Unnamed")]

# database_not_valid_number = pd.read_excel('database_not_valid_number.xlsx', sheet_name='Sheet1')
# database_not_valid_number.columns.str.match("Unnamed")
# database_not_valid_number = database_not_valid_number.loc[:, ~database_not_valid_number.columns.str.match("Unnamed")]

print(result_data_clean.equals(database_already_send))

for index, row in result_data_clean.iterrows():
    if row['No Telp.'] not in database_already_send.values:
            # and \
            # row['Nomor Paspor'] not in database_already_send.values:
        print(type(row['No Telp.']))
        # print(row["Nama Lengkap"])
        data = pd.DataFrame(row).transpose()
        message = f'Salam! Semoga Anda selalu dalam keadaan sehat dan bahagia. \n' \
                  f'Kami dari Petugas pemutakhiran data pemilih Luar Negeri (PANTARLIH-LN) bersama KDEI Taiwan dalam ' \
                  f'rangka Pemilihan umum (PEMILU) Presiden Indonesia 2024 sedang melakukan pencocokan ' \
                  f'data untuk memastikan anda terdaftar sebagai pemilih tetap (DPT), ' \
                  f'apakah benar anda ber: \n\n' \
                  f'Nama Lengkap: {row["Nama Lengkap"]}\n' \
                  f'No Passport: {row["Nomor Paspor"]}\n' \
                  f'Tempat/tanggal lahir: {row["Tempat & Tanggal Lahir"]}\n' \
                  f'Alamat di Taiwan: {row["Alamat"]}\n\n' \
                  f'Jika informasi sudah benar, mohon dipilih metode pencoblosan apakah anda berkenan *mendatangi ' \
                  f'Tempat Pemungutan Suara (TPS)* atau surat suara akan dikirim ke alamat tersebut melalui *POS*. ' \
                  f'Karena informasi ini penting untuk menyukseskan pemilu, harap untuk segera mengkonfirmasi ' \
                  f'kesesuaian data tersebut. Terima kasih. \n\n' \
                  f'PANTARLIH-LN Taiwan\n(Informasi detail dapat anda lihat di Bio profile akun ini)'

        number = f'+886{row["No Telp."]}'
        print(number)
        # print(message)
        # pywhatkit.sendwhats_image(number, img_path=r'D:/doc/Whatsapp_bot/form_ln.jpg',
        #                           caption="Bukti pendaftaran pemilu 2024", tab_close=True, wait_time=30)

        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)

        valid = is_valid_whatsapp_number(number, message)
        print(valid)

        if valid:
            database_already_send = pd.concat([database_already_send, data])
            database_already_send.to_excel("database_already_send.xlsx")


        # else:
        #     database_not_valid_number = pd.concat([database_not_valid_number, data])
        #     database_not_valid_number.to_excel("database_not_valid_number.xlsx")

    else:
        print(row['No Telp.'])
        print(row["Nama Lengkap"])
        print("already ever send")

