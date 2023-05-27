# import create_metadata
# from helpful_scripts import get_account, OPENSEA_URL
# from brownie import network, DeveloperNFT


# # def set_tokenURI(token_id, nft_contract, path):
# #     tokenURI = create_metadata.upload_developer_data_to_ipfs(path)
# #     account = get_account(None, "SecondAcc")
# #     tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
# #     tx.wait(1)
# #     print(
# #         f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
# #     )
# #     print("Please wait up to 20 minutes, and hit the refresh metadata button")


# def main():
#     print(f"Working on {network.show_active()}")
#     developer_nft = DeveloperNFT[-1]
#     token_id = 0
#     path = "data_from_web"
#     if not developer_nft.tokenURI(token_id).startswith("https://"):
#         print(f"Setting tokenURI of {token_id}")
#         set_tokenURI(token_id, developer_nft, path)
