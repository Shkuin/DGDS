from web3 import Web3
import json
from web3.middleware import geth_poa_middleware
from eth_account import Account


def read_json(name):
    with open(
        f"base/scripts_for_contract/developer_contract_info/test1/{name}.json", "r"
    ) as file:
        info = json.load(file)
    return info


def get_developer_contract(w3, contract_address, abi):
    contract = w3.eth.contract(address=contract_address, abi=abi)
    return contract


def create_web3_account(w3):
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # I have written this personal data here because it is convenient, but this is very bad practice to do it
    public_address = "0x99bc949975C4bd87D2a6d2a5043112C121EC68D1"
    private_key = "750bb8368c19376f2ddb57f78a4a810bc73789f7845a9f52a7651a444fd8fb84"

    account = Account.privateKeyToAccount(private_key)
    assert account.address.lower() == public_address.lower()

    return account


def create_developer_nft(metadata_uri, owner, account, w3, contract):
    transaction = contract.functions.createDeveloperNFT(
        metadata_uri, owner
    ).buildTransaction(
        {
            "from": account.address,
            "gas": 200000,
            "gasPrice": w3.toWei("40", "gwei"),
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    )
    signed_txn = w3.eth.account.sign_transaction(
        transaction, private_key=account.privateKey
    )
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    token_id = contract.functions.tokenId().call()
    print(token_id)
    return tx_hash, token_id


def check_statement(contract):
    tokenId = contract.functions.tokenId().call()
    print(contract.functions.tokenId().call())
    print(contract.functions.dgdsDeveloper().call())
    print(contract.functions.tokenIDtoMetadata(0).call())


def main(metadata_uri, owner_address):
    info = read_json("developer_contract_info")
    contract_address = info["contract_address"]
    w3 = Web3(Web3.HTTPProvider(info["http_provider"]))
    abi = read_json(contract_address)["abi"]
    print(contract_address)
    contract = get_developer_contract(w3, contract_address, abi)
    account = create_web3_account(w3)

    # check_statement(contract)
    tx_hash, token_id = create_developer_nft(
        metadata_uri, owner_address, account, w3, contract
    )

    # 0x5c74ff508b1c48c987bb62da14f7d2a0c075e016

    # return token_id


main("aue basota", "0x99bc949975C4bd87D2a6d2a5043112C121EC68D1")
