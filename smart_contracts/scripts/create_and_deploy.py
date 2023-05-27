from scripts.helpful_scripts import accounts, OPENSEA_URL, get_account
from brownie import DeveloperNFT, Contract


def deploy_and_create(metadataURI):
    # account = get_account()
    account = accounts.load("SecondAcc")
    name = "Test1"
    symbol = "t1"
    developer_nft = DeveloperNFT.deploy(name, symbol, {"from": account})
    tx = developer_nft.createDeveloperNFT(metadataURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(developer_nft.address, developer_nft.tokenId() - 1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")
    return developer_nft


# def deploy_and_create2(metadataURI):
#     contract_address = "0x9B01B5c2c46fa14Db220f4EC0FdD5fbDC3E2e650"
#     # developer_nft = Contract.from_explorer(contract_address)
#     contract_abi = [
#         {
#             "constant": False,
#             "inputs": [],
#             "name": "myFunction",
#             "outputs": [],
#             "payable": False,
#             "stateMutability": "nonpayable",
#             "type": "function",
#         }
#     ]
#     developer_nft = Contract.from_abi("DeveloperNFT", contract_address, contract_abi)
#     account = accounts.load("SecondAcc")
#     tx = developer_nft.createDeveloperNFT({"from": account}, metadataURI)
#     tx.wait(1)
#     print(
#         f"Awesome, you can view your NFT at {OPENSEA_URL.format(developer_nft.address, developer_nft.tokenId() - 1)}"
#     )
#     print("Please wait up to 20 minutes, and hit the refresh metadata button. ")
#     return developer_nft
