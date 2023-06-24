import requests


def get_file_name(ipfs_url):
    return ipfs_url.split("filename=")[1]


def download_file(ipfs_url):
    response = requests.get(ipfs_url)
    file_name = get_file_name(ipfs_url)
    with open(file_name, "wb") as f:
        f.write(response.content)

    print("File downloaded successfully!")
