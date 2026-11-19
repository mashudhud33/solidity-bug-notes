// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// The same vault, fixed the simple way: update the balance
// BEFORE the external call (checks-effects-interactions).
contract SafeVault {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "nothing to withdraw");
        balances[msg.sender] = 0;
        (bool ok, ) = msg.sender.call{value: amount}("");
        require(ok, "transfer failed");
    }
}
