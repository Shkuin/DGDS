class CustomerContract:
    def __init__(self, _account, _contract, _w3):
        self.account = _account
        self.contract = _contract
        self.w3 = _w3

    def create_customer_nft(self, gameId, owner):
        transaction = self.contract.functions.createCustomerNFT(
            owner, gameId
        ).buildTransaction(
            {
                "from": self.account.address,
                "gas": 200000,
                "gasPrice": self.w3.toWei("40", "gwei"),
                "nonce": self.w3.eth.getTransactionCount(self.account.address),
            }
        )
        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, private_key=self.account.privateKey
        )
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=600)
        game_copy_id = self.contract.functions.gameCopyId().call()
        return game_copy_id

    def get_game_copy_id(self):
        return self.contract.functions.gameCopyId().call()

    def get_game_id_from_game_copy_id(self, tokenId):
        return self.contract.functions.getGameIdFromGameCopyId(tokenId).call()

    def get_game_copies_id_from_address(self, address):
        return self.contract.functions.getGameCopiesIdFromAddress(address).call()
