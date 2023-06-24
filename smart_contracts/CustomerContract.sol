// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract CustomerContract is ERC721 {
    address public immutable dgdsDeveloper;
    uint256 public gameCopyId;
    mapping(uint256 => uint256) gameCopyIdToOriginalGame;
    mapping(address => uint256[]) customerAddressToGameCopies;

    event gameIdAssigned(
        uint256 indexed gameCopyId,
        uint256 indexed gamesIdArray
    );
    event GameIdRetrieved(uint256 gameId);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        dgdsDeveloper = msg.sender;
        gameCopyId = 0;
    }

    modifier onlyDgdsDeveloper() {
        require(
            msg.sender == dgdsDeveloper,
            "Only the developer can perform this action."
        );
        _;
    }

    function createCustomerNFT(
        address customer,
        uint256 gameId
    ) external onlyDgdsDeveloper returns (uint256) {
        require(customer != address(0), "Invalid customer address.");
        gameCopyIdToOriginalGame[gameCopyId] = gameId;
        emit gameIdAssigned(gameCopyId, gameId);
        customerAddressToGameCopies[customer].push(gameCopyId);
        _safeMint(customer, gameCopyId);
        gameCopyId++;
        return gameCopyId;
    }

    function getGameIdFromGameCopyId(uint256 id) public view returns (uint256) {
        return gameCopyIdToOriginalGame[id];
    }

    function getGameCopiesIdFromAddress(
        address customer
    ) public view returns (uint256[] memory) {
        return customerAddressToGameCopies[customer];
    }
}
