from web3 import Web3
import json


def connect_to_blockchain():
    json_file = get_json("infura_info.json")
    w3 = Web3(Web3.HTTPProvider(json_file["http_provider"]))
    return w3


def get_json(path):
    with open(path, "r") as file:
        info = json.load(file)
    return info


def get_recipient_wallet(transaction_address):
    w3 = connect_to_blockchain()
    tx_receipt = w3.eth.getTransactionReceipt(transaction_address)
    recipient_wallet = tx_receipt["to"]

    return recipient_wallet


def get_amount_of_transaction(transaction_address):
    w3 = connect_to_blockchain()
    transaction = w3.eth.getTransaction(transaction_address)
    amount = transaction["value"]

    amount_in_ether = w3.fromWei(amount, "ether")
    return amount


def check_transaction_status(transaction_address):
    w3 = connect_to_blockchain()
    tx_receipt = w3.eth.getTransactionReceipt(transaction_address)

    if tx_receipt is None:
        return False

    return True
