import json
import uuid

import requests

from awork.shipment_upload import ACCESS_TOKEN, BASE_URL

process_url = BASE_URL + "/api/system-service/excel/upload/crossPlay.json"


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
        'Access-Token2': ACCESS_TOKEN
    }
    response = requests.post(process_url, headers=headers, json=data, verify=False)
    if response.json().get('code') == 200:
        print(f"Successfully processed file with ID: {file_id}")
    else:
        print(f"Failed to process file with ID: {file_id}. Status code: {response.status_code}")
        raise Exception("Failed to process file")


if __name__ == '__main__':
    file_id = str(uuid.uuid4())
    process_file(file_id)
