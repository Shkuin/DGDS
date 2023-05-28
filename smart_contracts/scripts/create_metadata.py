from metadata.metadata_template import template
from path import Path
import requests
import os
import json
from scripts.defensive_scripts import defense


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
    metadata_template = template

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


# ---------------------------------------------------------------


def upload_file_to_ipfs_from_django(file):
    with Path(file).open("rb") as fp:
        file_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": file_binary})
        ipfs_hash = response.json()["Hash"]
        filename = str(file)
        file_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(file_uri)
        return file_uri


def upload_array_to_ipfs(array):
    uri_array = []
    for file in array:
        uri_array.append(upload_file_to_ipfs_from_django(file))
    return uri_array


def upload_json_to_ipfs(metadata_template):
    metadata_json = json.dumps(metadata_template)
    api_url = "http://127.0.0.1:5001/api/v0"
    files = {"file": ("metadata.json", metadata_json)}
    response = requests.post(f"{api_url}/add", files=files)
    ipfs_hash = response.json()["Hash"]
    return f"https://ipfs.io/ipfs/{ipfs_hash}?filename=metadata.json"


def create_metadata(
    name, genre, description, platform, images, game_files, price, wallet_address
):
    metadata_template = template
    metadata_template["name"] = name
    metadata_template["genre"] = genre
    metadata_template["description"] = description
    metadata_template["platform"] = platform
    metadata_template["images"] = upload_array_to_ipfs(images)
    metadata_template["price"] = price
    metadata_template["wallet_address"] = wallet_address

    key_array = []
    for uri in upload_array_to_ipfs(game_files):
        cipher = defense.AESCipher("")
        metadata_template["game_files"].append(cipher.encrypt(uri))
        key_array.append(cipher.key)

    return key_array, upload_json_to_ipfs(metadata_template)
