from web3 import Web3
from base.helpful_scripts.interaction_with_web3 import get_json


def get_latest_price():
    w3 = Web3(
        Web3.HTTPProvider(
            "https://mainnet.infura.io/v3/5c84d02cce30471ea955d1e9f6b3117c"
        )
    )

    agregator_abi = get_json(
        "base/scripts_for_contract/aggregator_V3_contract/info/aggregator_V3_contract"
    )

    contract_address = "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"

    contract = w3.eth.contract(address=contract_address, abi=agregator_abi)

    latest_round_id = contract.functions.latestRound().call()
    latest_answer = contract.functions.getAnswer(latest_round_id).call()
    return latest_answer / 10**8
