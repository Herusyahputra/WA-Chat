import cv2
from datetime import datetime

import pandas as pd


def read_image(image):
    return cv2.imread(image)


def write_tps_or_pos_text(image, passport):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (670, 865)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, passport, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_ppln_text(image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (670, 905)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, "Taipei", org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_perwakilan_ri_text(image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (670, 947)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, "KDEI Taiwan", org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_negara_text(image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (670, 985)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, "Taiwan", org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_date_address_text(image, address):
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2

    print(len(address))
    x = 33
    datas = [address[i: i + x] for i in range(0, len(address), x)]
    address = ""
    org = [670, 592]
    for data in datas:
        cv2.putText(image, data, tuple(org), font,
                    fontScale, color, thickness, cv2.LINE_AA)
        org[1] += 42

    return image


def write_date_pemutakhiran_text(image, date):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (240, 1145)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, date, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_nama_pemilih_text(image, passport):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (670, 552)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, passport, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_pantarlih_ttd_name_text(image, name):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (309, 1910)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, name, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_pasport_text(image, passport):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (670, 505)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, passport, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def write_pantarlih_name_text(image, name):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (930, 1910)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    return cv2.putText(image, name, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


source_file = pd.read_excel('/home/moil-dev002/Documents/Whatsapp/Pantarlih/Dataset.xlsx')
source_file.columns.str.match("Unnamed")
source_file = source_file.loc[:, ~source_file.columns.str.match("Unnamed")]
print(source_file)

image = read_image("formulir-ttd.png")
print("test")
for index, sources in enumerate(source_file["Pantarlih"]):
    print(sources)
    if sources == "HERU SYAH PUTRA":
        image = read_image("formulir-ttd.png")
        # ttd = read_image("scan.png")
        image = write_tps_or_pos_text(image, str(source_file["Cara Pilih"][index]))
        image = write_nama_pemilih_text(image, str(source_file["Nama Lengkap"][index]))
        image = write_pasport_text(image, str(source_file["Nomor Paspor"][index]))
        image = write_ppln_text(image)
        image = write_perwakilan_ri_text(image)
        image = write_negara_text(image)
        image = write_negara_text(image)

        image = write_date_address_text(image, str(source_file["Alamat"][index]))
        image = write_date_pemutakhiran_text(image, str(datetime.now().date()))

        # image[0:0 + 0, 0:0 + 0] = ttd

        image = write_pantarlih_ttd_name_text(image, str(source_file["Nama Lengkap"][index]))
        image = write_pantarlih_name_text(image, "Heru Syah Putra")
        image = cv2.resize(image, (int(image.shape[1] / 3), int(image.shape[0] / 3)),
                           interpolation=cv2.INTER_LINEAR)

        cv2.imwrite(f'{str(source_file["Nama Lengkap"][index])}.png', image)
        cv2.imshow("form", image)
        cv2.waitKey(0)
