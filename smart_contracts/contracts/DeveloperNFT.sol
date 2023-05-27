// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "node_modules/@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

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
        // address owner,
        string memory metadataURI,
        string memory address_string
    ) external onlyDgdsDeveloper returns (uint256) {
        // require(owner != address(0), "Invalid owner address.");
        developer_address = address(bytes20(bytes(address_string)));
        _mint(developer_address, tokenId);
        _setTokenURI(tokenId, metadataURI);
        tokenId++;
        return tokenId;
    }

    // function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
    //     require(
    //         _isApprovedOrOwner(_msgSender(), tokenId),
    //         "ERC721: caller is not owner or not approved"
    //     );
    //     _setTokenURI(tokenId, _tokenURI);
    // }
}
