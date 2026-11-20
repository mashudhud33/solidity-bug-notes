// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// An uninitialized storage pointer used to be a classic bug.
// In modern Solidity this pattern is harder to write by accident,
// but I keep it here because audit reports still mention
// uninitialized state as a root cause.
contract UninitializedOwner {
    address public owner;
    uint256 public balance;

    // No constructor, owner is never set.
    // Anyone calling init can become the owner.
    function init() external {
        owner = msg.sender;
    }

    function withdraw() external {
        require(msg.sender == owner, "not owner");
        payable(msg.sender).transfer(address(this).balance);
    }

    receive() external payable {}
}
