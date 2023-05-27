// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract GameNFT is ERC721 {
    uint256 public tokenId;
    mapping(uint256 => bool) public licenseTokens;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        tokenId = 0;
    }

    function mint(address owner) external returns (uint256) {
        require(owner != address(0), "Invalid owner address.");

        tokenId++;
        _mint(owner, tokenId);
        return tokenId;
    }

    function setLicense(uint256 tokenId, bool hasLicense) external {
        require(_exists(tokenId), "Token does not exist.");

        licenseTokens[tokenId] = hasLicense;
    }

    function hasLicense(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist.");

        return licenseTokens[tokenId];
    }
}
