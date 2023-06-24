from helpful_scripts.interaction_with_transactions import *
from helpful_scripts import interaction_with_web3


def main():
    testing_contract = interaction_with_web3.return_contract("Customer")
    print("aboba = {}", testing_contract.get_gameId_from_tokenId(0))


# def foo():
#     path = "info/DeveloperContract_metadata.json"
#     with open(path, "r") as file:
#         info = json.load(file)

#     name = "0x3646ff101beAC4D38F50d37A5C5caaC234cC9A68.json"

#     with open(name, "w") as file:
#         json.dump(info["output"], file)
