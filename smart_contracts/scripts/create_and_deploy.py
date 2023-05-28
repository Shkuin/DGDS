from scripts.helpful_scripts import accounts, OPENSEA_URL, get_account
from brownie import DeveloperNFT, network
from scripts.create_metadata import create_metadata


def create_and_deploy(metadataURI, name, symbol, account_name):
    network.disconnect()
    network.connect("sepolia")
    account = accounts.load(account_name)

    address = "0xF22cFb17fA3247eCF089024302b7b090AcD5c3CE"
    developer_nft = DeveloperNFT.deploy(name, symbol, {"from": account})
    developer_nft.createDeveloperNFT(metadataURI, address, {"from": account})

    print("Congratulations")

    return developer_nft


def main(name, genre, description, platform, image, game_file, price, wallet_address):
    keys, metadata_uri = create_metadata(
        name, genre, description, platform, image, game_file, price, wallet_address
    )

    print(create_and_deploy(metadata_uri, "aue", "symbol1", "SecondAcc"))

    return keys
