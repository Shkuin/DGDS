from metadata.simple_template import simple_template
from path import Path
import requests
import os
import json


# !we need to provide the user's operating system!


def connect_to_ipfs(file):
    ipfs_url = "http://127.0.0.1:5001"
    endpoint = "/api/v0/add"
    response = requests.post(ipfs_url + endpoint, files={"file": file})
    return response.json()["Hash"]


def upload_file_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        file_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": file_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("\\")[-1:][0]
        file_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(file_uri)
        return file_uri


def upload_data_to_ipfs(data_path):
    for folder in os.listdir(data_path):
        folder_path = os.path.join(data_path, folder)

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                upload_file_to_ipfs(file_path)


def upload_developer_data_to_ipfs(data_path):
    # metadata_template = developer.developer_metadata
    metadata_template = simple_template

    for folder in os.listdir(data_path):
        folder_path = os.path.join(data_path, folder)
        folder_name = folder_path.split("\\")[-1:][0]

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                metadata_template[folder_name] = upload_file_to_ipfs(file_path)

    metadata_json = json.dumps(metadata_template)
    api_url = "http://127.0.0.1:5001/api/v0"
    files = {"file": ("metadata.json", metadata_json)}
    response = requests.post(f"{api_url}/add", files=files)
    ipfs_hash = response.json()["Hash"]

    print("-----------access to json file is this link:----------")
    print(f"https://ipfs.io/ipfs/{ipfs_hash}?filename=metadata.json")
    print("---------------------")

    return f"https://ipfs.io/ipfs/{ipfs_hash}?filename=metadata.json"


# def main():
#     path = "data_from_web"
#     # upload_data_to_ipfs(path)
#     upload_developer_data_to_ipfs(path)
