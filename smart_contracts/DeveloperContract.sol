// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract DeveloperContract is ERC721 {
    address public immutable dgdsDeveloper;
    uint256 public gameId;
    mapping(uint256 => string) gameIdToMetadata;
    event metadataAssigned(uint256 indexed gameId, string metadata);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        dgdsDeveloper = msg.sender;
        gameId = 0;
    }

    modifier onlyDgdsDeveloper() {
        require(
            msg.sender == dgdsDeveloper,
            "Only the developer can perform this action."
        );
        _;
    }

    function createDeveloperNFT(
        string memory metadataURI,
        address developer
    ) external onlyDgdsDeveloper returns (uint256) {
        require(developer != address(0), "Invalid developer address.");
        gameIdToMetadata[gameId] = metadataURI;
        emit metadataAssigned(gameId, metadataURI);
        _safeMint(developer, gameId);
        gameId++;
        return gameId;
    }

    function getMetadataFromID(uint256 id) public view returns (string memory) {
        return gameIdToMetadata[id];
    }
}
