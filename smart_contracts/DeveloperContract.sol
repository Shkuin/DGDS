// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract DeveloperContract is ERC721 {
    address public immutable dgdsDeveloper;
    uint256 public tokenId;
    mapping(uint256 => string) tokenIDtoMetadata;
    event metadataAssigned(uint256 indexed tokenId, string metadata);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        dgdsDeveloper = msg.sender;
        tokenId = 0;
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
        address owner
    ) external onlyDgdsDeveloper returns (uint256) {
        require(owner != address(0), "Invalid owner address.");
        tokenIDtoMetadata[tokenId] = metadataURI;
        emit metadataAssigned(tokenId, metadataURI);
        _safeMint(owner, tokenId);
        tokenId++;
        return tokenId;
    }

    function getMetadataFromID(uint256 id) public view returns (string memory) {
        return tokenIDtoMetadata[id];
    }
}
