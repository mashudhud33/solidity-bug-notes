// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Using tx.origin for auth is a mistake I kept seeing in examples.
// A phishing contract can call this on behalf of the owner.
contract TxOriginAuth {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function withdraw() external {
        require(tx.origin == owner, "not owner");
        payable(msg.sender).transfer(address(this).balance);
    }

    receive() external payable {}
}
