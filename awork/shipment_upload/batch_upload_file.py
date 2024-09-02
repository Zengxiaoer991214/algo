import json
import os
import requests

from ..shipment_upload import ACCESS_TOKEN, BASE_URL

# 配置接口URL和Token

upload_url = BASE_URL + "/api/system-service/excel/upload/crossTemp?businessType=SHIPMENT_FILE_IMPORT&accessToken=" + ACCESS_TOKEN
process_url = BASE_URL + "/api/system-service/excel/upload/crossPlay.json"


def find_xml_files(directory):
    xml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml') and '_KF' in file:
                xml_files.append(os.path.join(root, file))
    return xml_files


def upload_file(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f, 'application/xml')}
        response = requests.post(upload_url, files=files, verify=False)
        rep_json = response.json()
        if rep_json.get('code') == 200:
            return rep_json.get('data')
        else:
            print(f"Failed to upload {file_path}. Status code: {response.status_code}")
            raise Exception("Failed to upload file")


def process_file(file_id):
    filter_param = {
        "deviceType": "METER",
        "fileName": "",
        "isAdd": True,
        "fileType": "XML",
        "regionId": "",
        "manufacturerCode": "KAIFA",
        "importId": file_id
    }
    data = {
        "businessType": "SHIPMENT_FILE_IMPORT",
        "fileId": file_id,
        "deviceType": "METER",
        "isAdd": True,
        "fileType": "XML",
        "manufacturerCode": "KAIFA",
        "importId": file_id,
        "fileStatus": "INITIAL",
        "filterParam": json.dumps(filter_param)
    }

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Token': ACCESS_TOKEN
    }
    response = requests.post(process_url, headers=headers, json=data, verify=False)
    if response.json().get("code") == 200:
        print(f"Successfully processed file with ID: {file_id}")
    else:
        print(f"Failed to process file with ID: {file_id}. Status code: {response.status_code}")
        raise Exception("Failed to process file")


def main(directory):
    xml_files = find_xml_files(directory)
    for xml_file in xml_files:
        print(f"Processing file: {xml_file}")
        file_id = upload_file(xml_file)
        if file_id:
            process_file(file_id)


if __name__ == "__main__":
    directory_to_search = r'E:\开发文档\202409\01 eagle 华立 200k\Eagle-200000pcs'  # 替换为你的文件夹路径
    # directory_to_search = r'E:\开发文档\202409\01 eagle 华立 200k\Eagle-200000pcs\AKF13A036-03&04-20000pcs\4000pcs(3)'  # 替换为你的文件夹路径
    main(directory_to_search)
