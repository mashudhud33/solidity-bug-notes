// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// A simple vault with a reentrancy bug, for learning only.
// The balance is set to zero AFTER the external call, so a
// malicious caller can withdraw again before the first one finishes.
contract VulnerableVault {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "nothing to withdraw");
        (bool ok, ) = msg.sender.call{value: amount}("");
        require(ok, "transfer failed");
        balances[msg.sender] = 0;
    }
}
