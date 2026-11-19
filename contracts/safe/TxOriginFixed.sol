// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Fixed: check msg.sender, not tx.origin.
contract TxOriginFixed {
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
