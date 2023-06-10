// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./DeveloperContract.sol";

contract BuyGameContract {
    address public immutable dgdsDeveloper;
    address public deployedContractAddress;
    DeveloperContract public deployedContract;

    event InformationRetrieved(string information);

    constructor(address _deployedContractAddress) {
        dgdsDeveloper = msg.sender;
        deployedContractAddress = _deployedContractAddress;
        deployedContract = DeveloperContract(deployedContractAddress);
    }

    modifier onlyOwner() {
        require(
            msg.sender == dgdsDeveloper,
            "Only the dgdsDeveloper can call this function."
        );
        _;
    }

    function payAndRetrieveInformation(
        address payable gameDeveloper,
        uint256 gameId
    ) external payable returns (string memory) {
        gameDeveloper.transfer(msg.value);
        string memory information = deployedContract.getMetadataFromID(gameId);
        emit InformationRetrieved(information);
        return information;
    }

    function updateDeployedContractAddress(
        address _deployedContractAddress
    ) external onlyOwner {
        deployedContractAddress = _deployedContractAddress;
        deployedContract = DeveloperContract(deployedContractAddress);
    }
}
