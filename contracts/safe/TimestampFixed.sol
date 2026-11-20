// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Fixed, in the simplest honest way: do not use block.timestamp
// to pick a winner. Use block.number as a rough clock instead,
// and accept that it is still not exact.
contract TimestampGameFixed {
    address public lastPlayer;
    uint256 public deadlineBlock;

    constructor() {
        deadlineBlock = block.number + 7200;
    }

    function play() external {
        require(block.number < deadlineBlock, "too late");
        lastPlayer = msg.sender;
    }

    function winner() external view returns (address) {
        require(block.number >= deadlineBlock, "not over yet");
        return lastPlayer;
    }
}
