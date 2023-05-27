// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract DeveloperNFT is ERC721URIStorage {
    address public dgds_developer;
    // address public developer_nft_address;
    uint256 public tokenId;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        dgds_developer = msg.sender;
        tokenId = 0;
    }

    modifier onlyDeveloper() {
        require(
            msg.sender == dgds_developer,
            "Only the dgds developer can perform this action."
        );
        _;
    }

    function createDeveloperNFT(
        // address owner,
        string memory metadataURI
    ) external onlyDeveloper returns (uint256) {
        // require(owner != address(0), "Invalid owner address.");
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, metadataURI);
        tokenId++;
        return tokenId;
    }
}
