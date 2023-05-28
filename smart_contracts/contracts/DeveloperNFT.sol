// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "smart_contracts/node_modules/@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract DeveloperNFT is ERC721URIStorage {
    address public immutable dgds_developer;
    uint256 public tokenId;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        dgds_developer = msg.sender;
        tokenId = 0;
    }

    modifier onlyDgdsDeveloper() {
        require(
            msg.sender == dgds_developer,
            "Only the developer can perform this action."
        );
        _;
    }

    function createDeveloperNFT(
        string memory metadataURI,
        address owner
    ) external onlyDgdsDeveloper returns (uint256) {
        _mint(owner, tokenId);
        _setTokenURI(tokenId, metadataURI);
        tokenId++;
        return tokenId;
    }
}
