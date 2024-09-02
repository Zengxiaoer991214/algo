import requests
import json

from ..shipment_upload import ACCESS_TOKEN, BASE_URL

history_url = BASE_URL + '/api/system-service/excel/SHIPMENT_FILE_IMPORT/history'
upload_url = BASE_URL + '/api/system-service/excel/upload/crossPlay.json'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Access-Token': ACCESS_TOKEN
}

# 请求历史记录
params = {
    'pageSize': 100,
    'pageNo': 1,
    'isMine': 'false',
    'fileStatus': 'INITIAL'
}

if __name__ == '__main__':
    response = requests.get(history_url, params=params, headers={'Access-Token': ACCESS_TOKEN}, verify=False)
    response.raise_for_status()  # 检查请求是否成功

    # 解析响应 JSON
    data = response.json()
    file_ids = [item['fileId'] for item in data.get("data").get('pageData', [])]

    # 遍历 fileId，发送 POST 请求
    for file_id in file_ids:
        payload = {
            'businessType': 'SHIPMENT_FILE_IMPORT',
            'fileId': file_id
        }
        response = requests.post(upload_url, headers=headers, json=payload, verify=False)
        if json.loads(response.content.decode('utf-8'))["code"] == 200:
            print(f"Response for fileId {file_id}:")
            print(response.json())
