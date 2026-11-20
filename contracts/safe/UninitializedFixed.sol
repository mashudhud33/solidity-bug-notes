// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Fixed: set the owner once, in the constructor, and do not
// leave an init function anyone can call.
contract UninitializedFixed {
    address public owner;
    uint256 public balance;

    constructor() {
        owner = msg.sender;
    }

    function withdraw() external {
        require(msg.sender == owner, "not owner");
        payable(msg.sender).transfer(address(this).balance);
    }

    receive() external payable {}
}
