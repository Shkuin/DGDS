# from scripts.create_and_deploy import create_and_deploy, deploy_and_create2
# from scripts.create_metadata import upload_developer_data_to_ipfs
# from scripts.defensive_scripts import defensive32
# from brownie import DeveloperNFT, Contract, accounts
# import requests


# def get_deployed_contract(contract_address, contract_name):
#     account = accounts.load("SecondAcc")
#     nft_abi = DeveloperNFT.abi
#     return Contract.from_abi(contract_name, contract_address, nft_abi)


# def create_another_nft():
#     # contract = DeveloperNFT[-1]
#     # contract_address = "0x8d55501fb6e9611f02ed8bfcaf167d351d9367a3"
#     account = accounts.load("SecondAcc")
#     nft_abi = DeveloperNFT.abi
#     contract_address = "0x8d55501fb6E9611f02eD8BfCaF167d351D9367A3"
#     contract = Contract.from_abi("DeveloperNFT", contract_address, nft_abi)
#     # contract = get_deployed_contract(
#     #     "0x8d55501fb6e9611f02ed8bfcaf167d351d9367a3", "DeveloperNFT"
#     # )

#     path = "data_from_web"
#     metadataURI = upload_developer_data_to_ipfs(path)
#     contract.createDeveloperNFT(metadataURI, {"from": account})


# def download_metadata(token_id):
#     contract = get_deployed_contract(
#         "0x8d55501fb6E9611f02eD8BfCaF167d351D9367A3", "DeveloperNFT"
#     )
#     token_uri = contract.tokenURI(token_id)
#     print(token_uri)
#     response = requests.get(token_uri)
#     metadata = response.json()
#     return metadata


# def test_defensive():
#     key = defensive32.generate_secret_key(32)
#     plaintext = b"This is a top secret message!"
#     ciphertext, iv = defensive32.encrypt_AES(key, plaintext)
#     print(f"Ciphertext: {ciphertext.hex()}")
#     print(f"IV: {iv.hex()}")

#     decrypted_plaintext = defensive32.decrypt_AES(key, ciphertext, iv)
#     print(f"Decrypted plaintext: {decrypted_plaintext}")


# def main():
#     pass
#     # path = "data_from_web"
#     # metadataURI = upload_developer_data_to_ipfs(path)
#     # deploy_and_create(metadataURI)
#     # create_another_nft()
#     # metadata = download_metadata(2)
#     # print(metadata)
