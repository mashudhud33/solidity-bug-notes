// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Using block.timestamp to decide a winner is risky.
// Miners can move the timestamp a little, and that is
// enough to change who wins here.
contract TimestampGame {
    address public lastPlayer;
    uint256 public deadline;

    constructor() {
        deadline = block.timestamp + 1 days;
    }

    function play() external {
        require(block.timestamp < deadline, "too late");
        lastPlayer = msg.sender;
    }

    function winner() external view returns (address) {
        require(block.timestamp >= deadline, "not over yet");
        return lastPlayer;
    }
}
