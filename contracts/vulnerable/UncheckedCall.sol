// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// The return value of the call is ignored here.
// If the call fails, the balance is still cleared, and the
// user loses their funds without knowing why.
contract UncheckedCall {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "nothing to withdraw");
        balances[msg.sender] = 0;
        msg.sender.call{value: amount}("");
    }
}
