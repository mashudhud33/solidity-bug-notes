// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Anyone can call withdraw here. There is no check at all.
// I wrote this after seeing the same mistake in a few tutorials.
contract NoAccessControl {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }

    receive() external payable {}
}
