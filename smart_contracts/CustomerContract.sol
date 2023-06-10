// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract CustomerContract is ERC721 {
    address public immutable dgdsDeveloper;
    uint256 public customerId;
    mapping(uint256 => uint256) customerIdtoGamesId;

    event gameIdAssigned(
        uint256 indexed customerId,
        uint256 indexed gamesIdArray
    );
    event GameIdRetrieved(uint256 gameId);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        dgdsDeveloper = msg.sender;
        customerId = 0;
    }

    modifier onlyDgdsDeveloper() {
        require(
            msg.sender == dgdsDeveloper,
            "Only the developer can perform this action."
        );
        _;
    }

    function createCustomerNFT(
        address owner,
        uint256 gameId
    ) external onlyDgdsDeveloper returns (uint256) {
        require(owner != address(0), "Invalid owner address.");
        customerIdtoGamesId[customerId] = gameId;
        emit gameIdAssigned(customerId, gameId);
        _safeMint(owner, customerId);
        customerId++;
        return customerId;
    }

    function getGameIdFromCustomerId(uint256 id) public returns (uint256) {
        uint256 gameId = customerIdtoGamesId[id];
        emit GameIdRetrieved(gameId);
        return gameId;
    }
}
