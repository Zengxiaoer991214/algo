"""
@File    :   asset_no_update.py
@Time    :   2024/8/16 11:09
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
import os

import pandas as pd


def generate_update_sql(excel_file: str, meter_no_col: str, asset_no_col: str, output_sql_file: str):
    # 读取Excel文件
    df = pd.read_excel(excel_file)

    # 打开一个文件来写SQL语句
    with open(output_sql_file, 'w') as sql_file:
        for index, row in df.iterrows():
            meter_no = row[meter_no_col]
            asset_no = row[asset_no_col]

            # 生成SQL语句
            sql = f"UPDATE h_ar_meter SET asset_no = '{asset_no}' WHERE meter_no = '{meter_no}';\n" \
                  f"UPDATE h_ar_device SET asset_no = '{asset_no}' WHERE device_no = '{meter_no}';\n" \
                  f"UPDATE m_ar_device SET asset_no = '{asset_no}' WHERE device_no = '{meter_no}';\n"
            sql_file.write(sql)

    print(f"SQL update statements have been written to {output_sql_file}")


base_uri: str = r"E:\linli\algo\algo\awork"

generate_update_sql(
    excel_file="./file/MeterWithoutDiscoNo_20240815_0.2.xlsx",
    meter_no_col='meter_no',  # Excel中的表头名
    asset_no_col='asset_no',  # Excel中的表头名
    output_sql_file='./output/update_MeterWithoutDiscoNo_20240815_0.2.sql'
)

generate_update_sql(
    excel_file="./file/01_ShipmentFile_20240814_LG_E570_MEDC.xlsx",
    meter_no_col='Serial_number',  # Excel中的表头名
    asset_no_col='Asset_number',  # Excel中的表头名
    output_sql_file='./output/update_01_ShipmentFile_20240814_LG_E570_MEDC.sql'
)

generate_update_sql(
    excel_file="./file/02_ShipmentFile_20240815_LG_E570_MJEC.xlsx",
    meter_no_col='Serial_number',  # Excel中的表头名
    asset_no_col='Asset_number',  # Excel中的表头名
    output_sql_file='./output/update_02_ShipmentFile_20240815_LG_E570_MJEC.sql'
)

generate_update_sql(
    excel_file="./file/03_ShipmentFile_20240815_LG_E570_MZEC.xlsx",
    meter_no_col='Serial_number',  # Excel中的表头名
    asset_no_col='Asset_number',  # Excel中的表头名
    output_sql_file='./output/update_03_ShipmentFile_20240815_LG_E570_MZEC.sql'
)

generate_update_sql(
    excel_file="./file/04_ShipmentFile_20240815_LG_E570_TNWR.xlsx",
    meter_no_col='Serial_number',  # Excel中的表头名
    asset_no_col='Asset_number',  # Excel中的表头名
    output_sql_file='./output/update_04_ShipmentFile_20240815_LG_E570_TNWR.sql'
)

# if __name__ == '__main__':
#     folder_path = r'E:\linli\algo\algo\awork\file'
#     output_path = r'E:\linli\algo\algo\awork\output'
#
#     for root, dirs, files in os.walk(folder_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)
#             print(f"Found file: {file_path} start")
