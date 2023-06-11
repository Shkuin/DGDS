from scripts_for_chainlink import interaction_with_chainlink
from scripts_for_chainlink import AgregatorV3Interface


def main():
    # transaction_address = (
    #     "0x2f8f149e86a5a4cb1ac624df2baa027c7edd91949324f5d6d92b8f3ff22e6013"
    # )
    # interaction_with_chainlink.foo(transaction_address)
    print(AgregatorV3Interface.get_foo())


main()
# Web3.toChecksumAd dress(lower_case_address).', '0x5f4ec3df9cbd43714fe2740f5e3616155c5b8419')
