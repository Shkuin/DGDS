// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract CustomerNFT is ERC721URIStorage {
    constructor(
        string memory name,
        string memory symbol
    ) ERC721(name, symbol) {}

    function mint(
        address owner,
        uint256 tokenId,
        string memory metadataURI
    ) external returns (uint256) {
        require(owner != address(0), "Invalid owner address.");
        tokenId++;
        _mint(owner, tokenId);
        _setTokenURI(tokenId, metadataURI);
        return tokenId;
    }
}
