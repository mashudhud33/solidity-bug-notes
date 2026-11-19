// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Fixed: only the owner can withdraw.
contract AccessControlFixed {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function withdraw() external {
        require(msg.sender == owner, "not owner");
        payable(msg.sender).transfer(address(this).balance);
    }

    receive() external payable {}
}
